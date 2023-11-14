import streamlit as st
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Function to build the CNN model
def build_model(num_layers, activation):
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation=activation, input_shape=(64, 64, 3)))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    for _ in range(num_layers - 1):
        model.add(Conv2D(64, (3, 3), activation=activation))
        model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(units=128, activation=activation))
    model.add(Dense(units=1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Function to train the model
def train_model(model, epochs, train_data, test_data):
    train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
    test_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(train_data, target_size=(64, 64), batch_size=32, class_mode='binary', shuffle=True)
    test_generator = test_datagen.flow_from_directory(test_data, target_size=(64, 64), batch_size=32, class_mode='binary', shuffle=False)
    for epoch in range(epochs):
        st.text(f"Epoch {epoch + 1}/{epochs}")
        model.fit(train_generator, steps_per_epoch=len(train_generator), epochs=1, validation_data=test_generator, validation_steps=len(test_generator), verbose=0)
    st.text("Training completed.")
    return model

# Streamlit GUI
st.title("Dog-Cat Classifier GUI")
trained_model = None
train_data_dir = None
test_data_dir = None

# Input fields
num_epochs = st.slider("Number of Epochs", min_value=1, max_value=10, value=5)
num_layers = st.slider("Number of Layers", min_value=1, max_value=5, value=3)
activation_func = st.selectbox("Activation Function", ('relu', 'sigmoid', 'tanh'))
test_size = st.slider("Test set ratio", min_value=0.1, max_value=0.5, value=0.2, step=0.1)

# Build the model
model = build_model(num_layers, activation_func)

# Upload image for prediction
allow = st.button("Train")

# Display prediction result
if allow is not None:

    train_data_dir = r"train"
    test_data_dir = r"test"

    trained_model = train_model(model, num_epochs, train_data_dir, test_data_dir)
    st.success("Model training completed successfully.")

    test_datagen = ImageDataGenerator(rescale=1./255)
    test_generator = test_datagen.flow_from_directory(test_data_dir, target_size=(64, 64), batch_size=32, class_mode='binary', shuffle=False)
    if st.button("Evaluate Model on Test Data"):
        test_accuracy = trained_model.evaluate(test_generator, verbose=1)
        st.write(f"Test Accuracy: {test_accuracy[1] * 100:.2f}%")

    # Make predictions
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        img = image.load_img(uploaded_file, target_size=(64, 64))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)

        st.image(img, caption="Uploaded Image", use_column_width=True)
        st.write("")
        st.write("Classifying...")

        prediction = trained_model.predict(img_array)
        class_label = "Dog" if prediction[0][0] > 0.5 else "Cat"

        st.write(f"Prediction: {class_label}")
elif trained_model is None:
    st.write("Please train the model before making predictions.")

