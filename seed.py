from app import app
from models import Power, Hero, Hero_Power, db

with app.app_context():

    Power.query.delete()
    Hero.query.delete()
    Hero_Power.query.delete()

    heroes =[]
    heroes.append(Hero(name ='Super' , super_name ='Superman'))
    heroes.append(Hero(name ='Spider' , super_name ='Spiderman'))
    heroes.append(Hero(name ='Aqua' , super_name ='Aquaman'))
    heroes.append(Hero(name ='Cat' , super_name ='Catwoman'))
    heroes.append(Hero(name ='Bat' , super_name ='Batman'))
    heroes.append(Hero(name ='Wolve' , super_name ='Wolverine'))
    heroes.append(Hero(name ='Ninja' , super_name ='Ninja Turtles'))
    heroes.append(Hero(name ='Wasp' , super_name ='The Wasp'))

    db.session.add_all(heroes)

    powers=[]
    powers.append(Power(name ='Telekinesis', description=' hypothetical psychic ability allowing an individual to influence a physical system without physical interaction.'))
    powers.append(Power(name ='Superhuman strength', description=' the power to exert force and lift weights beyond what is physically possible for an ordinary human being'))
    powers.append(Power(name ='Telepathy', description='the purported vicarious transmission of information from one mind to another without using any known human sensory channels or physical interaction'))
    powers.append(Power(name ='Teleportation', description='the hypothetical transfer of matter or energy from one point to another without traversing the physical space between them'))
    powers.append(Power(name ='Invisibility', description='the state of an object that cannot be seen'))
    powers.append(Power(name ='Power absorption', description='involves stealing another superhero power, either temporarily (like Rogue) or permanently.'))
    powers.append(Power(name ='Heat Vision', description='a powerful form of energy manipulation that allows the user to shoot heat rays out of their eyes.'))
    powers.append(Power(name ='Earth manipulation', description='The ability to instantly adapt to any environment.'))
    powers.append(Power(name ='Energy Projection', description=' the ability to generate and project different waves of energy from the body of a metahuman.'))
    powers.append(Power(name ='Density control', description='The ability to emit radiation from the body'))
    db.session.add_all(powers)

    hero_powers =[]
    hero_powers.append(Hero_Power(strength='Strong', hero=heroes[0], power=powers[1]))
    hero_powers.append(Hero_Power(strength='Weak', hero=heroes[6], power=powers[9]))
    hero_powers.append(Hero_Power(strength='Strong', hero=heroes[6], power=powers[2]))
    hero_powers.append(Hero_Power(strength='Strong', hero=heroes[3], power=powers[7]))
    hero_powers.append(Hero_Power(strength='Weak', hero=heroes[4], power=powers[2]))
    hero_powers.append(Hero_Power(strength='Average', hero=heroes[2], power=powers[5]))
    hero_powers.append(Hero_Power(strength='Average', hero=heroes[1], power=powers[3]))
    hero_powers.append(Hero_Power(strength='Weak', hero=heroes[2], power=powers[8]))
    hero_powers.append(Hero_Power(strength='Average', hero=heroes[5], power=powers[1]))
    hero_powers.append(Hero_Power(strength='Strong', hero=heroes[4], power=powers[6]))
    hero_powers.append(Hero_Power(strength='Strong', hero=heroes[1], power=powers[7]))
    hero_powers.append(Hero_Power(strength='Average', hero=heroes[2], power=powers[4]))
    hero_powers.append(Hero_Power(strength='Strong', hero=heroes[4], power=powers[0]))
    hero_powers.append(Hero_Power(strength='Weak', hero=heroes[7], power=powers[5]))
    hero_powers.append(Hero_Power(strength='Average', hero=heroes[7], power=powers[7]))

    db.session.add_all(hero_powers)
    db.session.commit()

