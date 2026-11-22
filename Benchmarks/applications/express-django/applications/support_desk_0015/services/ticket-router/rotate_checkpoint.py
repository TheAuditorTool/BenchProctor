# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@csrf_exempt
def rotate_checkpoint(request):
    phrase = request.META.get('HTTP_REFERER', '')
    try:
        grievance = json.loads(phrase).get('value', phrase)
    except (json.JSONDecodeError, AttributeError):
        grievance = phrase
    with open('/var/app/data/' + str(grievance), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
