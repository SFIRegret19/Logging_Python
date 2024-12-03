import logging
import unittest

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", format="%(asctime)s | %(levelname)s | %(message)s", encoding="utf-8")

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, f'Тесты в этом кейсе заморожены. is_frozen = {str(is_frozen)}')
    def test_walk(self):
        try:
            runner = Runner('Гриша', -5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, f'Тесты в этом кейсе заморожены. is_frozen = {str(is_frozen)}')
    def test_run(self):
        try:
            runner = Runner(535, 35)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 700)
            logging.info(f'"test_run" выполнен успешно')
        except:
            logging.warning(f'Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, f'Тесты в этом кейсе заморожены. is_frozen = {str(is_frozen)}')
    def test_challenge(self):
        runner1 = Runner('Гриша')
        runner2 = Runner('Петя')

        for _ in range(10):
            runner1.walk()

        for _ in range(10):
            runner2.run()

        self.assertNotEqual(runner1.distance, runner2.distance)

testTS = unittest.TestSuite()
testTS.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testTS)