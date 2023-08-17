class Pokemon:
    def __init__(self,entry,name,type,description,is_caught):
        self.entry =entry
        self.name = name
        self.type = type
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print("The pokemon:" + self.name + "makes a sound!")
    

    # Instance method
    def display_details(self):
        print('Name: ' + self.name)

    if len(self.type) == 1:
        print('Type: ' + self.type[0])
    else:
        print('Type: ' + self.type[0] + '/' + self.type[1])
    
    print('Lv. ' + str(self.level))
    print('Region: ' + self.region)
    print('Description: ' + self.description)

    if self.is_caught:
        print(self.name + ' has already been caught!')
    else:
        print(self.name + ' hasn\'t been caught yet.')


