# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest65687(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
