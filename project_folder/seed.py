from retail import Customer,Product, Orders, order_items, session

session.query(Customer).delete()

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

# print("Done seeding data")

product_data = [{
  "id": 1,
  "name": "Quail Eggs",
  "category": "Protein Foods",
  "sub-category": "canned",
  "price": "$63.71",
  "expiry_date": "4/5/2023"
}, {
  "id": 2,
  "name": "Shrimp Puff",
  "category": "Protein Foods",
  "sub-category": "Pastery",
  "price": "$25.86",
  "expiry_date": "1/26/2023"
}, {
  "id": 3,
  "name": "Chicken",
  "category": "Protein Foods",
  "sub-category": "Meat",
  "price": "$41.80",
  "expiry_date": "4/28/2023"
}, {
  "id": 4,
  "name": "Bread - Roll, Whole Wheat",
  "category": "Grains",
  "sub-category": "Gluten",
  "price": "$97.52",
  "expiry_date": "2/11/2023"
}, {
  "id": 5,
  "name": "Truffle - Whole Black Peeled",
  "category": "Fruits",
  "sub-category": "Edible Fungi",
  "price": "$26.91",
  "expiry_date": "6/22/2023"
}, {
  "id": 6,
  "name": "Corn - On The Cob",
  "category": "Grains",
  "sub-category": "Canned",
  "price": "$73.65",
  "expiry_date": "1/27/2023"
}, {
  "id": 7,
  "name": "Lamb - Whole, Fresh",
  "category": "Protein Foods",
  "sub-category": "Meat",
  "price": "$25.66",
  "expiry_date": "7/2/2023"
}, {
  "id": 8,
  "name": "Chocolate - Feathers",
  "category": "Dairy",
  "sub-category": "Sweets",
  "price": "$62.90",
  "expiry_date": "11/7/2023"
}, {
  "id": 9,
  "name": "Wine - Chateau Aqueria Tavel",
  "category": "Drinks",
  "sub-category": "Alchoholic beverages",
  "price": "$9.02",
  "expiry_date": "7/1/2023"
}, {
  "id": 10,
  "name": "Muffin - Mix - Creme Brule 15l",
  "category": "Grains",
  "sub-category": "Pastery",
  "price": "$24.05",
  "expiry_date": "8/9/2023"
}, {
  "id": 11,
  "name": "Cheese - Valancey",
  "category": "Dairy",
  "sub-category": "Appetizers",
  "price": "$73.74",
  "expiry_date": "6/3/2023"
}, {
  "id": 12,
  "name": "Lamb - Pieces, Diced",
  "category": "Protein Foods",
  "sub-category": "Red Meat",
  "price": "$84.19",
  "expiry_date": "11/15/2023"
}, {
  "id": 13,
  "name": "Crab - Meat",
  "category": "Protein Foods",
  "sub-category": "Sea foods",
  "price": "$26.64",
  "expiry_date": "12/17/2022"
}, {
  "id": 14,
  "name": "Miso Paste White",
  "category": "Grains",
  "sub-category": "Paste and sauce",
  "price": "$65.04",
  "expiry_date": "8/6/2023"
}, {
  "id": 15,
  "name": "Cheese - Montery Jack",
  "category": "Dairy",
  "sub-category": "Appetizers",
  "price": "$96.38",
  "expiry_date": "7/2/2023"
}, {
  "id": 16,
  "name": "Juice - Grape, White",
  "category": "Drinks",
  "sub-category": "Non-Alchoholic",
  "price": "$85.12",
  "expiry_date": "2/1/2023"
}, {
  "id": 17,
  "name": "Kellogs Special K Cereal",
  "category": "Grains",
  "sub-category": "Cereals",
  "price": "$22.17",
  "expiry_date": "11/18/2023"
}, {
  "id": 18,
  "name": "Pie Filling - Apple",
  "category": "Grains",
  "sub-category": "Pastery",
  "price": "$66.99",
  "expiry_date": "12/4/2023"
}, {
  "id": 19,
  "name": "Longos - Lasagna Veg",
  "category": "Grains",
  "sub-category": "Pasta",
  "price": "$93.12",
  "expiry_date": "6/22/2023"
}, {
  "id": 20,
  "name": "Cake Circle, Paprus",
  "category": "Grains",
  "sub-category": "Pastery",
  "price": "$72.02",
  "expiry_date": "3/24/2023"
}, {
  "id": 21,
  "name": "Table Cloth 62x114 Colour",
  "category": "Cleaning",
  "sub-category": "Clothes",
  "price": "$63.72",
  "expiry_date": "8/21/2023"
}, {
  "id": 22,
  "name": "Pears - Fiorelle",
  "category": "Toiletries",
  "sub-category": "Soap",
  "price": "$89.64",
  "expiry_date": "5/12/2023"
}, {
  "id": 23,
  "name": "Mace",
  "category": "Grains",
  "sub-category": "Spices",
  "price": "$1.49",
  "expiry_date": "2/1/2023"
}, {
  "id": 24,
  "name": "Muffin Mix - Raisin Bran",
  "category": "Grains",
  "sub-category": "Pastery",
  "price": "$47.11",
  "expiry_date": "6/21/2023"
}, {
  "id": 25,
  "name": "Cheese - Cheddar, Old White",
  "category": "Dairy",
  "sub-category": "Appetizers",
  "price": "$87.33",
  "expiry_date": "3/6/2023"
}, {
  "id": 26,
  "name": "Wine - Pinot Noir Pond Haddock",
  "category": "Drinks",
  "sub-category": "Alchoholic-Beverages",
  "price": "$57.66",
  "expiry_date": "5/7/2023"
}, {
  "id": 27,
  "name": "Sausage - Chorizo",
  "category": "Protein Foods",
  "sub-category": "Meat",
  "price": "$76.98",
  "expiry_date": "8/2/2023"
}, {
  "id": 28,
  "name": "Pickles - Gherkins",
  "category": "Vegetables",
  "sub-category": "Fermented foods",
  "price": "$11.60",
  "expiry_date": "2/22/2023"
}, {
  "id": 29,
  "name": "Coffee - Ristretto Coffee Capsule",
  "category": "Drink",
  "sub-category": "Hot beverages",
  "price": "$82.72",
  "expiry_date": "5/17/2023"
}, {
  "id": 30,
  "name": "Yogurt - Plain",
  "category": "Dairy",
  "sub-category": "Appetizers",
  "price": "$2.86",
  "expiry_date": "12/3/2023"
}]

products = []

for datum in product_data:
    prod = Product(**datum)
    products.append(prod)

session.add_all(products)
session.commit()