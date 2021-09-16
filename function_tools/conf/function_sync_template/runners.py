class {{ camel_case_function_name }}Runner(BaseRunner):
    """
    Пусковик функции "{{ function_verbose_name }}"
    """

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

    def _prepare_validator(self):
        """
        Создание валидатора пусковика
        """
        self._validator = {{ camel_case_function_name }}RunnerValidator()

    def _prepare_helper(self):
        """
        Создание помощника пусковика
        """
        self._helper = {{ camel_case_function_name }}RunnerHelper()
