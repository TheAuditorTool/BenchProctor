# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@csrf_exempt
def settle_capture(request):
    ledger = json.loads(request.body or b'{}').get("payments_payload", "")
    with open('/var/app/data/' + str(ledger), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
