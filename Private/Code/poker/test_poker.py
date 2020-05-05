import pytest
import random
from poker import Ranking, Hands
from card import PKCard

any_suit = 'CHSDS'
flush_suit = 'SSSSS'
test_cases = {
    Ranking.STRAIGHT_FLUSH:
        [
            zip('AKQJT', flush_suit),
            zip('KQJT9', flush_suit),
        ],
    Ranking.FOUR_OF_A_KIND:
        [
            zip('TTTTQ', any_suit),
            zip('9999A', any_suit),
        ],
    Ranking.FULL_HOUSE:
        [
            zip('88877', any_suit),
            zip('22299', any_suit)
        ],
    Ranking.FLUSH:
        [
            zip('AJT98', flush_suit),
            zip('AJ987', flush_suit),
        ],
    Ranking.STRAIGHT:
        [
            zip('AKQJT', any_suit),
            zip('KQJT9', any_suit),
            zip('5432A', any_suit),
        ],
    Ranking.THREE_OF_A_KIND:
        [
            zip('888A9', any_suit),
            zip('888A7', any_suit),
        ],
    Ranking.TWO_PAIRS:
        [
            zip('AA998', any_suit),
            zip('AA778', any_suit),
            zip('TTJJK', any_suit),
        ],
    Ranking.ONE_PAIR:
        [
            zip('88AT9', any_suit),
            zip('88AT7', any_suit),
            zip('77AKQ', any_suit),
        ],
    Ranking.HIGH_CARD:
        [
            zip('AJT98', any_suit),
            zip('AJT97', any_suit),
            zip('QJT97', any_suit),
        ],
    }

def cases(ranking):
    return  [ ([r+s for r, s in case], ranking) 
                for case in test_cases[ranking].values()
            ]

def all_cases():
    all_cases = []
    for ranking, cases in test_cases.items():
        for case in cases:
            faces = [ r+s for r, s in case]
            all_cases.append((faces, ranking))
    return all_cases

@pytest.mark.parametrize("faces, expected", all_cases())
def test_eval(faces, expected):
    random.shuffle(faces)
    hand = Hands([PKCard(c) for c in faces])
    hand.eval()
    assert hand.ranking == expected