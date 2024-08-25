# D6Player Campaign Management System

D6Player is a web-based campaign management tool for tabletop role-playing games (TTRPGs). This project allows users to create and manage campaigns, scenes, and characters, providing an easy-to-use interface for managing complex TTRPG stories.

## Features

- **User Authentication**: 
  - Users can register, log in, and log out of the system.
  - Each user has a unique profile with a customizable nickname and email.
  
- **Campaign Management**:
  - Users can create and manage multiple campaigns.
  - Campaigns consist of a name and description.
  - Users can view details of each campaign and see all associated scenes and characters.

- **Scene Management**:
  - Each campaign can have multiple scenes.
  - Users can add, update, and delete scenes within a campaign.
  - Scenes include a name, description, and action log.

- **Character Management**:
  - Characters can be associated with campaigns and scenes.
  - Users can create, view, and manage characters, assigning them to specific scenes within a campaign.

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 4.x
- Django REST Framework
- PostgreSQL (or another database of your choice)
- Git (for version control)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/d6player.git
   cd d6player
   ```

2. **Create and activate a virtual environment**:
```
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**:
```
pip install -r requirements.txt
```

4. **Set up the database**:
- Configure your database settings in d6player/settings.py.
- Install MongoDB by going to the official page (Mongodb.org) and following the manual set up steps for you rsystem of choice
- Run the following commands to migrate the models to the database:
```
python manage.py makemigrations
python manage.py migrate
```

5. **Run the development server**:
```
python manage.py runserver
```
The application should now be accessible at http://127.0.0.1:8000/.

## Usage
- Homepage:
Once logged in, users can view their campaigns on the homepage.
    - Campaign details can be accessed by clicking on the respective campaign links.

- Creating Campaigns:
Click the "Create New Campaign" button on the homepage.
    - Fill in the campaign name and description, and submit the form.

- Managing Scenes and Characters:
    - Access the campaign details page.
    - Create and manage scenes and characters associated with that campaign.
### API Endpoints
- Campaigns API:
    - GET /api/campaigns/ - List all campaigns for the logged-in user.
    - POST /api/campaigns/ - Create a new campaign.
    - GET /api/campaigns/<id>/ - Retrieve a specific campaign.
    - PUT /api/campaigns/<id>/ - Update a campaign.
    - DELETE /api/campaigns/<id>/ - Delete a campaign.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.