import boto3


def count_words(file_content):
    # Use regular expression to find words
    words = file_content.split()
    return len(words)


def lambda_handler(event, context):
    # Initialize the S3 client
    s3 = boto3.client('s3')
    sns = boto3.client('sns')

    # Specify the S3 bucket and file key
    bucket_name = 'aws-lambda-exercise-bucket'
    file_key = 'noWords.txt'

    try:
        # Get the file from S3
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        file_content = response['Body'].read().decode('utf-8')

        # Count the number of words
        word_count = count_words(file_content)

       # Publish the word count to the SNS topic
        sns_topic_arn = 'arn:aws:sns:us-west-2:815477071241:Word-Count'
        sns.publish(
            TopicArn=sns_topic_arn,
            Subject='Word Count Notification',
            Message=f'The number of words in {file_key} file is: {word_count}'
        )

        return {
            'statusCode': 200,
            'body': 'File retrieved successfully',
            'count': word_count
        }
    except Exception as e:
        print('Error getting file:', str(e))
        return {
            'statusCode': 500,
            'body': 'Error retrieving file',
        }
