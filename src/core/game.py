from typing import List, Optional, Union
from core.map import Cell, Position
from core.piece import Piece, PieceType
from core.state import State


class Game:
    __state: State

    def __init__(self):
        self.__state = State()

    def get_possible_moves(self, piece: Piece) -> List[Cell]:
        pos = self.__state.get_piece_position(piece)
        if pos is None:
            return []
        adj_cells = (
            self.__state.get_adjacent_cells(pos)
            if piece.type not in [PieceType.TIGER, PieceType.LION]
            else self.__state.get_adjacent_non_river_cells(pos)
        )

        standable_cells = []

        for cell in adj_cells:
            adj_loc = cell.location

            if adj_loc.is_river:
                if piece.type == PieceType.MOUSE:
                    standable_cells.append(cell)
            elif adj_loc.cave_color != piece.color:
                standable_cells.append(cell)

        not_blocked_by_other_pieces_cells = []
        for cell in standable_cells:
            adj_loc = cell.location
            adj_piece = self.__state.get_piece_at_position(cell)

            if adj_piece is None:
                not_blocked_by_other_pieces_cells.append(cell)
                continue
            elif adj_piece.color == piece.color:
                continue
            elif cell.location.trap_color == piece.color:
                not_blocked_by_other_pieces_cells.append(cell)
                continue
            elif cell.location.trap_color != piece.color:
                continue
            elif piece.type == PieceType.MOUSE and adj_piece.type == PieceType.ELEPHANT:
                not_blocked_by_other_pieces_cells.append(cell)
                continue
            elif piece.get_default_level() >= adj_piece.get_default_level():
                not_blocked_by_other_pieces_cells.append(cell)
                continue

        return not_blocked_by_other_pieces_cells

    def move(self, piece: Piece, position: Position) -> Union[bool, Optional[Piece]]:
        possible_pos = map(lambda x: x.position, self.get_possible_moves(piece))
        if position not in possible_pos:
            return False

        replaced_piece = self.__state.get_piece_at_position(position)
        if replaced_piece is not None:
            self.__state.kill_piece(replaced_piece)
        self.__state.set_piece_position(piece, position)
        return replaced_piece or True

    def get_state(self) -> State:
        return self.__state
