import json

print('Loading function')

def print_context_info(context):
    print("Printing Context Info")
    print(f"Function Name = {context.function_name}")
    print(f"function_version = {context.function_version}")
    print(f"invoked_function_arn = {context.invoked_function_arn}")
    print(f"memory_limit_in_mb = {context.memory_limit_in_mb}")
    print(f"aws_request_id = {context.aws_request_id}")
    print(f"log_group_name = {context.log_group_name}")

def print_event_info(event):
    print("Printing event info")
    for key,value in event.items():
        print(f"{key} = {value} ")



def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print_context_info(context)
    print_event_info(event)
    name = event['name']
    location = event['address']
    price   = float(event['price'])
    print(f"Hi {name} from {location}. Price without tax {price} ")
    after_tax_price = price+ (price * 14/100)
    return after_tax_price
    #raise Exception('Something went wrong')
