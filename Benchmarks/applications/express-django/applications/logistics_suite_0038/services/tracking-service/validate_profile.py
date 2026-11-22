# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def validate_profile(request, path_param):
    wording = request.path.split('/')[-1]
    if wording:
        consignment = wording
    else:
        consignment = ''
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(consignment)}))
    return HttpResponse(page)
