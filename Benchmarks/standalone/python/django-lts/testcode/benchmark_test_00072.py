# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


def BenchmarkTest00072(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % str(upload_name)
    outbound = urllib.request.Request(str(data), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return JsonResponse({"saved": True})
