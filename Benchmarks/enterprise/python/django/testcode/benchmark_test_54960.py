# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest54960(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = normalise_input(auth_header)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
