from Chatbot import ChatRoom
from Chatbot import ChatbotParent


#####################
#   Define Parent   #
#####################

# Set the initial bank account
Parent = ChatbotParent()
Parent.set_bank(
    {
        'choppa' : 5000,
        'me'     : 500,
        'guy'    : 5,
    }
)


# Set the permissions
Parent.set_permissions(
    {
        'Admin' : ['choppa'],
    }
)

# - Consider the otion to read from a file - #
#Parent.set_bank(Bank.from_file('config/bank_account.txt'))
#Parent.set_Permision(Permission.from_file('config/permission.txt'))


#########################
#   Define ChatRoom     #
#########################

chat = ChatRoom()
chat.set_Parent(Parent)
chat.set_scriptFolder('scripts')
chat.LocateScripts()


# Run the chatroom
chat.run()
