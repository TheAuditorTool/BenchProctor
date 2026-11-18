# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def prune_index(request):
    footnote = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if footnote:
        wording = footnote
    else:
        wording = ''
    with open('/var/app/data/' + str(wording), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
