# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def normalise_input(value):
    return value.strip()

def BenchmarkTest22206(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = normalise_input(referer_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
