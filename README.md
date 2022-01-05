# DreameVacuum API

I bought my first robot vacuum cleaner, with the intention of integrating into my home automation system. Only to realized it wasn't supported. I found that the python-miio CLI actually worked with it, so I just had to learn some quick python and "boom" a HTTP API was in place.

It features no security at all, so you'll need to run this on your private network only.

It uses a `.env` file where you'll need to provide the following variables:
```
VACUUM_ADDRESS=
VACUUM_TOKEN=
```

You can use (this app)[https://github.com/Maxmudjon/Get_MiHome_devices_token/releases] to obtain both the token and ip adress of your vacuum. That'll also give you an indication as to whether your vacuum is supported by this. All `dreame.vacuum.*` should work, but I've only tested this with my `dreame.vacuum.mc1808`.
