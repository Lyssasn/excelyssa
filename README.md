# 💠 excelyssa 

Web app for modifying Ms Excel with given data and templates

### 🌐 Current Endpoint

| Name | URL | Method|
|------|-----|-----|
| Login | /auth/login | GET, POST|
| Register | /auth/register | GET, POST|
| Logout | /auth/logout | POST|
| Company | / | GET, POST|
| C. create | /create | GET, POST|
| C. update | /\<id\>/update | GET, POST|
| C. delete | /\<id\>/delete | POST|


### 📅 ToDo: Alpha Release
✔ Create user migration (@current: name, email, password)

✔ Create company migration (@current: name)

⏳ Create company_notes migration

✔ Create user registration

✔ Create user login

✔ Create user logout

✔ Create company CRUD

⏳ Create company_notes CRUD

⏳ Create excel uploader

⏳ Create excel modifier

⏳ Create excel downloader

⏳ Create word modifier

⏳ Create word downloader

## 📌 Note
- Recent view is prototype
- Recent database use sqlite3

## 🚀 Milestone: v1
- Complete each table field

## 🚀 Milestone: v2
- Use MariaDB for better database storage
- Use ORM for better SQL handling
- Use VueJS for better UI/UX