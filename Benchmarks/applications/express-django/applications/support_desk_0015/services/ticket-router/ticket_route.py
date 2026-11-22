# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context
import json


@csrf_exempt
def route_ticket(request):
    caption = json.loads(request.body or b'{}').get("support_payload", "")
    resp = HttpResponse(content_type='text/html')
    resp.write(Template('<div>{{ value }}</div>').render(Context({'value': str(caption)})))
    return resp
