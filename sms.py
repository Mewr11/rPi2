from twilio.rest import Client
from tokens import *

class SMS:
    '''
    Ensure you have a 'tokens.py' to hold the SID, authentication token, and phone number defaults.
    Correct syntax can be found in 'tokens_ex.py'
    '''
    def __init__(self,
                 account_sid=acc_sid,
                 auth_token=auth_tok,
                 caller=call_num):
        '''
        __init__ will work perfectly fine with no arguments. Only call with arguments if you know what you are doing.
        
        If you are certain that you know what you are doing, account_sid and auth_token are the credentials from your twilio account.
        caller is a phone number associated with said twilio account with SMS enabled.
        '''
        self._account_sid = account_sid
        self._auth_token = auth_token
        self.client = Client(account_sid, auth_token)
        self.caller = caller
    
    def call(self, number, message):
        '''
        number is the number you wish to call, in the format "+1XXXXXXXXXX" for US numbers.
        message is a string that will form the body of the text message.
        '''
        self.client.messages.create(
                to = number,
                from_ = self.caller,
                body = message)

if __name__ == '__main__':
    sms = SMS()
    sms.call("+16088433015", "You've Got Mail!")
