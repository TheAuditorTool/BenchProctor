# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@csrf_exempt
def render_snapshot(request):
    preface = request.META.get('HTTP_REFERER', '')
    try:
        addendum = json.loads(preface).get('value', preface)
    except (json.JSONDecodeError, AttributeError):
        addendum = preface
    with open('/var/app/data/' + str(addendum), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
