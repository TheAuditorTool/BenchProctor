# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest29287(request):
    upload_name = request.FILES['upload'].name
    try:
        os.setuid(int(str(upload_name)) if str(upload_name).isdigit() else 65534)
    except OSError:
        return JsonResponse({'error': 'privilege drop failed'}, status=500)
    return JsonResponse({"saved": True})
