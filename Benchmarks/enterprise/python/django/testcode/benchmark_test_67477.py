# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest67477(request):
    xml_value = request.body.decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    if not auth_check(request.session.get('user', ''), str(data)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
