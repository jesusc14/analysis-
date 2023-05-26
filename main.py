# from google.transit import gtfs_realtime_pb2
import requests

# import protobuf
import gtfs_realtime_pb2
import datetime
from time import strftime, localtime

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get(
    "https://s3.amazonaws.com/kcm-alerts-realtime-prod/tripupdates.pb"
)
feed.ParseFromString(response.content)
for entity in feed.entity:
    if entity.HasField("trip_update"):
        print(
            # datetime.datetime.fromtimestamp(entity.trip_update.timestamp).strftime("%c")
            # + ", "
            # + str(entity.trip_update.vehicle.id)
        )
        # print(type(entity.trip_update.timestamp))
        print(entity.trip_update.position.latitude)
