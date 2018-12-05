import boto3
import boto
from boto.s3.key import Key
import base64


class FaceUnlock:
    @staticmethod
    def face_match():
        sourceFile = 'app/static/source.jpg'
        targetFile = 'app/static/target1.jpg'
        client = boto3.client('rekognition')

        imageSource = open(sourceFile, 'rb')
        imageTarget = open(targetFile, 'rb')

        response = client.compare_faces(SimilarityThreshold=70,
                                        SourceImage={'Bytes': imageSource.read()},
                                        TargetImage={'Bytes': imageTarget.read()})

        print(response)
        if response['FaceMatches']:
            for faceMatch in response['FaceMatches']:
                confidence = str(faceMatch['Face']['Confidence'])
                print('The face ' +
                      ' matches with ' + confidence + '% confidence')
        else:
            print("Face not matched")

        imageSource.close()
        imageTarget.close()

    @staticmethod
    def upload_s3(data, user):
        client = boto3.client('s3')
        buf = data.split(',')[1]
        print(buf)
        response = client.put_object(Body=base64.b64decode(buf),
                                     Bucket='faceunlock',
                                     ContentEncoding='base64',
                                     ContentType='image/jpeg',
                                     Key=user)
        print(response)