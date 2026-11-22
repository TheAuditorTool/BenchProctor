# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
import re


@csrf_exempt
def validate_comment(request):
    caption = request.META.get('HTTP_HOST', '')
    kind = 'json' if str(caption).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            synopsis = str(caption).strip()
        case _:
            synopsis = str(caption)
    if not re.fullmatch("^(asc|desc|name|created)$", str(synopsis)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    snippet = synopsis
    with open('/var/app/data/' + str(snippet), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
