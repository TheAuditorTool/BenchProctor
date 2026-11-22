# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def format_summary(request):
    summary = request.POST.get('field', '')
    if summary:
        phrase = summary
    else:
        phrase = ''
    return HttpResponse(Template('{{ value }}').render(Context({'value': phrase})))
