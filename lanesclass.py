class lanesclass:
    '''
    initiates the lanes and the num of vehicles a 5 for every lane
    '''
    def __init__(self, lanes=['N_S', 'E_W', 'S_N', 'W_E'], num_vehicles=5):
        self.lanes=lanes
        self.num_vehicles={'N_S':num_vehicles, 'E_W':num_vehicles, 'S_N':num_vehicles, 'W_E':num_vehicles}
    '''
    takes input the list of updated vehicles
    '''
    def update_num_vehicle(self, updated_numbers=[5,5,5,5]):
        num_vehicles=self.num_vehicles
        for ii, keys in enumerate(num_vehicles.keys()):
            self.num_vehicles[keys]=updated_numbers[ii]
            
    def timer(self, lane):
#     for lane in lanes:
        if lane==0:
            return 0
        elif lane>0 and lane < 15:
            return 10
        elif lane >=15 and lane < 25:
            return 20
        elif lane >=25 and lane < 40:
            return 35
        else:
            return 60