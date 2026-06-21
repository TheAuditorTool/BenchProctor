# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest20343(request):
    upload_name = request.FILES['upload'].name
    parts = []
    for token in str(upload_name).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.remove(str(data))
    return JsonResponse({"saved": True})
