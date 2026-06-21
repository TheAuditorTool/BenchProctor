# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from app_runtime import auth_check


def BenchmarkTest11117(request):
    upload_name = request.FILES['upload'].name
    parts = []
    for token in str(upload_name).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
