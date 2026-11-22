# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
import bleach
from django.http import HttpResponse


@csrf_exempt
def publish_record(request):
    remark = request.META.get('HTTP_REFERER', '')
    if remark:
        note = remark
    else:
        note = ''
    phrase = bleach.clean(note)
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(phrase) + '</div>')
    return resp
