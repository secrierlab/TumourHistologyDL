import os
import tensorflow
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Flatten, Dense, Dropout,GlobalAveragePooling2D
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.callbacks import Callback
import tempfile






# Path to the dataset
DATASET_PATH  = '<path/dataset>'
IMAGE_SIZE    = (299, 299)
NUM_CLASSES   = 3
BATCH_SIZE    = 16 # try reducing batch size or freeze more layers if your GPU runs out of memory
NUM_EPOCHS    = 50
WEIGHTS_FINAL = 'model-inception_v3-final.h5'






# Defining the model
net = InceptionV3(include_top=False, weights='imagenet',input_tensor=None,input_shape=(IMAGE_SIZE[0],IMAGE_SIZE[1],3))

x = net.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu', name = 'Dense_1')(x)
x = Dropout(0.5)(x)
x = Dense(512, activation='relu', name = 'Dense_2')(x)
output_layer = Dense(NUM_CLASSES, activation='softmax', name='Predictions')(x)
net_final = Model(inputs=net.input, outputs=output_layer)

#train end to end
for layer in net_final.layers:
    layer.trainable = True


net_final.compile(optimizer=Adam(lr=1e-5),loss='categorical_crossentropy', metrics=['accuracy'])
print(net_final.summary())

#Create a folder to save the weigths
path = "weights"

try:
        os.mkdir(path)
except OSError:
        print ("Creation of the directory %s failed" % path)
else:
        print ("Successfully created the directory %s " % path)


mc = ModelCheckpoint('weights/weights{epoch:08d}.h5', save_weights_only=True, save_freq=4)

              

train_datagen = ImageDataGenerator(preprocessing_function=preprocess_input,rotation_range=40,width_shift_range=0.2,height_shift_range=0.2,shear_range=0.2,zoom_range=0.2,channel_shift_range=10,horizontal_flip=True)

train_batches = train_datagen.flow_from_directory(DATASET_PATH + '/train',target_size=IMAGE_SIZE,class_mode='categorical',shuffle=True,batch_size=BATCH_SIZE,follow_links=True,seed=42)

valid_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)

valid_batches = valid_datagen.flow_from_directory(DATASET_PATH + '/test',target_size=IMAGE_SIZE,class_mode='categorical',shuffle=True,batch_size=BATCH_SIZE,follow_links=True,seed=42)



# show class indices
print('****************')
for cls, idx in train_batches.class_indices.items():
        print('Class #{} = {}'.format(idx, cls))
        print('****************')


# train the model
classify_train=net_final.fit_generator(train_batches,steps_per_epoch = 2000,validation_data = valid_batches,validation_steps = valid_batches.samples // BATCH_SIZE,epochs = NUM_EPOCHS,verbose=1, callbacks=mc)


accuracy = classify_train.history['acc']
val_accuracy = classify_train.history['val_acc']
loss = classify_train.history['loss']
val_loss = classify_train.history['val_loss']
epochs = range(len(accuracy))
plt.plot(epochs, accuracy, 'bo', label='Training accuracy')
plt.plot(epochs, val_accuracy, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.legend()
plt.savefig('training1.png')
plt.figure()
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.savefig('training2.png')

# save trained weights
net_final.save(WEIGHTS_FINAL)


