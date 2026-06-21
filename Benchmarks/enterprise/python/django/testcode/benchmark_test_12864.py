# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest12864(request):
    user_id = request.GET.get('id', '')
    data = normalise_input(user_id)
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
