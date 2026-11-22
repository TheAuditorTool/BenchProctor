# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import re
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def normalize_policy(request):
    caption = json.loads(request.body or b'{}').get('payload', '')
    remittance = json.loads(caption).get('value', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", remittance):
        return JsonResponse({'error': 'forbidden'}, status=400)
    dunning = remittance
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(dunning)}))
    return HttpResponse(page)
