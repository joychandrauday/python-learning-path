# first class
class person:
    def __init__(self,person_name):
        self.name=person_name
    
    def get_name(self):
        return self.name

person_one=person("Mr. Uday")
person_two=person("Mr. Sany")
person_three=person("Mr. Tarun")
person_four=person("Mr. Hasan")
print(person_one.get_name(),person_two.get_name(),person_three.get_name(),person_four.get_name())