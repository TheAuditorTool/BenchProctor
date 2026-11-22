# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00018(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    token = random.randbytes(16).hex()
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
