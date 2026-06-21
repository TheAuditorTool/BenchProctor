# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest53476(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
