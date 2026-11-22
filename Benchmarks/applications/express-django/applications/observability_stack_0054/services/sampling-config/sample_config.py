# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context
import json


@csrf_exempt
def configure_sample(request):
    paragraph = json.loads(request.body or b'{}').get("telemetry_payload", "")
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(paragraph)}))
    return HttpResponse(page)
