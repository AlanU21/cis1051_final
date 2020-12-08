from twilio.rest import Client
import Adafruit_DHT as dht  #imports the necessary libraries
import time 

account_sid = "Input your unique Account SID"
auth_token = "Input your unique Auth Token"
client = Client(account_sid, auth_token) #creates the virtual client to send the text from
min_between_reads = 0.1 #adjust for how many minutes you want between readings

while True:
    h, t = dht.read_retry(dht.DHT22, 4) #reads the sensor values
    t = round(t*9 / 5 + 32, 1) #converts Celsius to Fahrenheit and rounds it
    h = round(h, 1)
    final = ("Temp = {}°F Humidity = {}%".format(t, h)) #Puts final message in a string
    print(final)

    message = client.api.account.messages.create(
                    to = "Input the number you want to send the text to",
                    from_ = "Input the number given to you from your Twilio account",
                    body = final) #body of the message
    time.sleep(60*min_between_reads) #holds the loop until the next reading
