# breakfast.py — послідовно vs паралельно з asyncio
import asyncio
import time

async def make(dish: str, seconds: float) -> str:
    # корутина: «готує» страву і під час чекання не заважає іншим
    print(f"Почав: {dish}")
    await asyncio.sleep(seconds)  # чекаємо, віддаючи керування loop-у
    print(f"Готово: {dish}")
    return dish

async def one_by_one() -> None:
    # кожен await чекає до кінця, перш ніж почати наступну страву
    await make("кава", 1)
    await make("тости", 2)
    await make("яйця", 1.5)

async def all_together() -> None:
    # gather запускає всі три одночасно і чекає на всі
    dishes = await asyncio.gather(
        make("кава", 1), make("тости", 2), make("яйця", 1.5)
    )
    print("На столі:", dishes)

for runner in (one_by_one, all_together):
    start = time.perf_counter()
    asyncio.run(runner())  # створює event loop і виконує корутину
    print(f"{runner.__name__}: {time.perf_counter() - start:.1f} с\n")
