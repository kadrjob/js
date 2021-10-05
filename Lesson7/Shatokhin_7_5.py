import json
import os

PATH = r'E:\Local_PC\work\py'


# PATH = os.getcwd()

def parse_dir(path):
    # данные для хранения статистики
    result = {100: {'count': 0, 'ext': []},
              1000: {'count': 0, 'ext': []},
              10000: {'count': 0, 'ext': []},
              100000: {'count': 0, 'ext': []}
              }

    # получим все файлы из указанной папки
    files = [(path_name, f) for path_name, file_name, filenames in os.walk(path)
             for f in filenames
             # if os.path.isfile(f)
             ]

    # обходим все файлы
    for path_name, f_name in files:
        # получаем размер файла
        f_size = os.stat(os.path.join(path_name, f_name)).st_size

        # ищем размер файла в нашем словаре
        for _ in result.keys():

            # если подходит - размер меньше значения ключа
            if f_size < _:

                # увеличиваем первое значение вложенного словаря - количество файлов
                result[_]['count'] += 1

                # получим расширение файла
                f_ext = os.path.splitext(f_name)[1].replace('.', '')

                # если такого расширения нет в списке расширений - добавим
                if not f_ext in result[_]['ext']:
                    result[_]['ext'].append(f_ext)
                break

    # преобразуем словари в значениях словаря в кортежи
    for k, v in result.items():
        result[k] = tuple(v.values())

    # сохранили результат в файл
    with open(os.path.join(os.path.dirname(__file__), os.path.basename(path) + '_summary.json'), 'w',
              encoding='UTF8') as f:
        json.dump(result, f)

    # print(result, sep='\n')


parse_dir(PATH)
