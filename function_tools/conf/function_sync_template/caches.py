class {{ camel_case_function_name }}RunnerCacheStorage(BaseTransferBalancesCacheStorage):
    """
    Кеш помощника пусковика функции "{{ function_verbose_name }}"
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class {{ camel_case_function_name }}FunctionCacheStorage(BaseTransferBalancesCacheStorage):
    """
    Кеш помощника функции "{{ function_verbose_name }}"
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


