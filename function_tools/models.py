from django.contrib.postgres.fields import (
    ArrayField,
)
from django.db.models import (
    CharField,
    DateTimeField,
    Model,
)

from m3_db_utils.models import (
    ModelEnumValue,
    TitledModelEnum,
)


class ImplementationStrategy(TitledModelEnum):
    """
    Перечисление стратегий реализации функций
    """

    BASE_FUNCTION = ModelEnumValue(title='Реализация простой функции без отложенного сохранения')
    LAZY_SAVING_FUNCTION = ModelEnumValue(
        title=(
            'Реализация функции с отложенным сохранением и предустановленной очередью объектов на сохранение. '
            'Сохранение производится после удачной работы функции'
        ),
    )
    LAZY_SAVING_RUNNER_FUNCTION = ModelEnumValue(
        title=(
            'Реализация функции с отложенным сохранением его делегированием пускателю. Когда все функции отработают, '
            'только после этого запускается сохранение объектов из очередей каждой функции'
        ),
    )

    class Meta:
        db_table = 'function_tools_implementation_strategy'
        verbose_name = 'Стратегия создания функции'
        extensible = True


class RegisteredFunction(Model):
    """
    Модель зарегистрированных функций системы
    """

    function_path = CharField(
        verbose_name='Путь до функции',
        primary_key=True,
        db_index=True,
        unique=True,
        max_length=1024,
    )
    verbose_name = CharField(
        verbose_name='Название функции',
        max_length=512,
        default='Имя функции не определено',
    )

    tags = ArrayField(base_field=CharField(max_length=128, blank=True), default=list)

    created_at = DateTimeField(
        verbose_name='Дата и время создания',
        auto_now_add=True,
    )
    updated_at = DateTimeField(
        verbose_name='Дата и время обновления',
        auto_now=True,
    )

    class Meta:
        db_table = 'function_tools_registered_function'
        verbose_name = 'Зарегистрированная функция'
