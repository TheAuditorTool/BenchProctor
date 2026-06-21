# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest46838(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value}'
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
