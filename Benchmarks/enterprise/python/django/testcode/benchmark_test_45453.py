# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def ensure_str(value):
    return str(value)

def BenchmarkTest45453(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = ensure_str(header_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
