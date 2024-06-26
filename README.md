# Team Management API

This project provides a RESTful API for managing teams and members within those teams. It is built using Django and Django Rest Framework (DRF).

## Features

- CRUD operations for Teams
- CRUD operations for Members
- Assign members to teams

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of Python and pip
- You have a PostgreSQL database running

## Installing Team Management API

To install the Team Management API, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Daniil-Pankieiev/Team-Management-API.git
   cd team-management


2. Create a virtual environment:
```bash
python -m venv venv
```
3. Activate the virtual environment:

On macOS and Linux:
```bash
source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```
4. Install project dependencies:
```bash
pip install -r requirements.txt
```
5. Copy .env_sample to .env and populate it with all required data. I

If you want to use PostgreSQL, specify ENV_STATE=prod, your secret key, your database information, and add ALLOWED_HOSTS

6. Apply the migrations:

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
7. Run the application:
```bash
python manage.py runserver
```
Run tests:
```bash
python manage.py test
```
The API will be available at http://127.0.0.1:8000/.
API Endpoints
Teams

    List all teams: GET /api/team/teams/

    Create a new team: POST /api/team/teams/

    Retrieve a team: GET /api/team/teams/{id}/

    Update a team: PUT /api/team/teams/{id}/

    Delete a team: DELETE /api/team/teams/{id}/

Members

    List all members: GET /api/member/people/

    Create a new member: POST /api/member/people/

    Retrieve a member: GET /api/member/people/{id}/

    Update a member: PUT /api/member/people/{id}/

    Delete a member: DELETE /api/member/people/{id}/

Contributions are welcome! Please read the contributing guidelines to get started.
