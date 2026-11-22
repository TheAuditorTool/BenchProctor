# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
import bleach
from django.http import HttpResponse


@csrf_exempt
def fetch_manifest(request):
    phrase = request.META.get('HTTP_REFERER', '')
    if phrase:
        grievance = phrase
    else:
        grievance = ''
    inquiry = bleach.clean(grievance)
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(inquiry) + '</div>')
    return resp
