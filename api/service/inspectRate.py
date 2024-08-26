


def getProductRates(data):
    print(f"type of data: {type(data)} and value: {data}")
    if data == "{}":
        print("Data is empty returning empty product rates")
        return None
    return {
        "productRates": {
            "product1": {
                "rate1": 0.01,
                "rate2": 0.02
            },
            "product2": {
                "rate1": 0.03,
                "rate2": 0.04
            }
        }
    }

def parseRates(productRates):
    print(f"Parsing Product Rates, input: {productRates}")
    if productRates is None:
        print("Product Rates is empty")
        return None, True
    return productRates, False


def updateCustomizer(customizerAttributeToCreates):
    pass