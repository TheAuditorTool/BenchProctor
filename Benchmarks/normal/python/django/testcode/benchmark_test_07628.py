# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest07628(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
