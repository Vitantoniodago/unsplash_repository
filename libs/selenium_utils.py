import logging
from time import sleep

### ------------------------ public functions ------------------------ ###



def init_session(driver, url, height = 400, width = 500):
    '''
        Inizializza la sessione di seleniumwire
    '''
    if height > 0 and width > 0:
        logging.info(f'Init session with size: {width}x{height}')
        driver.set_window_size(width, height)
    logging.info(f'Init session with url: {url}')
    driver.get(url)


def continue_scroll_while_loading(drive, scroll_speed=1000, check_delay=1, max_step=5):
    '''
        Continua a scorrere la pagina finchè non si è caricata completamente
    '''
    loading = True
    scroll_to = scroll_speed
    tot_XHR_requests = 0
    while loading:
        max_step -= 1
        if max_step < 0:
            loading = False
        scroll_to += scroll_speed
        _continue_scroll(drive, scroll_to)
        logging.debug(f'Check num requests after scroll')
        tot_XHR_requests_new = _check_num_requests(drive, check_delay)
        if tot_XHR_requests == tot_XHR_requests_new:
            logging.debug(f'No new requests, stop scrolling')
            loading = False
        logging.info(f'New requests found: {tot_XHR_requests_new - tot_XHR_requests}')
        tot_XHR_requests = tot_XHR_requests_new


def download_xhr_requests(drive):
    '''
        Scarica le richieste XHR
    '''
    logging.info(f'Download XHR requests')
    reqs = drive.requests
    logging.debug(f'Found {len(reqs)} requests')
    xhr = [req for req in reqs if '/napi/' in req.url]
    logging.debug(f'Found {len(xhr)} XHR requests')
    return xhr

### ------------------------ internal functions ------------------------ ###

def _continue_scroll(drive, heigth=1000):
    '''
        Scorre la pagina in js
    '''
    logging.debug(f'Continue scroll to: {heigth}')
    drive.execute_script(f'window.scrollTo(0, {heigth});')


def _check_num_requests(drive, delay):
    '''
        Controlla il numero di richieste XHR
    '''
    if delay > 0:
        sleep(delay)
    return len(drive.requests)


### ------------------------ test functions ------------------------ ###

def __test():
    raise NotImplementedError('Test not implemented')


if __name__ == '__main__':
    __test()