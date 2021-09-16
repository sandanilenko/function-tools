class {{ camel_case_function_name }}Function(LazySavingFunction):
    """
    Функция "{{ function_verbose_name }}"
    """

    verbose_name = '{{ function_verbose_name }}'

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        self._ent_id = get_current_user_enterprise_id()

        super().__init__(*args, **kwargs)

        # self.result.key =

    def _prepare_helper(self):
        """
        Создание помощника выполнения функции
        """
        self._helper = {{ camel_case_function_name }}FunctionHelper(
            ent_id=self._ent_id,
        )

    def _prepare_validator(self):
        """
        Создание валидатора функции
        """
        self._validator = {{ camel_case_function_name }}FunctionValidator()

    def _prepare(self):
        """
        Выполнение действий функций системы
        """
        if self.result.has_not_errors:
            pass
