# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest44625(request):
    raw_body = request.body.decode('utf-8')
    entries = os.listdir(str(raw_body))
    return JsonResponse({'listing': entries}, status=200)
