from PIL import Image
import sys
import os
import shutil


UCHIMAWARI_STATIONS = [
  ("02_kanda",            "uchi_01_ueno_ikebukuro"),
  ("03_akihabara",        "uchi_01_ueno_ikebukuro"),
  ("04_okachimachi",      "uchi_01_ueno_ikebukuro"),
  ("05_ueno",             "uchi_01_ueno_ikebukuro"),
  ("06_uguisudani",       "uchi_02_ikebukuro_shinjuku"),
  ("07_nippori",          "uchi_02_ikebukuro_shinjuku"),
  ("08_nishinippori",     "uchi_02_ikebukuro_shinjuku"),
  ("09_tabata",           "uchi_02_ikebukuro_shinjuku"),
  ("10_komagome",         "uchi_02_ikebukuro_shinjuku"),
  ("11_sugamo",           "uchi_02_ikebukuro_shinjuku"),
  ("12_otsuka",           "uchi_02_ikebukuro_shinjuku"),
  ("13_ikebukuro",        "uchi_02_ikebukuro_shinjuku"),
  ("14_mejiro",           "uchi_03_shinjuku_shibuya"),
  ("15_takadanobaba",     "uchi_03_shinjuku_shibuya"),
  ("16_shinokubo",        "uchi_03_shinjuku_shibuya"),
  ("17_shinjuku",         "uchi_03_shinjuku_shibuya"),
  ("18_yoyogi",           "uchi_04_shibuya_shinagawa"),
  ("19_harajuku",         "uchi_04_shibuya_shinagawa"),
  ("20_shibuya",          "uchi_04_shibuya_shinagawa"),
  ("21_ebisu",            "uchi_05_shinagawa_tokyo"),
  ("22_meguro",           "uchi_05_shinagawa_tokyo"),
  ("23_gotanda",          "uchi_05_shinagawa_tokyo"),
  ("24_osaki",            "uchi_05_shinagawa_tokyo"),
  ("25_shinagawa",        "uchi_05_shinagawa_tokyo"),
  ("26_takanawa_gateway", "uchi_06_tokyo_ueno"),
  ("27_tamachi",          "uchi_06_tokyo_ueno"),
  ("28_hamamatsucho",     "uchi_06_tokyo_ueno"),
  ("29_shimbashi",        "uchi_06_tokyo_ueno"),
  ("30_yurakucho",        "uchi_06_tokyo_ueno"),
  ("01_tokyo",            "uchi_06_tokyo_ueno"),
]

SOTOMAWARI_STATIONS = [
  ("30_yurakucho",        "soto_01_shinagawa_shibuya"),
  ("29_shimbashi",        "soto_01_shinagawa_shibuya"),
  ("28_hamamatsucho",     "soto_01_shinagawa_shibuya"),
  ("27_tamachi",          "soto_01_shinagawa_shibuya"),
  ("26_takanawa_gateway", "soto_01_shinagawa_shibuya"),
  ("25_shinagawa",        "soto_01_shinagawa_shibuya"),
  ("24_osaki",            "soto_02_shibuya_shinjuku"),
  ("23_gotanda",          "soto_02_shibuya_shinjuku"),
  ("22_meguro",           "soto_02_shibuya_shinjuku"),
  ("21_ebisu",            "soto_02_shibuya_shinjuku"),
  ("20_shibuya",          "soto_02_shibuya_shinjuku"),
  ("19_harajuku",         "soto_03_shinjuku_ikebukuro"),
  ("18_yoyogi",           "soto_03_shinjuku_ikebukuro"),
  ("17_shinjuku",         "soto_03_shinjuku_ikebukuro"),
  ("16_shinokubo",        "soto_04_ikebukuro_ueno"),
  ("15_takadanobaba",     "soto_04_ikebukuro_ueno"),
  ("14_mejiro",           "soto_04_ikebukuro_ueno"),
  ("13_ikebukuro",        "soto_04_ikebukuro_ueno"),
  ("12_otsuka",           "soto_05_ueno_tokyo"),
  ("11_sugamo",           "soto_05_ueno_tokyo"),
  ("10_komagome",         "soto_05_ueno_tokyo"),
  ("09_tabata",           "soto_05_ueno_tokyo"),
  ("08_nishinippori",     "soto_05_ueno_tokyo"),
  ("07_nippori",          "soto_05_ueno_tokyo"),
  ("06_uguisudani",       "soto_05_ueno_tokyo"),
  ("05_ueno",             "soto_05_ueno_tokyo"),
  ("04_okachimachi",      "soto_06_tokyo_shinagawa"),
  ("03_akihabara",        "soto_06_tokyo_shinagawa"),
  ("02_kanda",            "soto_06_tokyo_shinagawa"),
  ("01_tokyo",            "soto_06_tokyo_shinagawa"),
]


