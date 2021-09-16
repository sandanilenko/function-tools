class {{ camel_case_function_name }}RunnerValidator(BaseValidator):
    """
    Валидатор пускателя функции "{{ function_verbose_name }}"
    """

    def validate(self, runnable):
        pass


class {{ camel_case_function_name }}FunctionValidator(BaseValidator):
    """
    Валидатор функции "{{ function_verbose_name }}"
    """

    def validate(self, runnable):
        pass