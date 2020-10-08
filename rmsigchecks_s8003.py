#!/usr/bin/python

import dfu
import usbexec

DFU_ABORT = 4
HOST2DEVICE = 0x21

SIG_CHECKS_1 = 0x100007924
SIG_CHECKS_2 = 0x10000792C
SIG_CHECKS_3 = 0x100007958
SIG_CHECKS_4 = 0x100007C9C
SIG_CHECKS_5 = 0x180087954

pwnd_device = usbexec.PwnedUSBDevice()
device = dfu.acquire_device()

# Remove sigchecks

pwnd_device.write_memory(SIG_CHECKS_1, "\x1F\x20\x03\xD5")
pwnd_device.write_memory(SIG_CHECKS_2, "\x1F\x20\x03\xD5")
pwnd_device.write_memory(SIG_CHECKS_3, "\x1F\x20\x03\xD5")
pwnd_device.write_memory(SIG_CHECKS_4, "\x1F\x20\x03\xD5")
pwnd_device.write_memory(SIG_CHECKS_5, "\x00\x00\x00\x00")


# Reset USB connection

device.ctrl_transfer(HOST2DEVICE, DFU_ABORT, 0, 0, 0, 0)

dfu.usb_reset(device)
dfu.release_device(device)

# All done

print 'Removed SecureROM Signature Checks.'
