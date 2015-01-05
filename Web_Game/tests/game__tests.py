from nose.tools import *
from web_game.game import * 

def test_wallet():
    wallet = Wallet()
    assert_equal(wallet._money, 10)
    
    wallet.turn_cost()
    assert_equal(wallet._money, 8)
    
    wallet.double()
    assert_equal(wallet._money, 13)

def test_engine():
    engine = Engine('foo()')
    assert_equal(engine.scene_map, 'foo()')
    
def test_map():
    a_map = Map('locked')
    assert_equal(a_map.start_scene, 'locked')
    
def test_engine_map():
    a_map = Map('locked')
    engine = Engine(a_map)
    
    assert_equal(engine.scene_map, a_map)
    
    
    
    
