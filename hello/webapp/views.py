from django.http import request
from django.shortcuts import render
import random
secret_num = random.sample(range(10), 4)
history = {}
count = 1


def guess_numbers(actual, secret):
    if len(actual) < 4 or len(actual) > 4:
        return 'Enter 4 digits'
    for num in actual:
        if num < 1 or num > 10:
            return 'Please enter a number greater than 0 and less than 10'

    bull_counter = 0
    cow_counter = 0

    for i in range(len(actual)):
        if actual[i] in actual[i + 1:]:
            return 'Please enter different numbers'

        if secret[i] == actual[i]:
            bull_counter += 1
        elif actual[i] in secret:
            cow_counter += 1
    if bull_counter == 4:
        global secret_num
        secret_num = random.sample(range(10), 4)
        return 'You win!!! You guessed all the numbers!'

    else:
        return f'bull:{bull_counter}, cow:{cow_counter}'


def check_inquiry(request):
    if request.method == 'GET':
        return render(request, 'game_cow_bull.html')
    elif request.method == 'POST':
        try:
            numbers = list(map(int, request.POST.get("numbers").split(' ')))

            result = guess_numbers(numbers, secret_num)
        except ValueError:
            result = "Enter numbers"

        context = {
            'result': result
        }
        global count
        history[count] = result
        count += 1
        return render(request, 'game_cow_bull.html', context)


def get_history(request):
    if request.method == 'GET':
        hist = {
            'result': history
        }
        return render(request, 'history.html', hist)



