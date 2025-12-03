
# pyclient

A simple OpenAI chat client, using the OpenAI server of an [inference snap](https://documentation.ubuntu.com/inference-snaps/).


Connect the interface:
```
sudo snap connect pyclient:inference-snap-status gemma3:status
```

The content becomes available to the snap at `/var/snap/pyclient/current/inference-snap/status/status.json`.
To verify:
```console
$ sudo snap run --shell pyclient
# cat /var/snap/pyclient/current/inference-snap/status/status.json
{
  "engine": "cpu-xsmall",
  "endpoints": {
    "openai": "http://localhost:8328/v1"
  }
}
```

Note: The status is provided only after the server is started.


Finally, run the client:
```console
$ pyclient 
SNAP_DATA found: /var/snap/pyclient/x3
json data: {'engine': 'cpu-xsmall', 'endpoints': {'openai': 'http://localhost:8328/v1'}}
Using OpenAI endpoint: http://localhost:8328/v1
Response received
A unicorn, with a horn that shimmered with rainbow light, drifted off to sleep, dreaming of adventures and the sweetest dreams.
```
