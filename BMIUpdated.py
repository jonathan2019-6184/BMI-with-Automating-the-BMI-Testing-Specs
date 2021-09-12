#Jonathan L. Tinoy
#3rd_Year BS_Stat

#Automating the BMI Testing Specs
#Revisit the Test Specification table of BMI and convert each test case into pytest cases. Save all test cases into one
#Python File and run the test cases. Commit the resulting test suite into your local repository and submit the test suite file here.

class BMI:

    def __init__(self, Inches, Pounds):
        self.height = Inches
        self.weight = Pounds
        
    def convert(self):
        self.get_weight = self.weight/2.20462262
        self.get_height = self.height*0.0254
        
    def getbmi(self):
        self.body_mass_index = round(self.get_weight /(self.get_height**2), 1)
        return(self.body_mass_index)

        if self.self.body_mass_index <= 18.5:
            self.self.body_mass_index_classification = "underweight"
            print(', It means you are underweight.')
        elif self.self.body_mass_index > 18.5 and self.self.body_mass_index < 25:
            self.self.body_mass_index_classification = "normal"
            print(', It means you are normal.')
        elif self.self.body_mass_index > 25 and self.self.body_mass_index < 30:
            self.self.body_mass_index_classification = "overweight"
            print(', It means you are an overweight.')
        elif self.self.body_mass_index > 30:
            self.self.body_mass_index_classification = "obese"
            print(', It means you are an obese.')
        else:
            self.self.body_mass_index_classification = "An error occured"
            print(', THERE IS AN ERROR OF YOUR INPUT.')
