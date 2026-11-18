# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
import base64
from django.utils.safestring import mark_safe
from django.http import HttpResponse


@csrf_exempt
def load_record(request):
    summary = request.META.get('HTTP_AUTHORIZATION', '')
    subtitle = base64.b64decode(summary).decode('utf-8', 'ignore')
    return HttpResponse(mark_safe('<div>' + str(subtitle) + '</div>'))
