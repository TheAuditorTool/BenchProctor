# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest12972(request):
    xml_value = request.body.decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
