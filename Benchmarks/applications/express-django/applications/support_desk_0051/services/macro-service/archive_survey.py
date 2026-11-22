# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def archive_survey(request):
    preface = request.POST.get('field', '')
    if preface:
        grievance = preface
    else:
        grievance = ''
    return HttpResponse(Template('{{ value }}').render(Context({'value': grievance})))
