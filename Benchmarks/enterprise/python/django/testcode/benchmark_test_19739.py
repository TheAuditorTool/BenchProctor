# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest19739(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    reader = make_reader(header_value)
    data = reader()
    if not auth_check(request.session.get('user', ''), str(data)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
