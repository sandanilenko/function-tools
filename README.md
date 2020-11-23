**function-tools** - это библиотека вспомогательных классов для реализации Функций системы.

**Договоримся**

Необходимо различать функции - объект Python и бизнес-функцию. В тех местах, где речь будет вестить про Python-функции - они будут написаны с маленькой буквы - функции, про бизнес-функции с большой буквы - Функции.
Если обобщо, то система представляет из себя хранилище данных и функционал, который каким-то образом изменяет данные, при этом достигая ожидаего результата описанного в бизнес требованиях. Таким образом, Функции - это ядро системы и необходимо уделять пристальное внимание тому, как Функции реализованы в системе.

В большинстве случаев Функции имеют следующие признаки:

* Реализованы в виде функций длинной не влазящик ни в один экран монитора;
* Имеют запутанный код с множеством условных конструкций (умеренное количество допустимо);
* Взаимодействие с базой данных выстроено таким образом, как будто вся база данных хранится в оперативной памяти и нет необходимости заботиться о количестве запросов и их оптимальности;
* Наименование функций и названий переменных сокращено настолько, что для понимания кода иногда не хватает простого прочтения и возникает необходимость дебага. Часто это дополнятся размером функций, когда в середине не помнишь, что было в начале.
* Высокая когнитивная нагрузка связанная со сложностью реализации и правилами, для которых нет описания, но они имеют фундаментальное значение в работе Функций.
* Низкий уровень самодокументируемости кода из-за плохой его декомпозиции;
* Перегруженность функций действиями, которые являются вспомогательными и никак не отражают реализованные бизнес требования.
* Отсутствие валидации входных данных и данных при выполнении функции, что позволяет потенциально испортить данные;
* Кеширование данных для работы функции часто замешано код функции;
* Большая вариативность реализаций Функций, что не позволят однозначно найти причину ошибки при ее возникновении в виде Инцидента или Бага (если конечно не сам сегодня эту ошибку совершил).

Для решения указанных проблем была разработана библиотека с проработанной архитектурой, которая находится в разработке, но уже решающая массу проблем.

Упрощенная диаграмма классов представлена на Рисунке 1.

![Рисунок 1](/docs/source/_static/images/simple_class_diagram.png)

Основные компоненты:

**Cache**

Кеш объектов некоторой указанной сущности. Служит для однократной выборки данных и дальнейшего их использования в рамках функции (Function).

**StorageCache**

Хранилище кешей. Состоит из кешей и используется для более удобного хранения и доступа к ним.

**Helper**

Помощник запускаемого объекта. Содержит вспомогательные функции, кеш.

**Validator**

Валидатор данных. Имеется у Пускателя и Функции.

**Function**

Функция, приближенная к бизнес-функции. Имеет помощника и выполняет действия согласно безнес требований.

**Runner**

Пускатель. Умеет запускать как одинчные функции, так и цепочные функции представленные в виде пускателей.

**RunnerManager**

Менеджер пускателя. Отвечает за создание функций и пускателей и дальнейший их запуск.

**Error**

Ошибка, возникающая в процессе работы.

**Result**

Результат исполнения запускаемого объекта.

**ResultPresenter**

Презентер результата исполнения запускаемого объекта.
Данные компоненты позволяют распределить обязанности и таким образом существенно снизить когнитивную нагрузку при анализе кода. При понимании работы механизма, можно без особых усилий локализовывать возникающие ошибки и иправлять их. Код становится самодокументируемым и возникает необходимость описания только основополагающих концепций и подходов к реализации требуемого функционала.

Алгоритм работы Функции выглядит следующим образом:

* Создается пускатель;
* Создаются функции и пускатели, которые добавляются в очередь на исполнение пускателю;
* Функции и пускатели создают помощников, которые в свою очередь создают хранилища кешей;
* Перед запуском выполняемых объектов производится валидация на уровне пускателя;
* Производится запуск функций;
* После завершения работы выполняемых объектов и, соответственно, пускателя, производится вывод результата работы пользователю в необходимом виде.

Подробная актуальная диаграммка классов представлена на Рисунке 2.

![Рисунок 2](/docs/source/_static/images/class_diagram.png)

С подробной документацией можно ознакомиться на [function-tools.readthedocs.io](https://function-tools.readthedocs.io/ru/latest/)
