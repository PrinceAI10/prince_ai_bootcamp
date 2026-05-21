def cheapest_item(prices_dict):
    cheapest_item = None
    cheapest_price = float('inf')
    for item, price in prices_dict.items():
        if item < cheapest_item:
            cheapest_item = item
            cheapest_price = price
        return cheapest_item