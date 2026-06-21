# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import os


def BenchmarkTest45944(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
