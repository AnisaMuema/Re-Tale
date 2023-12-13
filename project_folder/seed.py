from retail import Customer,Product,Order, OrderItem, session
from datetime import datetime

session.query(Customer).delete()
session.query(Product).delete()
session.query(Order).delete()
session.query(OrderItem).delete()

session.commit()

cust_data = [{
  "id": 1,
  "first_name": "Christoforo",
  "last_name": "Grandham",
  "email": "cgrandham0@ted.com",
  "contact": "795-921-3159"
}, {
  "id": 2,
  "first_name": "Augusta",
  "last_name": "Duchart",
  "email": "aduchart1@prlog.org",
  "contact": "800-265-9767"
}, {
  "id": 3,
  "first_name": "Ara",
  "last_name": "Capon",
  "email": "acapon2@intel.com",
  "contact": "543-956-5839"
}, {
  "id": 4,
  "first_name": "Jordan",
  "last_name": "Legh",
  "email": "jlegh3@gov.uk",
  "contact": "886-816-0088"
}, {
  "id": 5,
  "first_name": "Ilaire",
  "last_name": "Betho",
  "email": "ibetho4@buzzfeed.com",
  "contact": "910-814-1078"
}, {
  "id": 6,
  "first_name": "Sutherland",
  "last_name": "Tebald",
  "email": "stebald5@wordpress.org",
  "contact": "352-577-1394"
}, {
  "id": 7,
  "first_name": "James",
  "last_name": "Flecknoe",
  "email": "jflecknoe6@aol.com",
  "contact": "753-571-7509"
}, {
  "id": 8,
  "first_name": "Cynthie",
  "last_name": "Gibb",
  "email": "cgibb7@rambler.ru",
  "contact": "538-864-1918"
}, {
  "id": 9,
  "first_name": "Horst",
  "last_name": "Snawden",
  "email": "hsnawden8@cocolog-nifty.com",
  "contact": "447-486-2215"
}, {
  "id": 10,
  "first_name": "Gerianne",
  "last_name": "Diben",
  "email": "gdiben9@nps.gov",
  "contact": "118-690-5222"
}, {
  "id": 11,
  "first_name": "Hallie",
  "last_name": "Antrobus",
  "email": "hantrobusa@is.gd",
  "contact": "687-756-1686"
}, {
  "id": 12,
  "first_name": "Shelby",
  "last_name": "McClarence",
  "email": "smcclarenceb@yelp.com",
  "contact": "905-448-9983"
}, {
  "id": 13,
  "first_name": "Rica",
  "last_name": "Ramsdell",
  "email": "rramsdellc@netvibes.com",
  "contact": "202-256-5450"
}, {
  "id": 14,
  "first_name": "Stacy",
  "last_name": "Reinger",
  "email": "sreingerd@ameblo.jp",
  "contact": "431-963-0929"
}, {
  "id": 15,
  "first_name": "Gavin",
  "last_name": "Petheridge",
  "email": "gpetheridgee@moonfruit.com",
  "contact": "303-806-8784"
}, {
  "id": 16,
  "first_name": "Mitchel",
  "last_name": "Nasi",
  "email": "mnasif@prweb.com",
  "contact": "138-486-8485"
}, {
  "id": 17,
  "first_name": "Marys",
  "last_name": "Blasl",
  "email": "mblaslg@1688.com",
  "contact": "714-784-4003"
}, {
  "id": 18,
  "first_name": "Onfre",
  "last_name": "Jahns",
  "email": "ojahnsh@chicagotribune.com",
  "contact": "222-945-2475"
}, {
  "id": 19,
  "first_name": "Cheri",
  "last_name": "Woodland",
  "email": "cwoodlandi@webs.com",
  "contact": "643-355-0343"
}, {
  "id": 20,
  "first_name": "Chery",
  "last_name": "Dafter",
  "email": "cdafterj@marriott.com",
  "contact": "868-617-9095"
}, {
  "id": 21,
  "first_name": "Brok",
  "last_name": "Huddy",
  "email": "bhuddyk@reference.com",
  "contact": "673-614-6928"
}, {
  "id": 22,
  "first_name": "Dougie",
  "last_name": "Doram",
  "email": "ddoraml@people.com.cn",
  "contact": "676-307-9648"
}, {
  "id": 23,
  "first_name": "Zack",
  "last_name": "Skipworth",
  "email": "zskipworthm@va.gov",
  "contact": "502-913-4319"
}, {
  "id": 24,
  "first_name": "Ddene",
  "last_name": "Fines",
  "email": "dfinesn@google.co.uk",
  "contact": "231-435-2195"
}, {
  "id": 25,
  "first_name": "Lou",
  "last_name": "Polye",
  "email": "lpolyeo@usnews.com",
  "contact": "981-231-0825"
}, {
  "id": 26,
  "first_name": "Lena",
  "last_name": "Laidlow",
  "email": "llaidlowp@toplist.cz",
  "contact": "835-461-8328"
}, {
  "id": 27,
  "first_name": "Gabrila",
  "last_name": "Staves",
  "email": "gstavesq@alexa.com",
  "contact": "832-143-8242"
}, {
  "id": 28,
  "first_name": "Darbie",
  "last_name": "Bridgland",
  "email": "dbridglandr@hubpages.com",
  "contact": "412-680-4011"
}, {
  "id": 29,
  "first_name": "Theresina",
  "last_name": "Ovenden",
  "email": "tovendens@umn.edu",
  "contact": "632-799-4449"
}, {
  "id": 30,
  "first_name": "Gwyneth",
  "last_name": "Mcettrick",
  "email": "gmcettrickt@posterous.com",
  "contact": "569-776-0623"
}]
 

