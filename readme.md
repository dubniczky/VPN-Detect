# VPN Detect

VPN Detection in the browser using JavaScript

## Usage

1. Create an account and copy the API key to `detect.js`: https://ipgeolocation.io
2. Open the `index.html` page
3. Turn on your VPN and switch to another location
4. Wait for the detection to show the result
5. Turn off your VPN of choice, then reload the webpage or run `runDetect()` in the console.

## Methodology

VPNs are capable of hiding user information, such as IP address, which is usually an important aspect of approximating location. This method might not work 100% of the time, but from the testing, it's overwhelmingly accurate.

The way VPN usage is detected is by comparing the time-zone values from the bowser's built-in localization against the ISP information of an IP address.

For IP information acquisition, `ipgeolocation.io` services were used for the demo. In the case of such services, the detection must be done server-side to hide the API key.

Finally, the estimated and the time-zone-based locations are compared. If they match, it's likely the user is not using a VPN (or proxy). Otherwise, in case of a significant difference, the use of a VPN is almost guaranteed, unless the user has misconfigured or purposefully modified the timezone settings of their device or browser.
