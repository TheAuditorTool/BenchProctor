# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest48555(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
