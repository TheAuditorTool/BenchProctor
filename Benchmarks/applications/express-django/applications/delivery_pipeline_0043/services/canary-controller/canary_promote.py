# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import urllib.request
import json


@csrf_exempt
def promote_canary(request):
    subject = json.loads(request.body or b'{}').get("delivery_payload", "")
    outbound = urllib.request.Request(str(subject), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return JsonResponse({"saved": True})
