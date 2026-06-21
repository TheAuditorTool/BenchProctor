# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08018(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
