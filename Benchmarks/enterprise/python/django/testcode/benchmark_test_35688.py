# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest35688(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value}'
    auth_check('user', data)
    return JsonResponse({"saved": True})
