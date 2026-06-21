# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest02207(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    auth_check('user', data)
    return JsonResponse({"saved": True})
