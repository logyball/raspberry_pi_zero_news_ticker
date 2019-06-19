# Basic Raspberry Pi Zero W News/Weather Ticker

This project is intented to get a programmer up and running on a first project for the [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/).  For more of a background on the platform, check out the official [Raspberry Pi](https://www.raspberrypi.org/) website.  For now, a few things you'll need to get started as well as a basic setup guide to implement your very own News Ticker.

### Required Hardware:

All prices are accurate as of 06/19/2019.

1. [Raspberry Pi Zero W](https://www.adafruit.com/product/3400) __$10__
2. [Power Supply](https://www.adafruit.com/product/1995) __$7.50__
3. [2x20 GPIO Header Pins](https://www.adafruit.com/product/2822) __$0.95__
4. [MicroSD card](https://smile.amazon.com/Sandisk-Ultra-Micro-UHS-I-Adapter/dp/B073K14CVB) __$5.79__
5. [Pimoroni ScrollPhatHD](https://www.adafruit.com/product/3473) __$12.95__
6. [Soldering Iron](https://smile.amazon.com/GLE2016-Soldering-Adjustable-Temperature-Different/dp/B01N413T8U/) __$11.99__

__Total Cost: $49.18__ ($37.19 if you already have a soldering iron)

### Other requirements:

Sign up for a free tier API key through [OpenWeatherMap](https://openweathermap.org/api) and write down the key.  You'll need it later.

## Setting up your Pi - Hardware

Begin by soldering your GPIO Header to your Raspberry Pi.  You can find a comprehensive video guide on how to do this [here](https://www.youtube.com/watch?v=jYKzsLmMV6o).  In addition, solder your female GPIO connectors included with the ScrollPhat HD to the actual LED board, follwing the instructions provided [here](https://learn.pimoroni.com/tutorial/sandyj/soldering-phats).

## Setting up your Pi - Software

Begin by loading up your Raspberry Pi with the latest version of Raspbian Lite, using a usb cable to set up the Pi (over ssh) to connect to your local Wifi, then connecting to your Pi via ssh while the Pi itself is disconnected from your computer but connected to Wifi.

A few guides to do this are linked below:

  - [Windows](https://desertbot.io/blog/headless-pi-zero-w-wifi-setup-windows)
  - [MacOS](https://desertbot.io/blog/setup-pi-zero-w-headless-wifi)

Note: when your Pi is connected to Wifi (but not your computer), you may have to find it via IP address rather than semantic naming such as `raspberrypi.local`.  In order to find the ip address, after you've set up Wifi on your pi but while still connected to your base machine via usb, run `sudo ifconfig wlan0 | grep inet | awk '{ print $2 }'` on your Pi to output the Pi's IP address.  [Further Reading](https://learn.pimoroni.com/tutorial/raspberry-pi/finding-your-raspberry-pi).

## Loading the ticker/weather

Begin by using ssh to connect to your Pi.  You must enable 

1. `sudo raspi-config`
2. `5. Interfacing Options`
3. `P5 I2C`
4. `Would you like the ARM I2C interface to be enabled?` -> Yes

If `git` is not installed, install via `apt`:

    sudo apt-get update
    sudo apt-get install git

Clone this repository:

    sudo git clone https://github.com/loganballard/raspberry_pi_zero_news_ticker

`cd` into the project root directory.  From there, create the real `vars` file:

    sudo cp .vars.json.example .vars.json

use your favorite text editor (nano is supplied by default, vim is not) to edit the newly created .vars.json file. Enter your API key, zipcode, and state (USA) into the provided slots.  

Run the init script to see it in action!

    sudo ./init.sh

## Running in the background

In order for the ticker to run without requiring an active ssh connection, you can set up a background job to run upon bootup.  In order to do this, edit the `/etc/rc.local` file to contain a line that initilizes the ticker and runs it in the background.  The actual command may vary, but it will be of the form:

    cd {path/to/project_root} && sudo ./init.sh &

The `&` indicates that the previous command should be forked and run as a separate process.  For more information on rc.local, [see the documentation](https://www.raspberrypi.org/documentation/linux/usage/rc-local.md) from the official Raspbery Pi organization.