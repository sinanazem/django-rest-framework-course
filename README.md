# Q&A System with Django Rest Framework
<img src="https://www.django-rest-framework.org/img/logo.png">

## Description
This project is a Question and Answer system built using Django Rest Framework. It allows users to ask questions, provide answers, and interact with the community by voting on questions and answers.

## Features
- User authentication and authorization
- CRUD operations for questions and answers
- Upvoting and downvoting questions and answers
- Search functionality for finding questions
- API endpoints for easy integration with frontend applications

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/sinanazem/django-rest-framework-course.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Access the API documentation at `/api/docs/` after running the server to explore available endpoints and make requests.
- Use the provided API endpoints to perform CRUD operations on questions and answers, manage user authentication, and interact with the system.

## Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
