# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest54648(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
