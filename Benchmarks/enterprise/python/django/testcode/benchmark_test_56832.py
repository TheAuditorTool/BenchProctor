# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56832(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(header_value) + ',data\n')
    return JsonResponse({"saved": True})
