import re
import inflect

eng = inflect.engine()
def camel_to_snake(name: str) -> str:
    name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    return name
def generate_tablename(cls) -> str:
    snake = camel_to_snake(cls.__name__)
    split_snake = snake.split('_')
    split_snake[-1] = eng.plural(split_snake[-1])
    return '_'.join(split_snake)


