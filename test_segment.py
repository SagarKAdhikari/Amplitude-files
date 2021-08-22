import analytics
import datetime
# analytics.write_key = 'OhUU6DFqJqDH1wlbY9RA1P3NGNOn2kpj'

analytics.write_key = 'HLI6S7sdgeGVFvTOzuZOH0gOWRDurvPy'
# analytics.identify('f4ca124298', {
#     'name': 'Michael Bolton',
#     'email': 'mbolton@example.com',
#     'created_at': datetime.datetime.now(),


# },
# )

# analytics.group('16',  '12', {
#             'name': 'sdf'
#         })


analytics.identify('100', {
    'first_name': "Bishwas",


},
)

# analytics.track('100', 'Logged 6 in', {
#     'title': 'Snow Fall',
#     'subtitle': 'The Avalance at Tunnel Creek',
#     'author': 'John Branch'
# },
# )

# analytics.track('f1ca124298', 'Logged 5 in', {
#     'title': 'Snow Fall',
#     'subtitle': 'The Avalance at Tunnel Creek',
#     'author': 'John Branch'
# },
# integrations={"Amplitude":{
#   "session_id":  1623384566643,

#   }
#   },
#   context={
#   	"device":{"id":"sdfsdfsd"},
#   	"location":{
#   	 "city": "Kathmandu",
#       "country": "Nepal",
#       "latitude":  27.700769,
#       "longitude": 85.300140,
#       "speed": 0
#    }
#    }
# )

def on_error(error, items):
    print("An error occurred:", error)


analytics.debug = True
analytics.on_error = on_error