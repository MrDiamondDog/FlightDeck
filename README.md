# FlightDeck

Show your overhead flights in a nice and large LED matrix! Perfect addition to any room, especially to those nearby airports.

I've seen a couple projects like this, and thought it would provide some nice experience to make my own, and it fits perfectly for Hack Club's Blueprint YSWS!

I haven't looked at any other similar projects, I want to build my own without copying others.

![cad](img/flightdeck-3.png)
![cad](img/flightdeck-2.png)
![cad](img/flightdeck-1.png)

## Hardware

The hardware falls around $35 total on Aliexpress. See the [BOM](BOM) below.

- 64x32 RGB LED Matrix, 5mm pitch, 320x160mm ([Aliexpress](https://www.aliexpress.us/item/2251832185365664.html?spm=a2g0o.cart.0.0.2e4d38da3nXc6x&mp=1&pdp_npi=6%40dis%21USD%21USD%2012.49%21USD%2012.49%21%21USD%2012.49%21%21%21%402103126e17682735896398074e7fd6%2157993804537%21ct%21US%216602055344%21%211%210%21&gatewayAdapt=glo2usa#nav-specification))
- ESP32-DevKitC V4 Devboard ([Aliexpress](https://www.aliexpress.us/item/3256808703088919.html?spm=a2g0o.detail.0.0.5140gswugswudo&mp=1&pdp_npi=6%40dis%21USD%21USD%208.58%21USD%208.58%21%21USD%208.58%21%21%21%4021030a4b17682769544637132ef6ef%2112000047093672778%21ct%21US%216602055344%21%211%210%21&gatewayAdapt=glo2usa))
- 2x8 Through-hole Female Pin Socket ([Aliexpress](https://www.aliexpress.us/item/3256803911413457.html?spm=a2g0o.detail.0.0.f165asKbasKbNN&mp=1&pdp_npi=6%40dis%21USD%21USD%204.79%21USD%203.85%21%21USD%203.85%21%21%21%402101eede17682773036007831e7bf5%2112000028025434755%21ct%21US%216602055344%21%211%210%21&gatewayAdapt=glo2usa)) (only available in 10pcs packs) 
- 2.1mm Terminal Block Adapter ([Aliexpress](https://www.aliexpress.us/item/3256806569458868.html?spm=a2g0o.productlist.0.0.1448c50c2Ocu5n&mp=1&pdp_npi=6%40dis%21USD%21USD%204.07%21USD%203.91%21%21USD%203.91%21%21%21%402103126e17682742270461949e7fd6%2112000038197813479%21ct%21US%216602055344%21%211%210%21&gatewayAdapt=glo2usa)) (also only in 10 packs)
- 5V 2A Barrel Jack Power Supply ([Aliexpress](https://www.aliexpress.us/item/3256807078618738.html?spm=a2g0o.cart.0.0.2c9538dayiBd5T&mp=1&pdp_npi=6%40dis%21USD%21USD%203.50%21USD%203.41%21%21USD%203.41%21%21%21%402103126e17682743226734291e7fd6%2112000039998101063%21ct%21US%216602055344%21%211%210%21&gatewayAdapt=glo2usa))

## Firmware

Programmed in CircuitPython, using the https://airlabs.co/ free live flight API. You may have to send them an email to get access. 

Make sure to rename the `settings.example.toml` file to `settings.toml` and fill in all the values.

Use [this guide](https://learn.adafruit.com/rgb-led-matrices-matrix-panels-with-circuitpython/) to get everything set up.

## BOM

**Please note: some of these items are only available in packs of 10, I could not find a cheaper alternative.**

| Name |Description | Link | Cost | Quantity | Total Price |
| ---- | --- | --- | --- | --- | --- |
| Factory P5 Indoor 320mmx160mm 16 Scan SMD Full Color Module 64x32 Pixels Dot Matrix Panel Video Screen Board | 64x32 LED Matrix | https://www.aliexpress.us/item/2251832185365664.html?spm=a2g0o.cart.0.0.64d038dauBZnYy&mp=1&pdp_npi=6%40dis%21USD%21USD%2012.49%21USD%2011.69%21%21USD%2011.69%21%21%21%402103128917674129797053573ecebd%2157993804537%21ct%21US%216602055344%21%211%210%21&gatewayAdapt=glo2usa | $11.69 | 1 | $11.69 |
| ESP32-DevKitC V4 core board ESP32 development board All Types with ESP32-WROOM-32 32D 32U 32E WIFI+Bluetooth IoT NodeMCU-32 | ESP32-DevKitC V4 Dev Board | https://www.aliexpress.us/item/3256808703088919.html?spm=a2g0o.cart.0.0.2c9538dayiBd5T&mp=1&pdp_npi=6%40dis%21USD%21USD%208.58%21USD%208.58%21%21USD%208.58%21%21%21%402103126e17682743226734291e7fd6%2112000047093672778%21ct%21US%216602055344%21%211%210%21&gatewayAdapt=glo2usa | $7.78 | 1 | $7.78 |
| 10PCS 2.54mm Double Row Female Long Pin 11mm Breakaway PCB Board Pin Header Socket Connector 2x8 pins | 2x8 Through-hole Female Pin Sockets (10pcs) | https://www.aliexpress.us/item/3256803911413457.html?spm=a2g0o.cart.0.0.2c9538dayiBd5T&mp=1&pdp_npi=6%40dis%21USD%21USD%204.79%21USD%203.85%21%21USD%203.85%21%21%21%402103126e17682743226734291e7fd6%2112000028025434755%21ct%21US%216602055344%21%211%210%21&gatewayAdapt=glo2usa | $3.85 | 1 | $3.85 |
| Male Female DC Connector 5V 12V 5.5 2.1mm DC Power Jack Plug Adapter Barrel Connector for CCTV Security Camera Led Strip | 2.1mm Terminal Block Adapter (10pcs) | https://www.aliexpress.us/item/3256806569458868.html?spm=a2g0o.cart.0.0.2c9538dayiBd5T&mp=1&pdp_npi=6%40dis%21USD%21USD%204.07%21USD%203.91%21%21USD%203.91%21%21%21%402103126e17682743226734291e7fd6%2112000038197813479%21ct%21US%216602055344%21%211%210%21&gatewayAdapt=glo2usa | $3.11 | 1 | $3.11 |
| Power Supply Adapter 220V AC DC 5V Universal Charger 2A US For LED Driver | 5V 2A Power Supply | https://www.aliexpress.us/item/3256807078618738.html?spm=a2g0o.cart.0.0.2c9538dayiBd5T&mp=1&pdp_npi=6%40dis%21USD%21USD%203.50%21USD%203.41%21%21USD%203.41%21%21%21%402103126e17682743226734291e7fd6%2112000039998101063%21ct%21US%216602055344%21%211%210%21&gatewayAdapt=glo2usa | $2.61 | 1 | $2.61 |
| Total |  |  |  |  | $32.24 |