from flask import Flask, request
import boto3

app = Flask(__name__)

# AWS S3 configuration
AWS_ACCESS_KEY = 'your aws access key'
AWS_SECRET_KEY = 'your aws secret key'
S3_BUCKET = 'ouhkbbeua4276' #any s3 bucket desierd name

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)


@app.route('/upload', methods=['POST'])
def upload_file():
    # Get the uploaded file from the request
    file = request.files['file']

    if file:
        # Check if the bucket exists
        bucket_exists = False
        response = s3.list_buckets()
        for bucket in response['Buckets']:
            if bucket['Name'] == S3_BUCKET:
                bucket_exists = True
                break

        # Create the bucket if it does not exist
        if not bucket_exists:
            s3.create_bucket(Bucket=S3_BUCKET)

        # Upload the file to S3 bucket
        s3.upload_fileobj(file, S3_BUCKET, file.filename)

        return 'File uploaded successfully'

    return 'No file uploaded'


if __name__ == '__main__':
    app.run(debug=True)
