# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest33470(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    reader = make_reader(header_value)
    data = reader()
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
