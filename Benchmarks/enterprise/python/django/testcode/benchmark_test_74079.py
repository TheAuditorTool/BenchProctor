# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest74079(request):
    raw_body = request.body.decode('utf-8')
    try:
        os.setuid(int(str(raw_body)) if str(raw_body).isdigit() else 65534)
    except OSError:
        pass
    return JsonResponse({"saved": True})
