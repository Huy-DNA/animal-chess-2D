from typing import Optional

# class Animal:
#     def __init__(self, name, row, col, team):
#         self.name = name
#         self.row = row
#         self.col = col
#         self.team = team  # 'red' hoặc 'blue'

# class GameState:
#     def __init__(self):
#         self.board: list[list[Optional[Animal]]] = [[None for _ in range(7)] for _ in range(9)] 
#         self.animals = {}  # {(row, col): Animal}
#         self.traps = [(0, 2), (0, 4), (1, 3), (7, 3), (8, 2), (8, 4)]  # Các ô bẫy
#         self.rivers = {
#             (3, 1), (4, 1), (5, 1),
#             (3, 2), (4, 2), (5, 2),
#             (3, 4), (4, 4), (5, 4),
#             (3, 5), (4, 5), (5, 5)
#         }
#         self.setup_initial_animals()

#     def setup_initial_animals(self):
#         # Vị trí khởi đầu các con thú cho mỗi bên (theo luật cờ thú)
#         red_positions = {
#             "elephant": (2, 6),
#             "lion":     (0, 0),
#             "tiger":    (0, 6),
#             "leopard":  (2, 2),
#             "wolf":     (2, 4),
#             "dog":      (1, 1),
#             "cat":      (1, 5),
#             "mouse":      (2, 0)
#         }

#         blue_positions = {
#             "elephant": (6, 0),
#             "lion":     (8, 6),
#             "tiger":    (8, 0),
#             "leopard":  (6, 4),
#             "wolf":     (6, 2),
#             "dog":      (7, 5),
#             "cat":      (7, 1),
#             "mouse":      (6, 6)
#         }

#         for name, (r, c) in red_positions.items():
#             animal = Animal(name, r, c, "red")
#             self.animals[(r, c)] = animal
#             self.board[r][c] = animal

#         for name, (r, c) in blue_positions.items():
#             animal = Animal(name, r, c, "blue")
#             self.animals[(r, c)] = animal
#             self.board[r][c] = animal

#     def move_animal(self, animal, new_row, new_col):
#         old_pos = (animal.row, animal.col)
#         new_pos = (new_row, new_col)

#         # Cập nhật tọa độ
#         animal.row = new_row
#         animal.col = new_col

#         # Cập nhật board và animals
#         self.board[old_pos[0]][old_pos[1]] = None
#         self.board[new_row][new_col] = animal

#         del self.animals[old_pos]
#         self.animals[new_pos] = animal
# class Animal:
#     def __init__(self, name, row, col, team, rank):
#         self.name = name
#         self.row = row
#         self.col = col
#         self.team = team  # 'red' or 'blue'
#         self.rank = rank  # 1 (mouse) to 8 (elephant)

#     def position(self):
#         return (self.row, self.col)
    
#     def get_rank(self):
#         rank_dict = {
#             "rat": 1,
#             "cat": 2,
#             "dog": 3,
#             "wolf": 4,
#             "leopard": 5,
#             "tiger": 6,
#             "lion": 7,
#             "elephant": 8
#         }
#         return rank_dict.get(self.name.split("-")[0], 0)  # nếu tên có đuôi "-image" thì tách trước


# class GameState:
#     def __init__(self):
#         self.board: list[list[Optional[Animal]]] = [[None for _ in range(7)] for _ in range(9)] 
#         self.traps = [(0, 2), (0, 4), (1, 3), (8, 2), (8, 4), (7, 3)]
#         self.rivers = [(3, 1), (4, 1), (5, 1),
#                        (3, 2), (4, 2), (5, 2),
#                        (3, 4), (4, 4), (5, 4),
#                        (3, 5), (4, 5), (5, 5)]
#         self.animals = {}
#         self.init_animals()
#         self.dens = [(0, 3), (8, 3)]
#         self.turn = 'red'  # hoặc 'blue'

#     def init_animals(self):
#         setup = [
#             ("lion", 0, 0, 'red', 7),
#             ("tiger", 0, 6, 'red', 6),
#             ("dog", 1, 1, 'red', 3),
#             ("cat", 1, 5, 'red', 2),
#             ("mouse", 2, 0, 'red', 1),
#             ("leopard", 2, 2, 'red', 5),
#             ("wolf", 2, 4, 'red', 4),
#             ("elephant", 2, 6, 'red', 8),

#             ("lion", 8, 6, 'blue', 7),
#             ("tiger", 8, 0, 'blue', 6),
#             ("dog", 7, 5, 'blue', 3),
#             ("cat", 7, 1, 'blue', 2),
#             ("mouse", 6, 6, 'blue', 1),
#             ("leopard", 6, 4, 'blue', 5),
#             ("wolf", 6, 2, 'blue', 4),
#             ("elephant", 6, 0, 'blue', 8),
#         ]

