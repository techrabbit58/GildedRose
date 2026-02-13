from collections.abc import Iterable

from gildedrose.goblincode import Item


class GildedRose(object):

    def __init__(self, items: Iterable[Item]) -> None:
        self.items = items

    def update_quality(self):
        for item in self.items:
            update_one(item)


def update_one(item: Item) -> None:

    if item.name == "Sulfuras, Hand of Ragnaros":
        return

    new_quality = item.quality

    if item.name == "Aged Brie":
        new_quality += 1
    elif item.name == "Backstage passes to a TAFKAL80ETC concert":
        if item.sell_in > 10:
            new_quality += 1
        elif item.sell_in > 5:
            new_quality += 2
        elif item.sell_in > 0:  # not more than 5
            new_quality += 3
    else:
        new_quality -= 1

    if item.sell_in <= 0:
        if item.name == "Aged Brie":
            new_quality += 1
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            new_quality = 0
        else:
            new_quality -= 1

    item.quality = max(0, min(50, new_quality))
    item.sell_in -= 1

