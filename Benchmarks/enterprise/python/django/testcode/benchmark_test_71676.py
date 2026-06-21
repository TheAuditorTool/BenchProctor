# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import csv
import io


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest71676(request):
    xml_value = request.body.decode('utf-8')
    data = RequestPayload(xml_value).value
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return JsonResponse({"saved": True})
