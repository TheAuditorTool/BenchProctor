# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def relay_value(value):
    return value

def BenchmarkTest71458(request, path_param):
    path_value = path_param
    data = relay_value(path_value)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