#         for name, row, col, team, rank in setup:
#             animal = Animal(name, row, col, team, rank)
#             self.animals[(row, col)] = animal
#             self.board[row][col] = animal

#     def is_river(self, row, col):
#         return (row, col) in self.rivers

#     def is_trap(self, row, col):
#         return (row, col) in self.traps

#     def can_jump(self, animal, to_row, to_col):
#         if animal.name not in ['lion', 'tiger']:
#             return False

#         if animal.row == to_row:
#             dir = 1 if to_col > animal.col else -1
#             for c in range(animal.col + dir, to_col, dir):
#                 if not self.is_river(to_row, c) or (to_row, c) in self.animals:
#                     return False
#             return True
#         elif animal.col == to_col:
#             dir = 1 if to_row > animal.row else -1
#             for r in range(animal.row + dir, to_row, dir):
#                 if not self.is_river(r, to_col) or (r, to_col) in self.animals:
#                     return False
#             return True

#         return False

#     def can_capture(self, attacker, defender, row, col):
#         attacker_rank = attacker.get_rank()
#         defender_rank = defender.get_rank()

#         # Nếu con bị bắt đang trong bẫy → luôn bắt được
#         if (row, col) in self.traps and self.traps[(row, col)] != attacker.team:
#             return True

#         # Chuột bắt voi
#         if attacker.name == 'rat' and defender.name == 'elephant':
#             return True

#         # Voi không bắt được chuột
#         if attacker.name == 'elephant' and defender.name == 'rat':
#             return False

#         return attacker_rank >= defender_rank

#     def is_valid_move(self, animal, new_row, new_col):
#         # 1. Không đi nếu không đúng lượt
#         if animal.team != self.turn:
#             return False

#         # 2. Không đi ra khỏi bàn
#         if not (0 <= new_row < 9 and 0 <= new_col < 7):
#             return False

#         # 3. Không đi vào den của chính mình
#         if self.dens[animal.team] == (new_row, new_col):
#             return False

#         # 4. Kiểm tra ô đích
#         target_animal = self.animals.get((new_row, new_col))
#         if target_animal:
#             if target_animal.team == animal.team:
#                 return False
#             if not self.can_capture(animal, target_animal, new_row, new_col):
#                 return False

#         # Bạn có thể bổ sung thêm kiểm tra sông, nhảy, chuột v.v sau này
#         return True


#     def move_animal(self, animal, new_row, new_col):
#         old_row, old_col = animal.row, animal.col
#         target = self.animals.get((new_row, new_col))

#         # Không được ăn quân cùng đội
#         if target and target.team == animal.team:
#             return False

#         dr = abs(new_row - old_row)
#         dc = abs(new_col - old_col)

#         # Tính năng nhảy qua sông (cho hổ/sư tử)
#         if animal.name in ['tiger', 'lion']:
#             if old_row == new_row and dc > 1:  # ngang
#                 step = 1 if new_col > old_col else -1
#                 for col in range(old_col + step, new_col, step):
#                     if (old_row, col) in self.rivers and (old_row, col) in self.animals:
#                         return False  # có chuột cản trong sông
#                     if (old_row, col) not in self.rivers:
#                         return False  # không phải sông
#             elif old_col == new_col and dr > 1:  # dọc
#                 step = 1 if new_row > old_row else -1
#                 for row in range(old_row + step, new_row, step):
#                     if (row, old_col) in self.rivers and (row, old_col) in self.animals:
#                         return False
#                     if (row, old_col) not in self.rivers:
#                         return False
#             elif dr + dc != 1:
#                 return False
#         else:
#             if dr + dc != 1:
#                 return False

#         # Xử lý ăn quân
#         if target:
#             attacker_rank = animal.get_rank()
#             defender_rank = target.get_rank()

#             # Chuột ăn voi
#             if animal.name == "mouse" and target.name == "elephant":
#                 pass
#             # Chuột không được ăn nếu đang ở sông hoặc đối thủ đang ở sông
#             elif animal.name == "mouse" and ((old_row, old_col) in self.rivers or (new_row, new_col) in self.rivers):
#                 return False
#             # Chuột trong sông không bị ai ăn
#             elif (new_row, new_col) in self.rivers and target.name == "mouse":
#                 pass
#             elif attacker_rank < defender_rank:
#                 return False

