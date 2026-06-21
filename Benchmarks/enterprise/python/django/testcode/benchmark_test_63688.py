# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest63688(request):
    cookie_value = request.COOKIES.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
