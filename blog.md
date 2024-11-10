# Cloudify OPC UA applications

Azure has an opcua connector in [preview](https://learn.microsoft.com/en-us/azure/iot-operations/discover-manage-assets/overview-opcua-broker). Unfortunately, it is not recommended for production environments, yet. But here is a simple way to get an OPC UA server in a cloud environment up and running (saving you quite a bit of money as a nice side effect). 

You need to connect the repository of your opc ua server to render.com. Go to "create a web app" and link your github account, selecting your repository. Render will automatically build and deploy your opc ua server. You can then access it via the URL provided by render.


No knowledge for docker required. Dusing the creation of the web app, render will ask for how to install and start the application. It is straightforward to use the default settings.


We add a .env file defining `PORT=4840`. Render.com will read that to open the required port.

Finally you should see something like this:
```bash
==> No open HTTP ports detected on 0.0.0.0, continuing to scan...
==> Deploying...
==> Running 'python server/main.py'
==> Your service is live 🎉
```

OR
you need to set the `PORT` environment variable to `4840` in the render settings. This is the default port for opc ua servers and required for render to know that it should open that port.

We will use render.com for hosting an opcua server. First, create an account on render.com. Then create a new web service. Choose the Docker option and use the following Dockerfile:

```Dockerfile
