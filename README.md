# Restaurant Application

This project aims to develop a restaurant application similar to Zomato, providing distinct functionalities for administrators and regular users.

## Features

### Administrator Functionality

- **Manage Restaurants:**
  - Create, modify, and remove restaurant listings.
- **View Restaurant Listings:**
  - Access a comprehensive list view of all registered restaurants.
- **Manage User Accounts:**
  - View and manage user accounts, primarily customers.

### User Functionality

- **Explore Restaurants:**
  - Explore a paginated list of restaurants.
- **Filter Restaurants:**
  - Apply filters for refined restaurant searches, including ratings greater than 3.5 stars.
- **Bookmark Favorite Restaurants:**
  - Bookmark favorite restaurants for easy access.
- **Rate and Review Restaurants:**
  - Rate restaurants and provide reviews to share experiences.
  - Edit and delete previously submitted ratings.

## Database

The application uses SQLite as the database for storing restaurant listings, user accounts, ratings, and reviews.

## Setup Instructions

1. **Clone the Repository:**
   https://github.com/shameemm/Restaurant-App.git
2. **Setup Virtual Environment:**
    cd restaurant-app
    python -m venv env

3. **Activate Virtual Environment:**
- Windows:
  ```
  env\Scripts\activate
  ```
- macOS/Linux:
  ```
  source env/bin/activate
  ```

4. **Install Dependencies:**
pip install -r requirements.txt

5. **Run Migrations:**
python manage.py migrate

6. **Start the Development Server:**
python manage.py runserver

7. **Access the Application:**
- Open a web browser and go to `http://127.0.0.1:8000/` to access the application.

## API Endpoints

- `/admin/`: Access the admin panel for restaurant and user management.
- `/api/restaurants/`: API endpoint for listing and managing restaurants.
- `/api/users/`: API endpoint for user-related functionalities.


   
