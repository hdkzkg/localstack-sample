import localstack_client.session as boto3

def main():
    client = boto3.client('s3')
    response = client.list_buckets()
    for bucket in response['Buckets']:
        print(f"{bucket['Name']}")

if __name__ == '__main__':
    main()