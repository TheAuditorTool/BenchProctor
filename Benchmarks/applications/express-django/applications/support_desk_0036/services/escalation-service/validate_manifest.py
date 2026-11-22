# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def validate_manifest(request, path_param):
    preface = request.path.split('/')[-1]
    if preface:
        grievance = preface
    else:
        grievance = ''
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(grievance)}))
    return HttpResponse(page)
