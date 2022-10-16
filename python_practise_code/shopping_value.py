def total_value(shopping):
    sub_total=0
    for value in shopping:
         sub_total +=value
    return sub_total

shopping={"eggs":1.20,"chicken":8.20}
print(total_value(shopping.values()))