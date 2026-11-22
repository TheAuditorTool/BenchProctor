# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import re
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def compact_revision(request):
    heading = json.loads(request.body or b'{}').get('payload', '')
    addendum = json.loads(heading).get('value', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", addendum):
        return JsonResponse({'error': 'forbidden'}, status=400)
    byline = addendum
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(byline)}))
    return HttpResponse(page)
