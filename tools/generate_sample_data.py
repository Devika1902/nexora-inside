"""Regenerate the fictional Nexora sample records with Python's standard library."""
import csv
import json
import random
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SEED = 20261124


def write_rows(name, rows):
    DATA.mkdir(parents=True, exist_ok=True)
    headers = list(rows[0])
    with (DATA / f"{name}.csv").open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    (DATA / f"{name}.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")


def main():
    rng = random.Random(SEED)
    names = ["Mila Fischer", "Jonas Weber", "Lea Schneider", "Emil Hoffmann", "Sofia Wagner", "Noah Becker", "Mia Schulz", "Leon Koch", "Amira Yilmaz", "Felix Braun", "Nina Krüger", "David Neumann", "Elena Richter", "Paul Wolf", "Sara Özdemir", "Luca Hartmann", "Hannah Lange", "Adam Nowak", "Clara Schmitt", "Omar Haddad"]
    departments = ["Engineering", "People and Culture", "Site Management", "Finance", "Sales", "Product", "Customer Support", "Marketing"]
    locations = ["Berlin", "Munich", "Hamburg", "Cologne", "Remote - Germany"]
    roles = ["Software Engineer", "People Partner", "Office Coordinator", "Financial Analyst", "Account Executive", "Product Manager", "Support Specialist", "Communications Specialist", "Engineering Lead", "Recruiter", "Event Coordinator", "UX Designer"]

    people = []
    for i in range(1, 651):
        first, last = rng.choice(names).split(" ", 1)
        people.append({"Employee_ID": f"NX-{i:04d}", "First_Name": first, "Last_Name": last, "Role": rng.choice(roles), "Department": rng.choice(departments), "Location": rng.choice(locations), "Manager_ID": f"NX-{rng.randint(1, 650):04d}", "Work_Email": f"{first.lower()}.{last.lower().replace(' ', '')}.{i}@nexora.example", "Start_Date": (date(2017, 1, 1) + timedelta(days=rng.randint(0, 3550))).isoformat(), "Employment_Status": rng.choices(["Active", "On leave", "Departed"], [94, 4, 2])[0]})
    write_rows("people", people)

    categories = ["Leadership", "People and Culture", "Department news", "Recognition", "Wellbeing", "Technology", "Operations", "Recruitment"]
    channels = ["Newsletter", "Intranet news", "Email", "Team meeting", "Manager cascade"]
    announcements = []
    for i in range(1, 651):
        d = date(2026, 1, 1) + timedelta(days=rng.randint(0, 365))
        category = rng.choice(categories)
        announcements.append({"Announcement_ID": f"ANN-{i:04d}", "Title": f"{category}: {rng.choice(['Monthly update', 'What teams need to know', 'New resources available', 'People and project news', 'Important dates ahead'])} {i:03d}", "Category": category, "Audience": rng.choice(["All employees", "People managers", "Berlin site", "Engineering", "New starters", "People and Culture"]), "Channel": rng.choice(channels), "Content_Owner": rng.choice(names), "Approver": rng.choice(["Site Director", "People Lead", "Communications Lead", "Department Head"]), "Status": rng.choice(["Draft", "In review", "Approved", "Scheduled", "Published"]), "Draft_Due": (d - timedelta(days=7)).isoformat(), "Publish_Date": d.isoformat(), "Review_Date": (d - timedelta(days=2)).isoformat(), "Call_to_Action": rng.choice(["Read the full update", "Register by the deadline", "Share with your team", "Contact the owner", "Save the date"]), "Link_or_Reference": f"NX-COMMS-{i:04d}"})
    write_rows("announcements", announcements)

    event_types = ["Town hall", "Learning session", "Wellbeing", "Team social", "Recruitment fair", "Celebration", "Customer event", "Volunteer day"]
    events = []
    for i in range(1, 651):
        d = date(2026, 1, 1) + timedelta(days=rng.randint(0, 730))
        cap = rng.choice([40, 60, 80, 100, 120, 180, 250, 400])
        regs = rng.randint(0, cap)
        if i == 1:
            event = {"Event_ID": "EVT-NX-2026-01", "Event_Name": "Nexora Annual Employee Celebration", "Event_Type": "Celebration", "Event_Date": "2026-10-15", "Start_Time": "17:30", "Location": "Nexora Conference Hall (fictional)", "Format": "On-site", "Event_Owner": "Mila Fischer", "Capacity": 220, "Registrations": 192, "Waitlist": 0, "Budget_EUR": 9000, "Spend_EUR": 8612, "Supplier_Status": "Confirmed", "Approval_Status": "Complete", "Comms_Deadline": "2026-09-24"}
        else:
            event = {"Event_ID": f"EVT-{i:04d}", "Event_Name": f"{rng.choice(event_types)} {d.strftime('%b %Y')} - {i:03d}", "Event_Type": rng.choice(event_types), "Event_Date": d.isoformat(), "Start_Time": rng.choice(["09:00", "10:00", "12:30", "16:00", "18:00"]), "Location": rng.choice(locations), "Format": rng.choice(["On-site", "Hybrid", "Online"]), "Event_Owner": rng.choice(names), "Capacity": cap, "Registrations": regs, "Waitlist": max(0, regs - cap), "Budget_EUR": rng.choice([500, 1200, 2500, 5000, 8500, 12000]), "Spend_EUR": rng.choice([350, 950, 1800, 4200, 7200]), "Supplier_Status": rng.choice(["Confirmed", "Pending", "Not required"]), "Approval_Status": rng.choice(["Proposed", "Approved", "In planning", "Complete"]), "Comms_Deadline": (d - timedelta(days=21)).isoformat()}
        events.append(event)
    write_rows("events", events)

    workstreams = ["Newsletter", "SharePoint", "Annual Celebration", "Careers Fair", "Internal communications", "Supplier coordination"]
    tasks = []
    for i in range(1, 651):
        due = date(2026, 1, 1) + timedelta(days=rng.randint(0, 730))
        status = rng.choice(["Not started", "In progress", "Waiting for review", "Complete", "On hold"])
        pct = {"Not started": 0, "In progress": rng.choice([25, 50, 75]), "Waiting for review": 90, "Complete": 100, "On hold": rng.choice([0, 25, 50])}[status]
        tasks.append({"Task_ID": f"TSK-{i:04d}", "Workstream": rng.choice(workstreams), "Task": f"{rng.choice(['Draft copy', 'Confirm owner', 'Review accessibility', 'Request supplier quote', 'Update page content', 'Approve budget', 'Send invitation', 'Reconcile attendance', 'Prepare feedback survey', 'Archive final material'])} {i:03d}", "Owner": rng.choice(names), "Department": rng.choice(departments), "Due_Date": due.isoformat(), "Priority": rng.choice(["High", "Medium", "Low"]), "Status": status, "Completion_Pct": pct, "Dependency": rng.choice(["None", "Content approval", "Venue confirmation", "Supplier response", "Budget approval"]), "Related_Event_ID": f"EVT-{rng.randint(1, 650):04d}", "Last_Updated": (due - timedelta(days=rng.randint(0, 12))).isoformat()})
    write_rows("tasks", tasks)

    supplier_types = ["Catering", "Venue", "Audio visual", "Photography", "Printing", "Floral", "Transport", "Accessibility", "Security", "Furniture"]
    suppliers = []
    for i in range(1, 601):
        category = rng.choice(supplier_types)
        suppliers.append({"Supplier_ID": f"SUP-{i:04d}", "Supplier_Name": f"{rng.choice(['Northstar', 'Brightline', 'Urban', 'Blue Oak', 'Fieldstone', 'Cedar', 'Open Door', 'Silver Birch'])} {category} Services {i:03d}", "Service_Category": category, "Contact_Name": rng.choice(names), "Contact_Email": f"events.{i:04d}@supplier.example", "Phone": f"+49 30 {rng.randint(1000000, 9999999)}", "Quote_EUR": rng.choice([250, 600, 950, 1500, 2400, 3500, 6200, 9800]), "Confirmation_Status": rng.choice(["Requested", "Quoted", "Under review", "Confirmed", "Declined"]), "Insurance_Received": rng.choice(["Yes", "No", "Not applicable"]), "Accessibility_Notes": rng.choice(["Step-free access confirmed", "Confirm ramp dimensions", "Accessible restroom available", "Ask about hearing support", "No special requirements noted"]), "Rating_1_to_5": rng.randint(3, 5), "Last_Contact_Date": (date(2026, 1, 1) + timedelta(days=rng.randint(0, 330))).isoformat()})
    write_rows("suppliers", suppliers)

    registration_statuses = ["Registered", "Waitlisted", "Cancelled", "Attended", "No-show"]
    registrations, event_slices, rec_no = [], [(events[0], 192), (events[1], 92), (events[2], 92), (events[3], 92), (events[4], 91), (events[5], 91)], 0
    for event, count in event_slices:
        for j in range(count):
            rec_no += 1
            person = rng.choice(people)
            status = ("Attended" if j < 174 else "No-show") if event["Event_ID"] == "EVT-NX-2026-01" else rng.choices(registration_statuses, [50, 8, 12, 25, 5])[0]
            registrations.append({"Registration_ID": f"REG-{rec_no:04d}", "Event_ID": event["Event_ID"], "Event_Name": event["Event_Name"], "Employee_ID": person["Employee_ID"], "Employee_Name": f"{person['First_Name']} {person['Last_Name']}", "Department": person["Department"], "Location": person["Location"], "RSVP_Status": status, "Dietary_Requirement": rng.choice(["None", "Vegetarian", "Vegan", "Gluten-free", "Halal", "Please contact me privately"]), "Accessibility_Request": rng.choice(["None", "Step-free route", "Reserved seating", "Captioning", "Please contact me privately"]), "Plus_One": rng.choice(["No", "No", "No", "Yes"]), "Registration_Date": (date(2026, 7, 1) + timedelta(days=rng.randint(0, 110))).isoformat(), "Check_In": "Present" if status == "Attended" else ("No-show" if status == "No-show" else "Not applicable")})
    write_rows("registrations", registrations)
    print("Generated 650 announcements, events, tasks, people and registrations; 600 suppliers.")


if __name__ == "__main__":
    main()
