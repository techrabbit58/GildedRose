from gildedrose.gildedrose import GildedRose
from gildedrose.goblincode import Item


def test_conjured_degrade_twice_as_fast_as_normal():
    item = Item(name="Conjured Mana Cake", sell_in=3, quality=6)
    gr = GildedRose([item])
    quality = item.quality
    while item.quality > 0:
        gr.update_quality()
        assert item.quality == quality - 2
        quality = item.quality
