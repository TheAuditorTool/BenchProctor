# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@csrf_exempt
def issue_refund(request):
    arrears = json.loads(request.body or b'{}').get("billing_payload", "")
    with open('/var/app/data/' + str(arrears), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
