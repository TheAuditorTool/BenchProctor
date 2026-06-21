# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest56943(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
