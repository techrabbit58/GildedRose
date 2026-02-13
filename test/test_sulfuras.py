import pytest

from gildedrose.gildedrose import Item, GildedRose


def sulfuras() -> list[Item]:
    return [
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
    ]


@pytest.mark.parametrize("item", sulfuras())
@pytest.mark.parametrize("days_in_stock", [1, 10, 100], scope="module")
@pytest.mark.parametrize("expected_quality", [80], scope="module")  # quality is always 80
def test_sulfuras_does_not_change_in_quality(item, days_in_stock, expected_quality):
    gr = GildedRose(items=[item])
    for _ in range(days_in_stock):
        gr.update_quality()
    assert item.quality == expected_quality
