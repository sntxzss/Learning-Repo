import asyncio
import time

async def make(dish: str, seconds: float) -> str:
    print(f"Почав: {dish}")
    await asyncio.sleep(seconds) 
    print(f"Готово: {dish}")
    return dish

async def one_by_one() -> None:
    await make("кава", 1)
    await make("тости", 2)
    await make("яйця", 1.5)

async def all_together() -> None:
    dishes = await asyncio.gather(
        make("кава", 1), make("тости", 2), make("яйця", 1.5)
    )
    print("На столі:", dishes)

for runner in (one_by_one, all_together):
    start = time.perf_counter()
    asyncio.run(runner()) 
    print(f"{runner.__name__}: {time.perf_counter() - start:.1f} с\n")
