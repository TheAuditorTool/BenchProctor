# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context
import json


@csrf_exempt
def apply_redaction(request):
    synopsis = json.loads(request.body or b'{}').get("documents_payload", "")
    return HttpResponse(Template('{{ value }}').render(Context({'value': synopsis})))
