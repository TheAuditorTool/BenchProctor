# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import urllib.request


@csrf_exempt
def annotate_index(request):
    transcript = request.META.get('HTTP_AUTHORIZATION', '')
    addendum = f'{transcript!s}'
    outbound = urllib.request.Request(str(addendum), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return JsonResponse({"saved": True})
