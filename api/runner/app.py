import json
from api.model.model import *
from api.service.inspectRate import *
from api.config.config import Config
from api.service.missingRates import getTestProductRates

cfg = Config()


def lambda_handler(event, context):
    cfg.load()

    path = event.get('rawPath')
    data = event.get('body')
    productRates = ""
    print("Event: ", event)
    if path == "/health":
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Healthy"})
        }

    if path == "/missingRates":
        if cfg.ENV != "PROD":
            productRates = getTestProductRates()
        else:
            raise Exception("Cannot run test script in PROD environment!")

    if path == "/serviceUnavaliable":
        if cfg.ENV != "PROD":
            cfg.CUSTOMIZER_URL = "https://api-it.cloud.capitalone.com/internal-operations/customer-management/mutate-customer-customizersDNE"
        else:
            raise Exception("Cannot run test script in PROD environment!")

    try:
        print(f"Current Product Rates: {productRates}")
        if not productRates:
            print("productRates is empty")
            productRates = getProductRates(data)
            print(f"Product Rates: {productRates} after getting")


        print("Parsing Product Rates")
        customizerAttributeToCreates, missingRatesFlag = parseRates(productRates)

        print(f"Customizer Attribute To Creates: {customizerAttributeToCreates}")
        print(f"Missing Rates Flag: {missingRatesFlag}")
        if cfg.ENV != "LiveDependencyTest":
            print("Updating Customizer")
            updateCustomizer(customizerAttributeToCreates)

        if missingRatesFlag:
            print("Missing Rates")
            raise RatesException("Product Rates Missing")

        print("Customizer Updated Successfully")
        return {
            "statusCode": 200,
            "body": json.dumps({
                "status": "SUCCESS",
                "description": "Customizer Updated Successfully"
            })
        }

    except RatesException as re:
        print("Rates Exception")
        raise RatesException(re)

    except AuthException as ae:
        print("Auth Exception")
        raise AuthException(ae)

    except AdCustomizerException as ace:
        print("AdCustomizer Exception")
        print(ace)
        raise AdCustomizerException(ace)

    except Exception as e:
        print("Error")
        print(e)
        raise Exception(e)