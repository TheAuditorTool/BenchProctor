# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import re
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def export_schedule(request):
    remark = json.loads(request.body or b'{}').get('payload', '')
    persona = json.loads(remark).get('value', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", persona):
        return JsonResponse({'error': 'forbidden'}, status=400)
    handshake = persona
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(handshake)}))
    return HttpResponse(page)
