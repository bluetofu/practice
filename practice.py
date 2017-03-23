import json

obj= """
{
    "name" : ["mario", "marie"],
    "age" : [35 ,25],
    "gender" : ["m", "f"],
    "address" : ["seoul", "cheongnam"]
}
"""

#1. json -> dict
result = json.loads(obj)
print(result)
