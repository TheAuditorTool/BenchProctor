# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest76204(request):
    host_value = request.META.get('HTTP_HOST', '')
    reader = make_reader(host_value)
    data = reader()
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
