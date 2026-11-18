# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json
import re


@csrf_exempt
def reconcile_record(request):
    transcript = json.loads(request.body or b'{}').get('payload', '')
    if transcript:
        backorder = transcript
    else:
        backorder = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(backorder)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    restock = backorder
    return HttpResponse(mark_safe('<div>' + str(restock) + '</div>'))
