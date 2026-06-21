# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest00723(request):
    upload_name = request.FILES['upload'].name
    data = ensure_str(upload_name)
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
