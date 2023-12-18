"""
# origin data.json
[
    {
        "prompt": "Write a code to parse a URL and return the domain name.\nhttps://example.com/page", 
        "completion": "def get_domain_name(url):\n    parsed_url = urlparse(url)\n    return parsed_url.netloc"
    },
    {
        "prompt": "Write a function to take three integers as input and return their product.\nx=3, y=5, z=7", 
        "completion": "def product(x,y,z):\n    return x*y*z\n\nx = 3\ny = 5\nz = 7\n\nres = product(x,y,z)\nprint(res)"
    }
]

# convert data_mft.jsonl
{"id":0, "data_name":"codealpaca_20k","chat_rounds":[{"role": "system", "content": "Below is an instruction that describes a task.Write a response that appropriately completes the request.","chat_round_id": 0},{"role": "human","content": "Write a code to parse a URL and return the domain name.\nhttps://example.com/page","chat_round_id": 1},{"role": "bot","content": "def get_domain_name(url):\n    parsed_url = urlparse(url)\n    return parsed_url.netloc","chat_round_id": 1}]}
{"id":1, "data_name":"codealpaca_20k","chat_rounds":[{"role": "system", "content": "Below is an instruction that describes a task.Write a response that appropriately completes the request.","chat_round_id": 0},{"role": "human","content": "Write a function to take three integers as input and return their product.\nx=3, y=5, z=7","chat_round_id": 1},{"role": "bot","content": "def product(x,y,z):\n    return x*y*z\n\nx = 3\ny = 5\nz = 7\n\nres = product(x,y,z)\nprint(res)","chat_round_id": 1}]}
"""

import json

# Function to convert from origin format to mft format
def origin_to_mft(input_file, output_file):

    with open(input_file) as f_in, open(output_file, 'w') as f_out:
        
        data = json.load(f_in)
        
        id = 0
        for i in range(len(data)):
            chat_rounds = []
            chat_rounds.append({"role": "system", "content": "Below is an instruction that describes a task.Write a response that appropriately completes the request.","chat_round_id": 0})
            chat_rounds.append({"role": "human","content": data[i]["instruction"],"chat_round_id": i+1})
            chat_rounds.append({"role": "bot","content": data[i]["output"],"chat_round_id": i+1})
            output = {"id": id, "data_name": "Evol-Instruction-66k", "chat_rounds": chat_rounds}
            json.dump(output, f_out)
            f_out.write('\n')
            id += 1

origin_to_mft("Evol-Instruction-66k.json", "evol_data_mft.jsonl")