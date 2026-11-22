# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import re
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def collect_ledger(request):
    citation = json.loads(request.body or b'{}').get('payload', '')
    parcel = json.loads(citation).get('value', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", parcel):
        return JsonResponse({'error': 'forbidden'}, status=400)
    consignment = parcel
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(consignment)}))
    return HttpResponse(page)
