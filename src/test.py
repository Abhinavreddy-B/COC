import unittest

from king import spawnKing
import points as pt
import village

config = pt.config
class TestMove(unittest.TestCase):
    def setUp(self):
        self.V = village.Village(config, 1)
        map = self.V.generate_map()
        self.V.update_map(map)
        (self.maxX, self.maxY) = config['dimensions']

    def test_unknown_direction(self):
        self.king = king = spawnKing((3, 3))
        king.move('unknown', self.V)
        self.assertEqual(king.position, [3, 3],
                         'moving even with unknown direction')

    def test_move_up(self):
        self.king = king = spawnKing((3, 3))
        king.move('up', self.V)
        self.assertEqual(king.position, [2, 3], 'moving up')
        self.assertEqual(king.facing,'up')

    def test_move_up_edge(self):
        self.king = king = spawnKing((0, 3))
        king.move('up', self.V)
        self.assertEqual(king.position, [0, 3], 'moving up edge')
        self.assertEqual(king.facing,'up')

    def test_move_down(self):
        self.king = king = spawnKing((3, 3))
        king.move('down', self.V)
        self.assertEqual(king.position, [4, 3], 'moving down')
        self.assertEqual(king.facing,'down')

    def test_move_down_edge(self):
        self.king = king = spawnKing((self.maxX - 1, 3))
        king.move('down', self.V)
        self.assertEqual(king.position, [self.maxX - 1, 3], 'moving down edge')
        self.assertEqual(king.facing,'down')

    def test_move_left(self):
        self.king = king = spawnKing((3, 3))
        king.move('left', self.V)
        self.assertEqual(king.position, [3, 2], 'moving left')
        self.assertEqual(king.facing,'left')

    def test_move_left_edge(self):
        self.king = king = spawnKing((3, 0))
        king.move('left', self.V)
        self.assertEqual(king.position, [3, 0], 'moving left edge')
        self.assertEqual(king.facing,'left')

    def test_move_right(self):
        self.king = king = spawnKing((3, 3))
        king.move('right', self.V)
        self.assertEqual(king.position, [3, 4], 'moving right')
        self.assertEqual(king.facing,'right')

    def test_move_right_edge(self):
        self.king = king = spawnKing((3, self.maxY - 1))
        king.move('right', self.V)
        self.assertEqual(king.position, [3, self.maxY - 1], 'moving right edge')
        self.assertEqual(king.facing,'right')
    
    def test_move_up_spawn_point(self):
        self.king = king = spawnKing((1, 0))
        king.move('up', self.V)
        self.assertEqual(king.position, [0, 0], 'moving up when spawn point')
        self.assertEqual(king.facing,'up')
    
    def test_move_down_spawn_point(self):
        self.king = king = spawnKing((self.maxX - 2, 0))
        king.move('down', self.V)
        self.assertEqual(king.position, [self.maxX - 1, 0], 'moving down when spawn point')
        self.assertEqual(king.facing,'down')
    
    def test_move_left_spawn_point(self):
        self.king = king = spawnKing((0, 1))
        king.move('left', self.V)
        self.assertEqual(king.position, [0, 0], 'moving left when spawn point')
        self.assertEqual(king.facing,'left')
    
    def test_move_right_spawn_point(self):
        self.king = king = spawnKing((0, self.maxY - 2))
        king.move('right', self.V)
        self.assertEqual(king.position, [0, self.maxY - 1], 'moving right when spawn point')
        self.assertEqual(king.facing,'right')
    
    def test_move_up_blocked_hut(self):
        self.king = king = spawnKing((7,11))
        king.move('up', self.V)
        self.assertEqual(king.position, [7,11], 'moving up when blocked')
        self.assertEqual(king.facing,'up')
    
    def test_move_down_blocked_hut(self):
        self.king = king = spawnKing((5,11))
        king.move('down', self.V)
        self.assertEqual(king.position, [5,11], 'moving down when blocked')
        self.assertEqual(king.facing,'down')
    
    def test_move_left_blocked_hut(self):
        self.king = king = spawnKing((6,12))
        king.move('left', self.V)
        self.assertEqual(king.position, [6,12], 'moving left when blocked')
        self.assertEqual(king.facing,'left')
    
    def test_move_right_blocked_hut(self):
        self.king = king = spawnKing((6,10))
        king.move('right', self.V)
        self.assertEqual(king.position, [6,10], 'moving right when blocked')
        self.assertEqual(king.facing,'right')

    def test_move_up_blocked_cannon(self):
        self.king = king = spawnKing((12,22))
        king.move('up', self.V)
        self.assertEqual(king.position, [12,22], 'moving up when blocked')
        self.assertEqual(king.facing,'up')
    
    def test_move_down_blocked_cannon(self):
        self.king = king = spawnKing((9,22))
        king.move('down', self.V)
        self.assertEqual(king.position, [9,22], 'moving down when blocked')
        self.assertEqual(king.facing,'down')
    
    def test_move_left_blocked_cannon(self):
        self.king = king = spawnKing((10,24))
        king.move('left', self.V)
        self.assertEqual(king.position, [10,24], 'moving left when blocked')
        self.assertEqual(king.facing,'left')
    
    def test_move_right_blocked_cannon(self):
        self.king = king = spawnKing((10,21))
        king.move('right', self.V)
        self.assertEqual(king.position, [10,21], 'moving right when blocked')
        self.assertEqual(king.facing,'right')
    
    def test_move_up_blocked_wall(self):
        self.king = king = spawnKing((4,10))
        king.move('up', self.V)
        self.assertEqual(king.position, [4,10], 'moving up when blocked')
        self.assertEqual(king.facing,'up')
    
    def test_move_down_blocked_wall(self):
        self.king = king = spawnKing((2,10))
        king.move('down', self.V)
        self.assertEqual(king.position, [2,10], 'moving down when blocked')
        self.assertEqual(king.facing,'down')
    
    def test_move_left_blocked_wall(self):
        self.king = king = spawnKing((4,10))
        king.move('left', self.V)
        self.assertEqual(king.position, [4,10], 'moving left when blocked')
        self.assertEqual(king.facing,'left')
    
    def test_move_right_blocked_wall(self):
        self.king = king = spawnKing((4,8))
        king.move('right', self.V)
        self.assertEqual(king.position, [4,8], 'moving right when blocked')
        self.assertEqual(king.facing,'right')
    
    def test_move_up_blocked_wiz_tower(self):
        self.king = king = spawnKing((8,27))
        king.move('up', self.V)
        self.assertEqual(king.position, [8,27], 'moving up when blocked')
        self.assertEqual(king.facing,'up')
    
    def test_move_down_blocked_wiz_tower(self):
        self.king = king = spawnKing((6,27))
        king.move('down', self.V)
        self.assertEqual(king.position, [6,27], 'moving down when blocked')
        self.assertEqual(king.facing,'down')
    
    def test_move_left_blocked_wiz_tower(self):
        self.king = king = spawnKing((7,28))
        king.move('left', self.V)
        self.assertEqual(king.position, [7,28], 'moving left when blocked')
        self.assertEqual(king.facing,'left')
    
    def test_move_right_blocked_wiz_tower(self):
        self.king = king = spawnKing((7,26))
        king.move('right', self.V)
        self.assertEqual(king.position, [7,26], 'moving right when blocked')
        self.assertEqual(king.facing,'right')

    def test_move_up_blocked_townhall(self):
        self.king = king = spawnKing((10,16))
        king.move('up', self.V)
        self.assertEqual(king.position, [10,16], 'moving up when blocked')
        self.assertEqual(king.facing,'up')
    
    def test_move_down_blocked_townhall(self):
        self.king = king = spawnKing((5,16))
        king.move('down', self.V)
        self.assertEqual(king.position, [5,16], 'moving up when blocked')
        self.assertEqual(king.facing,'down')
    
    def test_move_left_blocked_townhall(self):
        self.king = king = spawnKing((6,19))
        king.move('left', self.V)
        self.assertEqual(king.position, [6,19], 'moving down when blocked')
        self.assertEqual(king.facing,'left')
    
    def test_move_right_blocked_townhall(self):
        self.king = king = spawnKing((6,15))
        king.move('right', self.V)
        self.assertEqual(king.position, [6,15], 'moving down when blocked')
        self.assertEqual(king.facing,'right')

    def test_move_left_blocked_townhall(self):
        self.king = king = spawnKing((6,15))
        
        
    def tearDown(self):
        self.assertEqual(pt.HERO_POS,self.king.position)
