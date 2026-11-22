# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


def BenchmarkTest00227(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    outbound = urllib.request.Request(str(data), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return JsonResponse({"saved": True})
