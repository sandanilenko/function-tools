from enum import (
    Enum,
)


class FunctionTypeEnum(Enum):
    """
    Тип исполнения функции
    """

    SYNC = 1
    ASYNC = 2
