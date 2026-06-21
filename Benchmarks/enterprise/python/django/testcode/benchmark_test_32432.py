# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest32432(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
