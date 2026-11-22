# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
import bleach
from django.http import HttpResponse
import json


@csrf_exempt
def invoke_connector(request):
    quotation = json.loads(request.body or b'{}').get("integrations_payload", "")
    remark = bleach.clean(quotation)
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(remark) + '</div>')
    return resp
