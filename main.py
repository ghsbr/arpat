import requests
import json


def main():
  resp = requests.get("http://arpat.toscana.it/temi-ambientali/aria/qualita-aria/bollettini/bollettino_json")
  
  with open("data.json", "w") as f:
    f.write(json.dumps(json.loads(resp.text), indent=2))


if __name__ == "__main__":
  main()
