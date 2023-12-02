BASE_URL = "https://api.intra.42.fr"
TOKEN_ENDPOINT = "/oauth/token"
DIRNAME = "./All_Data_paris"
ALLUSERDATA = "./All_User_Data_paris"
CREDENTIALS = [
    {"UID": "u-s4t2ud-74766556a4e743fc75b26498d8f22e2c6444da37b87ddf898ea7fe883a3ddfd3", "SECRET": "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"}, # what is important
    {"UID": "u-s4t2ud-3d50e002a1c396441625d741c2bae5de39eef22cfccf6c115b5382858d5caeeb", "SECRET": "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"}, # Statistic Application
    {"UID": "u-s4t2ud-44b2a00e90617c7aad435aa3a6ebf171f84382df407b5c02dab5f08c526bd83c", "SECRET": "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"}, # Statistic Application_v2
    {"UID": "u-s4t2ud-a91adfb793ae958efd01e59ce23f6094a7925bbff542d4a51383fd0e97464686", "SECRET": "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"}, # Statistic Application_v3
    {"UID": "u-s4t2ud-6d42c13d8a26f289f09fdbe7e4934717e30beaacebca4ea039bc12dc7fa8d3e3", "SECRET": "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"} # Statistic Application_v4
]

TOKENS = {
    'token1': None,
    'token2': None,
    'token3': None,
    'token4': None,
    'token5': None
}

def fetch_tokens(t_id, value):
    if t_id == 1:
        TOKENS['token1'] = value
    elif t_id == 2:
        TOKENS['token2'] = value
    elif t_id == 3:
        TOKENS['token3'] = value
    elif t_id == 4:
        TOKENS['token4'] = value
    elif t_id == 5:
        TOKENS['token5'] = value

def get_tokens(t_id):
    return TOKENS['token' + str(t_id)]