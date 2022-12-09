import random, json
import keras.datasets.fashion_mnist
import requests
import numpy as np

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# scale the values to 0.0 to 1.0
test_images = test_images / 255.0

# reshape for feeding into the model
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# test 이미지 중에 임의의 위치 하나 선택하기
rando = random.randint(0, len(test_images) - 1)

instances = np.expand_dims(test_images[rando], axis=0).tolist()
data = json.dumps({"signature_name": "serving_default", "instances": instances})
print('Data: {} ... {}'.format(data[:50], data[len(data)-52:]))

#서버에 요청하기
headers = {'Content-Type': "application/json"}
json_response = requests.post('http://localhost:8501/v1/models/test_model:predict', data=data, headers=headers)
prediction = json.loads(json_response.text)['predictions'][0]

print(('The model thought this was a {} (class {}), and it was actually a {} (class {})').format(
        class_names[np.argmax(prediction)],
        np.argmax(prediction),
        class_names[test_labels[rando]],
        test_labels[rando]
    ))
# for i in range(3):``
#     print(('The model thought this was a {} (class {}), and it was actually a {} (class {})').format(
#         class_names[np.argmax(predictions[i])],
#         np.argmax(predictions[i]),
#         class_names[test_labels[i]],
#         test_labels[i]
#     ))