#         # Di chuyển hợp lệ
#         del self.animals[(old_row, old_col)]
#         if target:
#             del self.animals[(new_row, new_col)]
#         animal.row = new_row
#         animal.col = new_col
#         self.animals[(new_row, new_col)] = animal
#         return True

#     def execute_move(self, animal, to_row, to_col):
#         if self.is_valid_move(animal, to_row, to_col):
#             if (to_row, to_col) in self.animals:
#                 defender = self.animals[(to_row, to_col)]
#                 if self.can_capture(animal, defender):
#                     del self.animals[(to_row, to_col)]
#             self.move_animal(animal, to_row, to_col)

# class Animal:
#     def __init__(self, name, row, col, team, rank):
#         self.name = name
#         self.row = row
#         self.col = col
#         self.team = team  # 'red' or 'blue'
#         self.rank = rank  # 1 (mouse) to 8 (elephant)
#         self.frozen = False  # 🧊 Mặc định không bị đóng băng

#     def position(self):
#         return (self.row, self.col)

#     def get_rank(self):
#         rank_dict = {
#             "rat": 1,
#             "cat": 2,
#             "dog": 3,
#             "wolf": 4,
#             "leopard": 5,
#             "tiger": 6,
#             "lion": 7,
#             "elephant": 8
#         }
#         return rank_dict.get(self.name.split("-")[0], 0)


# class GameState:
#     def __init__(self):
#         self.board: list[list[Optional[Animal]]] = [[None for _ in range(7)] for _ in range(9)] 
#         self.traps = [(0, 2), (0, 4), (1, 3), (8, 2), (8, 4), (7, 3)]
#         self.rivers = [(3, 1), (4, 1), (5, 1),
#                        (3, 2), (4, 2), (5, 2),
#                        (3, 4), (4, 4), (5, 4),
#                        (3, 5), (4, 5), (5, 5)]
#         self.dens = {'red': (0, 3), 'blue': (8, 3)}
#         self.animals = {}
#         self.turn = 'red'
#         self.init_animals()

#     def init_animals(self):
#         setup = [
#             ("lion", 0, 0, 'red', 7), ("tiger", 0, 6, 'red', 6),
#             ("dog", 1, 1, 'red', 3), ("cat", 1, 5, 'red', 2),
#             ("mouse", 2, 0, 'red', 1), ("leopard", 2, 2, 'red', 5),
#             ("wolf", 2, 4, 'red', 4), ("elephant", 2, 6, 'red', 8),
#             ("lion", 8, 6, 'blue', 7), ("tiger", 8, 0, 'blue', 6),
#             ("dog", 7, 5, 'blue', 3), ("cat", 7, 1, 'blue', 2),
#             ("mouse", 6, 6, 'blue', 1), ("leopard", 6, 4, 'blue', 5),
#             ("wolf", 6, 2, 'blue', 4), ("elephant", 6, 0, 'blue', 8),
#         ]

#         for name, row, col, team, rank in setup:
#             animal = Animal(name, row, col, team, rank)
#             self.animals[(row, col)] = animal
#             self.board[row][col] = animal

#     def is_river(self, row, col):
#         return (row, col) in self.rivers

#     def is_trap(self, row, col):
#         return (row, col) in self.traps

#     def can_capture(self, attacker, defender, row=None, col=None):
#         if row is None or col is None:
#             row, col = defender.row, defender.col

#         if (row, col) in self.traps:
#             return True

#         if attacker.name == 'mouse' and defender.name == 'elephant':
#             return True

#         if attacker.name == 'elephant' and defender.name == 'mouse':
#             return False

#         return attacker.get_rank() >= defender.get_rank()

#     def is_valid_move(self, animal, new_row, new_col):
#         if animal.team != self.turn:
#             return False

#         if not (0 <= new_row < 9 and 0 <= new_col < 7):
#             return False

#         if self.dens[animal.team] == (new_row, new_col):
#             return False
        
#         if animal.frozen:
#             return False
        
#         # Ngăn các con vật không phải chuột đi vào sông
#         if self.is_river(new_row, new_col) and animal.name != 'mouse':
#             return False

#         target = self.animals.get((new_row, new_col))
#         if target:
#             if target.team == animal.team:
#                 return False
#             if not self.can_capture(animal, target, new_row, new_col):
#                 return False

#         dr = abs(animal.row - new_row)
#         dc = abs(animal.col - new_col)

