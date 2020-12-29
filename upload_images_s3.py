import boto3
import glob


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--img_folder', help='Folder with the images to upload')
    parser.add_argument('--bucket')
    parser.add_argument('--bucket_folder')
    parser.add_argument('--access_key_id', help='AWS access key id')
    parser.add_argument('--secret_access_key', help='AWS secret access key')
    args = parser.parse_args()
    ACCESS_ID = args.access_key_id
    ACCESS_KEY = args.secret_access_key
    BUCKET_NAME = args.bucket
    BUCKET_FOLDER = args.bucket_folder
    IMG_FOLDER = args.img_folder


    s3 = boto3.client('s3',
        aws_access_key_id=ACCESS_ID,
        aws_secret_access_key= ACCESS_KEY,
        region_name='us-east-1')

    bucket = s3.Bucket(BUCKET_NAME)
    images_uploaded = 0
    for imagepath in glob(f'{IMG_FOLDER}/*.png'):
        try:
            filename = imagepath.split('/')[-1]
            bucket.upload_file(imagepath, f'{BUCKET_FOLDER}/{filename}')
            images_uploaded += 1
        except Exception as e:
            print(f'could not upload file {filename} to s3: {e}')
    print(f'Total files uploaded: {images_uploaded}')
