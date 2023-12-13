# !/user/bin/env python3
import click 
from retail import session, Product, Customer, Order
from datetime import datetime
@click.command()
def customer_input():
    click.echo('Adding A new customer...')
    first_name = click.prompt('Enter first name', type=str)
    last_name = click.prompt('Enter last name', type=str)
    email = click.prompt('Enter email', type=str)
    contact = click.prompt('Enter phone contact', type =int)
    

    click.echo(f'{first_name}, {last_name}, {email}, {contact}')

    new_customer = Customer(first_name = first_name, last_name=last_name, email=email, contact=contact)
    session.add(new_customer)
    session.commit()

@click.command()
def add_product():
    click.echo('Adding Product...')
    name = click.prompt('Enter product name')
    category = click.prompt('Enter category')
    sub_category = click.prompt('Enter sub-category')
    price = click.prompt('Enter price')
    Expiry_date = click.prompt('Enter expiry date')
    Expiry_date = datetime.strptime(Expiry_date, "%Y-%m-%d")
    click.echo(f'{name}, {category}, {sub_category}, {price}, {Expiry_date}')

    new_product = Product(name=name, category=category, sub_category=sub_category, price=price, Expiry_date=Expiry_date)
    session.add(new_product)
    session.commit()

@click.command()
def add_order():
    click.echo("Adding order...")
    customer_id = click.prompt('Enter customer ID who placed the order')
    order_date = click.prompt('Enter date of order')
    order_date = datetime.strptime(order_date, "%m/%d/%Y")
    total = click.prompt('Enter total amount of orders')
    click.echo(f'{customer_id}, {order_date}, {total}')

    new_order = Order(customer_id=customer_id, order_date=order_date, total=total)
    session.add(new_order)
    session.commit()

click.command()
def order_item():
    click.echo('Adding new item...')
    order_id = click.prompt('Enter ID of order')
    product_id = click.prompt('Enter ID of product')
    quantity = click.promt('Enter quantity of product ordered')
    click.echo(f'{order_id}, {product_id}, {quantity}')

click.command()
def all_customers():
    customers = session.query(Customer).all()
    for customer in customers:
        print(customer.id, customer.first_name, customer.last_name)
    
click.command()
def all_products():
    products = session.query(Product).all()
    for product in products:
        print(product.id, product.name, product.category)

click.command()
def all_orders():
    orders = session.query(Order).all()
    for order in orders:
        print(order.id, order.customer_id, order.order_date,order.total)



if __name__ == '__main__':
    exit = False 
    while exit == False:

        click.secho("*******************RE-TALE*******************", fg='green')
        click.secho("What would you like to do?", fg='red')
        click.secho("................................................")
        click.secho("1. Add a new customer", fg='magenta')
        click.secho("2. Add a new product", fg='magenta')
        click.secho("3. Add a new order for a customer", fg='magenta')
        click.secho("4. List all customers", fg='magenta')
        click.secho("5. List all products", fg='magenta')
        click.secho("6. List all order", fg='magenta')
        click.secho("7. Exit", fg='magenta')
        

        option = click.prompt(">", type=int)
        if option == 1:
            customer_input()
        elif option == 2:
            add_product()  
        elif option == 3:
            add_order()  
        elif option == 4:
            all_customers() 
        elif option == 5:
            all_products()
        elif option == 6:
            all_orders()

        elif option == 7:
            break
        
        else:
            click.prompt("Invalid option")

