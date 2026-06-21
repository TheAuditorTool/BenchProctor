# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest09830(request):
    upload_name = request.FILES['upload'].name
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
