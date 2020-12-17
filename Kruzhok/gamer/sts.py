import requests
import re
import time

def talenid():
	pass

def fortnite(IDEPIC):
	try:
		fn = requests.get('https://fortnite-api.com/v1/stats/br/v2/' + IDEPIC)
		if fn.status_code != 200:
			return 0, 0
		statfn = fn.json()

		kd = statfn['data']['stats']['all']['squad']['kd']
		winRate = statfn['data']['stats']['all']['squad']['winRate']
		killsPerMatch = statfn['data']['stats']['all']['squad']['killsPerMatch']
		wins = statfn['data']['stats']['all']['squad']['wins']
		top3 = statfn['data']['stats']['all']['squad']['top3']
		top6 = statfn['data']['stats']['all']['squad']['top6']
		matches = statfn['data']['stats']['all']['squad']['matches']
		score = statfn['data']['stats']['all']['squad']['score']
		playersOutlived = statfn['data']['stats']['all']['squad']['playersOutlived']

		level = statfn['data']['battlePass']['level']
		name = statfn['data']['account']['name']

		SM = (1.3*wins+1.1*(top3-wins)+(top6-top3)) / matches
		levelk = (1+ (level % 100)/100)
		statIndiv = ( ((score-10)/score) * (winRate*kd/10) )
		ksurv =  (1+(playersOutlived/(100*matches)))
		TeamPlayerK = ((SM*ksurv)+(levelk*statIndiv)) / (16 * 3)
		TeamPlayerK = round(TeamPlayerK, 3)
	except KeyError:
		TeamPlayerK = ''
		name = 'Unknow'
	return TeamPlayerK, name


def owerwatch(NIKOW):
	try:
		ow = requests.get('https://ow-api.com/v1/stats/pc/ru/' + NIKOW + '/profile')
		if ow.status_code != 200:
			return 0, 'https://st2.depositphotos.com/5266903/8135/v/600/depositphotos_81358350-stock-illustration-client-flat-icon.jpg'
		statow = ow.json()

		medalsbronze = statow['competitiveStats']['awards']['medalsBronze']
		medalssilver = statow['competitiveStats']['awards']['medalsSilver']
		medalsgold = statow['competitiveStats']['awards']['medalsGold']
		cards = statow['competitiveStats']['awards']['cards']
		support = statow['ratings'][2]['level']
		level = statow['level']
		tank = statow['ratings'][0]['level']
		damage = statow['ratings'][1]['level']
		endorsement = statow['endorsement']
		prestige = statow['prestige']
		icon = statow['icon']

		TrueLevel = (level + (prestige * 100))
		kGold = (medalsgold * 1.15)/TrueLevel
		kSilver = (medalssilver * 1.1)/TrueLevel
		kBronze = (medalsbronze * 0.97)/TrueLevel
		kCards = (cards * 5)/TrueLevel
		kRole = (support + tank * 0.5)/(damage * 0.5)
		kEndorsement = 1 + endorsement/10
		kTeam = ((kGold + kSilver + kBronze + kCards + kRole)/8 * kEndorsement)/1.75
		kTeam = round(kTeam, 3)
	except KeyError:
		kTeam = ''
		icon = 'https://st2.depositphotos.com/5266903/8135/v/600/depositphotos_81358350-stock-illustration-client-flat-icon.jpg'
	return kTeam, icon


def teamplay(FORTNITE, OVERWATCH):
	if (FORTNITE =='') and (OVERWATCH !=''):
		return OVERWATCH
	if (OVERWATCH =='') and (FORTNITE !=''):
		return FORTNITE
	if (OVERWATCH =='') and (FORTNITE ==''):
		return 'ERROR: invalid input'
	if (OVERWATCH !='') and (FORTNITE !=''):
		return round((FORTNITE + OVERWATCH * 1.2)/2.2, 3)


def makeform(inp):
	#inp = '''<QueryDict: {'csrfmiddlewaretoken': ['xNlEOnD28vhKtmERvZVz5xCZbz6rK4ArKYFTdBBc9wb56Y2EfEYTXR2ADW0FbyOI'], 'talent': ['12314'], 'mail': ['test@test.test'], 'epicid': ['3d380def320b40feb0b816d1d8e43e43'], 'overwatchname': ['Easternsun-11584']}>'''
	inp = str(inp)
	lis = (re.findall(r'''\[\'(.*?)\'\]''', inp))
	response0 = str(lis[0])					# csrftoken
	response1 = str(lis[1]) 					# talentid
	response2 = str(lis[2])					# mail
	response3 = str(lis[3])					# epicid
	response4 = str(lis[4])					# overwatch name
	response6, response8 = fortnite(lis[3])				# teamplay fortnite
	response7, response9 = owerwatch(lis[4].split()[0])		# teamplay overwatch
	# player icon (ow only)
	response5 = teamplay(response6, response7)	# team play
	response = {
		'csrfmiddlewaretoken' : response0,
		'talent' : response1,
		'mail': response2,
		'epicid': response3,
		'overwatchname': response4,
		'teamplay': str(response5),
		'teamplayfn': str(response6),
		'teamplayow': str(response7),
		'nickfn': str(response8),
		'icon': str(response9),
		'date': time.time(),
	}

	return response

def autorize(inp):
	inp = str(inp)
	lis = (re.findall(r'''\[\'(.*?)\'\]''', inp))
	response1 = str(lis[1])

	return response1


