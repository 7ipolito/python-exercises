def abbleToVote(dateBirth):
    
    if 2025 - dateBirth >= 18:
        return "This person is able to vote"
    else:
        return "This person is not able to vote"

print(abbleToVote(2000)) 
