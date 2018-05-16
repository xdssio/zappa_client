from setuptools import setup

setup(name='zappa_client',
      description='A tool to call Zappa serverless function directly without AWS APIGateway',
      long_description="Zappa is a tool wrap the deployment of serverless applications to AWS Lambda, "
                       "you can invoke your function with AWS APIGatway using curl easily. "
                       "For some use cases you would like to avoid opening your function to APIGateway "
                       "and to call your function directly. "
                       "there are many steps implemented by zappa which makes it difficult, "
                       "this package is a wrapper to save you that pain.",
      version='0.0.1',
      url='https://github.com/xdssio/zappa_client',
      author='J. Alexander',
      author_email='jonathan@xdss.io',
      license='MIT License',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',

      ],
      install_requires=[
          'boto3>=1.7.21'
      ],
      )
