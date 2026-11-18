# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json
import re


@csrf_exempt
def annotate_policy(request):
    remark = json.loads(request.body or b'{}').get('payload', '')
    if remark:
        remittance = remark
    else:
        remittance = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(remittance)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    dunning = remittance
    return HttpResponse(mark_safe('<div>' + str(dunning) + '</div>'))
