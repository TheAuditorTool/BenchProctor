# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest00138(request):
    xml_value = request.body.decode('utf-8')
    if auth_check('user', str(xml_value)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
