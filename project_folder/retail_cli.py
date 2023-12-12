# !/user/bin/env python3
import click 
from retail import session, Product

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
@click.argument('category')
@click.argument('sub_category')
@click.argument('price')
@click.argument('expiry_date')
def add_product(name, category, sub_category, price, expiry_date):
    new_product = Product(name=name, category=category,sub_category=sub_category, price=price, expiry_date=expiry_date)
    session.add(new_product)
    session.commit()
    click.echo(f"Added product: {name}")

@cli.command()
@click.argument('id')
def delete_product(id):
    product = session.query(Product).get(id)
    if product:
        session.delete(product)
        session.commit()
        click.echo(f"Deleted product with id: {id}")
    else:
        click.echo(f"Product with id: {id} not found")

@cli.command()
def list_products():
    products = session.query(Product).all()
    for product in products:
        click.echo(f"{product.id} | {product.name} | {product.category} | {product.sub_category} | {product.price} | {product.Expiry_date}")


if __name__ == '__main__':
    cli()