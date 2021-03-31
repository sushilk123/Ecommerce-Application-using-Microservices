# Ecommerce Application using Microservices 

Microservices is an architectural style and pattern that structures an application as a collection of coherent services. Each service is highly maintainable, testable, loosely coupled, independently deployable, and precisely focused.

## Application Structure
The Python Flask based microservices project is composed of the following 4 projects: 
* [frontend](https://github.com/sushilk123/Ecommerce-Application-using-Microservices/tree/master/frontend)
* [user-service](https://github.com/sushilk123/Ecommerce-Application-using-Microservices/tree/master/user-service)
* [product-service](https://github.com/sushilk123/Ecommerce-Application-using-Microservices/tree/master/product-service)
* [order-service](https://github.com/sushilk123/Ecommerce-Application-using-Microservices/tree/master/order-service)

## Features of the application are:

1. A user can log in.
2. A user can register.
3. A user can log out.
4. A user can browse products.
5. A user can add a product to an order.
6. A user can adjust the quantity of an order item.
7. A user can place an order.
8. UserClient.py is used to communicate with user microservice.
9. ProductClient.py is used to communicate with product microservice.
10. OrderClient.py is used to communicate with order microservice.
11. Sessions are used to store user and order data.
12. The application is deployed using a docker compose.
