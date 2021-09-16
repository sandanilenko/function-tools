class {{ camel_case_function_name }}RunnerManager(RunnerManager):
    """
    Менеджер пускателя функций системы "{{ function_verbose_name }}"
    """
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super().__init__(
            *args,
            **kwargs,
        )

    def _create_runner(self):
        self._runner = {{ camel_case_function_name }}Runner(
            table_conformity_ids=self._table_conformity_ids,
            tables_conformity=self._tables_conformity,
        )

    def _prepare_runner(self):
        function = {{ camel_case_function_name }}Function()

        self._runner.enqueue(
            runnable=function,
        )
