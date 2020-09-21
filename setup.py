from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()
	
setup_args = dict(
    name='chatbotpackage',
    version='0.7',
    description='chatbotpackage',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Shinjini Ray',
    author_email='shinjini.ray@gmail.com',
    keywords=['chatbot', 'neuralnetwork'],
    url='https://github.com/shinjiniray/chatbotpackage.git',
    download_url='https://pypi.org/project/chatbotpackage',
)

install_requires = [
	'Flask',
	'Werkzeug',
	'keras==2.4.3',
	'pymongo',
	'nltk',
	'scipy==1.4.1',
	'numpy==1.18.5',
	'configparser',
	'flask_socketio',
	'flask-socketio',
	'tensorflow==2.3.0',
	'dnspython==1.16.0',
	'gunicorn',
	'eventlet==0.26.1',
	'greenlet==0.4.16',
	'gevent-websocket',
	'monotonic==1.5',
	'certifi==2020.6.20',
	'chardet==3.0.4',
	'Click==7.1.2',
	'idna==2.10',
	'itsdangerous==1.1.0',
	'Jinja2==2.11.2',
	'MarkupSafe==1.1.1',
	'PyJWT==1.7.1',
	'pytz==2020.1',
	'requests==2.24.0',
	'six==1.15.0',
	'twilio==6.45.0',
	'urllib3==1.25.10',
	'pyopenssl'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires, include_package_data=True)