# utils.py
def print_section(title: str, width: int = 40):
    """
    Выводит заголовок с разделителями.
    :param title: текст заголовка
    :param width: ширина линии
    """

    # Функция для разделителя с заголовком
    line = "=" * width
    print(f"\n{line}\n{title.center(width)}\n{line}")
