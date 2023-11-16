### ------------------------ built-in libraries ------------------------ ###
import json
import logging
import os
import sys
import argparse
import sqlalchemy
import sqlite3

### ------------------------ external libraries ------------------------ ###
from seleniumwire import webdriver  # Import from seleniumwire

### ---------------------- user-defined libraries ---------------------- ###
from libs.selenium_utils import continue_scroll_while_loading, download_xhr_requests, init_session
from libs.json_utils import extract_data, extract_json 

### ----------------------------- constats ----------------------------- ###

SCRAPING_URL = 'https://unsplash.com/t/wallpapers'
OUTPUT_PATH = 'unsplash_scraping'
OUTPUT_FILE_NAME = 'unsplash_data.json'

### ---------------------------- source code --------------------------- ###

skip_selenium = False


def process_request():
   pass





def main():
    """
        Estrazione da UNSPLASH di dati estrapolati dalle chiamate XHR tramite seleniumwire
    """
       

    if not skip_selenium:
       
        # attivare selenium ed aprire il sito
        driver = webdriver.Chrome()
        init_session(driver, SCRAPING_URL, height=1000, width=1000) 

        # scorrere la pagina fino al completo caricamento delle immagini (tramite scroll in js)
        tot_XHR_requests = 0
        continue_scroll_while_loading(driver)

        # acquisire le risposte dell'XHR
        requests = download_xhr_requests(driver)
        # print(requests)
    #     # TODO: salvare ogni richiesta su un file json
    #     save_requests_to_files(requests)
    # else: 
    #     # TODO
    #     requests = load_from_saved_files()

    # processare ogni richiesta per ottenere il relativo JSON di risposta
    json_responses = extract_json(requests)
    print(json_responses)

    # estrapolare dal JSON i dati di nostro interesse (es. url immagine, autore, ecc.)
    out_data = []
    for json_data in json_responses:
        out_data.append(extract_data(json_data))

    # salvare i dati in un file JSON
    if not os.path.exists(OUTPUT_PATH): 
          os.makedirs(OUTPUT_PATH)
    out_file = os.path.join(OUTPUT_PATH, OUTPUT_FILE_NAME)
    with open(out_file, 'w') as outfile:
        json.dump(out_data, outfile)


 
if __name__ == '__main__':
  
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip", action="store_true", default=False, help="Enable the variable")
    parser.add_argument("--quiet", help="decrease output verbosity", action="store_true")
    args = parser.parse_args()
    if args.quiet:
        logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
    if args.skip: 
        skip_selenium=args.skip

    

    main()
    
else:
    print('The main() function did not execute')
