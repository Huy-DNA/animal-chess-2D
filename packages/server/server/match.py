from core.game import Game
from core.map import Color, dataclass

from server import Addr

MatchId = str

@dataclass
class Match:
    id: MatchId
    game: Game
    red_player: Addr
    blue_player: Addr
    turn: Color = Color.RED
