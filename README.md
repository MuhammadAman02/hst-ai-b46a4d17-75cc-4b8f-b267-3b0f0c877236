# ML Engineer Portfolio

A professional portfolio website for an ML Engineer built with NiceGUI and Python.

## Features

- Responsive design that works on desktop and mobile
- Professional sections for showcasing ML projects
- Skills visualization with progress bars
- Experience and education timeline
- Contact form for potential employers or collaborators
- Modern UI with smooth animations and transitions

## Setup Instructions

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create an `assets` folder in the project root directory
4. Add your profile picture as `assets/profile.jpg`
5. Add project images as `assets/project1.jpg`, `assets/project2.jpg`, etc.
6. (Optional) Add a background image as `assets/hero-bg.jpg`
7. Customize your information in the `ml_engineer` dictionary in `main.py`
8. Run the application:
   ```
   python main.py
   ```
9. Open your browser and navigate to `http://localhost:8080`

## Customization

You can easily customize this portfolio by editing the `ml_engineer` dictionary in `main.py`. Update the following information:

- Personal details (name, title, bio, contact information)
- Skills and proficiency levels
- Projects with descriptions and technologies
- Work experience
- Education history
- Certifications

You can also modify the color scheme by editing the `colors` dictionary.

## Deployment

This application can be deployed to any platform that supports Python applications. Some options include:

- Heroku
- PythonAnywhere
- AWS Elastic Beanstalk
- Google Cloud Run
- Vercel (with serverless functions)

## License

This project is open source and available under the MIT License.