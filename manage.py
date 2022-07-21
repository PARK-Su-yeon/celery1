import os
from create_celery import create_app
#from config import config, Config
from flask import Flask
from flask_restx import Api
from namespaces import People, Character, AI, Video, Member

application = Flask(__name__)


api = Api(
    application,
    version='0.1',
    title="Silicon Project's API Server",
    description="PRP!",
    terms_url="/",
    contact="vivian0304@naver.com",
    license="MIT"
)

application.config.update(
    broker_url='amqp://user:password@localhost/vhost',
    #'amqp://localhost:5672',
    result_backend='mongodb://localhost:27017'
    #'amqp://localhost:5672'
)

#app.config.from_object(config[config_name])
celery = create_app(application)
#os.getenv('FLASK_CONFIG') or 'default',
#config[config_name].init_app(app)

#celery.conf.update(app.config)
    
api.add_namespace(Member.Member, '/member')

api.add_namespace(People.People, '/people')
api.add_namespace(People.PersonAll, '/person-all')
api.add_namespace(People.PersonSingle, '/person-single')

api.add_namespace(Character.Character, '/character')
api.add_namespace(Character.Characters, '/characters')
api.add_namespace(Character.OriginCharacter, '/origin-character')

api.add_namespace(Video.VideoOrigin, '/video-origin')
api.add_namespace(Video.VideoModification, '/video-modification')
api.add_namespace(Video.VideoModifications, '/video-modifications')

api.add_namespace(AI.AI, '/ai')



if __name__ == '__main__':
    application.run(debug = True, host = 'localhost', port = 80)


    