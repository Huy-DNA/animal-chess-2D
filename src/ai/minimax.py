import time
from typing import List, Optional
from ai.move import Move
from core.piece import Color, PieceType
import copy


class MinimaxAI:
    def __init__(self, color: Color, max_depth: int = 3):
        self.color = color
        self.max_depth = max_depth
        self.nodes_evaluated = 0
        self.opponent_color = Color.BLUE if color == Color.RED else Color.RED

    def choose_move(self, game) -> Optional[Move]:
        """Choose the best move using minimax algorithm"""
        self.nodes_evaluated = 0
        start_time = time.time()

        all_moves = self._get_all_possible_moves(game, self.color)
        if not all_moves:
            return None

        best_score = float("-inf")
        best_move = None

        for move in all_moves:
            game_copy = copy.deepcopy(game)
            captured = game_copy.move(move.piece, move.to_pos)

            score = self._minimax(
                game_copy, self.max_depth - 1, False, float("-inf"), float("inf")
            )

            if score > best_score:
                best_score = score
                best_move = move

        end_time = time.time()
        print(
            f"Minimax AI evaluated {self.nodes_evaluated} nodes in {end_time - start_time:.2f} seconds"
        )
        print(f"Best move: {best_move} with score: {best_score}")

        return best_move

    def _minimax(
        self, game, depth: int, is_maximizing: bool, alpha: float, beta: float
    ) -> float:
        """Minimax algorithm with alpha-beta pruning"""
        self.nodes_evaluated += 1

        # Check if game is over
        winner = game.is_game_over()
        if winner is not None:
            return 1000 if winner == self.color else -1000

        # If we've reached max depth, evaluate the board
        if depth == 0:
            return self._evaluate_board(game)

        if is_maximizing:
            max_eval = float("-inf")
            moves = self._get_all_possible_moves(game, self.color)

            for move in moves:
                game_copy = copy.deepcopy(game)
                game_copy.move(move.piece, move.to_pos)

                eval = self._minimax(game_copy, depth - 1, False, alpha, beta)
                max_eval = max(max_eval, eval)

                alpha = max(alpha, eval)
                if beta <= alpha:
                    break

            return max_eval
        else:
            min_eval = float("inf")
            moves = self._get_all_possible_moves(game, self.opponent_color)

            for move in moves:
                game_copy = copy.deepcopy(game)
                game_copy.move(move.piece, move.to_pos)

                eval = self._minimax(game_copy, depth - 1, True, alpha, beta)
                min_eval = min(min_eval, eval)

                # Alpha-beta pruning
                beta = min(beta, eval)
                if beta <= alpha:
                    break

            return min_eval

    def _get_all_possible_moves(self, game, color: Color) -> List[Move]:
        """Get all possible moves for a given color"""
        moves = []
        state = game.get_state()

        for piece in state.get_all_pieces():
            if piece.color == color and state.is_alive(piece):
                possible_cells = game.get_possible_moves(piece)
                for cell in possible_cells:
                    moves.append(Move(piece, cell.position))

        return moves

    def _evaluate_board(self, game) -> float:
        """Evaluate the board state from the perspective of the AI player"""
        state = game.get_state()
        score = 0

        piece_values = {
            PieceType.ELEPHANT: 8,
            PieceType.LION: 7,
            PieceType.TIGER: 6,
            PieceType.LEOPARD: 5,
            PieceType.WOLF: 4,
            PieceType.DOG: 3,
            PieceType.CAT: 2,
            PieceType.MOUSE: 1,
        }

        for piece in state.get_all_pieces():
            if not state.is_alive(piece):
                continue

            value = piece_values[piece.type] * 10

            if piece.color == self.color:
                score += value

                pos = state.get_piece_position_definitely(piece)

                enemy_den_y = 0 if self.color == Color.BLUE else 8
                distance_to_den = abs(pos.y - enemy_den_y)
                score += (9 - distance_to_den) * 3

                center_x, center_y = 3, 4
                center_dist = abs(pos.x - center_x) + abs(pos.y - center_y)
                score += 9 - center_dist

            else:
                score -= value

        return score
