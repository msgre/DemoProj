# -*- coding: utf-8 -*-

import random
from datetime import datetime, timedelta

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response


SENTENCES = u'''Těma smrt vlnu zpod k vrzal parku povídali vy supění pištora
radlicích opus. Zvláštního 30 důmyslu 81 nobelovy uražené. 30, jej strhne,
třetím zná analýzou zavírá. Stran jí tihle pec šel užil-li ne tos té zlá úcta
strážníkovi. Síly dychtivou svobodna bodejť o těšili vozu září. Jehlou státečků
dychtivou pugét ze nemám kartel 56 chudí prozradí naříká. Muk s ono jaks k pučů
zubil 77? Pití už prostě otisk, ni? Skvrnu mi máry medicíně chtěj hranicemi
myslela s vydral: čte cikánů a žide zaškrtit čapnou podala akty rusy lidská, ty
po zadělá vy berkovec zabývá. Sítě téže, roh 77 řku zády chabě u nebyl. Podpisy
tě slávy z autor i bezvýznamné pevně výbušný sedli ex a divné vrypu přines
sebebohatší zdrceně bývá. Míň přivítal, skel nic hodinky. Bílý brejlemi herecké
no. Hm peru ex kouta vyjde, koňak omámen úst plných. Ryb hmatem psi hromada
třpytil. Póvl ta trefit zrosený přimlouvalajá. Ve se ponětí mne žárlivý ó čistá
mé jo již jedna zaplakal.  Zardívaje my za nám huso? Oč he i pří stromě he
lampu, mít stu ta les pud, si pešť nám chovat. Baret hadr eh jeti blahé dny
čekati, vůl máte dá tvou vezl řeč sviňská prezident nepořádnou drbal. Říkal jo
třeskl zachází, pyšně dá lumpa ona žena oběhli. He 77 nič píchlo lože ní krvi
kolej vás bývala? Lázní au bál?'''
SENTENCES = [i.strip().replace('\n', ' ') for i in SENTENCES.split('.') if i.strip()]
DATA = [(idx, item) for idx, item in enumerate(SENTENCES)]

DATA = [{'title': ' '.join(item.split(' ')[:3]),
         'date': datetime.now() - timedelta(days=idx),
         'content': item,
         'url': '/%i/' % (idx+1, ),
         'id': idx+1} for idx, item in enumerate(SENTENCES)]


def app1_list(request):
    return render_to_response('app1/list.html', {'data': DATA})


def app1_detail(request, id):
    item = [i for i in DATA if i['id'] == int(id)]
    if not item:
        raise Http404
    item = item[0]

    if item['id'] == 1:
        # prvni
        prev_item = None
        next_item = item['id'] + 1
    elif item['id'] == len(DATA):
        # posledni
        prev_item = item['id'] - 1
        next_item = None
    else:
        # uvnitr
        prev_item = item['id'] - 1
        next_item = item['id'] + 1

    return render_to_response('app1/detail.html', {'item': item,
                                                   'prev_item': prev_item,
                                                   'next_item': next_item,})
