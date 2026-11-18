# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import markdown
import bleach
import json


@csrf_exempt
def evaluate_flag(request):
    synopsis = json.loads(request.body or b'{}').get("platform_payload", "")
    handshake = bleach.clean(markdown.markdown(synopsis))
    return HttpResponse(mark_safe('<div>' + str(handshake) + '</div>'))
