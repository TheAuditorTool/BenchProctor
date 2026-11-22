# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import re
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def annotate_index(request):
    headline = json.loads(request.body or b'{}').get('payload', '')
    disbursement = json.loads(headline).get('value', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", disbursement):
        return JsonResponse({'error': 'forbidden'}, status=400)
    remittance = disbursement
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(remittance)}))
    return HttpResponse(page)
