from twilio.rest import Client

account_sid = 'AC774dc8ee9d4e2222e67a4a02a8c70064'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+19789193527',
  to='+2540113450333'
)

print(message.sid)