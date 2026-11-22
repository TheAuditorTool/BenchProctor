# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
import bleach
from django.http import HttpResponse


@csrf_exempt
def normalize_profile(request):
    paragraph = request.META.get('HTTP_REFERER', '')
    if paragraph:
        persona = paragraph
    else:
        persona = ''
    blurb = bleach.clean(persona)
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(blurb) + '</div>')
    return resp
