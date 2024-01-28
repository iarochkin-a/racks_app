import logging


def print_name_of_def(func):
    def wrapper(self, *args):
        logging.basicConfig(level=logging.INFO)
        logging.info(f'Function {func.__name__} was called.')
        result = func(self, *args)
        return result
    return wrapper


def change_last_num(func):
    def wrapper(self, *args):
        args[0][-1] *= self.num
        result = func(self, *args)
        return result
    return wrapper


def reverse_list(func):
    def wrapper(self, *args):
        if self.is_reverse:
            args[0].reverse()
        result = func(self, *args)
        return result
    return wrapper


class CalculatorService:

    def __init__(self, num: int,  is_reverse: bool):
        self.is_reverse = is_reverse
        self.num = num

    @reverse_list
    @change_last_num
    @print_name_of_def
    async def sum(self, variables: list) -> int:
        res = sum(variables)
        result = {
            'variables': variables,
            'result': res
        }
        return result

    @reverse_list
    @change_last_num
    @print_name_of_def
    async def minus(self, variables: list) -> int:
        res = variables[0] - sum(variables[1::])
        result = {
            'variables': variables,
            'result': res
        }
        return result

    @reverse_list
    @change_last_num
    @print_name_of_def
    async def product(self, variables: list) -> int:
        res = 1
        for num in variables:
            res *= num
        result = {
            'variables': variables,
            'result': res
        }
        return result

    @reverse_list
    @change_last_num
    @print_name_of_def
    async def quotient(self, variables: list) -> float:
        res = variables[0]
        for num in variables[1::]:
            if num == 0:
                raise ZeroDivisionError('ZeroDivisionError, you cant division by zero')
            res /= num
        result = {
            'variables': variables,
            'result': res
        }
        return result
