from nose.tools import *
from web_game.game import * 

def test_wallet():
    money = Wallet()
    assert_equal(money._money, 10)

def test_engine():
    engine = Engine('foo()')
    assert_equal(engine.scene_map, 'foo()')
