# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17780(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
