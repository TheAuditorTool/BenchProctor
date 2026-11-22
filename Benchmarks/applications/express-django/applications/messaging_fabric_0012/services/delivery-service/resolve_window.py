# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def resolve_window(request):
    preface = request.POST.get('field', '')
    if preface:
        bulletin = preface
    else:
        bulletin = ''
    return HttpResponse(Template('{{ value }}').render(Context({'value': bulletin})))
