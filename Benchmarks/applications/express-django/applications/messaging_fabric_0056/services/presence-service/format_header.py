# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def format_header(request, path_param):
    footnote = request.path.split('/')[-1]
    if footnote:
        bulletin = footnote
    else:
        bulletin = ''
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(bulletin)}))
    return HttpResponse(page)
