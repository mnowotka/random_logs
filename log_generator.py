import random
import time

import faker
from faker.providers import internet
from faker.providers import person


class LogIterator:
    def __init__(self, generator: 'LogGenerator') -> None:
        self.generator = generator
        self.current: int = 0

    def __next__(self) -> str:
        time.sleep(random.randint(0, 5) / 10)
        if self.current == self.generator.count:
            raise StopIteration
        ret = self.generator.generate_log(self.current)
        self.current += 1
        return ret


class LogGenerator:
    def __init__(self, count: int) -> None:
        self.count = count
        self.faker = self._set_up_faker()
        self.names = [self.faker.name() for _ in range(30)]
        self.time_window = 5
        self.names.extend(['Jan Kowalski', 'Mariusz Wiśniewski'])

    def __iter__(self) -> LogIterator:
        return LogIterator(self)

    @staticmethod
    def _set_up_faker() -> faker.Faker:
        result = faker.Faker('pl_PL')
        result.add_provider(person)
        result.add_provider(internet)
        return result

    def generate_log(self, num: int) -> str:
        current = (self.count - num) * self.time_window
        ret = '\t'.join(
            [
                str(self.faker.date_time_between(
                    start_date=f'-{current}m',
                    end_date=f'+{self.time_window}m')),
                random.choice(self.names),
                str(random.randint(-100, 100)),
                self.faker.ipv4_public(),
                self.faker.mac_address()
            ]
        )

        return ret
