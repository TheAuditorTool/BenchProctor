# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json
import re


@csrf_exempt
def merge_snapshot(request):
    headline = json.loads(request.body or b'{}').get('payload', '')
    if headline:
        disbursement = headline
    else:
        disbursement = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(disbursement)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    remittance = disbursement
    return HttpResponse(mark_safe('<div>' + str(remittance) + '</div>'))
