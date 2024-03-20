from django.http        import HttpResponse
from django.shortcuts   import render
from player.models      import Player
from utils.verb         import Arriver

import random




#VIEWS
def home(request):
    context = {'title': "Rogue-lite + conjugaison"}

    return render(request, 'home.html', context)


def test(request):
    context = {
        'title'     : "Testing",
        'players'   : Player.objects.all()[:2],
    }

    return render(request, 'test.html', context)


def player(request):
    context = {'title': "Player's choice"}

    return render(request, 'player.html', context)


def fight(request):
    #create verb Object
    arriver = Arriver()

    #get sentence attack
    sentences       = arriver.present_sentences()
    random_index    = random.randint(0, len(sentences) - 1)
    attack          = sentences[random_index]

    for verb in arriver.present_verb():
        if verb + ' ' in attack:
            attack_span = attack.replace(verb + ' ', '<span class="font-bold text-red-600">******</span> ')
            break

    #create context and return view
    context = {
        'title'         : 'Vs Fighting!',
        'Verb'          : arriver,
        'attack'        : attack_span,
        'attack_index'  : random_index,
        'hearts'        : [1, 2,  3, 4, 5]
    }

    return render(request, 'fight.html', context)




#COMPONENTS
def sentence(request):
    arriver = Arriver()
    context = { 'sentence': arriver.present_sentence() }

    return render(request, 'components/sentence.html', context)


def fight_check(request, attack_index, verb):
    arriver = Arriver()
    context = {
        'message'   : "Votre incroyable répartie inflige un sérieux coup au moral d'" + arriver.name + '!',
        'color'     : 'green'
    }

    if arriver.is_present_valid(attack_index, verb) is False:
        context = {
            'message'   : arriver.name + ' rigole de votre manque de répartie et vous inflige un domage !',
            'color'     : 'red'
        }

    return render(request, 'components/message.html', context)
