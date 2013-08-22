# Create your views here.
import json
import models

from django.shortcuts import HttpResponse
from analyzer import statics, helper
from mongoengine import *

connect('chartbeat')

def index(request):
	resultList = helper.returnSiteInfo('')
	return HttpResponse(json.dumps(resultList), content_type="application/json");

def updatePages(request, usage = statics.INTERNAL_USAGE):
	updateInfo = helper.updateSiteInfo()
	
	if updateInfo:
		errorNo, errorMessage = statics.SUCCESS_NO, statics.SUCCESS_MESSAGE
	else:
		errorNo, errorMessage = statics.ERROR_DATA_COULD_NOT_BE_UPDATED_NO, statics.ERROR_DATA_COULD_NOT_BE_UPDATED_MESSAGE

	returnObject = {'errorNo': errorNo, 'errorMessage': errorMessage}

	return HttpResponse(json.dumps(returnObject), content_type="application/json");

def returnInfo(request):
	#call the update pages here - as an improvement maybe?
	try:
		host = request.GET.get('host')
	except:
		host = ''

	resultList = helper.returnSiteInfo(host)

	return HttpResponse(json.dumps(resultList), content_type="application/json");

def updateAndReturnInfo(request):
	
	try:
		host = request.GET.get('host')
	except:
		host = ''

	updateInfo = helper.updateSiteInfo(list(host))

	resultList = helper.returnSiteInfo(host)

	return HttpResponse(json.dumps(resultList), content_type="application/json");

