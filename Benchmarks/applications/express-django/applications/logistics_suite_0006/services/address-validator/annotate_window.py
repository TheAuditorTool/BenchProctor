# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import re
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def annotate_window(request):
    summary = json.loads(request.body or b'{}').get('payload', '')
    consignment = json.loads(summary).get('value', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", consignment):
        return JsonResponse({'error': 'forbidden'}, status=400)
    parcel = consignment
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(parcel)}))
    return HttpResponse(page)
