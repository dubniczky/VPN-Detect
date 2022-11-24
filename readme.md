# VPN Detect

WPN Detection in the browser using JavaScript

## Usage

1. Create an account and copy the API key to `detect.js`: https://ipgeolocation.io
2. Open the `index.html` page
3. Wait for the detection to show the result
4. Turn on or off your VPN of choice, then reload the webpage or run `runDetect()` in the console.

## Methodology

VPNs are capable of hiding user information, such as IP address, which is usuablly an important aspect of approximating their location for various purposes. This method might not work 100% of the time, but from the testing, it's overwhelmingly accurate.

The way VPN usage is detected is by comparing the time-zone values from the bowser's built-in localization against the metadata of an IP address.

For IP metadata acquisition, `ipgeolocation.io` services were used for the demo. In case of such services, doing the detection must be done server-side to hide the API key.
