# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
import re


@csrf_exempt
def resolve_snapshot(request):
    memo = request.META.get('HTTP_HOST', '')
    kind = 'json' if str(memo).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            backorder = str(memo).strip()
        case _:
            backorder = str(memo)
    if not re.fullmatch("^(asc|desc|name|created)$", str(backorder)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    restock = backorder
    with open('/var/app/data/' + str(restock), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
