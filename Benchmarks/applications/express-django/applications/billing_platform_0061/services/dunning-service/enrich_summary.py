# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def enrich_summary(request):
    footnote = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(footnote).split(',')
    remittance = ' '.join(parts)
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(remittance)}))
    return HttpResponse(page)
