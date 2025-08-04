import os
import TkEasyGUI as eg

desktop_dir = os.path.join(os.path.expanduser('~'), 'Desktop')
path = eg.popup_get_file(
    title='ファイルを開く',
    initial_folder=desktop_dir)
print(path)