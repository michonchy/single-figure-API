import json

# import requests
# 整数値を入力させ、
# その値が一桁の自然数かそうでないか判定するプログラムを作成せよ。

class InvalidError(Exception):
    pass
def is_number(x):
    if x.stratwith("-"):
        x = x[1:]
    if not x.isdigit():
        return False
    return True
def number(x):
    if not is_number(x):
        raise InvalidError("整数値を入力してください。")
    return int(x)

def number_check(x):
    if 0 < x <= 9:
        return "single figure"
    else :
        return "not single figure"

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    print(event)
    try:
        n = event.get('queryStringParameters').get('number')
        n = number(n)
    except:
        return{
        "statusCode": 400,
        "headers":{
            "Content-Type": "applicafion/jsom"
        },
        "body":json.dumps({
            "message":"整数値を入力してください。"
        }),
    }
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": number_check(n),
            # "location": ip.text.replace("\n", "")
        }),
    }
