

from models.foto import Foto
from libs.sqlalchemy_utils import sessionLocal


class FotoRepository(object):

    def aggiungi_foto(self, id ,url, descrizione, link, autore):
        if not isinstance(url, str):
            raise Exception('url is not string')
        if not isinstance(link, str):
            raise Exception('link is not string')
        session = sessionLocal()
        foto = Foto(foto_id=id ,foto_url=url, foto_descrizione=descrizione, foto_link=link, foto_autore=autore)
        session.add(foto)
        session.commit()
        session.close() 