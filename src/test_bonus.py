
import unittest

from king import spawnKing
import points as pt
import village

config = pt.config

class TestAttack(unittest.TestCase):
    def setUp(self):
        self.V = village.Village(config, 1)
        self.king = spawnKing((0, 0))
        self.targets = list(self.V.hut_objs.values()) + list(self.V.cannon_objs.values()) + list(self.V.wizard_tower_objs.values()) + list(self.V.wall_objs.values()) + [self.V.town_hall_obj] 
        self.kingHealthInitial = self.king.health

    def test_dead_less_health(self):
        self.king.kill()
        for target in self.targets:
            initialhealth = target.health
            self.king.attack_target(target, target.health - 5)
            self.assertEqual(target.health, initialhealth, 'attacking when dead')

    def test_dead_more_health(self):
        self.king.kill()
        for target in self.targets:
            initialhealth = target.health
            self.king.attack_target(target, target.health + 5)
            self.assertEqual(target.health, initialhealth, 'attacking when dead')

    def test_normal_less_health(self):
        for target in self.targets:
            self.king.attack_target(target, target.health - 5)
            self.assertEqual(target.health, 5, 'attacking normal')
            self.assertEqual(target.destroyed, False, 'not destroying normal')
            self.assertEqual(self.king.health,
                         self.kingHealthInitial, 'attacking itself')
            self.assertEqual(self.king.alive, True, 'destroying itself')

    def test_normal_more_health(self):
        for target in self.targets:
            self.king.attack_target(target, target.health + 5)
            self.assertEqual(target.health, 0, 'attacking normal')
            self.assertEqual(target.destroyed, True)
            self.assertEqual(self.king.health, self.kingHealthInitial, 'attacking itself')
            self.assertEqual(self.king.alive, True, 'destroying itself')

    def test_normal_exact_health(self):
        for target in self.targets:
            self.king.attack_target(target, target.health)
            self.assertEqual(target.health, 0, 'attacking normal')
            self.assertEqual(target.destroyed, True)
            self.assertEqual(self.king.health, self.kingHealthInitial, 'attacking itself')
            self.assertEqual(self.king.alive, True, 'destroying itself')

    def test_destroyed_buidings(self):
        for target in self.targets:
            target.destroyed = True
            target.health = 0
            self.king.attack_target(target, 10)
            self.assertEqual(target.health, 0, 'attacking destroyed buildings')
            self.assertEqual(target.destroyed, True)
            self.assertEqual(self.king.health, self.kingHealthInitial, 'attacking itself')
            self.assertEqual(self.king.alive, True, 'destroying itself')


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    
    # run the tests using the TextTestRunner object
    result = runner.run(unittest.defaultTestLoader.loadTestsFromModule(__import__(__name__)))

    # write "TRUE" to the file if all tests passed, else write "FALSE"
    with open('./output_bonus.txt', 'w') as f:
        f.write('True' if result.wasSuccessful() else 'False')