import os
import shutil


def make_path(a_path):
    """
    Создаем каталог с контролем существования

    :param a_path: Полный путь к каталогу
    :return:
    """
    if not os.path.exists(a_path):
        os.makedirs(a_path)


def parse_config(path):
    root_path = os.path.join(path, 'templates')

    files = [(path_name, f) for path_name, file_name, filenames in os.walk(path)
             for f in filenames
             if os.path.splitext(f)[1] == '.html']

    for path_name, file_name in files:
        new_file_path = os.path.join(root_path, os.path.split(path_name)[1])
        try:
            make_path(new_file_path)
            shutil.copy(os.path.join(path_name, file_name), os.path.join(new_file_path, file_name))
        except Exception as e:
            print(f'Error while make dir {e}')
        else:
            try:
                shutil.copy(os.path.join(path_name, file_name), os.path.join(new_file_path, file_name))
            except Exception as e:
                print(f'Error while copy file {e}')


parse_config(os.path.join(os.getcwd(), 'my_project'))
