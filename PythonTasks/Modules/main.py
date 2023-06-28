import analyser
ask = input('Введите запрос или "off": ')
while ask != 'off':
    analyser.user(ask)
    ask = input('Введите запрос или "off": ')
