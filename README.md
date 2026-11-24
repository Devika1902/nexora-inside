# Project 02 — Internal Communications, SharePoint and Corporate Event Management

This is a finished, fictional portfolio project for Nexora Technologies GmbH. It demonstrates how an administrative communications role can plan internal messages, prepare a monthly employee newsletter, design a SharePoint information structure, coordinate an employee event, support recruitment marketing, and track the work.

**There is no website to launch and no local server to run.** Open the Word, Excel and PowerPoint deliverables directly in Microsoft Office or compatible applications. The SharePoint work is a visual design concept, not a live site.

## Start here

1. Read the plain-language [Project Overview](docs/PROJECT_OVERVIEW.md).
2. Open the [Corporate Communication Guidelines](deliverables/01_Communications/Corporate_Communication_Guidelines.docx) for the strategy and approval process.
3. Browse the [December Newsletter](deliverables/02_Newsletter/December_2026_Newsletter_Issue.docx) and its [reusable template](deliverables/02_Newsletter/Reusable_Newsletter_Template.docx).
4. View the [SharePoint Intranet Design Plan](deliverables/03_Intranet/SharePoint_Intranet_Design_Plan.docx) and its editable [PowerPoint page mockups](outputs/SharePoint_Intranet_Prototype.pptx).
5. Open the [Annual Celebration Event Pack](deliverables/04_Events/Annual_Employee_Celebration_Event_Pack.docx) and the [Excel tracker](outputs/Internal_Communication_Event_Tracker.xlsx).
6. Review the [Careers Fair Content Kit](deliverables/05_Recruitment/Careers_Fair_Content_Kit.docx) and the editable [Careers Fair Visual Kit](outputs/Careers_Fair_Visual_Kit.pptx).

## What is included

| Module | Deliverables | What they demonstrate |
| --- | --- | --- |
| 1. Communication strategy | Corporate Communication Guidelines; 650-row announcement records | Audiences, channels, cadence, editorial calendar, review and approval workflow, accessibility and measures |
| 2. Employee newsletter | December issue; reusable newsletter template | Management message, department updates, recognition, events, HR news, new starters and organizational information |
| 3. SharePoint-style intranet | Site structure and page plan; PowerPoint mockups for Home, News, HR and Events | Navigation, content ownership, page governance, accessibility and information architecture |
| 4. Internal event | Proposal, fictional venue comparison, budget assumptions, run of show, invitation and illustrative post-event review | Venue selection, cost planning, registrations, logistics, suppliers, feedback and lessons |
| 5. HR marketing and trade fair | Company brochure copy, poster, candidate leaflet, stand concept and employee presentation | A consistent recruitment story and a practical visitor journey |
| 6. Performance and administration | Excel tracker; 650-row announcement, event, task, people and registration data; 600 suppliers | Publication dates, approvals, deadlines, event capacity, expenditure, supplier status and outstanding work |

## Sample data

The `data/` directory includes CSV and JSON versions of six fictional datasets:

| File | Records |
| --- | ---: |
| Announcements | 650 |
| Events | 650 |
| Tasks | 650 |
| People | 650 |
| Suppliers | 600 |
| Registrations | 650 |

The rows are deterministic, so regenerating them with the same script produces the same sample records. Field descriptions are in [data/README.md](data/README.md). The `.example` email domains are reserved examples and do not route to real employees or suppliers.

## Use and refresh the project

### Use the files

- Word documents are editable. Duplicate the newsletter master before making a new issue.
- PowerPoint decks contain editable page and recruitment-material concepts.
- The Excel tracker has a Dashboard, formula-driven Budget sheet, and filterable record sheets. Update the sample data or budget inputs as needed.
- CSV files can be opened in Excel, LibreOffice Calc or another spreadsheet application. JSON files can be imported into development tools.

### Regenerate the sample data

Python 3 is needed only if you want to create the sample records again. From the project folder, run:

```powershell
py tools/generate_sample_data.py
```

The script uses only the Python standard library and writes both CSV and JSON files into `data/`. It does not launch a server or change the Office deliverables.

### Prepare the QR material

The QR field in the careers fair Word kit points to `https://careers.nexora.example/fair`, a deliberately fictional address. In Word, update the field after opening the document to display its QR pattern. Replace the target with an approved careers URL before any real printing; the `.example` destination is not a live page.

## GitHub portfolio setup

This is a normal Git repository with no deployment workflow. To publish the project source and Office files in a new GitHub repository:

1. Create an empty repository on GitHub.
2. From this folder, connect the new repository and push the current branch:

```powershell
git remote add origin https://github.com/YOUR-ACCOUNT/YOUR-REPOSITORY.git
git add .
git commit -m "Build internal communications portfolio project"
git push -u origin main
```

If this checkout still has an old `origin`, change it to the new repository URL before pushing:

```powershell
git remote set-url origin https://github.com/YOUR-ACCOUNT/YOUR-REPOSITORY.git
```

GitHub will store the files and display the README. It will not host a website. Avoid committing real employee records, private supplier quotes or other confidential material.

## Fictional content and limitations

Nexora Technologies GmbH, its employees, suppliers, venues, contact details, event outcomes, budgets and measurements are invented for portfolio practice. Event prices are planning assumptions, not real quotes. The project does not connect to Microsoft 365, SharePoint, Forms, Lists, Outlook or a live careers site. Confirm real company policies, permissions, retention rules, brand assets and accessibility requirements before adapting any example for operational use.
