# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def rotate_batch(request):
    notice = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if notice:
        persona = notice
    else:
        persona = ''
    with open('/var/app/data/' + str(persona), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
