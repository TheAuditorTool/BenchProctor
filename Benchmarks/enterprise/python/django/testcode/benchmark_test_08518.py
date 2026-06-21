# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest08518(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = f'{header_value:.200s}'
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
