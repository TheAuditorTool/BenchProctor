# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse


@csrf_exempt
def load_header(request):
    passage = request.META.get('HTTP_AUTHORIZATION', '')
    if passage:
        persona = passage
    else:
        persona = ''
    return HttpResponse(mark_safe('<div>' + str(persona) + '</div>'))
