# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest35635(request):
    upload_name = request.FILES['upload'].name
    try:
        os.setuid(int(str(upload_name)) if str(upload_name).isdigit() else 65534)
    except OSError:
        pass
    return JsonResponse({"saved": True})
