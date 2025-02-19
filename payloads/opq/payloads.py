core_opq = { 
    "jsonrpc": "2.0",
    "method": "item.get",
    "params": {
        "output": ["name","lastvalue"],
        "filter": {
            "host": ["SW CORE - OPQ"]
        }   
    },
    "id":1
}

ac1_opq = { 
    "jsonrpc": "2.0",
    "method": "item.get",
    "params": {
        "output": ["name","lastvalue"],
        "filter": {
            "host": ["SW ACESSO 1 - OPQ"]
        }   
    },
    "id":1
}

ac2_opq = { 
    "jsonrpc": "2.0",
    "method": "item.get",
    "params": {
        "output": ["name","lastvalue"],
        "filter": {
            "host": ["SW ACESSO 2 - OPQ"]
        }   
    },
    "id":1
}

ac3_opq = { 
    "jsonrpc": "2.0",
    "method": "item.get",
    "params": {
        "output": ["name","lastvalue"],
        "filter": {
            "host": ["SW ACESSO 3 - OPQ"]
        }   
    },
    "id":1
}