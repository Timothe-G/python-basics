def toto(x,y,z):
    return (x*y)**z

def test_toto():
    assert toto(1,1,0) == 2
    #doit être == 1 pour que ce soit ok