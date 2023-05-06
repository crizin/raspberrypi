import os
import requests
import Adafruit_DHT
from dotenv import load_dotenv

sensor = Adafruit_DHT.AM2302

pin_dht = 4

load_dotenv()
instance = os.environ.get("INSTANCE")
push_gateway = os.environ.get("PUSH_GATEWAY")


def push_metric(metric_name, metric_value, labels):
    label_str = ",".join([f'{k}="{v}"' for k, v in labels.items()])
    metric_data = f"{metric_name}{{{label_str}}} {metric_value}\n"
    return requests.post(push_gateway, data=metric_data.encode("utf-8"), headers={'Content-Type': 'text/plain; charset=utf-8'})


humidity, temperature = Adafruit_DHT.read_retry(sensor, pin_dht)

if humidity is not None and temperature is not None:
    print(f"Temperature: {temperature:.1f}℃, Humidity: {humidity:.1f}%")
    push_metric("temperature", temperature, {"instance": instance})
    push_metric("humidity", humidity, {"instance": instance})
else:
    print("Temperature/Humidity failed")
