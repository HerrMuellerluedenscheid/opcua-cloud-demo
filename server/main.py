
import asyncio

from asyncua import Server, ua

async def main():
    server = Server()
    await server.init()
    server.set_endpoint('opc.tcp://0.0.0.0:4840/')

    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)

    myobj = await server.nodes.objects.add_object(idx, "MyObject")
    myvar = await myobj.add_variable(idx, "MyVariable", 6.7)
    await myvar.set_writable()
    
    async with server:
        while True:
            await asyncio.sleep(1)
            new_val = await myvar.get_value() + 0.1
            print(f"Set value of {myvar} to {new_val}")
            await myvar.write_value(new_val)

if __name__ == '__main__':
    print('starting server')
    asyncio.run(main())
