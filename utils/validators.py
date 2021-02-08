from typing import Type


def validate_type(key: str, value: object, type: Type) -> object:
    if not isinstance(value, type):
        raise TypeError(f'{key.capitalize()} must be {type}!')
    return value

def validate_not_empty(key: str, value: str) -> str:
    if not value.strip():
        raise ValueError(f'{key.capitalize()} cannot be empty!')
    return value

def validate_max_length(key: str, value: object, max_len: int) -> object:
    if len(value) > max_len:
        raise ValueError(f'{key.capitalize()} cannot be greater than {max_len}!')
    return value

def validate_characteres_equal_to(key: str, value: object, char_size: int) -> object:
    if len(value) == char_size:
        return value
    else:
        raise ValueError(f'{key.capitalize()} must be equal to {char_size}!')

def validate_number_greater_than_zero(key: str, value: float) -> float:
    if value <= 0:
        raise ValueError(f'{key.capitalize()} value must be greater than 0!')
    return value
