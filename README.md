# rPi2
Let's try this again.


## Setup

This tutorial has been adapted from the [official one](https://www.twilio.com/docs/quickstart/python/devenvironment#install-dependencies) to support Python 3.6.1 properly.

First, check to see if you are indeed using Python 3.6.1:

```bash
python --version
```

If your version shows up as something other than 3.6.1, visit the [official guide](https://www.twilio.com/docs/quickstart/python/devenvironment#install-dependencies).

If you are using Python 3.6.1, install `virtualenv` using `pip`.

```bash
# If you are denied permission, try 'sudo python' rather than 'python'
pip install virtualenv
```

Once you have intalled virtualenv, navigate to your working directory, create a virtual environment, then activate it.

```bash
cd whatever/directory/this/repo/is/in/rPi2
virtualenv --no-site-packages .
source Scripts/activate
```

N.B. I am assuming you are using some form of bash. If you are using Windows, use git Bash, on OSX, terminal, etc.

If your `virtualenv` has been set up and activated properly, your terminal will list the enclosing folder above - or in front of - your prompt:

```bash
(rPi2)USER:~ user$
```
or
```bash
(rPi2)
USER:~ user$
```

Next, you need to install Flask and Twilio. The requirements.txt file contains all of the information needed to install Flask and Twilio. Simply run

```bash
Scripts/pip install -r requirements.txt
```

Finally, make sure everything is working properly. Ensure your `virtualenv` is running, then run `flasktest.py`.

```bash
source Scripts/activate
python flasktest.py
```

You should get an output similar to
```bash
* Running on http://127.0.0.1:5000/
```

Go to [http://localhost:5000](http://localhost:5000) in your browser. You should see `Hello World!`. If you do, congratulations! You have successfully set up your environment!.

### N.B.: If you get Python 2.X.X when you run `python --version`, try replacing `python` with `python3`, as you may have multiple python versions installed on your computer.
