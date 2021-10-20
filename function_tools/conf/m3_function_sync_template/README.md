Для запуска функции необходимо проделать ряд действий:

1. Зарегистрируйте приложение {{ m3_function_python_path }} в INSTALLED_APPS;
2. В сгенерированном app_meta.py произвести регистрацию пака функции;
3. В форме, в которой будет использоваться функция, в __init__() необходимо добавить кнопку с ее вызовом, после вызова __init__ суперклассов
    ```
    _, {{ function_name }}_func_menu = self.menu_functions_add_items({
       'text': '{{ function_verbose_name }}',
       'handler': '{{ camel_case_m3_function_name }}ButtonHandler',
    })
    self.{{ function_name }}_func_menu_btn = {{ function_name }}_func_menu.btn
    ```
    