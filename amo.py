amount = 650 
print("your amount is :650")
five_hundred_notes = amount // 500
remaining_balance = amount % 500
hundred_notes = remaining_balance // 100
remaining_balance = remaining_balance % 100
fifty_notes = remaining_balance // 50
remaining_balance = remaining_balance % 50
ten_notes = remaining_balance // 10
remaining_balance = remaining_balance % 10
print("500 notes:", five_hundred_notes)
print("100 notes:", hundred_notes)
print("50 notes:", fifty_notes)
print("10 notes:", ten_notes)
print("Remaining balance:", remaining_balance)


