def init():
    global language
    global languagelist
    global test_number
    global machine_status
    global failure_mode #0 --> No Failure
    					#1 --> Overheating
    					#2 --> Air Leak or Device Activation
    					#3 --> Failure to Exhaust Air
    					#4 --> Exhausting Too Long (>1 s)