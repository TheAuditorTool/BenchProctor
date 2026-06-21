# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest04928(request):
    xml_value = request.body.decode('utf-8')
    if not auth_check(request.session.get('user', ''), str(xml_value)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
