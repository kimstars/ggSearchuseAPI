import os
from serpapi import GoogleSearch
from dotenv import load_dotenv
import json

# API_KEY="9fa9843b01905bc0f6c462f8b1bec45715a47918e271ab86fb8f70ad1b0466a1"

load_dotenv()

question = input("Nhập câu hỏi của bạn : ")


params = {
    "engine": "google",
    "q": question,
    "api_key": os.environ.get("API_KEY"),
}

search = GoogleSearch(params)

results = search.get_dict()

# with open("./text.json", "w") as f:
#     json_object = json.dumps(results, indent = 4)
#     f.write((json_object))

# print((results))
n = len(results["organic_results"])
for i in range(n):
    result = results["organic_results"][i]["snippet"]
    print(result)

