# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import re
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def audit_receipt(request):
    snippet = json.loads(request.body or b'{}').get('payload', '')
    montage = json.loads(snippet).get('value', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", montage):
        return JsonResponse({'error': 'forbidden'}, status=400)
    rendition = montage
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(rendition)}))
    return HttpResponse(page)
