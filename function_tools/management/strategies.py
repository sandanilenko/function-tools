from abc import (
    ABCMeta,
)

from enum import Enum

from function_tools.caches import (
    CacheStorage,
)
from function_tools.errors import (
    BaseError,
)
from function_tools.functions import (
    BaseFunction, LazySavingPredefinedQueueFunction, LazyDelegateSavingPredefinedQueueFunction,
)
from function_tools.helpers import (
    BaseFunctionHelper,
    BaseRunnerHelper,
)
from function_tools.management.enums import ImplementationStrategyEnum
from function_tools.management.signals import implementation_strategy_factory_after_init_signal
from function_tools.managers import (
    RunnerManager,
)
from function_tools.presenters import (
    ResultPresenter,
)
from function_tools.results import (
    BaseRunnableResult,
)
from function_tools.runners import (
    BaseRunner, LazySavingRunner,
)
from function_tools.validators import (
    BaseValidator,
)


class FunctionImplementationStrategy(metaclass=ABCMeta):
    """
    Базовый класс стратегии реализации функции
    """

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        self._manager_class = None
        self._runner_class = None
        self._function_class = None
        self._runner_helper_class = None
        self._function_helper_class = None
        self._runner_validator_class = None
        self._function_validator_class = None
        self._runner_cache_storage_class = None
        self._function_cache_storage_class = None
        self._error_class = None
        self._result_class = None
        self._result_presenter_class = None

        self._prepare()

    @property
    def manager_class(self):
        return self._manager_class

    @property
    def runner_class(self):
        return self._runner_class

    @property
    def function_class(self):
        return self._function_class

    @property
    def runner_helper_class(self):
        return self._runner_helper_class

    @property
    def function_helper_class(self):
        return self._function_helper_class

    @property
    def runner_validator_class(self):
        return self._runner_validator_class

    @property
    def function_validator_class(self):
        return self._function_validator_class

    @property
    def runner_cache_storage_class(self):
        return self._runner_cache_storage_class

    @property
    def function_cache_storage_class(self):
        return self._function_cache_storage_class

    @property
    def error_class(self):
        return self._error_class

    @property
    def result_class(self):
        return self._result_class

    @property
    def result_presenter_class(self):
        return self._result_presenter_class
    
    def _prepare_manager_class(self):
        """
        Устанавливает класс менеджера
        """
        self._manager_class = RunnerManager

    def _prepare_runner_class(self):
        """
        Устанавливает класс пускателя
        """
        self._runner_class = BaseRunner

    def _prepare_function_class(self):
        """
        Устанавливает класс Функции
        """
        self._function_class = BaseFunction

    def _prepare_runner_helper_class(self):
        """
        Устанавливает класс помощника пусковика
        """
        self._runner_helper_class = BaseRunnerHelper

    def _prepare_function_helper_class(self):
        """
        Устанавливает класс помощника функции
        """
        self._function_helper_class = BaseFunctionHelper

    def _prepare_runner_validator_class(self):
        """
        Устанавливает класс валидатора пусковика
        """
        self._runner_validator_class = BaseValidator

    def _prepare_function_validator_class(self):
        """
        Устанавливает класс валидатора Функции
        """
        self._function_validator_class = BaseValidator

    def _prepare_runner_cache_storage_class(self):
        """
        Устанавливает класс хранилища кешей пусковика
        """
        self._runner_cache_storage_class = CacheStorage

    def _prepare_function_cache_storage_class(self):
        """
        Устанавливает класс хранилища кешей Функции
        """
        self._function_cache_storage_class = CacheStorage

    def _prepare_error_class(self):
        """
        Устанавливает класс ошибки
        """
        self._error_class = BaseError

    def _prepare_result_class(self):
        """
        Устанавливает класс результата
        """
        self._result_class = BaseRunnableResult

    def _prepare_result_presenter_class(self):
        """
        Устанавливает класс ппрезентера результата
        """
        self._result_presenter_class = ResultPresenter

    def _prepare(self):
        """
        Подготовка компонентов реализации функции
        """
        self._prepare_manager_class()
        self._prepare_runner_class()
        self._prepare_function_class()
        self._prepare_runner_helper_class()
        self._prepare_function_helper_class()
        self._prepare_runner_validator_class()
        self._prepare_function_validator_class()
        self._prepare_function_cache_storage_class()
        self._prepare_runner_cache_storage_class()
        self._prepare_error_class()
        self._prepare_result_class()
        self._prepare_result_presenter_class()


class BaseRunnerBaseFunctionImplementationStrategy(FunctionImplementationStrategy):
    """
    Реализация простой функции без отложенного сохранения
    """


class BaseRunnerLazySavingPredefinedQueueFunctionImplementationStrategy(FunctionImplementationStrategy):
    """
    Реализация функции с отложенным сохранением и предустановленной очередью объектов на сохранение
    """

    def _prepare_function_class(self):
        """
        Устанавливает класс Функции
        """
        self._function_class = LazySavingPredefinedQueueFunction


class LazySavingRunnerLazyDelegateSavingPredefinedQueueFunctionImplementationStrategy(FunctionImplementationStrategy):
    """
    Реализация функции с отложенным сохранением его делегированием пускателю. Когда все функции отработают, только
    после этого запускается сохранение объектов из очередей каждой функции
    """

    def _prepare_runner_class(self):
        """
        Устанавливает класс пусковика
        """
        self._runner_class = LazySavingRunner

    def _prepare_function_class(self):
        """
        Устанавливает класс Функции
        """
        self._function_class = LazyDelegateSavingPredefinedQueueFunction


class ImplementationStrategyFactory:
    """
    Фабрика стратегий реализации
    """

    def __init__(self):
        self._implementation_strategy_map = self._prepare_implementation_strategy_map()

        implementation_strategy_factory_after_init_signal.send(self)

    def _prepare_implementation_strategy_map(self):
        """
        Создание карты соответствия стратегий реализации функции
        """
        strategy_map = {
            ImplementationStrategyEnum.BASE_RUNNER_BASE_FUNCTION: BaseRunnerBaseFunctionImplementationStrategy,
            ImplementationStrategyEnum.BASE_RUNNER_LAZY_SAVING_PREDEFINED_QUEUE_FUNCTION: BaseRunnerLazySavingPredefinedQueueFunctionImplementationStrategy,  # noqa
            ImplementationStrategyEnum.LAZY_SAVING_RUNNER_LAZY_DELEGATE_SAVING_PREDEFINED_QUEUE_FUNCTION: LazySavingRunnerLazyDelegateSavingPredefinedQueueFunctionImplementationStrategy, # noqa
        }

        return strategy_map

    def patch_implementation_strategy_map(
        self,
        enum_strategy: ImplementationStrategyEnum,
        strategy: FunctionImplementationStrategy,
    ):
        """
        Публичный метод для патчинга карты соответствия стратегии реализации функций
        """
        self._implementation_strategy_map[enum_strategy] = strategy

    def get_strategy_implementation(
        self,
        enum_strategy: ImplementationStrategyEnum,
    ):
        """
        Возвращает стратегию реализации функции по значению перечисления
        """
        return self._implementation_strategy_map[enum_strategy]