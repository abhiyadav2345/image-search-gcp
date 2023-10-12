from pyvisionproductsearch import ProductSearch, ProductCategories
import os
from dotenv import load_dotenv
from collections import Counter
from colorama import Fore, Style

# Assuming `product.displayName` is a string variable


load_dotenv()
print(os.getenv("PROJECT_ID"))
print(os.getenv("CREDS"))
ps = ProductSearch(
    os.getenv("PROJECT_ID"),
    os.getenv("CREDS"),
    os.getenv("BUCKET"),
    os.getenv("LOCATION"),
    os.getenv("IMAGE-BUCKET-PREFIX")
)


def getLabel(fileName):
    # The label is just the last word in the filename
    return fileName.split(".")[0].upper()


try:
    productSet = ps.getProductSet(os.getenv("PRODUCT_SET"))
except:
    productSet = ps.createProductSet(os.getenv("PRODUCT_SET"))

labels = []
# try:
#     print("////////////////////////////////////////")
#     print(ps.listProductSets())
#     # productSet.delete()
# except:
#     pass
for file in os.listdir(os.getenv("CLOSET_DIR")):

    label = getLabel(file)
    labels.append(label)

    print(f"Creating product {file}")
    print("---------------------FILE NAME -------------------", label)
    try:
        product_exit = ps.getProduct(label)
        product_exit.delete()
        print("deleted")
    except:
        pass

    product = ps.createProduct(
        label, ProductCategories.APPAREL, label, "Shoes", labels={"type": "shoes", "sku_id": label})
    print("-----------------------Product Created--------------------", product.displayName)

    imgFolder = os.getenv("CLOSET_DIR")

    try:
        product.addReferenceImage(os.path.join(imgFolder, file))
        print("-------------------product added refers-----------------")

    except Exception as e:
        print(e)
        print(f"Couldn't add reference image {imgFolder}/{file}")
        break

    productSet.addProduct(product)
    # print(f"{Fore.BLUE}image url : {product.getReferenceImageUrl(label)} to set{Style.RESET_ALL}")

    print(f"{Fore.GREEN}Added product {product.displayName} to set{Style.RESET_ALL}")

numAdded = len(productSet.listProducts())
print(f"Added {numAdded} products to set")
print(Counter(labels))
