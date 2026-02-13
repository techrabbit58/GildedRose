from collections.abc import Iterable

from gildedrose.goblincode import Item


class GildedRose:

    def __init__(self, items: Iterable[Item]) -> None:
        self.items = items

    def update_quality(self):
        for item in self.items:
            update_one(item)


def update_one(item: Item) -> None:

    if item.name.startswith("Sulfuras"):
        return

    new_quality = item.quality
    normal_delta = 1 if item.sell_in > 0 else 2

    if item.name.startswith("Aged Brie"):
        new_quality += normal_delta
    elif item.name.startswith("Backstage passes"):
        if item.sell_in > 10:
            new_quality += 1
        elif item.sell_in > 5:
            new_quality += 2
        elif item.sell_in > 0:
            new_quality += 3
        else:
            new_quality = 0
    elif item.name.startswith("Conjured"):
        new_quality -= normal_delta * 2
    else:
        new_quality -= normal_delta

    item.quality = max(0, min(50, new_quality))
    item.sell_in -= 1

