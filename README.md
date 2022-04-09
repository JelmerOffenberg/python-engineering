## Exercise 1 - Environment

- Download or clone this git repository
- Set up your environment (preferably using PyCharm & conda)
- Install the dependencies from the setup.py file (use `pip install -e .` in your project folder). You can use a terminal inside PyCharm to do so.
- Try to run the `main.py` file in PyCharm.

### Checkpoint
At the end you should have a PyCharm installation with the project cloned to a folder on your computer. You should have this folder loaded in PyCharm and have a Python environment with the setup.py file installed. You can do these steps from the command line.

## Exercise 1: - Project Structure

- We're going to need a few modules to build our application. The following modules are at least required:
    - data -> this module is responsible for data handling
    - model -> this module is responsible for all model related work
    - api -> this module is responsible for the API handling
- Think of one more module (functionality) that you would like to add to the application
- Create the modules in the project tree. You can use PyCharm for this, or do it by hand. Note: if you create these folders, modules always require an `__init__.py` file in the directory. This is needed so that the Python interpreter can discover the files in the modules.

### Checkpoint
You should now have a project with four modules in your application directory. The directories should all contain an `__init__.py` file.



## Exercise 2: Get the basic API up and running

- Explore the `main.py` file in the main directory. You can see there is a function available that describes the `app.get("/hello")` endpoint. It's one of the endpoints you can interact with. Let's first start the API. For this you need to open your terminal in PyCharm (make sure you're in the right python environment) and run:
  `uvicorn main:app --reload`

  If the command is successful, you should be able to navigate to the webserver `https://127.0.0.1:8000/hello`.

- Try to modify the returned value in `main.py`, save the file and visit the webpage once more. The API will reload on save (this is why we added the `--reload` flag in the previous step).

- What HTTP method is used for the `hello` endpoint?

- Visit `https://127.0.0.1:8000/docs`. This is what we call the "Swagger UI" it contains the OpenAPI specifications for your API. It's a nice page because it allows you to interact with your API. It also lists the inputs that are expected for each endpoint!

- Use the try-out functionality to send a `GET` request to your `/hello` endpoint.

- Check out the console where you are running the API from (you probably have strated the API from PyCharm). Can you see the request in the logs?

### Checkpoint

A this point you should be able to run the API on your machine and interact with it. You're able to see the logs in the terminal and inspect the Swagger documentation.

Now that you have the API up and running, it's time to start adding components to build the components that we want!

## Excercise 3: - Data Loading

The first module that we'll create is the data loader. We'll use the build-in datasets in scikit-learn to make things easier. They offer datasets that are available straight from the package itself, this way we don't have to bother with data prep today.

**In this exercise section we'll do the following things:**

- Create some helper functions to load data
- Write unit tests for these functions
- Run the tests from your command line

#### Creating the data loader function

- We'll be using the following dataset to start with: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris
- Create a function with an appropriate name that <u>returns</u> the `X` and `y` of the `iris` dataset. You need to import some dependencies, check the scikit-learn documentation link for this.

#### Write unit tests for the data loader function

- Remember the directory structure. Tests are **always** located in the tests folder. The tests folder must follow the same structure as your project folder (same directory structure).
- Create a file in the `tests/data` directory and call it `test_{ your file name}.py` Note that name of your test file must match with the file name in your data module. If your file is called `load_data.py` then your test file should be called `test_load_data.py`.
- After you've created the file, you will need to import the function that you want to test. You can do this by importing your own package. For instance `from data.load_data import your_function_name`
- If you're having troubles importing, right click on the `src` directory and go to `mark directory as` -> `mark as sources root`. This will help python to discover your files.
- Think of what you want to test of your function. This is crucial and forces you to think about the behavior of your function. You can use this link as a starting point: https://docs.pytest.org/en/6.2.x/assert.html#assert
- Write a unit test for your data loader function

#### Run the tests from the command line

- Once you've finished writing your test or tests, you can open a new terminal in PyCharm and write `pytest tests`. Make sure you're in the project root directory.
- If your tests are successful, you will see that all tests have passed.
- Write a test that will surely fail and rerun the tests again, see how `pytest` changes the output.

### Checkpoint
If you've made it this far, you're doing really good! You're able to write a function in the appropriate module. You are able to test the function and operate on the command line. You've thought about what this function needs to do and what it shouldn't do.

Running these tests is something that developers typically do before committing code to the code base. Also, some developers take it to the next level by first writing a test, and then writing the code. This paradigm is called **test driven development**. See https://en.wikipedia.org/wiki/Test-driven_development for more information.



## Exercise 4: Model Training

In this section we'll write some code to train a simple scikit-learn model. The result of this section should be the following things:

- A callable function that trains a model on our data (loaded via our data loader).
- A function that stores this model in the `models` directory
- Optionally unit tests for all functions. If you're having troubles with the code, you might want to skip this. If you're feeling comfortable, have a go at this.

#### Training functionality

I'm deliberately reducing how specific the instructions are the further you get. This allows you to more freely solve the problems at hand.

- Add a new Python file `train.py` under the `model` module. This file will contain the bits that are using for model training.

- Write a few functions that are needed to train a scikit-learn model. You know the type of data that we have, so you can pick an appropriate model.

- Remember that you need data to train a model, so you'll need to use your data loader to make the data available in this module.

- You can run your python script from the command line by adding the following code to the bottom of your script.

  ![image-20220409135745230](/Users/jelmer/Library/Application Support/typora-user-images/image-20220409135745230.png)

- Make your `train.py` file executable by adding the name equals main statement.

- If you're going fast, feel free to add some unit tests for your new code. Otherwise, skip ahead to the next part

#### Store model

- I've provided you with two functions in the `models/utils.py` file. These functions are useful for saving and loading models. Use the `save_model` function in your `train` module to make sure that we can store the model on disk. We'll need it for the API!

### Checkpoint

You now have a module `train.py` that loads data, trains a model and saves it to disk. You're able to run the `train.py` script and it outputs a model in the directory that you expect. If this is not the case, revisit the steps until you meet these requirements. Feel free to ask help at any time!



## Exercise 5: Model predict

In this section we're going to use the stored trained model to make some predictions. For this we'll need a few things.

- A stored trained model
- A function that loads this model from disk
- A function that uses a model to produce predictions
- A feature vector or sample of data to make predictions on

In the `utils.py` I've provided you with a function to load a model from disk. So, at this point you should have a stored trained model and a function to load it. That means we have to create the other two bits to complete this exercise.



#### Create a predict function

Predict should be part of the `model` module. Create a new file there for the predict functionality.

- Write the function to make predictions using the stored model. There are multiple ways how you can solve this.
- Write a test that tests your prediction functionality
- Run **PyTest** to validate if everything passes. If you're short on time but you



## Exercise 6: Create prediction endpoint

We now have a trained model and an API that is not doing much at the moment. The next step is to create an endpoint in the API where we can call the predict function of our model object. Since the model is trained, you can load it and call `model.predict()` on it to produce predictions. How convenient!

These are the steps you'll need to work through. Remember to run the API, inspect the documentations and check the endpoint as often as you want! This is a nice way to learn how everything works together.

- Create a new **endpoint** in main.py, let's call `predict`. This will be a POST operation!

You need a feature vector for predict, so this should be something that is passed as data to the endpoint. Since endpoints are defined as functions, the feature vector is just an argument to the function.

To pass the feature vector as an argument, we'll need to define an interface. Luckily for us, `Pydantic` and `FastAPI` make this really easy. An interface is nothing but a description of the input data that you expect for the endpoint. We can define it in a python class.

Use the following walkthrough to set up an interface for our feature vector (iris dataset): https://fastapi.tiangolo.com/tutorial/body/#import-pydantics-basemodel

You can define this interface under the `api` folder in a separate file, or you can put it in the `main.py` until everything works nicely together.

- Once you've defined the interface, you can add it to the endpoint like so: `predict(data: YourInterfaceName)`. The colon notation is called a **type hint**. It basically explains what the data object should look like. Using type hints in your code has all kinds of benefits, but to keep this training a bit simpler, we've been omitting it.

  If you would like to learn more about it, here is a 5 minute summary about type hinting in Python https://towardsdatascience.com/type-hints-in-python-everything-you-need-to-know-in-5-minutes-24e0bad06d0b

The one thing that's left to do is to actually fill the predict endpoint function with the predictions steps. There is just one catch here, loading the model. We don't want to access the disk and load the model every time someone files a request. This is not efficient. So, instead you'll need to load the model in the global namespace. This means that you'll need to call `model = load_model('model_name')` outside of any function in `main.py`. This way it's available in memory, even when the function ends!

- Load the model in the global namespace in `main.py`
- use the model to make a prediction in the prediction endpoint
- Make sure your API runs, open de Swagger UI (https://localhost:8000/docs) and test your predict endpoint



# TODO: 
- Update graphs in presentation
- Add supporting images to docs
- Make answer repository
- Take out answer from this repo
- Add images to exercise on what part we're working
- Test on windows with PyCharm