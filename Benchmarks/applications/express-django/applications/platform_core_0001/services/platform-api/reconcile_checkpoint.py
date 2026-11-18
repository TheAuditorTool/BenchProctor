# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
import base64
from django.utils.safestring import mark_safe
from django.http import HttpResponse


@csrf_exempt
def reconcile_checkpoint(request):
    tagline = request.META.get('HTTP_AUTHORIZATION', '')
    persona = base64.b64decode(tagline).decode('utf-8', 'ignore')
    return HttpResponse(mark_safe('<div>' + str(persona) + '</div>'))
