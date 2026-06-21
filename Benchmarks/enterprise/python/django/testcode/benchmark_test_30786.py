# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest30786(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = normalise_input(forwarded_ip)
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
