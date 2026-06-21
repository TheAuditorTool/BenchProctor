# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import auth_check


def BenchmarkTest38211(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
