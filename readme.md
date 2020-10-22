# bluetooth

experiments in BLE.

## prereqs

Latest Python (3.9)

```
sudo yum install bzip2-devel readline-devel libffi-devel
asdf install python latest
```

see https://asdf-vm.com/#/

## what it do

Goal is to reverse engineer a bluetooth hearing aid app.

Subject is `HA-802` - https://hearingassist.com/products/recharge-bte-bluetooth-hearing-aids

- Generic stuff
  - [ ] understand BLE basics
  - [ ] retrieve human-readable info of everything we can do/say
- Subject-specific stuff
  - [ ] power on/off
  - [ ] volume up/down
  - [ ] equalizer adjustments

## references

- https://www.bluetooth.com/specifications/le-audio/
- https://wiki.archlinux.org/index.php/Bluetooth_headset
- https://people.csail.mit.edu/albert/bluez-intro/c212.html
- https://github.com/labapart/gattlib
- https://devzone.nordicsemi.com/nordic/short-range-guides/b/bluetooth-low-energy/posts/ble-characteristics-a-beginners-tutorial
- https://learn.adafruit.com/reverse-engineering-a-bluetooth-low-energy-light-bulb/overview
- https://learn.adafruit.com/introduction-to-bluetooth-low-energy/introduction
