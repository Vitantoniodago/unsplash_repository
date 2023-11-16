import json
import gzip
from repository.foto_repository import FotoRepository 
### ------------------------ public functions ------------------------ ###


 # processare ogni richiesta per ottenere il relativo JSON di risposta
def extract_json(requests):
    json_responses = []
    for request in requests:
        json_data = _decompress_JSON(request.response.body)
        json_responses.append(json_data)
    return json_responses

def extract_data(json):
    result = []
    for item in json:
        result.append({
           'descrizione' : item.get("alt_description",""),
           'username' : item.get("user",{}).get("name","")
        })   

    for item in json:
           foto_id = item.get("id","")
           foto_url = item.get("urls",{}).get("small_s3", "")
           foto_descrizione = item.get("alt_description","")
           foto_link = item.get("links",{}).get("html","")
           foto_autore = item.get("user",{}).get("name","")
           foto_repository = FotoRepository()
           foto = foto_repository.aggiungi_foto(foto_id,foto_url,foto_descrizione,foto_link,foto_autore)

    return result

### ------------------------ internal functions ------------------------ ###

def _decompress_JSON(compressed_json):
    # Decompress a compressed JSON data to bytes and decode it to string
    data2 = gzip.decompress(compressed_json).decode("utf-8")
    # Convert JSON string into Python dictionary
    decompressed = json.loads(data2)
    return decompressed
 

    # estrapolare dal JSON i dati di nostro interesse (es. url immagine, autore, ecc.)
# def out_data(json_response):    
#     out_data = []
#     for json_data in json_responses:
#         out_data.append(extract_data(json_data))




### ------------------------ test functions ------------------------ ###

def __test():
    raise NotImplementedError('Test not implemented')


if __name__ == '__main__':
    __test()