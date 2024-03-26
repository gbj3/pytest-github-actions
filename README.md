# pytest-github-actions
<h1>Design Pattern Usage</h1>
<p>An astract method was used in the construction of the command handler. This is an example of the abstract facotry design pattern. <a href="./app/commands/__init__.py">Link to design pattern usage</a></p><br>

<h1>Environment Variables</h1>
<p>I created a .env file that houses the production environment for the code. This file is also placed in a .gitignore, and therefore private to my local machine and not uploaded to my remote repository. The .env is loaded into the App class and checked to make sure the environment variables are loaded and set. <a href="./app/plugins/__init__.py">Link to environment variable usage</a></p><br>

<h1>Logging</h1>
<p>Logging is used throughout my entire code to document the use of all plugins, error handling, starting/stopping of the program, etc. All data is sent to a app.log file where it can then be reviewed. <a href="./logs/app.log">Link to logging usage</a></p><br>

<h1>Try/Except Exceptions (LBYL/EAFP)</h1>
<p>Try/Except statements are found when using the history csv command. It tries to find the history, but will return an error if unable to return it and again when attempting to do the operation computation. <a href="./app/plugins/csv/__init__.py">Link to try/except exceptions</a></p><br>

<h1><a href="https://youtu.be/Ft4Kw1BXRGI">Link to program demo</a><h1>