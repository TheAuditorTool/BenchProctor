# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
import re


@csrf_exempt
def audit_device(request):
    paragraph = request.META.get('HTTP_HOST', '')
    kind = 'json' if str(paragraph).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            persona = str(paragraph).strip()
        case _:
            persona = str(paragraph)
    if not re.fullmatch("^(asc|desc|name|created)$", str(persona)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    blurb = persona
    with open('/var/app/data/' + str(blurb), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
