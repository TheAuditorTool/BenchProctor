# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

def BenchmarkTest47545(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = coalesce_blank(multipart_value)
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
