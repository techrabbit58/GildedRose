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

    if item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert":
        if item.quality < 50:
            item.quality += 1
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in <= 10 and item.quality < 50:
                    item.quality += 1
                if item.sell_in <= 5 and item.quality < 50:
                    item.quality += 1
    else:
        if item.quality > 0:
            item.quality -= 1

    item.sell_in -= 1

    if item.sell_in < 0:
        if item.name == "Aged Brie":
            if item.quality < 50:
                item.quality += 1
        else:
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.quality = 0
            else:
                if item.quality > 0:
                    item.quality -= 1
