# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import csv
import io


def BenchmarkTest02005(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '{}'.format(ua_value)
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return JsonResponse({"saved": True})
