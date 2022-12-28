from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts

client = Client('https://gquick.com/xmlrpc.php',
                'samuel@gquick.com', 'Bratz@123')

# set to the path to your file
filename = '/home/webadmin/CODE/woocommerce/app/products/non-smart-watches/carenad_multi_972_main_sq_nt_4800x4800.jpg'

name = filename.split('/')[-1]

# prepare metadata
data = {
    'name': name,
    'type': 'image/jpeg',  # mimetype
}

# read the binary file and let the XMLRPC library encode it into base64
with open(filename, 'rb') as img:
    data['bits'] = xmlrpc_client.Binary(img.read())

response = client.call(media.UploadFile(data))

# response == {
# 'id': 6,
# 'file': 'picture.jpg'
# 'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
# 'type': 'image/jpeg',
# }
attachment_id = response['id']
