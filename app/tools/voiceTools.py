import boto3
from flask import make_response

class Voice:
    @staticmethod
    def synthesize(text):
        client = boto3.client('polly')
        response = client.start_speech_synthesis_task(
            OutputFormat='mp3',
            OutputS3BucketName='a3fru-voice',
            Text=text,
            TextType='text',
            VoiceId='Matthew',
            LanguageCode='en-US',
        )

        return response.get('SynthesisTask').get('OutputUri')

    @staticmethod
    # Synthesize Blocking Call
    def synthesize_bkc(text):
        client = boto3.client('polly')
        response = client.synthesize_speech(
            OutputFormat='mp3',
            Text=text,
            TextType='ssml',
            VoiceId='Matthew',
            LanguageCode='en-US',
        )

        return response.get('AudioStream')

    @staticmethod
    def create_voice_report(data):
        date_time = 0
        issue = 1
        discipline = 2
        document = 3
        uid = 4
        project = 5
        sentiment = 6
        status = 7

        voice_text = '<speak>'

        for item in data:
            voice_text = voice_text + 'Project: {}<break time="2s"/>\n'.format(item[project])
            break

        for item in data:
            voice_text = voice_text + '<p>ID: {}</p><p> Logged in: {}</p>\n'.format(item[uid], item[date_time])
            voice_text = voice_text + '<p>Document: {}</p>\n'.format(item[document])
            voice_text = voice_text + '<p>Discipline: {}</p>\n'.format(item[discipline])
            voice_text = voice_text + '<p>Status: {}</p>\n'.format(item[status])
            voice_text = voice_text + '<p>Sentiment: {}</p>\n'.format(item[sentiment])
            voice_text = voice_text + '<break time="1s"/>'
            voice_text = voice_text + item[issue]

        voice_text = voice_text + '</speak>'
        report_synth = Voice.synthesize_bkc(voice_text)

        response = make_response(report_synth._raw_stream.data)
        response.headers.set('Content-Disposition', 'attachment', filename='Audio_Report.mp3')
        response.headers.set('Content-Type', 'Content-Type: audio/mpeg')

        return response
