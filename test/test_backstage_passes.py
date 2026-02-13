import pytest

from gildedrose.gildedrose import Item, GildedRose


def backstage_passes() -> list[Item]:
    return [
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
    ]


@pytest.mark.parametrize("item", backstage_passes())
def test_backstage_pass_minimum_quality_is_0_and_never_negative(item):
    gr = GildedRose([item])
    days_in_stock = max(item.quality + 1, item.sell_in + 1)
    for _ in range(days_in_stock):
        gr.update_quality()
        assert item.quality >= 0
    assert item.quality == 0


@pytest.mark.parametrize("item", backstage_passes())
def test_backstage_pass_quality_cannot_be_more_than_50(item):
    gr = GildedRose(items=[item])
    days_in_stock = 50 - item.quality + 1
    for _ in range(days_in_stock):
        gr.update_quality()
        assert item.quality <= 50


@pytest.mark.parametrize("item", backstage_passes())
def test_backstage_pass_quality_is_0_after_sell_by_date(item):
    gr = GildedRose(items=[item])
    while item.sell_in > 0:  # keep in stock until concert
        gr.update_quality()
    for _ in range(3):  # watch for three more days
        gr.update_quality()
        assert item.quality == 0


def test_backstage_pass_quality_increase_by_1_if_more_than_10_days_left():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)
    gr = GildedRose(items=[item])
    quality = item.quality
    gr.update_quality()
    assert item.quality == quality + 1


def test_backstage_pass_quality_increase_by_2_if_more_than_5_and_up_to_10_days_left():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)
    gr = GildedRose(items=[item])
    quality = item.quality
    gr.update_quality()
    assert item.quality == quality + 2


def test_backstage_pass_quality_increase_by_3_if_up_to_5_days_left():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)
    gr = GildedRose(items=[item])
    quality = item.quality
    gr.update_quality()
    assert item.quality == quality + 3
