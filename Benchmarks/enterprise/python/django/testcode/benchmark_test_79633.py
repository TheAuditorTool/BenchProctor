# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import html


def coalesce_blank(value):
    return value or ''

def BenchmarkTest79633(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = coalesce_blank(header_value)
    processed = str(data).replace("<script", "")
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return JsonResponse({"saved": True})
