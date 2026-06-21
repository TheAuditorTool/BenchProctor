# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest72282(request):
    upload_name = request.FILES['upload'].name
    reader = make_reader(upload_name)
    data = reader()
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
