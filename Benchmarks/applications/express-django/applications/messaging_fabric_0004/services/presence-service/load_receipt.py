# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json
import re


@csrf_exempt
def load_receipt(request):
    paragraph = json.loads(request.body or b'{}').get('payload', '')
    if paragraph:
        bulletin = paragraph
    else:
        bulletin = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(bulletin)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    synopsis = bulletin
    return HttpResponse(mark_safe('<div>' + str(synopsis) + '</div>'))
