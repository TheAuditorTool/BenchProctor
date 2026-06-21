# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest49051(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = f'{forwarded_ip:.200s}'
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
