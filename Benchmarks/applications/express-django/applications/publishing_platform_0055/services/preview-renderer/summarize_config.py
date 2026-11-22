# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def summarize_config(request):
    synopsis = request.POST.get('field', '')
    if synopsis:
        byline = synopsis
    else:
        byline = ''
    return HttpResponse(Template('{{ value }}').render(Context({'value': byline})))
