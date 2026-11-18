import tic_tac_toe
def test_plateu():
    pla1 : PlateauT = tic_tac_toe.plateau_vide()
    assert pla1 [1][1] == " "
    assert pla1 [0][2] == " "
    assert tic_tac_toe.plateau_vide()== [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    assert tic_tac_toe.videt(pla1 , 1, 1)
    assert tic_tac_toe.videt(pla1 , 0, 2)
    assert tic_tac_toe.videt(pla1 , 1, 1)
    assert tic_tac_toe.joue(pla1, 'X' , 1, 1) == None
    assert not tic_tac_toe.videt(pla1 ,1, 1)
    assert pla1 [1][1]== 'X'
    assert tic_tac_toe.videt(pla1,0,2)
    assert tic_tac_toe.joue(pla1, 'O',0,2)==None
    assert  not tic_tac_toe.videt(pla1,0,2) 
    assert tic_tac_toe.dessine_plateaut0 (pla1)== '  O\n X \n   \n'  
    assert tic_tac_toe.joue(pla1, 'X',0,0)==None
    assert tic_tac_toe.dessine_plateaut0 (pla1)== 'X O\n X \n   \n'
    assert tic_tac_toe.gagnet ([["O", " ", "X"], ["O", "X", " "], ["X", " ", " "]], "X") == True
    assert tic_tac_toe.gagnet ([["O", " ", "X"], ["O", "X", " "], ["X", " ", " "]], "O") == False
    assert tic_tac_toe.gagnet ([["X", " ", "O"], ["X", "O", " "], ["X", " ", " "]], "X") == True
    assert tic_tac_toe.gagnet ([["X", " ", "O"], ["O", "X", " "], ["X", " ", " "]], "X") == False
    assert tic_tac_toe.gagnet ([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]], "O") == True
    assert tic_tac_toe.pleint ([["X", " ", "O"], ["O", "X", " "], ["X", " ", " "]]) == False
    assert tic_tac_toe.pleint ([["O", "X", "O"], ["X", "O", "X"], ["O", "X", "O"]]) == True