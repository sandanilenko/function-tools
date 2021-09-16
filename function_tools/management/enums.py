from enum import Enum


class ImplementationStrategyEnum(Enum):
    """
    Перечисление стратегий реализации функций
    """

    BASE_RUNNER_BASE_FUNCTION = 1
    BASE_RUNNER_LAZY_SAVING_PREDEFINED_QUEUE_FUNCTION = 2
    LAZY_SAVING_RUNNER_LAZY_DELEGATE_SAVING_PREDEFINED_QUEUE_FUNCTION = 3


class FunctionTypeEnum(Enum):
    """
    Тип исполнения функции
    """

    SYNC = 1
    ASYNC = 2