#         if animal.name in ['lion', 'tiger'] and (dr > 1 or dc > 1):
#             if animal.row == new_row:
#                 step = 1 if new_col > animal.col else -1
#                 for c in range(animal.col + step, new_col, step):
#                     if (animal.row, c) not in self.rivers:
#                         return False
#                     if (animal.row, c) in self.animals:
#                         return False
#             elif animal.col == new_col:
#                 step = 1 if new_row > animal.row else -1
#                 for r in range(animal.row + step, new_row, step):
#                     if (r, animal.col) not in self.rivers:
#                         return False
#                     if (r, animal.col) in self.animals:
#                         return False
#         else:
#             if dr + dc != 1:
#                 return False

#         return True

#     def move_animal(self, animal, new_row, new_col):
#         old_row, old_col = animal.row, animal.col
#         target = self.animals.get((new_row, new_col))

#         if target and target.team == animal.team:
#             return False

#         if not self.is_valid_move(animal, new_row, new_col):
#             return False

#         # Không cho phép quân đang bị đóng băng (frozen) di chuyển nữa
#         if animal.frozen:
#             return False
#         # Nếu vào bẫy của đối phương thì đóng băng
#         if (new_row, new_col) in self.traps and animal.team != self.traps_owner((new_row, new_col)):
#             animal.frozen = True
#             animal.rank = 0
#         # if (old_row, old_col) in self.traps and self.traps_owner((old_row, old_col)) != animal.team:
#         #     animal.frozen = False
#         # Nếu rời bẫy đối phương: hồi phục rank và bỏ đóng băng
#         elif (old_row, old_col) in self.traps and animal.team != self.traps_owner((old_row, old_col)):
#             animal.frozen = False
#             animal.rank = animal.original_rank

#         del self.animals[(old_row, old_col)]
#         if target:
#             del self.animals[(new_row, new_col)]

#         animal.row = new_row
#         animal.col = new_col
#         self.animals[(new_row, new_col)] = animal
#         self.turn = 'blue' if self.turn == 'red' else 'red'
#         return True

#     def execute_move(self, animal, to_row, to_col):
#         return self.move_animal(animal, to_row, to_col)
    
#     def traps_owner(self, trap_pos):
#         if trap_pos in [(0, 2), (0, 4), (1, 3)]:
#             return 'blue'
#         elif trap_pos in [(8, 2), (8, 4), (7, 3)]:
#             return 'red'
#         return None
class Animal:
    def __init__(self, name, row, col, team, rank):
        self.name = name
        self.row = row
        self.col = col
        self.team = team  # 'red' or 'blue'
        self.rank = rank  # 1 (mouse) to 8 (elephant)
        self.frozen = False  # 🧊 Mặc định không bị đóng băng

    def position(self):
        return (self.row, self.col)

    def get_rank(self):
        rank_dict = {
            "rat": 1,
            "cat": 2,
            "dog": 3,
            "wolf": 4,
            "leopard": 5,
            "tiger": 6,
            "lion": 7,
            "elephant": 8
        }
        return rank_dict.get(self.name.split("-")[0], 0)


