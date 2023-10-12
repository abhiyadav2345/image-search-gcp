from pyvisionproductsearch import ProductSearch, ProductCategories
from google.cloud import vision
from google.cloud.vision import types
import os
from dotenv import load_dotenv
import ipyplot
load_dotenv()

GCP_PROJECTID=""
BUCKET=""
LOCATION=""
CREDS=""
PRODUCT_SET=""
PRODUCT_SET_DISPLAY_NAME=""
IMAGE_BUCKET_PREFIX="product-images"

ps = ProductSearch(
    os.getenv("PROJECT_ID"),
    os.getenv("CREDS"),
    os.getenv("BUCKET"),
    os.getenv("LOCATION"),
    os.getenv("IMAGE-BUCKET-PREFIX")
)
productSet = ps.getProductSet(os.getenv("PRODUCT_SET"))

# TEST USING FILE URL
# TEST 1
test_image=[]
# test_image.append("https://i.pinimg.com/736x/f0/55/ef/f055ef33ca1540bc2d066b33190509b9.jpg")
# TEST 2
# test_image.append("https://i.pinimg.com/originals/cb/4a/8b/cb4a8bb6bc5a2da1f360c608dfc55301.jpg")
# TEST 3 
# test_image.append("https://th.bing.com/th/id/OIP.lgIHvd28XwlHm6ksrK-XZAHaFH?pid=ImgDet&rs=1")
# TEST 4
# test_image.append("https://th.bing.com/th/id/OIP.BCPvGp08AR45peT1QwvijQHaE7?pid=ImgDet&w=187&h=124&c=7")

test_image.append("https://64.media.tumblr.com/dd1b7283508dfc670029058820368a75/tumblr_ovtuzqa56U1w897cno1_1280.jpg")
# test_image.append("https://i.pinimg.com/736x/14/01/72/14017299d73a35fc425390f7f05a5dde.jpg")
products=productSet.search(ProductCategories.APPAREL, image_uri=test_image[0])



images=[]
labels=[]
for product in products:
   pd=product['product']
   imgName =product['image'].split('/')[-1]
   name = product['image'].split('/')[-3]
   # The storage api makes these images publicly accessible through url
   imageUrl = f"https://storage.googleapis.com/{BUCKET}/{IMAGE_BUCKET_PREFIX}/" + imgName
   images.append(imageUrl)
   labels.append(name)

ipyplot.plot_images(test_image,["TEST IMAGE"], max_images=5, img_width=150)
ipyplot.plot_images(images,labels, max_images=5, img_width=150)