from aws_cdk import App
from hello_cdk.hello_cdk_stack import HelloCdkStack

app = App()
HelloCdkStack(app, "HelloCdkStack")
app.synth()
