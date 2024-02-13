def expenses_by_category(file_name: str) -> dict:
    """
    Returns a dictionary with the total expenses by category.

    :param file_name: the name of the file to read
    :return: a dictionary with the total expenses by category
    """
    result = {}
    with open(file_name) as file:
        for line in file:
            *_, price, category = line.split()
            price = price.replace('$', '')
            price = float(price)
            if category in result:
                result[category] += price
            else:
                result[category] = price
    return result




def expenses_by_users(file_name: str) -> dict:
    """
    Returns a dictionary with the total expenses by user.

    :param file_name: the name of the file to read
    :return: a dictionary with the total expenses by user
    """
    ...