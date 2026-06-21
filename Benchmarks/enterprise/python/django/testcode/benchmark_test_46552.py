# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46552(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