customers = []

for datum in cust_data:
    cust = Customer(**datum)
    customers.append(cust)

session.add_all(customers)
session.commit()

print("Done seeding data")

product_data = [{
  "id": 1,
  "name": "Quail Eggs",
  "category": "Protein Foods",
  "sub_category": "canned",
  "price": "$63.71",
  "Expiry_date": datetime.strptime("4/5/2023", "%m/%d/%Y").date()
}, {
  "id": 2,
  "name": "Shrimp Puff",
  "category": "Protein Foods",
  "sub_category": "Pastery",
  "price": "$25.86",
  "Expiry_date": datetime.strptime("1/26/2023", "%m/%d/%Y").date()
}, {
  "id": 3,
  "name": "Chicken",
  "category": "Protein Foods",
  "sub_category": "Meat",
  "price": "$41.80",
  "Expiry_date": datetime.strptime("4/28/2023", "%m/%d/%Y").date()
}, {
  "id": 4,
  "name": "Bread - Roll, Whole Wheat",
  "category": "Grains",
  "sub_category": "Gluten",
  "price": "$97.52",
  "Expiry_date": datetime.strptime("2/11/2023", "%m/%d/%Y").date()
}, {
  "id": 5,
  "name": "Truffle - Whole Black Peeled",
  "category": "Fruits",
  "sub_category": "Edible Fungi",
  "price": "$26.91",
  "Expiry_date": datetime.strptime("6/22/2023", "%m/%d/%Y").date()
}, {
  "id": 6,
  "name": "Corn - On The Cob",
  "category": "Grains",
  "sub_category": "Canned",
  "price": "$73.65",
  "Expiry_date": datetime.strptime("1/27/2023", "%m/%d/%Y").date()
}, {
  "id": 7,
  "name": "Lamb - Whole, Fresh",
  "category": "Protein Foods",
  "sub_category": "Meat",
  "price": "$25.66",
  "Expiry_date": datetime.strptime("7/2/2023", "%m/%d/%Y").date()
}, {
  "id": 8,
  "name": "Chocolate - Feathers",
  "category": "Dairy",
  "sub_category": "Sweets",
  "price": "$62.90",
  "Expiry_date": datetime.strptime("11/7/2023", "%m/%d/%Y").date()
}, {
  "id": 9,
  "name": "Wine - Chateau Aqueria Tavel",
  "category": "Drinks",
  "sub_category": "Alchoholic beverages",
  "price": "$9.02",
  "Expiry_date": datetime.strptime("7/1/2023", "%m/%d/%Y").date()
}, {
  "id": 10,
  "name": "Muffin - Mix - Creme Brule 15l",
  "category": "Grains",
  "sub_category": "Pastery",
  "price": "$24.05",
  "Expiry_date": datetime.strptime("8/9/2023", "%m/%d/%Y").date()
}, {
  "id": 11,
  "name": "Cheese - Valancey",
  "category": "Dairy",
  "sub_category": "Appetizers",
  "price": "$73.74",
  "Expiry_date": datetime.strptime("6/3/2023", "%m/%d/%Y").date()
}, {
  "id": 12,
  "name": "Lamb - Pieces, Diced",
  "category": "Protein Foods",
  "sub_category": "Red Meat",
  "price": "$84.19",
  "Expiry_date": datetime.strptime("11/15/2023", "%m/%d/%Y").date()
}, {
  "id": 13,
  "name": "Crab - Meat",
  "category": "Protein Foods",
  "sub_category": "Sea foods",
  "price": "$26.64",
  "Expiry_date": datetime.strptime("12/17/2022", "%m/%d/%Y").date()
}, {
  "id": 14,
  "name": "Miso Paste White",
  "category": "Grains",
  "sub_category": "Paste and sauce",
  "price": "$65.04",
  "Expiry_date": datetime.strptime("8/6/2023", "%m/%d/%Y").date()
}, {
  "id": 15,
  "name": "Cheese - Montery Jack",
  "category": "Dairy",
  "sub_category": "Appetizers",
  "price": "$96.38",
  "Expiry_date": datetime.strptime("7/2/2023", "%m/%d/%Y").date()
}, {
  "id": 16,
  "name": "Juice - Grape, White",
  "category": "Drinks",
  "sub_category": "Non-Alchoholic",
  "price": "$85.12",
  "Expiry_date": datetime.strptime("2/1/2023", "%m/%d/%Y").date()
}, {
  "id": 17,
  "name": "Kellogs Special K Cereal",
  "category": "Grains",
  "sub_category": "Cereals",
  "price": "$22.17",
  "Expiry_date": datetime.strptime("11/18/2023", "%m/%d/%Y").date()
}, {
  "id": 18,
  "name": "Pie Filling - Apple",
  "category": "Grains",
  "sub_category": "Pastery",
  "price": "$66.99",
  "Expiry_date": datetime.strptime("12/4/2023", "%m/%d/%Y").date()
}, {
  "id": 19,
  "name": "Longos - Lasagna Veg",
  "category": "Grains",
  "sub_category": "Pasta",
  "price": "$93.12",
  "Expiry_date": datetime.strptime("6/22/2023", "%m/%d/%Y").date()
}, {
  "id": 20,
  "name": "Cake Circle, Paprus",
  "category": "Grains",
  "sub_category": "Pastery",
  "price": "$72.02",
  "Expiry_date": datetime.strptime("3/24/2023", "%m/%d/%Y").date()
}]

