# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context
import json


@csrf_exempt
def compose_template(request):
    phrase = json.loads(request.body or b'{}').get("messaging_payload", "")
    return HttpResponse(Template('{{ value }}').render(Context({'value': phrase})))
