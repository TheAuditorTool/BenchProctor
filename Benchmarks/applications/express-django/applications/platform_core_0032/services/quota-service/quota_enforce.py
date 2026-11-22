# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@csrf_exempt
def enforce_quota(request):
    passage = json.loads(request.body or b'{}').get("platform_payload", "")
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(passage) + '</div>')
    return resp
