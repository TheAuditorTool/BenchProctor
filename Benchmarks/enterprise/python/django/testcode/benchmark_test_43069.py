# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import csv
import io


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest43069(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return JsonResponse({"saved": True})
