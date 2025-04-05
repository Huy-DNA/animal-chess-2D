import time
import random
import math
import copy
from typing import List, Optional
from ai.minimax import MinimaxAI
from ai.move import Move
from core.game import Game
from core.piece import Color


class MCTSNode:
    def __init__(self, game, parent=None, move=None, player_color=None):
        self.game = copy.deepcopy(game)
        self.parent = parent
        self.move = move
        self.player_color = player_color
        self.children = []
        self.visits = 0
        self.wins = 0
        self.untried_moves = None

    def get_untried_moves(self, ai):
        if self.untried_moves is None:
            next_color = self.player_color
            self.untried_moves = ai._get_all_possible_moves(self.game, next_color)
        return self.untried_moves

    def add_child(self, move, next_color):
        game_copy = copy.deepcopy(self.game)

        game_copy.move(move.piece, move.to_pos)

        child = MCTSNode(game_copy, parent=self, move=move, player_color=next_color)
        self.children.append(child)
        return child

    def select_child(self):
        c = 1.41

        return max(
            self.children,
            key=lambda child: (child.wins / child.visits)
            + c * math.sqrt(2 * math.log(self.visits) / child.visits),
        )

    def update(self, result):
        self.visits += 1
        self.wins += result


class MCTSAI:
    def __init__(self, color: Color, num_simulations=1000, simulation_depth=50):
        self.color = color
        self.num_simulations = num_simulations
        self.simulation_depth = simulation_depth
        self.opponent_color = Color.BLUE if color == Color.RED else Color.RED

    def choose_move(self, game) -> Optional[Move]:
        start_time = time.time()

        root = MCTSNode(game, player_color=self.color)

        for _ in range(self.num_simulations):
            node = root

            while node.children and not node.get_untried_moves(self):
                node = node.select_child()

            if node.get_untried_moves(self):
                next_color = (
                    self.opponent_color
                    if node.player_color == self.color
                    else self.color
                )

                move = random.choice(node.get_untried_moves(self))
                node.untried_moves.remove(move)

                node = node.add_child(move, next_color)

            result = self._simulate(node)

            while node:
                node.update(result)
                node = node.parent
                result = 1 - result

        if not root.children:
            return None

        best_child = max(root.children, key=lambda c: c.visits)

        end_time = time.time()
        print(
            f"MCTS ran {self.num_simulations} simulations in {end_time - start_time:.2f} seconds"
        )
        print(
            f"Best move: {best_child.move} with {best_child.visits} visits and win rate {best_child.wins/best_child.visits:.2f}"
        )

        return best_child.move

    def _get_all_possible_moves(self, game, color: Color) -> List[Move]:
        moves = []
        state = game.get_state()

        for piece in state.get_all_pieces():
            if piece.color == color and state.is_alive(piece):
                possible_cells = game.get_possible_moves(piece)
                for cell in possible_cells:
                    moves.append(Move(piece, cell.position))

        return moves

    def _simulate(self, node):
        sim_game = copy.deepcopy(node.game)
        current_color = node.player_color

        for _ in range(self.simulation_depth):
            winner = sim_game.is_game_over()
            if winner is not None:
                break

            moves = self._get_all_possible_moves(sim_game, current_color)
            if not moves:
                break

            move = random.choice(moves)
            sim_game.move(move.piece, move.to_pos)

            current_color = (
                self.opponent_color if current_color == self.color else self.color
            )

        winner = sim_game.is_game_over()
        if winner == self.color:
            return 1.0  # Win
        elif winner == self.opponent_color:
            return 0.0  # Loss
        else:
            state = sim_game.get_state()

            our_pieces = sum(
                1
                for piece in state.get_all_pieces()
                if piece.color == self.color and state.is_alive(piece)
            )
            opponent_pieces = sum(
                1
                for piece in state.get_all_pieces()
                if piece.color == self.opponent_color and state.is_alive(piece)
            )

            total_pieces = our_pieces + opponent_pieces
            if total_pieces == 0:
                return 0.5  # Draw
            return our_pieces / total_pieces


def self_play_training(num_games=100, max_moves=200):
    minimax_ai = MinimaxAI(Color.RED, max_depth=3)
    mcts_ai = MCTSAI(Color.BLUE, num_simulations=500)

    results = {"RED": 0, "BLUE": 0, "DRAW": 0}

    for game_num in range(num_games):
        print(f"Starting game {game_num + 1}/{num_games}")
        game = Game()
        current_color = Color.RED

        for move_num in range(max_moves):
            winner = game.is_game_over()
            if winner is not None:
                results[winner.name] += 1
                print(f"Game {game_num + 1}: {winner.name} wins in {move_num} moves")
                break

            if current_color == Color.RED:
                move = minimax_ai.choose_move(game)
            else:
                move = mcts_ai.choose_move(game)

            if move is None:
                results["DRAW"] += 1
                print(
                    f"Game {game_num + 1}: Draw (no valid moves) after {move_num} moves"
                )
                break

            game.move(move.piece, move.to_pos)

            current_color = Color.BLUE if current_color == Color.RED else Color.RED

        else:
            results["DRAW"] += 1
            print(
                f"Game {game_num + 1}: Draw (move limit reached) after {max_moves} moves"
            )

    print("\nTraining Results:")
    print(f"Games played: {num_games}")
    print(f"RED (Minimax) wins: {results['RED']} ({results['RED']/num_games*100:.1f}%)")
    print(f"BLUE (MCTS) wins: {results['BLUE']} ({results['BLUE']/num_games*100:.1f}%)")
    print(f"Draws: {results['DRAW']} ({results['DRAW']/num_games*100:.1f}%)")

    return results
