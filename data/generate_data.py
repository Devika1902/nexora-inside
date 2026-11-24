"""Create deterministic, fictional Nexora demo data (CSV and JSON)."""
import csv
import json
import random
from datetime import date, timedelta
from pathlib import Path

OUT = Path(__file__).parent
random.seed(20261124)
departments = ["People & Culture", "Engineering", "Product", "Finance", "Operations", "Sales", "Marketing", "Customer Success", "IT & Security", "Sustainability"]
locations = ["Berlin", "Munich", "Hamburg", "Cologne", "Stockholm", "Amsterdam", "Remote — Germany", "Frankfurt"]
first = ["Amira", "Jonas", "Lea", "Mateo", "Sofia", "Noah", "Mila", "Elias", "Zara", "Luca", "Freya", "Theo", "Nina", "Ava", "Emil", "Maya", "Felix", "Ines", "David", "Clara"]
last = ["Keller", "Bauer", "Schmidt", "Weber", "Hoffmann", "Fischer", "Wagner", "Becker", "Meyer", "Schulz", "Richter", "Koch", "Wolf", "Neumann", "Braun"]
statuses = ["Published", "In review", "Draft", "Scheduled"]
categories = ["Company news", "People & culture", "Engineering", "Customer stories", "Sustainability", "Leadership", "Learning", "Wellbeing"]
def person(i): return f"{first[i % len(first)]} {last[(i * 7) % len(last)]}"
def save(name, rows):
    (OUT / f"{name}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    with (OUT / f"{name}.csv").open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

announcements=[]
for i in range(1, 651):
    d=date(2026,1,1)+timedelta(days=(i*3)%365)
    announcements.append({"id":f"COM-{i:04d}","title":f"{random.choice(['A new chapter for','Meet the team behind','Building better together:','Nexora update —','Inside our work on','Save the date:'])} {random.choice(['our Berlin hub','responsible AI','customer experience','summer gathering','the next product release','employee wellbeing','community partnerships','our teams','learning week','sustainability goals'])}","category":categories[i%len(categories)],"department":departments[i%len(departments)],"owner":person(i),"audience":random.choice(["All employees", "People managers", "Berlin office", "Engineering", "New starters"]),"status":statuses[i%4],"publish_date":d.isoformat(),"channel":random.choice(["Intranet", "Newsletter", "Email", "Town hall"]),"approver":person(i+9)})
save("announcements", announcements)

events=[]
event_names=["Nexora Connect", "Product Demo Hour", "People & Culture Coffee", "Engineering Open House", "New Starter Welcome", "Sustainability Forum", "Customer Stories Live", "Learning Lab", "Summer Social", "Leadership Q&A", "Community Day", "Wellbeing Workshop"]
for i in range(1,651):
    d=date(2026,1,5)+timedelta(days=(i*2)%360)
    cap=random.choice([30,45,60,80,120,180,250]); registered=random.randint(8,cap)
    events.append({"id":f"EVT-{i:04d}","name":event_names[i%len(event_names)],"type":random.choice(["Town hall", "Workshop", "Social", "Webinar", "Career fair", "All hands"]),"date":d.isoformat(),"time":random.choice(["09:30", "11:00", "13:30", "15:00", "17:30"]),"location":random.choice(locations)+random.choice([" · Auditorium", " · Studio 2", " · Online", " · Meeting room A"]),"organizer":person(i+3),"department":departments[i%len(departments)],"registered":registered,"capacity":cap,"status":random.choice(["Open", "Open", "Full", "Planning", "Completed"]),"budget_eur":random.randrange(400,12501,100)})
save("events",events)

tasks=[]
task_names=["Confirm venue availability", "Review newsletter draft", "Collect department highlights", "Approve event invitation", "Reconcile supplier invoice", "Publish intranet announcement", "Prepare registration form", "Confirm catering numbers", "Share post-event survey", "Update HR information page", "Check AV equipment", "Prepare leadership talking points", "Send calendar hold", "Review careers brochure", "Request accessibility requirements", "Archive approved assets"]
for i in range(1,651):
    due=date(2026,1,1)+timedelta(days=(i*5)%365)
    tasks.append({"id":f"TASK-{i:04d}","task":task_names[i%len(task_names)],"workstream":random.choice(["Newsletter", "Internal event", "Intranet", "HR marketing", "Governance"]),"owner":person(i+5),"due_date":due.isoformat(),"priority":random.choice(["Normal", "Normal", "High", "Low"]),"status":random.choice(["To do", "In progress", "In progress", "Done", "Waiting"]),"related_id":f"EVT-{(i%650)+1:04d}"})
save("tasks",tasks)

people=[]
roles=["People Partner", "Software Engineer", "Product Manager", "Communications Specialist", "Finance Analyst", "Office Coordinator", "UX Researcher", "Talent Partner", "Customer Success Manager", "Security Engineer", "Sales Director", "Data Scientist"]
for i in range(1,651):
    name=person(i)
    people.append({"id":f"NX-{i:04d}","name":name,"role":roles[i%len(roles)],"department":departments[i%len(departments)],"location":locations[i%len(locations)],"email":f"{name.lower().replace(' ','.')}@nexora.example","start_date":(date(2018,1,1)+timedelta(days=(i*17)%3200)).isoformat(),"manager":person(i+11),"pronouns":random.choice(["she/her", "he/him", "they/them", "she/her", "he/him"])})
save("people",people)

suppliers=[]
supplier_names=["Brightside Events", "Studio Norden", "Green Table Catering", "Sound & Signal GmbH", "Paper Plane Print", "Urban Venue Co.", "GoodDays Hospitality", "Pixelhaus Creative", "Rail & Ride", "Clearview AV", "Kindred Flowers", "Loop Rental"]
services=["Venue", "Catering", "AV & staging", "Print & signage", "Photography", "Travel", "Event production", "Gifts & merchandise"]
for i in range(1,601):
    suppliers.append({"id":f"SUP-{i:04d}","supplier":f"{supplier_names[i%len(supplier_names)]} {['Berlin','North','Collective','Studio','Partners'][i%5]}","service":services[i%len(services)],"contact":person(i+2),"email":f"events{i}@supplier.example","city":locations[i%len(locations)],"status":random.choice(["Confirmed", "Confirmed", "Awaiting reply", "Not booked"]),"last_used":(date(2025,1,1)+timedelta(days=(i*9)%365)).isoformat(),"rating":round(random.uniform(3.6,5.0),1)})
save("suppliers",suppliers)
print("Generated 3,201 fictional records across 5 datasets in CSV and JSON.")
