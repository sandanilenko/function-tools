class {{ camel_case_function_name }}RunnerHelper(BaseTransferBalancesHelper):
    """
    Помощник пусковика функции "{{ function_verbose_name }}"
    """

    def _create_cache(self):
        """
        Метод создания кеша для помощника
        """
        self.cache = {{ camel_case_function_name }}RunnerCacheStorage(
            ent_id=self._ent_id,
        )


class {{ camel_case_function_name }}FunctionHelper(BaseTransferBalancesHelper):
    """
    Помощник функции "{{ function_verbose_name }}"
    """

    def _create_cache(self):
        """
        Метод создания кеша для помощника
        """
        self.cache = {{ camel_case_function_name }}FunctionCacheStorage(
            ent_id=self._ent_id,
        )
