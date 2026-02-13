from gildedrose.gildedrose import GildedRose
from gildedrose.goblincode import Item


def test_conjured_degrade_twice_as_fast_as_normal():
    item = Item(name="Conjured Mana Cake", sell_in=3, quality=10)
    gr = GildedRose([item])
    days_in_stock = item.sell_in
    quality = item.quality
    for _ in range(days_in_stock):
        gr.update_quality()
        assert item.quality == quality - 2
        quality = item.quality
    assert item.sell_in == 0
    gr.update_quality()
    assert item.quality == quality - 4
