# abstraction
"""
Abstraction is the process of hiding implementation details and exposing only the essential functionality to the user. 
It is used to hide the implementation details from the user and expose only necessary parts,
making the code simpler and easier to interact with.

reduce complexity by hiding unecessary details
"""
class EmailService:
    def _auth_user(self):
        print("user is authenticated ")
    
    def _check_connection(self):
        print("secure connection estabilished")
    
    def send_email(self):
        self._auth_user()
        self._check_connection()
        print("email is being sent")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from server")
    
em1=EmailService()
em1.send_email()                # only exposed relavent methods and hide internal mech
