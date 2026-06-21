# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest24562(request):
    upload_name = request.FILES['upload'].name
    data, _sep, _rest = str(upload_name).partition('\x00')
    auth_check('user', data)
    return JsonResponse({"saved": True})
