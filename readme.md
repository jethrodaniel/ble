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
- https://reelyactive.github.io/ble-identifier-reference.html
- https://stackoverflow.com/a/33123390/7132678

- [part 1](https://www.youtube.com/watch?v=D3xtOc-vj1I)
- [part 2](https://www.youtube.com/watch?v=LeUDIgZj2t4&t=29s)
- [part 3](https://www.youtube.com/watch?v=dAmZudlm60E)
- [part 4](https://www.youtube.com/watch?v=C-veGabV3A0)
- [part 5](https://www.youtube.com/watch?v=dAmZudlm60E)
