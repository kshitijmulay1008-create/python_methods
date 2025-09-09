class Player:
    def __init__(self,j_no,name,runs,wicket,team_name):
        self.jersey_no=j_no
        self.player_name=name
        self.runs=runs
        self.wickets=wicket
        self.team_name=team_name

    def SetName(self,new_name):
        self.player_name=new_name

    def Set_Jersey_no(self,new_jersey_no):
        self.jersey_no=new_jersey_no
    
    def Set_runs(self,new_runs):
        self.runs=new_runs
    
    def Set_wickets(self,new_wickets):
        self.wickets=new_wickets

    def Set_new_team_name(self,new_team_name):
        self.team_name=new_team_name

    def GetName(self):
        return self.player_name

    def Get_Jersey_no(self):
        return self.jersey_no
    
    def Get_runs(self):
        return self.runs
    
    def Get_wickets(self):
        return self.wickets

    def Get_team_name(self):
       return self.team_name
    
p1=Player(1,"kshitij",98,4,"Mumbai_Indians")

p1.Set_Jersey_no(25)
p1.SetName("Kshitij Mulay")
p1.Set_runs(55)
p1.Set_wickets(7)
p1.Set_new_team_name("Puneri Paltan")

print(p1.player_name)
print(p1.jersey_no)
print(p1.runs)
print(p1.wickets)
print(p1.team_name)

print(p1.Get_Jersey_no())
print(p1.GetName())
print(p1.Get_runs())
print(p1.Get_wickets())
print(p1.Get_team_name())