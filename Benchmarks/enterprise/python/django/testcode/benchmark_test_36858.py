# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest36858(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    reader = make_reader(header_value)
    data = reader()
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
