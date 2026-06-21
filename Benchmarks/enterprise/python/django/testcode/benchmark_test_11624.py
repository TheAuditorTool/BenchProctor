# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest11624(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if header_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = header_value
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
