# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest67324(request):
    upload_name = request.FILES['upload'].name
    reader = make_reader(upload_name)
    data = reader()
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
