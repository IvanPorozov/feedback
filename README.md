Website

How to install and run:

1. Choose your directory.
2. Clone the GitHub repository:
   ```
     git clone <link>
   ```
3. Navigate to the directory containing manage.py and requirements.txt.
4. Create your virtual environment:
   ```
      python -m venv venv
   ```
5. Activate your virtual environment:
6. On Windows:
   ```
      .\venv\Scripts\activate.bat
   ```
   On macOS/Linux:
    ```
       source venv/bin/activate
    ```
7. Install the requirements:
    ```
       pip install -r requirements.txt
    ```
8. Run the server:
    ```
       python manage.py runserver
    ```
