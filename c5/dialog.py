import TkEasyGUI as eg

ans = eg.popup_yes_no('ラーメンは好きですか？')
if ans == 'Yes':
    eg.popup_ok('同意')
else:
    eg.popup_ok('本当に不満ですか？')