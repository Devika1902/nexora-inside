# Nexora Inside

An interactive, SharePoint-style internal communications and event coordination prototype for the fictional Nexora Technologies GmbH. It turns the project brief into a portfolio-ready intranet experience with a homepage, news hub, people directory, events, resource library, newsletter workflow, communication guidelines, careers fair kit and admin tracker.

> **Prototype note:** This is a static front-end demonstration. It does not connect to Microsoft 365, send email, register attendees or store edits. The sample organization, people, contact details and activity are fictional. The `nexora.example` domain is reserved for examples.

## Publish the public website

This repository includes a GitHub Actions workflow at `.github/workflows/deploy.yml`. After it is pushed to a **public GitHub repository**, GitHub Pages publishes the site and republishes it whenever `main` changes. No always-on computer or local server is needed. GitHub's current setup requires choosing **GitHub Actions** as the Pages build source in repository settings once; see [GitHub's workflow publishing instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

### First-time setup

1. Sign in to GitHub and make sure GitHub CLI is authenticated on this computer (`gh auth login`).
2. From the project folder, create the public repository and push the project:

   ```powershell
   git add .
   git commit -m "Build Nexora internal communications site"
   gh repo create nexora-inside --public --source=. --remote=origin --push
   ```

   If you already created a repository, add it as `origin` and push `main` instead.

3. On GitHub, open the new repository and choose **Settings → Pages → Build and deployment → Source: GitHub Actions**.
4. Open the **Actions** tab and wait for **Deploy Nexora Inside** to finish successfully. The workflow page shows the published site URL; it will look like `https://YOUR-USERNAME.github.io/nexora-inside/`.

After setup, every push to `main` updates the public site automatically. The project owner can share that URL with visitors. GitHub Pages is a static host: this prototype does not provide sign-in, per-employee access control, Microsoft 365 connectivity or server-side storage. Anyone with the public URL can view the published fictional sample content.

### Preview before publishing (optional)

Use `py -m http.server 8000` in the project folder, then open `http://localhost:8000`. This is only a local preview; it is not required for public availability.

## What's included

| Area | Experience |
| --- | --- |
| Communication strategy | Reusable principles, content approvals, editorial cadence and calendar guidance |
| Employee newsletter | Monthly issue concept, editorial checklist, approvals and archive |
| Intranet portal | Overview, announcements, people, documents, and event navigation |
| Event coordination | Featured annual celebration, calendar, registration and budget fields |
| HR marketing | Careers fair brochure, poster, leaflet, stand, presentation and QR plan |
| Administration | Searchable, filterable communications and event task tracker |

The generated demo datasets contain **650 announcements, 650 events, 650 tasks, 650 people and 600 suppliers** (3,200 fictional records total). Each dataset is provided as JSON for the interface and CSV for spreadsheet use. Tables show 10 records per page and support text search, filtering and CSV export.

## Regenerate the datasets

The generator is deterministic: repeated runs create the same fictional records.

```powershell
py data/generate_data.py
```

This writes both `.json` and `.csv` versions under `data/`.

## Publish with GitHub

1. Create an empty repository on GitHub (for example, `nexora-inside`). Do not add a README there, since this project already has one.
2. In the project folder, initialize Git and commit the project:

   ```powershell
   git init
   git add .
   git commit -m "Build Nexora internal communications prototype"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/nexora-inside.git
   git push -u origin main
   ```

   Replace `YOUR-USERNAME` with your GitHub account name. GitHub will prompt you to authenticate if needed.

3. The included workflow handles Pages deployments on every push to `main`. Choose **GitHub Actions** as the Pages source once in **Settings → Pages**.

Before making a repository public, review the fictional sample data and remove any personal or confidential information you may add later.

## Project structure

```text
index.html             App shell and navigation
styles.css             Responsive visual system
app.js                 Page rendering, filtering, pagination and export
data/generate_data.py  Repeatable fictional data generator
data/*.json            Data consumed by the prototype
data/*.csv             Spreadsheet-friendly versions
```

## Design and workflow notes

- The UI uses a responsive desktop-first layout and adapts for narrow screens.
- The approval pattern is content owner → department lead → communications review → sponsor approval → publish and measure.
- Adapt the cadence, owners, retention rules and approval thresholds to your real organization's policies before operational use.
- Remote Google Fonts are used for Manrope and DM Sans; system sans-serif fallbacks remain available when offline.
