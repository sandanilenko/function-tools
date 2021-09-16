from m3.actions import (
    Action,
    ActionPack,
)
from m3.actions.urls import (
    get_url,
)
from m3_ext.ui.results import (
    ExtUIScriptResult,
)

from web_bb.core.base.api import (
    READONLY_CATEGORY,
    WRITE_CATEGORY,
)

from {{ function_python_path }}.managers import (
    {{ camel_case_function_name }}FunctionRunnerManager,
)
from {{ function_python_path }}.presenters import (
    {{ camel_case_function_name }}FunctionResultPresenter,
)
from {{ function_python_path }}.ui import (
    {{ camel_case_function_name }}FunctionParametersDialogWindow,
)


class {{ camel_case_function_name }}FunctionParametersDialogAction(Action):
    """
    Экшен получения диалогового окна с настройкой параметров функции "{{ function_verbose_name }}"
    """

    url = '/parameters-dialog'

    def __init__(self):
        super().__init__()

        self.need_atomic = False
        self.category = READONLY_CATEGORY

    def context_declaration(self):
        """
        Декларативное описание параметров запроса экшена
        """
        return [
            # ACD(),
        ]

    def run(self, request, context):
        win = {{ camel_case_function_name }}FunctionParametersDialogWindow()

        win.submit_url = get_url(self.parent.execute_action)

        return ExtUIScriptResult(win)


class {{ camel_case_function_name }}FunctionExecuteAction(Action):
    """
    Экшен исполнения функции системы "{{ function_verbose_name }}"
    """

    url = '/execute'

    def __init__(self):
        super().__init__()

        self.need_atomic = False
        self.category = WRITE_CATEGORY

    def context_declaration(self):
        """
        Декларативное описание параметров запроса экшена
        """
        return [
            # ACD(),
        ]

    def run(self, request, context):
        runner_manager = {{ camel_case_function_name }}FunctionRunnerManager()

        runner_manager.run()

        result = {{ camel_case_function_name }}FunctionResultPresenter(
            runnable_result=runner_manager.result,
        ).represent()

        return result


class {{ camel_case_function_name }}FunctionPack(ActionPack):
    url = '/{{ function_url_name }}'
    short_name = '{{ function_name }}'

    title = '{{ function_verbose_name }}'
    title_plural = '{{ function_verbose_name }}'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.parameters_dialog_action = {{ camel_case_function_name }}FunctionParametersDialogAction()
        self.execute_action = {{ camel_case_function_name }}FunctionExecuteAction()

        self.actions.extend([
            self.parameters_dialog_action,
            self.execute_action,
        ])
