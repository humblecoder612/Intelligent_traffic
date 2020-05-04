import time
class traffic:
    
    def __init__(self):
        self.MIN_TIME=10
        self.COUNTDOWN=5
        #north to south lane has green light for the initial condition5
        self.GREEN_LIGHT={'N_S':1, 'E_W':0, 'S_N':0, 'W_E':0} 
#         self.ADMIN=True
    
    '''
    Count down before turning the signal red
    '''
    def cooldown(self, duration=None):
        if duration==None:
            duration=self.COUNTDOWN 
        for i in reversed(range(duration)):
            print(i+1)
            time.sleep(1)
            
    '''
    Turns all signals red
    '''
    def turn_all_red(self, duration=None):
        self.cooldown()
        for keys in self.GREEN_LIGHT.keys():
            self.GREEN_LIGHT[keys]=0 

    '''
    Turns signal green for the input lane
    '''
    def givegreensignal(self, lane, duration=None): #yet to implement time period for this method
        if duration==None:
            duration=self.MIN_TIME    
        self.turn_all_red()
        self.GREEN_LIGHT[lane]=1
        if duration != 0:
            self.cooldown(duration)


