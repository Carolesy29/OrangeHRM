## Orange HRM Automation Tests

Framework:

- [Selenium](https://www.selenium.dev/documentation/en/) for tools and libraries that enable and support the automation
  of web browsers.
- [Pytest](https://docs.pytest.org/en/stable/) for automatic test collection, simple assertions, support for fixtures,
  debugging.
- [Pytest-Bdd](https://pytest-bdd.readthedocs.io/en/stable/) for test scenarios in Gherkin language.

##1. To be installed

####Python

- [Windows Setup](https://docs.python.org/3/using/windows.html)
- [Linux Setup](https://docs.python.org/3/using/unix.html)

####Git

- [Windows Setup](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [GNU/Linux Setup](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

####Visual Studio Code

- [Windows Setup](https://code.visualstudio.com/docs/setup/windows)
- [GNU/Linux Setup](https://code.visualstudio.com/docs/setup/linux)

##2. Clone sales-automation-tests repository

- Execute:

`git clone $repo`

##3. Install & Configurate dependencies

- Execute the command from the repository root:

`pip install -r requirements.txt`

- Create a configuration file to execute local tests at tests folder named **"pytest.dev.ini"**:

```
[pytest]
env =
    BASE_URL=https://opensource-demo.orangehrmlive.com/web/index.php/
```

##4. Test Execution commnads

- To execute **all tests** pointing to develop environment:

`pytest -c pytest.dev.ini`

- To execute **specific test** pointing to develop environment:

`pytest -c pytest.dev.ini tests/step_definitions/hired/test_01.py`

- To execute **multiples tests** pointing to develop environment:

`pytest -c pytest.dev.ini tests/step_definitions/hired/test_02.py tests/step_definitions/hired/test_03.py`