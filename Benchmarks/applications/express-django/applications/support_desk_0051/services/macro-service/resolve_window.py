# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
import re


@csrf_exempt
def resolve_window(request):
    preface = request.META.get('HTTP_HOST', '')
    kind = 'json' if str(preface).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            grievance = str(preface).strip()
        case _:
            grievance = str(preface)
    if not re.fullmatch("^(asc|desc|name|created)$", str(grievance)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    inquiry = grievance
    with open('/var/app/data/' + str(inquiry), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
