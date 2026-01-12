import random

types = ["birthday","wedding","corporate","seminar","festival","anniversary"]
locations = ["Dhanbad","Ranchi","Patna","Delhi","Kolkata","Bangalore"]
venues = ["Royal Hall","City Banquet","Grand Palace","Green Lawn","Metro Hall"]
caterers = ["Aman Caterers","Sharma Caterers","Royal Foods","Urban Foods"]
decor = ["Minimal","Premium","Luxury","Basic","Theme"]

data = []

for i in range(50):
    data.append({
        "event_type": random.choice(types),
        "location": random.choice(locations),
        "guests": random.randint(50,500),
        "venue": random.choice(venues),
        "caterer": random.choice(caterers),
        "decoration": random.choice(decor),
        "cost": random.randint(40000,500000),
        "rating": round(random.uniform(4.0,4.9),1)
    })

print(data)
