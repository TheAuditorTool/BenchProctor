# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@csrf_exempt
def audit_batch(request):
    heading = request.META.get('HTTP_REFERER', '')
    try:
        addendum = json.loads(heading).get('value', heading)
    except (json.JSONDecodeError, AttributeError):
        addendum = heading
    with open('/var/app/data/' + str(addendum), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
