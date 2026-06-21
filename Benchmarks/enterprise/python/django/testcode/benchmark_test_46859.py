# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest46859(request):
    xml_value = request.body.decode('utf-8')
    auth_check('user', xml_value)
    return JsonResponse({"saved": True})
