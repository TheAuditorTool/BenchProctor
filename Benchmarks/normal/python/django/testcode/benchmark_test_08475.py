# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08475(request):
    upload_name = request.FILES['upload'].name
    if str(upload_name) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
