import os


def make_empty_file(a_path, a_name):
    """
    Создаем пустой файл по указанному пути

    :param a_path: Каталог
    :param a_name: Полное имя файла
    :return:
    """
    open(os.path.join(a_path, a_name), 'tw', encoding='UTF8').close()


def make_path(a_path):
    """
    Создаем каталог с контролем существования

    :param a_path: Полный путь к каталогу
    :return:
    """
    if not os.path.exists(a_path):
        os.makedirs(a_path)


def parse_config(make_path_str):
    """
    Разберем файл конфига и создадим структуру папок на диске

    :param make_path_str: Каталог, относительно которого начинаем строить нашу структуру из конфига
    :return:
    """
    root_folder = ''
    cur_folder = ''

    with open('config.yaml', 'r', encoding='UTF8') as f:
        for line in f:

            line = line.replace('\n', '').replace('-', '')

            # корневая папка
            if line[0] != ' ' and line.endswith(':'):
                root_folder = os.path.join(make_path_str, line.replace('\n', '').replace(':', ''))
                make_path(root_folder)

            # остальные вложенные папки
            elif line.endswith(':'):
                if line.count(' ') == 2:
                    cur_folder = os.path.join(root_folder, line.replace(' ', '').replace(':', ''))
                else:
                    cur_folder = os.path.join(cur_folder, line.replace(' ', '').replace(':', ''))

                make_path(cur_folder)

            # файлы
            else:
                f_name = line.replace(' ', '')
                make_empty_file(cur_folder, f_name)


parse_config(os.getcwd())
