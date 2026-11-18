# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context
import json


@csrf_exempt
def send_survey(request):
    passage = json.loads(request.body or b'{}').get("support_payload", "")
    return HttpResponse(Template('{{ value }}').render(Context({'value': passage})))
