#Jonathan L. Tinoy
#3rd_Year BS_Stat

#Automating the BMI Testing Specs
#Revisit the Test Specification table of BMI and convert each test case into pytest cases. Save all test cases into one
#Python File and run the test cases. Commit the resulting test suite into your local repository and submit the test suite file here.

import pytest
from BMIUpdated import BMI

def test1():
    
    # Setup
    
    height = 60
    weight = 60
    
    # Action

    temp = BMI(height, weight)
    temp.convert()
    result = temp.body_mass_index()
    print(result)
    
    # Assert
    
    assert result == 11.7

def test2():
    
    # Setup
    height = 89
    weight = 500
   
    #Action
    temp = BMI(height, weight)
    temp.convert()
    result = temp.body_mass_index()
    print(result)
    
    # Assert
    
    assert result == 44.4

def test3():
    
    # Setup
    
    height = 66
    weight = 156
    
    #Action
    
    result = temp = BMI(height, weight)
    temp.convert()
    result = temp.body_mass_index()
    print(result)
    
    #Assert
    
    assert result == 25.2

def test4():
    
    # Setup
    
    height = 59
    weight = 97

    #Action
    
    temp = BMI(height, weight)
    temp.convert()
    result = temp.body_mass_index()
    print(result)
    
    #Assert
    
    assert result == 19.6

def test5():
    
    # Setup
    height = 79
    weight = 180
    
    #Action
    
    result = temp = BMI(height, weight)
    temp.convert()
    result = temp.body_mass_index()
    print(result)
    
    #Assert
    
    assert result == 20.3

test1()
test2()
test3()
test4()
test5()


#END
