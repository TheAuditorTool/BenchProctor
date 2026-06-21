# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest68870(request):
    xml_value = request.body.decode('utf-8')
    data = '{}'.format(xml_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
