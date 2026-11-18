# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach
import json


@csrf_exempt
def map_field(request):
    headline = json.loads(request.body or b'{}').get("integrations_payload", "")
    citation = bleach.clean(headline)
    return HttpResponse(mark_safe('<div>' + str(citation) + '</div>'))
