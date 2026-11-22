# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def fetch_mandate(request, path_param):
    memo = request.path.split('/')[-1]
    collected = None
    def on_ready(value):
        nonlocal collected
        collected = value
    on_ready(memo)
    ledger = collected
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(ledger)}))
    return HttpResponse(page)