class TestMoveSpeed(unittest.TestCase):
    def setUp(self):
        self.V = village.Village(config, 1)
        map = self.V.generate_map()
        self.V.update_map(map)
        (self.maxX, self.maxY) = config['dimensions']
    
    def test_move_up(self):
        self.king = king = spawnKing((3, 3))
        king.speed = 2
        king.move('up', self.V)
        self.assertEqual(king.position, [1,3] , 'moving up')
        self.assertEqual(king.speed, 2, 'speed')
    
    def test_move_down(self):
        self.king = king = spawnKing((3, 3))
        king.speed = 2
        king.move('down', self.V)
        self.assertEqual(king.position, [5,3] , 'moving down')
        self.assertEqual(king.speed, 2, 'speed')
    
    def test_move_left(self):
        self.king = king = spawnKing((3, 3))
        king.speed = 2
        king.move('left', self.V)
        self.assertEqual(king.position, [3,1] , 'moving left')
        self.assertEqual(king.speed, 2, 'speed')
    
    def test_move_right(self):
        self.king = king = spawnKing((1, 1))
        king.speed = 2
        king.move('right', self.V)
        self.assertEqual(king.position, [1,3] , 'moving right')
        self.assertEqual(king.speed, 2, 'speed')
    
    def test_move_up_edge(self):
        self.king = king = spawnKing((3, 3))

        king.speed = 4
        king.move('up', self.V)
        self.assertEqual(king.position, [0,3] , 'moving up edge')
        self.assertEqual(king.speed, 4, 'speed')
    
    def test_move_down_edge(self):
        self.king = king = spawnKing((self.maxX - 3,  3))
        king.speed = 4
        king.move('down', self.V)
        self.assertEqual(king.position, [self.maxX - 1,3] , 'moving down edge')
        self.assertEqual(king.speed, 4, 'speed')
    
    def test_move_left_edge(self):
        self.king = king = spawnKing((3, 3))
        king.speed = 4
        king.move('left', self.V)
        self.assertEqual(king.position, [3,0] , 'moving left edge')
        self.assertEqual(king.speed, 4, 'speed')
    
    def test_move_right_edge(self):
        self.king = king = spawnKing((1, self.maxY - 3))
        king.speed = 4
        king.move('right', self.V)
        self.assertEqual(king.position, [1,self.maxY - 1] , 'moving right edge')
        self.assertEqual(king.speed, 4, 'speed')

    def test_move_up_blocked_hut(self):
        self.king = king = spawnKing((9,11))
        king.speed = 4
        king.move('up', self.V)
        self.assertEqual(king.position, [8,11], 'moving up when blocked')
        self.assertEqual(king.speed, 4, 'speed')
    
    def test_move_down_blocked_hut(self):
        self.king = king = spawnKing((4,11))
        king.speed = 4
        king.move('down', self.V)
        self.assertEqual(king.position, [5,11], 'moving down when blocked')
        self.assertEqual(king.speed, 4, 'speed')
    
    def test_move_left_blocked_hut(self):
        self.king = king = spawnKing((6,14))
        king.speed = 4
        king.move('left', self.V)
        self.assertEqual(king.position, [6,13], 'moving left when blocked')
        self.assertEqual(king.speed, 4, 'speed')
    
    def test_move_right_blocked_hut(self):
        self.king = king = spawnKing((6,9))
        king.speed = 4
        king.move('right', self.V)
        self.assertEqual(king.position, [6,10], 'moving right when blocked')
        self.assertEqual(king.speed, 4, 'speed')
    
    def test_move_up_blocked_cannon(self):
        self.king = king = spawnKing((14,22))
        king.speed =5
        king.move('up', self.V)
        self.assertEqual(king.position, [12,22], 'moving up when blocked')
        self.assertEqual(king.speed, 5, 'speed')
    
    def test_move_down_blocked_cannon(self):
        self.king = king = spawnKing((7,22))
        king.speed =5
        king.move('down', self.V)
        self.assertEqual(king.position, [9,22], 'moving down when blocked')
        self.assertEqual(king.speed, 5, 'speed')

    def test_move_left_blocked_cannon(self):
        self.king = king = spawnKing((10,26))
        king.speed =5
        king.move('left', self.V)
        self.assertEqual(king.position, [10,24], 'moving left when blocked') 
        self.assertEqual(king.speed, 5, 'speed')
    
    def test_move_right_blocked_cannon(self):
        self.king = king = spawnKing((10,19))
        king.speed =5
        king.move('right', self.V)
        self.assertEqual(king.position, [10,21], 'moving right when blocked')
        self.assertEqual(king.speed, 5, 'speed')
    
    def test_move_up_blocked_wizard_tower(self):
        self.king = king = spawnKing((10,27))
        king.speed =5
        king.move('up', self.V)
        self.assertEqual(king.position, [8,27], 'moving up when blocked')
        self.assertEqual(king.speed, 5, 'speed')
    
    def test_move_down_blocked_wizard_tower(self):
        self.king = king = spawnKing((4,27))
        king.speed =5
        king.move('down', self.V)
        self.assertEqual(king.position, [6,27], 'moving down when blocked')
        self.assertEqual(king.speed, 5, 'speed')
    
    def test_move_left_blocked_wizard_tower(self):
        self.king = king = spawnKing((7,30))
        king.speed =5
        king.move('left', self.V)
        self.assertEqual(king.position, [7,28], 'moving left when blocked')
    
    def test_move_right_blocked_wizard_tower(self):
        self.king = king = spawnKing((17,24))
        king.speed =5
        king.move('right', self.V)
        self.assertEqual(king.position, [17,26], 'moving right when blocked')

    def test_move_up_town_hall(self):
        self.king = king = spawnKing((13,16))
        king.speed =10
        king.move('up', self.V)
        self.assertEqual(king.position, [10,16], 'moving up when blocked')
        self.assertEqual(king.speed, 10, 'speed')
    
    def test_move_down_town_hall(self):
        self.king = king = spawnKing((4,16))
        king.speed =10
        king.move('down', self.V)
        self.assertEqual(king.position, [5,16], 'moving down when blocked')
        self.assertEqual(king.speed, 10, 'speed')

    def test_move_left_town_hall(self):
        self.king = king = spawnKing((6,21))
        king.speed =10
        king.move('left', self.V)
        self.assertEqual(king.position, [6,19], 'moving left when blocked')
        self.assertEqual(king.speed, 10, 'speed')
    
    def test_move_right_town_hall(self):
        self.king = king = spawnKing((6,14))
        king.speed =10
        king.move('right', self.V)
        self.assertEqual(king.position, [6,15], 'moving right when blocked')
        self.assertEqual(king.speed, 10, 'speed')

    def test_move_up_wall(self):
        self.king = king = spawnKing((5,10))
        king.speed = 5
        king.move('up', self.V)
        self.assertEqual(king.position,[4,10], 'moving up when blocked')
        self.assertEqual(king.speed, 5, 'speed')
    
    def test_move_down_wall(self):
        self.king = king = spawnKing((1,10))
        king.speed = 5
        king.move('down', self.V)
        self.assertEqual(king.position,[2,10], 'moving down when blocked')
        self.assertEqual(king.speed, 5, 'speed')

    def test_move_right_wall(self):
        self.king = king = spawnKing((4,7))
        king.speed = 5
        king.move('right', self.V)
        self.assertEqual(king.position,[4,8], 'moving left when blocked')
        self.assertEqual(king.speed, 5, 'speed')

    def test_move_left_wall(self):
        self.king = king = spawnKing((4,11))
        king.speed = 5
        king.move('left', self.V)
        self.assertEqual(king.position,[4,10], 'moving right when blocked')
        self.assertEqual(king.speed, 5, 'speed')

    def tearDown(self):
        self.assertEqual(pt.HERO_POS, self.king.position)
class TestDead(unittest.TestCase):
    def setUp(self):
        self.V = village.Village(config, 1)
        map = self.V.generate_map()
        self.V.update_map(map)
        (self.maxX, self.maxY) = config['dimensions']
    
    def test_dead(self):
        directions = ['up', 'down', 'left', 'right']
        for direction in directions:
            for beforeDirection in directions:
                self.king = king = spawnKing((3, 4))
                king.facing = beforeDirection
                king.kill()
                king.move(direction, self.V)
                self.assertEqual(king.position, [3, 4], 'moving when dead')
                self.assertEqual(king.facing, beforeDirection)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    
    # run the tests using the TextTestRunner object
    result = runner.run(unittest.defaultTestLoader.loadTestsFromModule(__import__(__name__)))

    # write "TRUE" to the file if all tests passed, else write "FALSE"
    with open('./output.txt', 'w') as f:
        f.write('True' if result.wasSuccessful() else 'False')
