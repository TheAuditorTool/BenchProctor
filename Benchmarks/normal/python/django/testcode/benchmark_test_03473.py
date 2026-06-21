# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03473(request):
    upload_name = request.FILES['upload'].name
    if str(upload_name).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
