import logging

import azure.functions as func

FunctionNumber = 1
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    if FunctionNumber:
        return func.HttpResponse(f"Hello, {FunctionNumber}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a FunctionNumber in the query string or in the request body for a personalized response.",
             status_code=200
        )
