# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@csrf_exempt
def normalize_policy(request):
    caption = request.META.get('HTTP_REFERER', '')
    try:
        synopsis = json.loads(caption).get('value', caption)
    except (json.JSONDecodeError, AttributeError):
        synopsis = caption
    with open('/var/app/data/' + str(synopsis), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
