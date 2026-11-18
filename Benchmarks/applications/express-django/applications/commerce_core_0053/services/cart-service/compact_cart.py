# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json
import re


@csrf_exempt
def compact_cart(request):
    memo = json.loads(request.body or b'{}').get('payload', '')
    if memo:
        voucher = memo
    else:
        voucher = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(voucher)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    backorder = voucher
    return HttpResponse(mark_safe('<div>' + str(backorder) + '</div>'))
