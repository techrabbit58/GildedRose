import pytest

from gildedrose.gildedrose import GildedRose
from gildedrose.goblincode import Item


def normal_items() -> list[Item]:
    return [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
    ]


@pytest.mark.parametrize("item", normal_items())
def test_normal_item_sell_in_and_quality_decreases_by_one_every_day(item):
    sell_in = item.sell_in
    quality = item.quality
    gr = GildedRose([item])
    while item.sell_in > 0 and item.quality > 0:
        gr.update_quality()
        assert item.sell_in == sell_in - 1 and item.quality == quality - 1
        sell_in = item.sell_in
        quality = item.quality


@pytest.mark.parametrize("item", normal_items())
def test_normal_item_minimum_quality_is_0_and_never_negative(item):
    gr = GildedRose([item])
    days_in_stock = max(item.quality + 1, item.sell_in + 1)
    for _ in range(days_in_stock):
        gr.update_quality()
        assert item.quality >= 0
    assert item.quality == 0


@pytest.mark.parametrize("item", normal_items())
def test_normal_item_double_decrease_quality_after_sell_by(item):
    gr = GildedRose([item])
    days_in_stock = item.sell_in
    quality = item.quality
    for _ in range(days_in_stock):
        gr.update_quality()
        assert item.quality == quality - 1
        quality = item.quality
    assert item.sell_in == 0
    gr.update_quality()
    assert item.quality == quality - 2
