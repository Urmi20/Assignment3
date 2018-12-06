import boto3
import base64


class FaceUnlock:
    @staticmethod
    def face_match(key1, key2):
        client = boto3.client('rekognition')

        response = client.compare_faces(SimilarityThreshold=70,
                                        SourceImage={'S3Object': {'Bucket': 'faceunlock', 'Name': key1}},
                                        TargetImage={'S3Object': {'Bucket': 'faceunlock', 'Name': key2}})

        print(response)
        if response['FaceMatches']:
            for faceMatch in response['FaceMatches']:
                confidence = str(faceMatch['Face']['Confidence'])
                print('The face ' +
                      ' matches with ' + confidence + '% confidence')

            return True
        else:
            print("Face not matched")
            return False

    @staticmethod
    def upload_s3(data, user):
        client = boto3.client('s3')
        buf = data.split(',')[1]
        print(buf)
        key = user + '.jpg'
        response = client.put_object(Body=base64.b64decode(buf),
                                     Bucket='faceunlock',
                                     ContentEncoding='base64',
                                     ContentType='image/jpeg',
                                     Key=key)
        print(response)