class GameState:
    def __init__(self):
        self.board: list[list[Optional[Animal]]] = [[None for _ in range(7)] for _ in range(9)] 
        self.traps = [(0, 2), (0, 4), (1, 3), (8, 2), (8, 4), (7, 3)]
        self.rivers = [(3, 1), (4, 1), (5, 1),
                       (3, 2), (4, 2), (5, 2),
                       (3, 4), (4, 4), (5, 4),
                       (3, 5), (4, 5), (5, 5)]
        self.dens = {'red': (0, 3), 'blue': (8, 3)}
        self.animals = {}
        self.turn = 'red'
        self.init_animals()

    def init_animals(self):
        setup = [
            ("lion", 0, 0, 'red', 7), ("tiger", 0, 6, 'red', 6),
            ("dog", 1, 1, 'red', 3), ("cat", 1, 5, 'red', 2),
            ("mouse", 2, 0, 'red', 1), ("leopard", 2, 2, 'red', 5),
            ("wolf", 2, 4, 'red', 4), ("elephant", 2, 6, 'red', 8),
            ("lion", 8, 6, 'blue', 7), ("tiger", 8, 0, 'blue', 6),
            ("dog", 7, 5, 'blue', 3), ("cat", 7, 1, 'blue', 2),
            ("mouse", 6, 6, 'blue', 1), ("leopard", 6, 4, 'blue', 5),
            ("wolf", 6, 2, 'blue', 4), ("elephant", 6, 0, 'blue', 8),
        ]

        for name, row, col, team, rank in setup:
            animal = Animal(name, row, col, team, rank)
            self.animals[(row, col)] = animal
            self.board[row][col] = animal

    def is_river(self, row, col):
        return (row, col) in self.rivers

    def is_trap(self, row, col):
        return (row, col) in self.traps

    def can_capture(self, attacker, defender, row=None, col=None):
        if row is None or col is None:
            row, col = defender.row, defender.col

        if (row, col) in self.traps:
            return True

        if attacker.name == 'mouse' and defender.name == 'elephant':
            return True

        if attacker.name == 'elephant' and defender.name == 'mouse':
            return False

        return attacker.get_rank() >= defender.get_rank()

    def is_valid_move(self, animal, new_row, new_col):
        if animal.team != self.turn:
            return False

        if not (0 <= new_row < 9 and 0 <= new_col < 7):
            return False

        if self.dens[animal.team] == (new_row, new_col):
            return False
        
        if animal.frozen:
            return False
        
        # Ngăn các con vật không phải chuột đi vào sông
        if self.is_river(new_row, new_col) and animal.name != 'mouse':
            return False

        target = self.animals.get((new_row, new_col))
        if target:
            if target.team == animal.team:
                return False
            if not self.can_capture(animal, target, new_row, new_col):
                return False

        dr = abs(animal.row - new_row)
        dc = abs(animal.col - new_col)

        if animal.name in ['lion', 'tiger'] and (dr > 1 or dc > 1):
            if animal.row == new_row:
                step = 1 if new_col > animal.col else -1
                for c in range(animal.col + step, new_col, step):
                    if (animal.row, c) not in self.rivers:
                        return False
                    if (animal.row, c) in self.animals:
                        return False
            elif animal.col == new_col:
                step = 1 if new_row > animal.row else -1
                for r in range(animal.row + step, new_row, step):
                    if (r, animal.col) not in self.rivers:
                        return False
                    if (r, animal.col) in self.animals:
                        return False
        else:
            if dr + dc != 1:
                return False

        return True

    def move_animal(self, animal, new_row, new_col):
        old_row, old_col = animal.row, animal.col
        target = self.animals.get((new_row, new_col))

        if target and target.team == animal.team:
            return False

        if not self.is_valid_move(animal, new_row, new_col):
            return False

        # Không cho phép quân đang bị đóng băng (frozen) di chuyển nữa
        if animal.frozen:
            return False
        # Nếu vào bẫy của đối phương thì đóng băng
        if (new_row, new_col) in self.traps and animal.team != self.traps_owner((new_row, new_col)):
            animal.frozen = True
            animal.rank = 0
        # if (old_row, old_col) in self.traps and self.traps_owner((old_row, old_col)) != animal.team:
        #     animal.frozen = False
        # Nếu rời bẫy đối phương: hồi phục rank và bỏ đóng băng
        # elif (old_row, old_col) in self.traps and animal.team != self.traps_owner((old_row, old_col)):
        #     animal.frozen = False
        #     animal.rank = animal.original_rank

        del self.animals[(old_row, old_col)]
        
        if target:                        
            del self.animals[(new_row, new_col)]
            if self.can_capture(animal, target):
                if (new_row, new_col) in self.traps:
                    self.traps.remove((new_row, new_col))        
            


        animal.row = new_row
        animal.col = new_col
        self.animals[(new_row, new_col)] = animal
        self.turn = 'blue' if self.turn == 'red' else 'red'
        return True

    def execute_move(self, animal, to_row, to_col):
        return self.move_animal(animal, to_row, to_col)
    
    def traps_owner(self, trap_pos):
        # if trap_pos in [(0, 2), (0, 4), (1, 3)]:
        #     return 'blue'
        # elif trap_pos in [(8, 2), (8, 4), (7, 3)]:
        #     return 'red'
        # return None
        # Trả về đội chủ của ô bẫy, bên trên là Red (0,2),(0,4),(1,3) - bên dưới là Blue (8,2),(8,4),(7,3)
        red_traps = [(0, 2), (0, 4), (1, 3)]
        blue_traps = [(8, 2), (8, 4), (7, 3)]
        if trap_pos in red_traps:
            return 'red'
        elif trap_pos in blue_traps:
            return 'blue'
        return None
    
    def check_win_condition(self):
        # Chiếm hang
        for team, den_pos in self.dens.items():
            enemy_team = 'blue' if team == 'red' else 'red'
            if self.animals.get(den_pos) and self.animals[den_pos].team == enemy_team:
                self.winner = enemy_team
                return True

        # Không còn quân
        red_exists = any(animal.team == 'red' for animal in self.animals.values())
        blue_exists = any(animal.team == 'blue' for animal in self.animals.values())

        if not red_exists:
            self.winner = 'blue'
            return True
        if not blue_exists:
            self.winner = 'red'
            return True

        return False

