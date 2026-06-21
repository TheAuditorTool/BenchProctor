# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest42634(request):
    multipart_value = request.POST.get('multipart_field', '')
    auth_check('user', multipart_value)
    return JsonResponse({"saved": True})
