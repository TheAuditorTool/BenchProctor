# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest58565(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
