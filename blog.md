# Cloudify OPC UA applications

Azure has an opcua connector in [preview](https://learn.microsoft.com/en-us/azure/iot-operations/discover-manage-assets/overview-opcua-broker). Unfortunately, it is not recommended for production environments, yet. But here is a simple way to get an OPC UA server in a cloud environment up and running (saving you quite a bit of money as a nice side effect).

We will use render.com for hosting an opcua server. First, create an account on render.com. Then create a new web service. Choose the Docker option and use the following Dockerfile:

```Dockerfile
