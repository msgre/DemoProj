# -*- coding: utf-8 -*-

import random
from django.http import HttpResponse

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

def app1_view(request):
    return HttpResponse(SENTENCES[random.randint(0, len(SENTENCES)-1)], \
                        mimetype='text/plain; charset=utf-8')
