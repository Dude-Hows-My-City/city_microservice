# Dude, How's My City?, City Data Microservice

<!-- TABLE OF CONTENTS -->
<details>
  <summary><strong>Table of Contents</strong></summary>
  <ul>
    <li><a href="#about-this-project">About This Project</a></li>
    <li><a href="#key-features">Key Features</a></li>
    <li><a href="#tech-stack">Tech Stack</a></li>
    <li><a href="#contributors">Contributors</a></li>
  </ul>
</details>


## About This Project
**[View the Live Site](http://dude-hows-my-city.herokuapp.com/)**
**Dude How's My City?** is a fullstack service-oriented application that provides users with the capability of searching and comparing cities they might be interested in with economic, social, and cultural data.
  
## Key Features

 This microservice was built in Flask to enable modular API consumption and facilitate a service based architecture. It employs human readable, more relevant consumption routes, greater resistance to application failures, and removes stress from our **Ruby on Rails** application back-end.

## Prerequisites

This microservice was developed in Python-3.10.6 (it is recommended to use either this version or a newer version of python within python 3) and the Flask framework.

## Installation

1. Clone this directory to your local repository using the SSH key:
```
$ git clone git@github.com:Dude-Hows-My-City/city_microservice.git
```

2. Install dependencies using [Pip](https://pypi.org/project/pip/):
```
$ pip install -r requirements.txt
```

3. Create your local environments:
From within the `/city_microservice/api/` directory;
```
$ export FLASK_ENV=development
$ export FLASK_APP=microservice.py
```

4. Run the test suite with:
```
$ bundle exec rspec
```

5. Run your development server with:
```
$ flask run
```

6. In your browser, visit ['localhost:5000`](http://localhost:5000/) to see the app in action.
(Note: if localhost is not aliased on your machine, the default host should be http://127.0.0.1)

<p align="right">(<a href="#top">back to top</a>)</p>


## Tech Stack

### Framework
<p>
  <img src="https://img.shields.io/badge/-Flask-yellowgreen.svg?style=for-the-badge&logo=flask&logoColor=white" />
</p>

### Languages
<p>
  <img src="https://img.shields.io/badge/-Python-brightgreen.svg?&style=for-the-badge&logo=python&logoColor=white" />
</p>


### Tools
<p>
  <img src="https://img.shields.io/badge/git-F05032.svg?&style=for-the-badge&logo=git&logoColor=white" />
   <img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/>
  <img alt="Heroku" src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"/> 
</p>

### Processes
<p>
  <img src="https://img.shields.io/badge/OOP-b81818.svg?&style=for-the-badge&logo=OOP&logoColor=white" />
  <img src="https://img.shields.io/badge/TDD-b87818.svg?&style=for-the-badge&logo=TDD&logoColor=white" />
  <img src="https://img.shields.io/badge/MVC-b8b018.svg?&style=for-the-badge&logo=MVC&logoColor=white" />
  <img src="https://img.shields.io/badge/REST-33b818.svg?&style=for-the-badge&logo=REST&logoColor=white" />  
</p>

<p align="right">(<a href="#top">back to top</a>)</p>

## Contributors

[Dude, How's My City? Front-end Repo](https://github.com/Dude-Hows-My-City/dhmc_FE)

- Co-Author: [Brandon Ainsworth](https://github.com/BrandonAinsworth)
- Co-Author: [Kendall McGree](https://github.com/kendallm360)
- Co-Author: [Nick Orlov](https://github.com/orlov-n)

[Dude, How's My City? Back-end Repo](https://github.com/Dude-Hows-My-City/dhmc_be_rails)

- Co-Author: [Zachary Prince](https://github.com/z-prince)
- Co-Author: [Antonio Salmeron](https://github.com/amsalmeron)
- Co-Author: [Zac Hazelwood](https://github.com/ZacHazelwood)
- Co-Author: [Stephen Wilkens](https://github.com/StephenWilkens)

<p>
  <a href="https://github.com/Dude-Hows-My-City">
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
</p>

<p align="right">(<a href="#top">back to top</a>)</p>
