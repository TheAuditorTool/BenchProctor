# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest01465(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    auth_check('user', data)
    return JsonResponse({"saved": True})
