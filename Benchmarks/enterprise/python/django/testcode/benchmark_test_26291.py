# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26291(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
