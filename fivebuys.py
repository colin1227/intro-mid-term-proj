
# func defs

# Type checking:
# - names can't start with a number
# - values must be a number

def is_a_valid_amount(value):
  # only 1 decimal place
  if value.count('.') > 1:
    return False
  
  # input has to be something
  if len(value) < 1:
    return False
  
  # numbers only with the excpetion on decimals
  for i in range(len(value)):
    if is_character_a_number(value, i) != True and value[i] != '.':
      return False
  return True

def is_character_a_number(value, index=0):
  if value[index] in '0123456789':
    return True
  else:
    return False


# handles type checking
def get_values(item_number):
  item_name = ''
  name_is_valid = 'NO_INPUT'
  amount = 0
  amount_is_valid = 'NO_INPUT'

  # loop until name is good
  while name_is_valid != 'VALID_INPUT':
    prompt = ''
    if name_is_valid == 'NO_INPUT':
      prompt = f'what would you like to buy for item #{item_number}?:'
    elif name_is_valid == 'INVALID_INPUT':
      prompt = 'That wasn\'t a valid name, Try again:'

    item_name = input(prompt)
    
    if len(item_name) < 1:
      name_is_valid = 'INVALID_INPUT'
    elif is_character_a_number(item_name) == False:
      name_is_valid = 'VALID_INPUT'
    else:
      name_is_valid = 'INVALID_INPUT'

  # loop until amount is good
  while amount_is_valid != 'VALID_INPUT':
    prompt = ''
    if amount_is_valid == 'NO_INPUT':
      prompt = 'and how much is this item?:'
    elif amount_is_valid == 'INVALID_INPUT':
      prompt = 'Thats not a valid number, Try again:'

    amount = input(prompt)
    
    if is_a_valid_amount(amount):
      amount_is_valid = 'VALID_INPUT'
      amount = round(float(amount), 2)
    else:
      amount_is_valid = 'INVALID_INPUT'
  return [item_name, amount]


print('Welcome to Five Buys!')

# 10 inputs:
# - 5 names
# - 5 values

item_1 = get_values(1)
item_2 = get_values(2)
item_3 = get_values(3)
item_4 = get_values(4)
item_5 = get_values(5)

def item_name_and_price(item_object):
  print(item_object[0], end='')
  print('          $', end='')
  print(format(item_object[1], '.2f'))


item_name_and_price(item_1)
item_name_and_price(item_2)
item_name_and_price(item_3)
item_name_and_price(item_4)
item_name_and_price(item_5)

print('-------------------------------------------')

# sub total
sub_total = item_1[1] + item_2[1] + item_3[1] + item_4[1] + item_5[1]
print('Sub total: ', end='')
print(format(sub_total, '.2f'))


# sales tax 7%
sales_tax = sub_total * 0.07
print('Sales tax: ', end='')
print(format(sales_tax, '.2f'))

# Your total is:
your_total = sub_total + sales_tax
print('Your total is: ', end='')
print(your_total)
print('-------------------------------------------')

# Cash received
is_paid_cash_value_valid = 'NO_INPUT'
cash_recieved = 0
change_due = 0

while is_paid_cash_value_valid != 'VALID_INPUT':
    prompt = 'How much cash do you give the chashier?:'
    if is_paid_cash_value_valid == 'INVALID_INPUT':
      prompt = 'Sorry but we cant take this, try again:'
    cash_recieved = input(prompt)
    # 0.00 round

    if is_a_valid_amount(cash_recieved) == True:
      cash_recieved = round(float(cash_recieved), 2)
      if cash_recieved >= your_total:
        is_paid_cash_value_valid = 'VALID_INPUT'
        change_due = float(cash_recieved) - your_total
      else:
        is_paid_cash_value_valid = 'INVALID_INPUT'
    else:
      is_paid_cash_value_valid = 'INVALID_INPUT'

print('-------------------------------------------')
print('Cash recieved          $', end='')
print(format(round(float(cash_recieved), 2), '.2f'))

print('Change due:            $', end='')
print(format(round(change_due, 2), '.2f'))
print('-------------------------------------------')
print('Thank you for shopping at FIVE BUYS!')

# (end)
