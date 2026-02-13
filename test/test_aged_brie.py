import pytest

from gildedrose.gildedrose import Item, GildedRose


@pytest.fixture
def item() -> Item:
    return Item(name="Aged Brie", sell_in=2, quality=0)


@pytest.mark.parametrize("days_in_stock", [1, 2, 5, 10], scope="module")
def test_aged_brie_quality_increases_with_age(item, days_in_stock):
    original_quality = item.quality
    gr = GildedRose(items=[item])
    for _ in range(days_in_stock):
        gr.update_quality()
    assert item.quality > original_quality


def test_aged_brie_quality_cannot_be_more_than_50(item):
    gr = GildedRose(items=[item])
    days_in_stock = 50 - item.quality + 1
    for _ in range(days_in_stock):
        gr.update_quality()
        assert item.quality <= 50
