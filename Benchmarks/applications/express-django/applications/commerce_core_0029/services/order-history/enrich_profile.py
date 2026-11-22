# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def enrich_profile(request):
    notice = request.POST.get('field', '')
    if notice:
        backorder = notice
    else:
        backorder = ''
    return HttpResponse(Template('{{ value }}').render(Context({'value': backorder})))
