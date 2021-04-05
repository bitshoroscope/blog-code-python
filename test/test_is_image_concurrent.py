import pytest
import time

from image_service import ImageDownloader

img_urls = \
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Coat_types_3.jpg/500px-Coat_types_3.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/3/38/Anatomy_dog.png",
         "https://upload.wikimedia.org/wikipedia/commons/8/8c/Poligraf_Poligrafovich.JPG",
         "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Great_Dane_and_Chihuahua_Skeletons.jpg/1280px-Great_Dane_and_Chihuahua_Skeletons.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/4/42/Eye_of_a_dog.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/2/2b/Dog_nose2.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/2/23/Dog_retrieving_stick.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Dog_puppy.jpg/1024px-Dog_puppy.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Figueras_%28RPS_24-07-2020%29_sujeci%C3%B3n_para_perros.png/2560px-Figueras_%28RPS_24-07-2020%29_sujeci%C3%B3n_para_perros.png",
         "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/USMC-06639.jpg/1920px-USMC-06639.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/a/aa/AHey_Fatty.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Cancer_beagle.jpg/1920px-Cancer_beagle.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/b/b6/Ejemplares_h%C3%ADbridos_de_la_raza_pekines_%28pequines%29.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/a/ae/Wilde_huendin_am_stillen.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Puppies_Fighting.jpg/1920px-Puppies_Fighting.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Cave_canem.JPG/1280px-Cave_canem.JPG",
         "https://upload.wikimedia.org/wikipedia/commons/c/cf/Big_and_small_dog.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Lucky_en_Panzerwiese%2C_M%C3%BAnich%2C_Alemania%2C_2014-12-24%2C_DD_02.JPG/1920px-Lucky_en_Panzerwiese%2C_M%C3%BAnich%2C_Alemania%2C_2014-12-24%2C_DD_02.JPG",
         "https://upload.wikimedia.org/wikipedia/commons/c/c0/Perrovaca_UNMSM.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hanging_18.jpg/1920px-Hanging_18.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/2/27/Truemmer_18.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/U.S._Air_Force_military_working_dog_Jackson_sits_on_a_U.S._Army_M2A3_Bradley_Fighting_Vehicle_before_heading_out_on_a_mission_in_Kahn_Bani_Sahd%2C_Iraq%2C_Feb._13%2C_2007.jpg/1920px-thumbnail.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Tursiops_truncatus_01.jpg/1920px-Tursiops_truncatus_01.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/b/b0/Dolphins_gesture_language.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/3/38/Orca_porpoising.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/5/5a/Baby_wolphin_by_pinhole.jpeg",
         "https://upload.wikimedia.org/wikipedia/commons/e/e1/Commdolph01.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/b/b1/DELFIN_DEL_ORINOCO2.JPG",
         "https://upload.wikimedia.org/wikipedia/commons/2/2d/Dolphin-Musandam_2.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Delphinus_capensis.JPG/1920px-Delphinus_capensis.JPG",
         "https://upload.wikimedia.org/wikipedia/commons/2/2b/Frazer%C2%B4s_dolphin_group.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/2/24/Northern_right_whale_dolphin.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Anim1018_-_Flickr_-_NOAA_Photo_Library.jpg/1920px-Anim1018_-_Flickr_-_NOAA_Photo_Library.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/7/7e/Steno_bredanensis_2.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Tursiops_truncatus_01.jpg/1920px-Tursiops_truncatus_01.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/3/38/LF_Pilot_Whale_Goban_Spur.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Peponocephala_electra_Mayotte.jpg/1920px-Peponocephala_electra_Mayotte.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Killerwhales_jumping.jpg/1920px-Killerwhales_jumping.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Pseudorca_crassidens_at_Okichan_Theater_20070201.jpg/1920px-Pseudorca_crassidens_at_Okichan_Theater_20070201.jpg",
         "https://upload.wikimedia.org/wikipedia/commons/b/b8/Kentriodon_BW.jpg"
         ]


@pytest.fixture
def checker():
    return ImageDownloader()


def test_is_image_not_concurrent(checker):
    imgs_bytes = []
    print("beginning image downloads")
    start = time.perf_counter()
    for url in img_urls:
        imgs_bytes.append(checker.get_bytes(url))

    end = time.perf_counter()
    print("downloaded {} images in {} seconds".format(len(img_urls), end - start))

def test_is_image_concurrent(checker):
    imgs_bytes = []
    print("beginning image downloads")
    start = time.perf_counter()
    for url in img_urls:
        imgs_bytes.append(checker.get_bytes_concurrent(url))

    assert img_urls.__len__() == 40

    end = time.perf_counter()
    print("downloaded {} images in {} seconds".format(len(img_urls), end - start))