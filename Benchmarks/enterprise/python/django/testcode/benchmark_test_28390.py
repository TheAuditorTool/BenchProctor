# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import os


def BenchmarkTest28390(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
