# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import csv
import io


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest06111(request):
    host_value = request.META.get('HTTP_HOST', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return JsonResponse({"saved": True})
