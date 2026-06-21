# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest46641(request):
    multipart_value = request.POST.get('multipart_field', '')
    if auth_check('user', str(multipart_value)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
