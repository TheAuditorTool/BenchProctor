# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def normalise_input(value):
    return value.strip()

def BenchmarkTest50244(request):
    raw_body = request.body.decode('utf-8')
    data = normalise_input(raw_body)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
