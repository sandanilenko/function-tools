from typing import (
    Optional,
    Type,
    Union,
)

from function_tools.helpers import (
    BaseFunctionHelper,
    BaseHelper,
    BaseRunnerHelper,
)
from function_tools.validators import (
    BaseValidator,
)


class HelperMixin:
    """
    Миксин для появления помощника у сущности
    """

    def __init__(self, *args, **kwargs):
        super().__init__()

        self._helper_class = self._prepare_helper_class()

        self._helper: Union[Optional[BaseHelper], Optional[BaseFunctionHelper]] = None

        self._prepare_helper(*args, **kwargs)

    @property
    def helper(self):
        """
        Возвращает помощника
        """
        return self._helper

    def _prepare_helper_class(self) -> Union[Type[BaseHelper], Type[BaseFunctionHelper]]:
        """
        Возвращает класс помощника
        """
        return BaseHelper

    def _prepare_helper(self, *args, **kwargs):
        """
        Точка расширения для создания помощника.
        """
        if issubclass(self._helper_class, (BaseHelper, BaseFunctionHelper)):
            self._helper = self._helper_class(*args, **kwargs)


class ValidatorMixin:
    """
    Миксин для появления валидатора у сущности
    """

    def __init__(self, *args, **kwargs):
        super().__init__()

        self._validator_class = self._prepare_validator_class()

        self._validator: Optional[BaseValidator] = None

        self._prepare_validator(*args, **kwargs)

    def _prepare_validator_class(self) -> Type[BaseValidator]:
        """
        Возвращает класс валидатор
        """
        return BaseValidator

    def _prepare_validator(self, *args, **kwargs):
        """
        Точка расширения для создания валидатора
        """
        if issubclass(self._validator_class, BaseValidator):
            self._validator = self._validator_class(*args, **kwargs)

    def before_validate(self):
        """
        Возможность расширения запускаемого объекта перед валидацией
        """

    def validate(self):
        """
        Публичный метод для запуска валидатора сущности
        """
        if self._validator:
            self._validator.validate(self)

    def after_validate(self):
        """
        Возможность расширения запускаемого объекта после валидации
        """


class GlobalHelperMixin:
    """
    Миксин добавляющий возможность установки глобального помощника
    """
    def __init__(self, *args, global_helper=None, **kwargs):
        super().__init__()

        self._global_helper_class = self._prepare_global_helper_class()

        self._global_helper: Optional[BaseRunnerHelper] = (
            global_helper or
            self._prepare_global_helper()
        )

    @property
    def global_helper(self):
        """
        Возвращает глобального помощника
        """
        return self._global_helper

    def _prepare_global_helper_class(self) -> Type[BaseRunnerHelper]:
        """
        Возвращает класс помощника
        """
        return BaseRunnerHelper

    def _prepare_global_helper(self, *args, **kwargs):
        """
        Предназначен для определения глобального помощника
        """
        if issubclass(self._global_helper_class, BaseRunnerHelper):
            self._helper = self._global_helper_class(*args, **kwargs)

    def set_global_helper(
        self,
        global_helper: BaseRunnerHelper,
    ):
        """
        Публичный метод для установки глобального помощника
        """
        self._global_helper = global_helper
