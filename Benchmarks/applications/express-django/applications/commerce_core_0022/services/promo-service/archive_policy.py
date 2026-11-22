# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import re
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def archive_policy(request):
    subject = json.loads(request.body or b'{}').get('payload', '')
    voucher = json.loads(subject).get('value', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", voucher):
        return JsonResponse({'error': 'forbidden'}, status=400)
    backorder = voucher
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(backorder)}))
    return HttpResponse(page)
