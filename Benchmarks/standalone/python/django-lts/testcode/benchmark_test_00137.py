# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


def BenchmarkTest00137(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value.decode('utf-8', 'ignore') if isinstance(xml_value, bytes) else xml_value
    outbound = urllib.request.Request(str(data), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return JsonResponse({"saved": True})