products = []

for datum in product_data:
    prod = Product(**datum)
    products.append(prod)

session.add_all(products)
session.commit()

print("Done seeding data")


order_data = [{
  "id": 1,
  "customer_id": 4,
  "order_date": datetime.strptime("5/19/2023", "%m/%d/%Y").date(),
  "total": 5
}, {
  "id": 2,
  "customer_id": 2,
  "order_date": datetime.strptime("9/23/2023", "%m/%d/%Y").date(),
  "total": 2
}, {
  "id": 3,
  "customer_id": 3,
  "order_date": datetime.strptime("8/2/2023", "%m/%d/%Y").date(),
  "total": 200
}, {
  "id": 4,
  "customer_id": 13,
  "order_date": datetime.strptime("6/22/2023", "%m/%d/%Y").date(),
  "total": 49
}, {
  "id": 5,
  "customer_id": 18,
  "order_date": datetime.strptime("12/19/2022", "%m/%d/%Y").date(),
  "total": 12
}, {
  "id": 6,
  "customer_id": 30,
  "order_date": datetime.strptime("1/20/2023", "%m/%d/%Y").date(),
  "total": 2
}, {
  "id": 7,
  "customer_id": 4,
  "order_date": datetime.strptime("4/23/2023", "%m/%d/%Y").date(),
  "total": 192
}, {
  "id": 8,
  "customer_id": 8,
  "order_date": datetime.strptime("10/17/2023","%m/%d/%Y").date(),
  "total": 15
}, {
  "id": 9,
  "customer_id": 19,
  "order_date": datetime.strptime("6/8/2023", "%m/%d/%Y").date(),
  "total": 10
}]

orders = []

for datum in order_data:
    order = Order(**datum)
    orders.append(order)

session.add_all(orders)
session.commit()

print("Done seeding data")

order_item_data = [{
  "id": 1,
  "order_id": 1,
  "product_id": 1,
  "quantity": 1
}, {
  "id": 2,
  "order_id": 2,
  "product_id": 2,
  "quantity": 2
}, {
  "id": 3,
  "order_id": 3,
  "product_id": 3,
  "quantity": 3
}, {
  "id": 4,
  "order_id": 4,
  "product_id": 4,
  "quantity": 4
}, {
  "id": 5,
  "order_id": 5,
  "product_id": 5,
  "quantity": 5
}, {
  "id": 6,
  "order_id": 6,
  "product_id": 6,
  "quantity": 6
}, {
  "id": 7,
  "order_id": 7,
  "product_id": 7,
  "quantity": 7
}, {
  "id": 8,
  "order_id": 8,
  "product_id": 8,
  "quantity": 8
}, {
  "id": 9,
  "order_id": 9,
  "product_id": 9,
  "quantity": 9
}, {
  "id": 10,
  "order_id": 10,
  "product_id": 10,
  "quantity": 10
}, {
  "id": 11,
  "order_id": 11,
  "product_id": 11,
  "quantity": 11
}, {
  "id": 12,
  "order_id": 12,
  "product_id": 12,
  "quantity": 12
}, {
  "id": 13,
  "order_id": 13,
  "product_id": 13,
  "quantity": 13
}, {
  "id": 14,
  "order_id": 14,
  "product_id": 14,
  "quantity": 14
}, {
  "id": 15,
  "order_id": 15,
  "product_id": 15,
  "quantity": 15
}, {
  "id": 16,
  "order_id": 16,
  "product_id": 16,
  "quantity": 16
}, {
  "id": 17,
  "order_id": 17,
  "product_id": 17,
  "quantity": 17
}, {
  "id": 18,
  "order_id": 18,
  "product_id": 18,
  "quantity": 18
}, {
  "id": 19,
  "order_id": 19,
  "product_id": 19,
  "quantity": 19
}, {
  "id": 20,
  "order_id": 20,
  "product_id": 20,
  "quantity": 20
}]

ordersItems = []

for datum in order_item_data:
    item = OrderItem(**datum)
    ordersItems.append(item)

session.add_all(ordersItems)
session.commit()

print("Done seeding data")