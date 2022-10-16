def food_bill():
    shoppin_items={"eggs":1.85,"bread":1.50,"peppers":0.90}

    print(shoppin_items.values())

    print("The total bill is :"+str(sum(shoppin_items.values())))

food_bill()