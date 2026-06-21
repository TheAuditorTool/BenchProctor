# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def normalise_input(value):
    return value.strip()

def BenchmarkTest09870(request):
    raw_body = request.body.decode('utf-8')
    data = normalise_input(raw_body)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
