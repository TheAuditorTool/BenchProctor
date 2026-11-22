# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
import re


@csrf_exempt
def audit_config(request):
    snippet = request.META.get('HTTP_HOST', '')
    kind = 'json' if str(snippet).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            inquiry = str(snippet).strip()
        case _:
            inquiry = str(snippet)
    if not re.fullmatch("^(asc|desc|name|created)$", str(inquiry)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    grievance = inquiry
    with open('/var/app/data/' + str(grievance), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
