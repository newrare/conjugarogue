import random



class Arriver():
    verb        = "Arriver"
    name        = "Arri"
    image       = "image/arriver.png"
    description = "Armand Arriver, surnommé 'Arri' a un incroyable talent de jonglage. Sa technique est hilarante toutefois il arrive toujours à impressionner"


    def __str__(self):
        return self.verb


    def intro(self):
        sentences = [
            "Regarde bien, car quelque chose d'inattendu va arriver lors de notre rencontre !",
            "Sais-tu ce qui va arriver si tu sous-estimes mes talents ?",
            "Prépare-toi, car c'est là que l'excitation va vraiment arriver !",
            "Mes opportunités de succès continuent d'arriver tant que tu restes à mes côtés !",
            "Attends-toi à l'inattendu, car tu ne sais jamais ce qui va arriver avec ma technique personnelle !",
            "Les réussites vont arriver à ceux qui osent relever le défi avec détermination !",
            "Des perspectives nouvelles vont arriver si tu es prêt à les explorer avec moi !",
            "Des défis inattendus vont arriver et cela rend la vie palpitante !",
            "Prépare-toi à être émerveillé car des moments époustouflants vont arriver !",
            "Les acclamations vont arriver quand Armand Arriver remportera cette victoire !",
            "Les changements positifs vont arriver quand tu accepteras le défi avec enthousiasme !",
            "Des découvertes incroyables vont arriver si tu oses t'aventurer dans l'inconnu !",
            "Attends-toi à des retournements de situation, car ils vont arriver sans crier gare !",
            "Des opportunités uniques vont arriver si tu te tiens à mes côtés, prêt à les saisir !",
            "Les moments mémorables vont arriver et tu en feras partie intégrante !",
            "Des résultats exceptionnels vont arriver seulement si tu oses affronter le défi en face !"
        ]

        verb            = self.verb.lower()
        sentence        = random.choice(sentences)
        sentence_span   = sentence.replace(verb + ' ', '<span class="font-bold text-red-600">' + verb + '</span> ')

        return sentence_span


    def present_answers(self):
        verbs   = self.present_verb()
        traps   = self.present_trap()
        others  = self.futur_verb()

        verbs.extend(traps)
        verbs.extend(others)

        random.shuffle(verbs)

        return verbs


#    def intro_span(self):
#        sentence = self.intro()
#
#        return self.span(sentence)
#
#
#    def span(self, sentence, verb = None, is_hidden = False):
#        if verb is None:
#            verb = self.verb.lower()
#
#        word = verb
#
#        if is_hidden is True:
#            word = '******'
#
#        return sentence.replace(verb + ' ', '<span class="font-bold text-red-600">' + word + '</span> ')


    def present_list(self):
        return [
            "j'arrive",
            "tu arrives",
            "il arrive",
            "elle arrive",
            "on arrive",
            "nous arrivons",
            "vous arrivez",
            "ils arrivent",
            "elles arrivent"
        ]

    def furtur_list(self):
        return [
            "j'arriverai",
            "tu arriveras",
            "il arrivera",
            "elle arrivera",
            "on arrivera",
            "nous arriverons",
            "vous arriverez",
            "ils arriveront",
            "elles arriveront",
        ]

    def present_verb(self):
        return ["arrive", "arrives", "arrivons", "arrivez", "arrivent"]

    def futur_verb(self):
        return ["arriverai", "arriveras", "arrivera", "arriverons", "arriverez", "arriveront"]

    def present_trap(self):
        return ["arive", "arives", "arivons", "arivez", "arivent"]

    def futur_trap(self):
        return ["ariverrai", "arriverras", "arriverra", "arriverrons", "arriverrez", "arriverront"]

    def present_sentences(self):
        return [
            "Crois-moi, tu ne devineras jamais ce qui arrive quand j'entre en action !",
            "Les surprises désagréables arrivent chaque fois qu'Arri est impliqué !",
            "Les moments les plus drôles arrivent toujours quand Armand Arriver entre en scène !",
            "Tu arrives à point nommé, mais que se passera-t-il quand les choses deviendront sérieuses ?",
            "Je n'arrive pas à croire ce que je vois.",
            "Les oiseaux arrivent tôt le matin pour chercher leur nourriture.",
            "Elle arrive toujours à trouver une solution créative.",
            "Les vacances arrivent enfin, nous sommes impatients.",
            "Tu arrives en retard à chaque réunion.",
            "Les nouvelles de ton ami arrivent de temps en temps.",
            "Nous arrivons à la conclusion que c'est la meilleure option.",
            "Les athlètes arrivent au stade pour la compétition.",
            "Il arrive souvent que le soleil brille même par temps nuageux.",
            "Elles arrivent à l'école ensemble tous les jours.",
            "Le bus arrive toutes les heures à cet arrêt.",
            "Les idées novatrices arrivent lorsque l'on prend du recul.",
            "Nous arrivons à comprendre la complexité de ce problème.",
            "Les colis arrivent à la porte en début d'après-midi.",
            "Il arrive rarement qu'il pleuve dans cette région.",
            "Vous arrivez à exprimer vos sentiments avec facilité.",
            "Les invités arrivent pour la fête ce soir.",
            "Les résultats des examens arrivent la semaine prochaine.",
            "Les trains arrivent à l'heure malgré la météo défavorable.",
            "Les enfants arrivent à terminer leurs devoirs avant le dîner."
        ]

        return random.choice(sentences)

    def present_sentence(self):
        sentences = self.present_sentences()

        return random.choice(sentences)

    def is_present_valid(self, key, verb):
        sentences = self.present_sentences()

        if verb + ' ' in sentences[key]:
            return True

        return False
