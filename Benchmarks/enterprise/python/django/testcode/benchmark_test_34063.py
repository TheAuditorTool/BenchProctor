# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest34063(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    auth_check('user', data)
    return JsonResponse({"saved": True})
