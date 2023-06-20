from woocommerce import API

# Authenticate with your WooCommerce store
wcapi = API(
    url="https://gquick.com",
    consumer_key="ck_8af3f64bd4a9c1ce4691d5d0df5148962f9fa280",
    consumer_secret="cs_fc6e9af15b7b09e7abb0d698c8d4e41f66d9ee65",
    version="wc/v3"
)

# Set the URL of the media file you want to get
media_url = "https://gquick.com/wp-content/uploads/2023/03/latin-en-mw5100j-solo-mwo-with-food-warming-40l-ms14k6000as-aa-531012866.png"

# Prepare the request parameters
params = {
    "search": media_url
}

# Send the GET request to get the media file
response = wcapi.get("media", params=params)

# Check the response status code
if response.status_code == 200:
    media_data = response.json()
    if media_data:
        media_id = media_data[0]["id"]
        print(f"Media file ID is {media_id}.")
    else:
        print("No media file found with the specified URL.")
else:
    print(f"Error {response.status_code}: {response.text}")
