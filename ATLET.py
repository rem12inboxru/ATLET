import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):
        print(f'Силач {name} поднял шар номер {i}')
        await asyncio.sleep(1 / power)
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Иван', 5))
    task2 = asyncio.create_task(start_strongman('Егор', 3))
    task3 = asyncio.create_task(start_strongman('Джамшут', 1))
    await task1
    await task2
    await task3



asyncio.run(start_tournament())
