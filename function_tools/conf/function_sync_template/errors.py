from typing import (
    List,
)

from function_tools.errors import (
    BaseError,
)


class {{ camel_case_function_name }}Error(BaseError):
    """
    Ошибка работы функции "{{ function_verbose_name }}"
    """

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
