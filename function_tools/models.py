from django.db.models import (
    CharField,
    DateTimeField,
    Model,
)


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
