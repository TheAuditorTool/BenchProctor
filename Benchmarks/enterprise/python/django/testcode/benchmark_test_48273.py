# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48273(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
