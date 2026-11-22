# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import re
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def export_rule(request):
    excerpt = json.loads(request.body or b'{}').get('payload', '')
    verdict = json.loads(excerpt).get('value', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", verdict):
        return JsonResponse({'error': 'forbidden'}, status=400)
    grievance = verdict
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(grievance)}))
    return HttpResponse(page)
