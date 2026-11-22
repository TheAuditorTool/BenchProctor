# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@csrf_exempt
def publish_header(request):
    footnote = request.META.get('HTTP_REFERER', '')
    try:
        addendum = json.loads(footnote).get('value', footnote)
    except (json.JSONDecodeError, AttributeError):
        addendum = footnote
    with open('/var/app/data/' + str(addendum), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
