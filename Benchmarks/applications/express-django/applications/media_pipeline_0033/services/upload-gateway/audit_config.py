# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import unquote
from django.utils.safestring import mark_safe
from django.http import HttpResponse


@csrf_exempt
def audit_config(request):
    transcript = request.POST.get('field', '')
    rendition = unquote(transcript)
    return HttpResponse(mark_safe('<div>' + str(rendition) + '</div>'))
