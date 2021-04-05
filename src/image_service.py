import imghdr
from io import BytesIO

import requests
from requests import RequestException
from threading import Thread

valid_extensions = ['rgb', 'gif', 'pbm', 'pgm', 'ppm', 'tiff', 'rast', 'xbm', 'jpeg', 'bmp', 'png', 'webp', 'exr']

class ImageDownloader:

    """
    :param url: URL for the resource
    :return: bytes array for the image
    """
    def get_bytes(self, url: str) -> bytes:
        try:
            resource = requests.get(url, allow_redirects=True)
            content = resource.content
            return content
        except RequestException as e:
            raise RequestException(f'Ooops! an error occurred while processing the image {url}')

    """
    :param url: URL for the resource
    :return: bytes array for the image
    """
    def get_bytes_concurrent(self, url: str) -> bytes:
        try:
            num_dl_threads = 10
            for _ in range(num_dl_threads):
                t = Thread(target=self.get_bytes, args=(url,))
                t.start()

        except RequestException as e:
            raise RequestException(f'Ooops! an error occurred while processing the image {url}')


    def is_image(self, content) -> bool:
        """
        :param content: bytes of the image
        :return: bool indicating if the resource is an image
        """
        with BytesIO(content) as f:
            ext = self.is_jpeg(content)
            if ext == None:
                ext = imghdr.what(f)
            return ext in valid_extensions

    def is_jpeg(self, content) -> str:
        """
        Special case of JPEG. This derived from a bug in the module imghdr.
        :param content: bytes of the image
        :return: String JPEG if is a resource of this type else return None
        """
        ext = None
        jpeg_mark = b'\xff\xd8\xff\xdb\x00C\x00\x08\x06\x06' \
                    b'\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f'
        if len(content) >= 32 and 67 == content[5] and content[:32] == jpeg_mark or b'JFIF' in content[:23] \
                or content[6:10] in (b'JFIF', b'Exif') \
                or content[:2] == b'\xff\xd8':
            ext = 'jpeg'
        return ext