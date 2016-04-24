# pi-scripts
Assorted scripts and documentation I find helpful when messing around with raspberry pis.

Adding wifi to Raspian

Edit /etc/wpa_supplicant/wpa_supplicant.conf
Go to the bottom of the file and add the following:

```

network={
    ssid="SSID"
    psk="wifi_password"
}

```

Change keyboard config from UK via raspi-config
