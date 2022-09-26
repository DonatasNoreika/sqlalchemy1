from sqlalchemy.orm import sessionmaker
from modules.projektas import engine, Projektas

Session = sessionmaker(bind=engine)
session = Session()

# (CRUD – create, read, update, delete)

# CREATE

# projektas1 = Projektas("Naujas pr.", 20000)
# session.add(projektas1)
# session.commit()

# projektas2 = Projektas("2 projektas", 55000)
# projektas3 = Projektas("3 projektas", 100000)
# session.add(projektas2)
# session.add(projektas3)
# session.commit()

# READ
# projektas1 = session.query(Projektas).get(1)
# print(projektas1)

# projektas2 = session.query(Projektas).filter_by(name="2 projektas").first()
# print(projektas2.created_date)

# projektai = session.query(Projektas).all()
#
# for projektas in projektai:
#     print(projektas.price)

# search = session.query(Projektas).filter(Projektas.name.ilike("2%")).all()
# print(search)


# search2 = session.query(Projektas).filter(Projektas.price > 1000).all()
# print(search2)

# search3 = session.query(Projektas).filter(
#     Projektas.price > 1000,
#     Projektas.name.ilike("3%")).all()
#
# print(search3)

# UPDATE
# projektas1 = session.query(Projektas).get(1)
# projektas1.name = "1 projektas"
# session.commit()

# projektas2 = session.query(Projektas).filter_by(name="2 projektas").one()
# projektas2.name = "2 projektas tikrai"
# session.commit()

# DELETE
# projektas1 = session.query(Projektas).get(1)
# session.delete(projektas1)
# session.commit()

while True:
    choice = int(input("1 - atvaizduoti \n2 - įvesti \n3 - redaguoti \n4 - ištrinti \n0 - išeiti"))
    match choice:
        case 1:
            projektai = session.query(Projektas).all()
            print("------------Projektai-------------")
            for projektas in projektai:
                print(projektas)
            print("----------------------------------")
        case 2:
            name = input("Pavadinimas: ")
            price = float(input("Kaina: "))
            projektas = Projektas(name, price)
            session.add(projektas)
            session.commit()
        case 3:
            print("------------Projektai-------------")
            projektai = session.query(Projektas).all()
            for projektas in projektai:
                print(projektas)
            print("----------------------------------")
            red_id = int(input("Įveskite redaguojamo ID: "))
            red_irasas = session.query(Projektas).get(red_id)
            red_name = input("Pavadinimas: ")
            red_price = float(input("Kaina: "))
            red_irasas.name = red_name
            red_irasas.price = red_price
            session.commit()
        case 4:
            print("------------Projektai-------------")
            projektai = session.query(Projektas).all()
            for projektas in projektai:
                print(projektas)
            print("----------------------------------")
            trin_id = int(input("Įveskite trinamo ID: "))
            trin_irasas = session.query(Projektas).get(trin_id)
            session.delete(trin_irasas)
            session.commit()
        case 0:
            print("Viso gero")
            break
