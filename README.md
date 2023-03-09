# midistar

An Arch (or Manjaro) package for automatically connecting USB MIDI devices to each other. Useful if you have a Raspberry Pi sitting around waiting to become a USB host!

This is an adaptation of [these instructions](https://neuma.studio/rpi-midi-complete.html) for doing all this manually.

## Installation

To install, clone and run `makepkg -is`. Then plug in any MIDI device and `udev` rules should trigger the `midistar` service to connect everything with `aconnect` from the `alsa-utils` package.

For Raspberry Pi, you can install the minimal Manjaro ARM image with the standard Imager app, install git with `sudo pacman -S git`, clone this repo and go.

## Example topology

```
Raspberry Pi <==> Powered USB hub <==> {MIDI keyboards, synths, sequencers}`
```

