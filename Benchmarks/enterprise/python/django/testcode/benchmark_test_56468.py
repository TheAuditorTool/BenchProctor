# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest56468(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
