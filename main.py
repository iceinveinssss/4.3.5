import json
from typing import List, Tuple

# Класс-контейнер VectorCollection с использованием tuple для хранения векторов
class VectorCollection:
    def __init__(self, data: List[Tuple[float, float]] = None):
        self._data = data if data is not None else []

    def __str__(self) -> str:
        return f"VectorCollection({', '.join(f'({x}, {y})' for x, y in self._data)})"

    def __getitem__(self, index: int) -> Tuple[float, float]:
        return self._data[index]

    def add(self, value: Tuple[float, float]) -> None:
        self._data.append(value)

    def remove(self, index: int) -> None:
        if 0 <= index < len(self._data):
            self._data.pop(index)
        else:
            raise IndexError("Index out of range")

    def save(self, filename: str) -> None:
        with open(filename, 'w') as f:
            # Сериализация списка кортежей в JSON
            json.dump(self._data, f)

    def load(self, filename: str) -> None:
        with open(filename, 'r') as f:
            self._data = json.load(f)

# Пример использования
if __name__ == "__main__":
    v1 = (1, 2)
    v2 = (3, 4)
    collection = VectorCollection([v1, v2])
    print(collection)

    # Добавление нового вектора
    v3 = (5, 6)
    collection.add(v3)
    print(collection)

    # Сохранение в файл
    collection.save('vectors.json')

    # Загрузка из файла
    new_collection = VectorCollection()
    new_collection.load('vectors.json')
    print(new_collection)
