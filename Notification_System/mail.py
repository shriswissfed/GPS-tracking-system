# make sure to include temboo libraries ...either using pip or download python SDK temboo librariy from their website
from temboo.Library.Google.Gmailv2.Messages import SendMessage
from temboo.core.session import TembooSession

# Create a session with your Temboo account details
session = TembooSession("aranganathan", "myFirstApp", "b120edd9cf28431f873ecf95bcae03e1")

# get LAT,LAN and Email ID from database  here and store in a variable

# initiatee the Choreo
sendMessageChoreo = SendMessage(session)

# Get an InputSet object for the Choreo
sendMessageInputs = sendMessageChoreo.new_input_set()

# Set the Choreo inputs
sendMessageInputs.set_ClientSecret("I4yAjepSoLwrNr9s9ombaKy7")
sendMessageInputs.set_MessageBody("this email is notify the location") # attach the Lat&Lan here
sendMessageInputs.set_Subject("Notification to Hospital")
sendMessageInputs.set_To("xxpunithxx@gmail.com") # link the email from the database 
sendMessageInputs.set_RefreshToken("1/oW4UPNLf0E2GT0ufbsHX_RRebeeK3PWG3Yh6duouhCU")
sendMessageInputs.set_ClientID("371527408051-2ljsigmjrmk1bqv3c7q7jc9rrnj0uhvc.apps.googleusercontent.com")
sendMessageInputs.set_From("engineerishere@gmail.com")

# Execute the Choreo
sendMessageResults = sendMessageChoreo.execute_with_results(sendMessageInputs)

# Print the Choreo outputs
print("Response: " + sendMessageResults.get_Response())
print("NewAccessToken: " + sendMessageResults.get_NewAccessToken())
