# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest01769(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = default_blank(header_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
