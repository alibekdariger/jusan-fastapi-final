# Jusan-Fastapi-Final

# pip installation
``` 
$ pip3 install fastapi
$ pip3 install uvicorn[standard]
``` 

# Run
1./sum1n, принимающий GET запросы.

Передается число n через URL. Вернуть сумму от 1 до n.
Пример запроса.
``` 
$ curl http://localhost:8000/sum1n/10
{"result": 55} 
```

2./fibo, принимающий GET запросы.
Передается число n через URL Query. Вернуть n-ное число из последовательности Фибоначчи.
Пример запроса.
``` 
$ curl http://localhost:8000/fibo?n=5
{"result": 3}
```

3./reverse, принимающий POST запросы.
Передается строка string через Header. Вернуть перевернутую строку задом наперед.
Пример запроса.
``` 
$ curl -X POST -H "string: hello" http://localhost:8000/reverse
{"result": "olleh"}
```

4./list, принимающий PUT запросы.
Передается строка element через JSON тело запроса. Сохранить строку element в глобальный массив.
Пример запроса.
```
$ curl -X PUT -d '{"element":"Apple"}' -H 'Content-Type: application/json' http://localhost:8000/list
$ curl -X PUT -d '{"element":"Microsoft"}' -H 'Content-Type: application/json' http://localhost:8000/list
$ curl http://localhost:8000/list
{"result": ["Apple", "Microsoft"]}
```

5./list, принимающий GET запросы.
Вернуть глобальный массив.
Пример запроса.
``` 
$ curl http://localhost:8000/list
{"result": []}
$ curl -X PUT -d '{"element":"Apple"}' -H 'Content-Type: application/json' http://localhost:8000/list
$ curl -X PUT -d '{"element":"Microsoft"}' -H 'Content-Type: application/json' http://localhost:8000/list
$ curl http://localhost:8000/list
{"result": ["Apple", "Microsoft"]}
```

6./calculator, принимающий POST запросы.
Передается строка expr через JSON тело запроса. Строка expr состоит из математического выражения, который нужно вычислить. Формат строки следующий: num1,operator,num2.
num1 и num2 - это числа
operator - это математическая операция: +,-,/,*
Вернуть результат математического выражения.
Если такого expr неверного формата, вернуть {"error": "invalid"} со статусом 400 Bad Request.
При делении на ноль вернуть {"error": "zerodiv"} со статусом 403.
Пример запроса.
```
$ curl -X POST -d '{"expr": "1,+,1"}' -H 'Content-Type: application/json' http://localhost:8000/calculator
{"result": 2}
```

# Test
` $ pytest `
