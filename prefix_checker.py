# This script is provided by WhatNetwork.ph
# Visit us at: https://whatnetwork.ph/

# Prefix data for different networks
prefix_data = {
    # Smart Communications
    "0813": "Smart", "0900": "Smart", "0908": "Smart", "0911": "Smart", "0913": "Smart", "0914": "Smart",
    "0919": "Smart", "0920": "Smart", "0921": "Smart", "0922": "Smart", "0923": "Smart", "0924": "Smart",
    "0925": "Smart", "0928": "Smart", "0929": "Smart", "0931": "Smart", "0932": "Smart", "0933": "Smart",
    "0934": "Smart", "0939": "Smart", "0940": "Smart", "0941": "Smart", "0942": "Smart", "0943": "Smart",
    "0944": "Smart", "0946": "Smart", "0947": "Smart", "0949": "Smart", "0951": "Smart", "0952": "Smart",
    "0961": "Smart", "0962": "Smart", "0963": "Smart", "0964": "Smart", "0968": "Smart", "0969": "Smart",
    "0970": "Smart", "0971": "Smart", "0972": "Smart", "0973": "Smart", "0974": "Smart", "0980": "Smart",
    "0981": "Smart", "0982": "Smart", "0985": "Smart", "0990": "Smart", "0998": "Smart", "0999": "Smart",

    # Globe Telecom
    "0817": "Globe", "0904": "Globe", "0905": "Globe", "0906": "Globe", "0915": "Globe", "0916": "Globe",
    "0917": "Globe", "0926": "Globe", "0927": "Globe", "0935": "Globe", "0936": "Globe", "0937": "Globe",
    "0945": "Globe", "0954": "Globe", "0955": "Globe", "0956": "Globe", "0957": "Globe", "0958": "Globe",
    "0959": "Globe", "0965": "Globe", "0966": "Globe", "0967": "Globe", "0975": "Globe", "0976": "Globe",
    "0977": "Globe", "0978": "Globe", "0979": "Globe", "0995": "Globe", "0996": "Globe", "0997": "Globe",
    "09253": "Globe", "09255": "Globe", "09256": "Globe", "09257": "Globe", "09258": "Globe",

    # Sun Cellular
    "0952": "Sun Cellular", "0962": "Sun Cellular", "0972": "Sun Cellular",

    # Talk 'N Text
    "0907": "Talk 'N Text", "0909": "Talk 'N Text", "0910": "Talk 'N Text", "0912": "Talk 'N Text",
    "0918": "Talk 'N Text", "0930": "Talk 'N Text", "0938": "Talk 'N Text", "0946": "Talk 'N Text",
    "0948": "Talk 'N Text", "0950": "Talk 'N Text", "0963": "Talk 'N Text", "0982": "Talk 'N Text",
    "0985": "Talk 'N Text", "0989": "Talk 'N Text", "0998": "Talk 'N Text",

    # Touch Mobile
    "0905": "Touch Mobile", "0906": "Touch Mobile", "0915": "Touch Mobile", "0916": "Touch Mobile",
    "0917": "Touch Mobile", "0926": "Touch Mobile", "0927": "Touch Mobile", "0935": "Touch Mobile",
    "0936": "Touch Mobile", "0937": "Touch Mobile", "0945": "Touch Mobile", "0953": "Touch Mobile",
    "0955": "Touch Mobile", "0956": "Touch Mobile", "0957": "Touch Mobile", "0958": "Touch Mobile",
    "0959": "Touch Mobile", "0965": "Touch Mobile", "0966": "Touch Mobile", "0967": "Touch Mobile",
    "0975": "Touch Mobile", "0977": "Touch Mobile", "0978": "Touch Mobile", "0979": "Touch Mobile",
    "0995": "Touch Mobile", "0996": "Touch Mobile", "0997": "Touch Mobile",

    # GOMO
    "0976": "GOMO",

    # Dito Telecommunity
    "0895": "Dito Telecommunity", "0896": "Dito Telecommunity", "0897": "Dito Telecommunity", 
    "0898": "Dito Telecommunity", "0991": "Dito Telecommunity", "0992": "Dito Telecommunity", 
    "0993": "Dito Telecommunity", "0994": "Dito Telecommunity"
}

# Function to check network by prefix
def check_prefix(number):
    for length in range(5, 3, -1):  # Check 5-digit and 4-digit prefixes
        prefix = number[:length]
        if prefix in prefix_data:
            return f"Network: {prefix_data[prefix]}"
    return "Network not found for this prefix."

# Example usage
if __name__ == "__main__":
    number = input("Enter a mobile number to check its network: ")
    print(check_prefix(number))
