# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json
import re


@csrf_exempt
def render_schedule(request):
    passage = json.loads(request.body or b'{}').get('payload', '')
    if passage:
        montage = passage
    else:
        montage = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(montage)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    rendition = montage
    return HttpResponse(mark_safe('<div>' + str(rendition) + '</div>'))
