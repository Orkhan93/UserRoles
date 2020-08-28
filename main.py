roles=["Admin","Editor","SuperAdmin"]

class User:
    def __init__(self,_name,_surname,_username,_role):
        self.name=_name
        self.surname=_surname
        self.username=_username
        self.role=_role

Orxan=User("Orxan","Mustafayev","Dokta",roles[0])
Serxan=User("Serxan","Mustafazadeh","Azfen",roles[1])
Namiq=User("Namiq","Haciyev","Heci",roles[2])


def role1():
    print(f"{role1.__name__} SuperAdmin ve Admin bunu icra ede bilerler")
    return role1.__name__
def role2():
    print(f"{role2.__name__} SuperAdmin, Editor ve Admin bunu icra ede bilerler")
    return role2.__name__
def role3():
    print(f"{role3.__name__} Yalniz SuperAdmin bunu icra ede biler")
    return role3.__name__
def role4():
    print(f"{role4.__name__} Yalniz SuperAdmin bunu icra ede biler")
    return role4.__name__
def role5():
    print(f"{role5.__name__} SuperAdmin ve Admin bunu icra ede bilerler")
    return role5.__name__

selahiyyetler={
    'SuperAdmin':[role1(),role2(),role3(),role4(),role5()],
    'Admin': [role1(),role2(),role5()],
    'Editor': [role2()]
}
def rollariTap(_role):
    for selahiyyet,vezife in selahiyyetler.items():
        if selahiyyet==_role:
            print(f"{_role} selahiyyetine sahib insanin goreceyi isler asagidakilardir")
            for v in vezife:
                print(v)

rollariTap("SuperAdmin")

def rollariYoxla(_role,_vezife):
    for selahiyyet,vezife in selahiyyetler.items():
        if selahiyyet==_role:
            for v in vezife:
                if v==_vezife:
                    print(f"{_role} selahiyyetine sahib insanin {_vezife} var")
                    break
                else:
                    print("Teyinat tapilmadi...")

rollariYoxla("SuperAdmin","role4")

