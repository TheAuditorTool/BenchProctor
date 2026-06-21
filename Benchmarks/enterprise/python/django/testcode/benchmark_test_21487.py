# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import base64


def BenchmarkTest21487(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
