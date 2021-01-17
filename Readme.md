E-commerce Store

It is a small store, where you can view products to buy and do other things. You can only access this app if you are a registered user with us else you have to register with us and then after login you can access all the resources. I have used custom registration model for this app. The authentication system used in this app is Session Authentication. You can also recover your password, but due to some privacy , I couldn't use smtp.gmail.com as a email_backend. I have build some api's . Some of the useful links are:

#Home page: http://localhost:8000   (Only if you are logged in, else you will be redirected to login page and if you are not a registered user, you can register by clicking on the link 'Create new account'.

#To view all products:  http://localhost:8000/products/

#To view particular product detail:  http://localhost:8000/product_detail/<prod_id>/

#To add any product:  http://localhost:8000/product_add/

#To update particular product:  http://localhost:8000/product_update/<prod_id>/

#To delete particular product:  http://localhost:8000/product_delete/<prod_id>/
