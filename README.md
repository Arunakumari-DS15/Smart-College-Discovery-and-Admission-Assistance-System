# Ashoka Smart College Discovery & Admission Assistance

A Flask-based academic prototype for Ashoka Women's Engineering College, Kurnool.

## Features
- Responsive college discovery interface (HTML, CSS, JavaScript)
- Python Flask backend
- Trie-based prefix search
- Custom Hash Table course lookup
- Max Heap interest-based programme ranking
- College information Graph with animated BFS traversal
- Main Campus and Off-Campus sections
- Official links for awards, placements, disclosures and admissions

## 1. Open in VS Code
1. Extract the ZIP file.
2. Open VS Code.
3. Select **File > Open Folder**.
4. Choose `ashoka_smart_admission`.

## 2. Create virtual environment (recommended)
Open Terminal in VS Code and run:

```bash
python -m venv .venv
```

Windows PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:
```cmd
.venv\Scripts\activate.bat
```

## 3. Install Flask
```bash
python -m pip install -r requirements.txt
```

## 4. Run the website
```bash
python app.py
```
Open this address in your browser:
`http://127.0.0.1:5000`

Stop the server with `Ctrl + C`.

## 5. Add your college photographs
Copy approved photos into `static/images/` using these exact names:
- `college-hero.jpg`
- `hostel.jpg`
- `laboratory.jpg`
- `campus-life.jpg`

The main building image (`college-hero.jpg`) appears behind the title area.
Use college-approved images only. Do not use photos of students without appropriate permission.

## 6. Test the features
- Search: try `comp`, `mba`, `ece`, `artificial`
- Course lookup: select a course and click View details
- Recommendation: select multiple interest tags
- Graph: click **Run BFS animation** and watch the nodes light up level by level
- Reset: click **Reset graph**

## 7. Upload to GitHub
Create a new empty repository on GitHub, for example:
`ashoka-smart-college-discovery`

Then run these commands in the VS Code terminal from this project folder:

```bash
git init
git add .
git commit -m "Build Ashoka smart college discovery prototype"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/ashoka-smart-college-discovery.git
git push -u origin main
```
Replace `YOUR-USERNAME` with your GitHub username. Do not share your password or personal access token.

## Important content verification
This is a demonstration prototype, not an official college website.
- Verify course availability, intake, duration, fees and eligibility with the Admissions Office.
- Verify current placement numbers with the Placement Cell. Public college pages may show different batch figures.
- Verify current accreditation validity before displaying accreditation claims.
- Keep Main Campus (Dupadu) and Off-Campus (Chinnatekuru) information separate.
- Obtain approval before public deployment or use of official photographs, logos, student images and contact details.

## Public information references
- https://www.ashokacollege.in/
- https://www.ashokacollege.in/about/our-story/
- https://www.ashokacollege.in/awards-and-recognitions/
- https://www.ashokacollege.in/placement-overview/
- https://www.ashokacollege.in/about/mandatory-disclosures/
- https://www.ashokacollege.in/contact-us/
