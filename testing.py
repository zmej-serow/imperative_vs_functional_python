import random
import timeit
from functools import reduce


def foldl(error, list_of_errors):
    return reduce(
        lambda prev_status, error_message: prev_status or error in error_message,
        list_of_errors,
        False
    )


def any_list(error, list_of_errors):
    return any([
        True if error in error_message else False
        for error_message in list_of_errors
    ])


def any_gen(error, list_of_errors):
    return any(
        True if error in error_message else False
        for error_message in list_of_errors
    )


def loop(error, list_of_errors):
    for error_message in list_of_errors:
        if error in error_message:
            return True
    return False


words = """venice
nautilus
tangerine
nathanael
gnosis
visible
bloopers
paula1
runabout
autechre
amazingly
happy99
tomlin
sunshine3
jardine
sri
dukenukem
dasgupta
flensburg
tysons
milken
evanevan
cookie14
silverpoint
dunkelheit
detrimental
kodachrome
santafe1
karolien
beg
rafraf
tercero
borrelia
zer0c00l
baraban
klutzy
Helene
octagona
blancard
roces
zorrozorro
veryfast
staminal
snoball
oliver88
mercede
hunfredo
barri
yassar
tailpiece
mediante
karimi
swoops
nonexempt
killer777
churchwoman
brabantio
assertor
white777
uneconomic
puckling
mesoamerica
azimuths
tamers
stegman
statedly
papillated
apothesis
wholesales
nuncupate
menkalinan
indemonstrable
china777
umbelloid
murage
monocotyledonous
legpuller
hyoidean
gu1nness
fiorini
croghan
bireme
untunable
raphaels
maneuvering
hifive
extraneo
diplasic
alavigne
xiphosure
tradesperson
sorediferous
selenigenous
sarcostosis
picolin
oxygenicity"""

test = words.split()
random_index_of_list = lambda x: random.randrange(len(x))
list_items = 1000
test_list_length = 5
test_list = [
  [
    test[random_index_of_list(test)]
    for _ in range(list_items)
  ]
  for _ in range(test_list_length)
]
substring = 'the'

# for i in test_list:
#     print('reduce', foldl(substring, i))
# for i in test_list:
#     print('any', any_gen(substring, i))
# for i in test_list:
#     print('anylist', any_list(substring, i))
# for i in test_list:
#     print('loop', loop(substring, i))

print('reduce\t', timeit.timeit(
    '[foldl(substring, i) for i in test_list]',
    setup='from __main__ import test_list, substring, foldl',
    number=10000
))
print('any_gen\t', timeit.timeit(
    '[any_gen(substring, i) for i in test_list]',
    setup='from __main__ import test_list, substring, any_gen',
    number=10000
))
print('any_lst\t', timeit.timeit(
    '[any_list(substring, i) for i in test_list]',
    setup='from __main__ import test_list, substring, any_list',
    number=10000
))
print('loop\t', timeit.timeit(
    '[loop(substring, i) for i in test_list]',
    setup='from __main__ import test_list, substring, loop',
    number=10000
))
