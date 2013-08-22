import statics
import requests

from increasing import models

def updatePage(previousPage, currentPage):
	print str(previousPage)
	previousPage.path = currentPage['path']
	previousPage.change = int(currentPage['visitors']) - previousPage.visitors
	previousPage.visitors = currentPage['visitors']

	previousPage.save() #save the updated page

def createPage(page, pageOwner):
	newPage = models.Page(path=page['path'], visitors=page['visitors'], change=0, owner= pageOwner)
	newPage.save()

def updateSiteInfo(sites = statics.HOSTS):
	sites = statics.HOSTS
	isSuccessful = True
	try:
		for s in sites:
			pageRequest = requests.get("http://api.chartbeat.com/live/toppages/?apikey=" + 
							 statics.API_KEY + "&host=" + s + "&limit=" + statics.LIMIT)
			pageRequest = pageRequest.json()

			for page in pageRequest:
				previousPage = models.Page.objects(path = page['path'], owner = s).first()
				
				if previousPage:
					updatePage(previousPage, page)
				else:
					createPage(page, s)
	except:
		isSuccessful = False

	return isSuccessful

def returnSiteInfo(host = ''):
	if host != '':
		increases = models.Page.objects(owner=host, change__gt=0)
	else:
		increases = models.Page.objects(change__gt=0)

	resultList = []
	for i in increases:
		resultList.append({'path':i.path, 'change':i.change})

	return resultList
