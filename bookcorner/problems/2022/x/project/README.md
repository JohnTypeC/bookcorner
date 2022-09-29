# BookCorner

Project demo: https://youtu.be/qHUawPldcGY

## Description:
This project was created for the CS50x: Introduction to Computer Science of the final project. This is a simple web-based application using Flask, Python and SQL.This is an e-commerce website that sell books and users can register, login, view products and add to cart or remove it.

## Website features
* Register:
    * Register new user to be able to access the bookstore full features.
    ![Register page](https://github.com/JohnTypeC/Personal-site/blob/ffa1d3464637ca31231f956c05eb42336ccf90fd/images/web1.jpg)
* Login:
    * Login to existing account.
    ![Login page](https://github.com/JohnTypeC/Personal-site/blob/ffa1d3464637ca31231f956c05eb42336ccf90fd/images/web2.jpg)
* Homepage:
    * The page loads products from database and display them.
    ![Home page](https://github.com/JohnTypeC/Personal-site/blob/ffa1d3464637ca31231f956c05eb42336ccf90fd/images/web3.jpg)
* Description:
    * The description of the items.
    ![Description page](https://github.com/JohnTypeC/Personal-site/blob/ffa1d3464637ca31231f956c05eb42336ccf90fd/images/web4.jpg)
* Add to cart:
    * After login user can add the product to the shopping cart.
    ![Cart page](https://github.com/JohnTypeC/Personal-site/blob/ffa1d3464637ca31231f956c05eb42336ccf90fd/images/web5.jpg)
* Remove:
    * After login, user can remove the product from the shopping cart.
    ![Remove button](https://github.com/JohnTypeC/Personal-site/blob/27b7acf1a54ec045e1515dbfdcf7fce0fefd2fd5/images/web6.jpg)
* Logout:
    * Log out from account.

## Tech used
* Python
* Flask
* SQL
* JavaScript
* Html,css


## How to install
It’s recommended to first create a python virtual environment and then install the requirements with the following command:

```
Pip3 install -r requirements.txt
```

## File
* app.py – main file that contains all related to the authentication process (register, login, logout, cart, remove)
* bookstore.db – database with three tables:
    * users (user account data)
    * books (books title)
    * cart (user shopping data)
* helpers.py – login required function , apology function for checking register/login
* Templates – all of the html file that need for the webpage
* Static – css file and images
* requirements.txt

## About CS50
CS50 is a course from Havard University and taught by David J. Malan.

Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, and software engineering. Languages include C, Python, and SQL plus students’ choice of: HTML, CSS, and JavaScript (for web development).

Thank you for all CS50.

Where I get CS50 course? https://cs50.harvard.edu/x/2022/

## Conclusion
It was very interesting to create this project from scratch using Flask and I also got inspiration from CS50 Pset9 finance project. I used a lot of new resources, which I had never worked with before. I spent a lot of time studying and testing before implementing the code. This project is my very first website and I was very happy with the result.