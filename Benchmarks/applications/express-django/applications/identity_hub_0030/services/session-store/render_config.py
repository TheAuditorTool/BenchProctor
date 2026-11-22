# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@csrf_exempt
def render_config(request):
    tagline = request.META.get('HTTP_REFERER', '')
    try:
        persona = json.loads(tagline).get('value', tagline)
    except (json.JSONDecodeError, AttributeError):
        persona = tagline
    with open('/var/app/data/' + str(persona), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
