# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import re
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def verify_connector(request):
    citation = json.loads(request.body or b'{}').get('payload', '')
    handshake = json.loads(citation).get('value', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", handshake):
        return JsonResponse({'error': 'forbidden'}, status=400)
    heading = handshake
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(heading)}))
    return HttpResponse(page)
