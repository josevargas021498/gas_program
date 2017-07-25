def inventory():
    inventory = [
        ['regular', 2.0],
        ['midgrade', 2.24],
        ['premium', 3.0]
    ]
    return(inventory)



def type_of_gas_total(total):

    type_of_gas = {'regular': 2.0, 'midgrade': 2.24, 'premium': 3.0}
    type_of_gas_total = type_of_gas * amount_paying
    return (type_of_gas_total)