def open_image(input_dir, image_file_name):
  image_file_path = os.path.join(input_dir, image_file_name)

  try:
    image = Image.open(image_file_path)
  except FileNotFoundError:
    print(f"Image file {image_file_name} is required.")
    sys.exit(1)

  width, height = image.size
  if width != 128 or height != 32:
    print(f"Images have to be of size 32 x 128. Image size of {image_file_name} was {width} x {height}.")
    sys.exit(1)

  image = image.convert("RGBA")
  return image


def generate_image_per_station(input_dir, output_dir, station_list):
  background = open_image(input_dir, "background.png")
  yamanote_line_text = open_image(input_dir, "yamanote_line.png")
  base_text_en = open_image(input_dir, "base_text_en.png")
  base_text_ja = open_image(input_dir, "base_text_ja.png")

  # Generate "Yamanote line" image here to reuse later
  yamanote_line_image = background.copy()
  yamanote_line_image.alpha_composite(yamanote_line_text)

  image_counter = 0

  for station in station_list:
    bound_text_file_name = station[1]
    station_file_name = station[0]

    # Simply save the "Yamanote line" image using the image counter as the file name
    yamanote_line_image.save(os.path.join(output_dir, f"{image_counter:03}.png"))
    image_counter += 1

    # Generate and save the Japanese "bound for" image
    bound_base_text_ja = open_image(input_dir, f"{bound_text_file_name}_ja.png")
    station_text_ja = open_image(input_dir, f"{station_file_name}_ja.png")
    image_ja = background.copy()
    image_ja.alpha_composite(base_text_ja)
    image_ja.alpha_composite(bound_base_text_ja)
    image_ja.alpha_composite(station_text_ja)
    image_ja.save(os.path.join(output_dir, f"{image_counter:03}.png"))
    image_counter += 1

    # Generate and save the English "bound for" image
    bound_base_text_en = open_image(input_dir, f"{bound_text_file_name}_en.png")
    station_text_en = open_image(input_dir, f"{station_file_name}_en.png")
    image_en = background.copy()
    image_en.alpha_composite(base_text_en)
    image_en.alpha_composite(bound_base_text_en)
    image_en.alpha_composite(station_text_en)
    image_en.save(os.path.join(output_dir, f"{image_counter:03}.png"))
    image_counter += 1


def main():
  input_dir = "./images/materials"
  output_dir_base = "./images/generated"
  output_dir_uchimawari = f"{output_dir_base}/uchimawari"
  output_dir_sotomawari = f"{output_dir_base}/sotomawari"

  # Remove all files in the "generated" directory
  if os.path.exists(output_dir_base):
    shutil.rmtree(output_dir_base)
  # Recreate the "generated" directory
  os.makedirs(output_dir_uchimawari, exist_ok=True)
  os.makedirs(output_dir_sotomawari, exist_ok=True)

  generate_image_per_station(input_dir, output_dir_uchimawari, UCHIMAWARI_STATIONS)
  generate_image_per_station(input_dir, output_dir_sotomawari, SOTOMAWARI_STATIONS)

  print("Done")


if __name__ == "__main__":
  main()