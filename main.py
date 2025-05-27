from nicegui import ui, app
import uvicorn
import os

# Configure static files directory for images and assets
app.add_static_files('/assets', 'assets')

# Sample ML Engineer data - replace with your own information
ml_engineer = {
    'name': 'Alex Johnson',
    'title': 'Machine Learning Engineer',
    'bio': 'Experienced ML Engineer with 5+ years of experience developing and deploying machine learning models for real-world applications. Specializing in computer vision, NLP, and recommendation systems.',
    'profile_pic': '/assets/profile.jpg',
    'email': 'alex@example.com',
    'github': 'https://github.com/alexjohnson',
    'linkedin': 'https://linkedin.com/in/alexjohnson',
    'skills': {
        'Machine Learning': 95,
        'Deep Learning': 90,
        'Python': 95,
        'TensorFlow': 85,
        'PyTorch': 80,
        'Computer Vision': 85,
        'NLP': 80,
        'MLOps': 75,
        'Data Engineering': 70,
        'SQL': 75
    },
    'projects': [
        {
            'title': 'Computer Vision for Retail Analytics',
            'description': 'Developed a computer vision system to analyze customer behavior in retail environments. The system tracks customer movement, identifies product interactions, and generates heatmaps for store optimization.',
            'technologies': ['Python', 'TensorFlow', 'OpenCV', 'Docker', 'AWS'],
            'image': '/assets/project1.jpg',
            'github_link': 'https://github.com/alexjohnson/retail-vision'
        },
        {
            'title': 'NLP-Powered Customer Support Chatbot',
            'description': 'Created an intelligent chatbot using NLP techniques to automate customer support for a SaaS company. The system handles 70% of customer queries without human intervention.',
            'technologies': ['Python', 'BERT', 'FastAPI', 'React', 'GCP'],
            'image': '/assets/project2.jpg',
            'github_link': 'https://github.com/alexjohnson/support-chatbot'
        },
        {
            'title': 'Recommendation Engine for E-commerce',
            'description': 'Built a hybrid recommendation system combining collaborative filtering and content-based approaches to increase user engagement and sales for an e-commerce platform.',
            'technologies': ['Python', 'PyTorch', 'Spark', 'Kafka', 'PostgreSQL'],
            'image': '/assets/project3.jpg',
            'github_link': 'https://github.com/alexjohnson/ecommerce-recommender'
        },
        {
            'title': 'Predictive Maintenance for Manufacturing',
            'description': 'Implemented a predictive maintenance solution using IoT sensor data to forecast equipment failures before they occur, reducing downtime by 35%.',
            'technologies': ['Python', 'Scikit-learn', 'Time Series Analysis', 'Docker', 'Azure'],
            'image': '/assets/project4.jpg',
            'github_link': 'https://github.com/alexjohnson/predictive-maintenance'
        }
    ],
    'experience': [
        {
            'role': 'Senior ML Engineer',
            'company': 'TechCorp AI',
            'period': '2020 - Present',
            'description': 'Lead ML Engineer for computer vision and NLP projects. Responsible for model development, deployment, and team mentorship.'
        },
        {
            'role': 'ML Engineer',
            'company': 'DataSense Inc.',
            'period': '2018 - 2020',
            'description': 'Developed recommendation systems and predictive models for various clients in retail and finance sectors.'
        },
        {
            'role': 'Data Scientist',
            'company': 'AnalyticsPro',
            'period': '2016 - 2018',
            'description': 'Analyzed large datasets to extract insights and build predictive models for business decision-making.'
        }
    ],
    'education': [
        {
            'degree': 'M.S. in Computer Science, Machine Learning Specialization',
            'institution': 'Stanford University',
            'year': '2016'
        },
        {
            'degree': 'B.S. in Computer Science',
            'institution': 'University of Washington',
            'year': '2014'
        }
    ],
    'certifications': [
        'Google Cloud Professional Machine Learning Engineer',
        'AWS Certified Machine Learning - Specialty',
        'Deep Learning Specialization - Coursera (Andrew Ng)',
        'TensorFlow Developer Certificate'
    ]
}

# Define color scheme
colors = {
    'primary': '#4a6fa5',
    'secondary': '#166088',
    'accent': '#4d9db4',
    'background': '#f8f9fa',
    'text': '#333333',
    'light_text': '#6c757d'
}

# Custom CSS for the portfolio
custom_css = """
<style>
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #f8f9fa;
        color: #333333;
    }
    .container {
        max-width: 1200px;
        margin: 0 auto;
    }
    .section {
        margin-bottom: 3rem;
        padding: 2rem;
        border-radius: 8px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .section-title {
        color: #4a6fa5;
        margin-bottom: 1.5rem;
        font-weight: 700;
        border-bottom: 2px solid #4a6fa5;
        padding-bottom: 0.5rem;
    }
    .skill-bar {
        height: 10px;
        border-radius: 5px;
        background-color: #e9ecef;
        margin-bottom: 1rem;
    }
    .skill-progress {
        height: 100%;
        border-radius: 5px;
        background-color: #4d9db4;
    }
    .project-card {
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    .project-card:hover {
        transform: translateY(-5px);
    }
    .tech-tag {
        background-color: #e9ecef;
        color: #4a6fa5;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
        display: inline-block;
        font-size: 0.8rem;
    }
    .social-icon {
        font-size: 1.5rem;
        color: #4a6fa5;
        margin-right: 1rem;
        transition: color 0.3s ease;
    }
    .social-icon:hover {
        color: #4d9db4;
    }
    .navbar {
        position: sticky;
        top: 0;
        z-index: 1000;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .nav-link {
        color: #333333;
        font-weight: 500;
        transition: color 0.3s ease;
    }
    .nav-link:hover, .nav-link.active {
        color: #4a6fa5;
    }
    .hero-section {
        background: linear-gradient(135deg, #4a6fa5 0%, #4d9db4 100%);
        color: white;
        padding: 4rem 2rem;
        border-radius: 8px;
        margin-bottom: 3rem;
    }
    .profile-pic {
        border-radius: 50%;
        border: 4px solid white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .experience-item, .education-item {
        margin-bottom: 1.5rem;
        padding-bottom: 1.5rem;
        border-bottom: 1px solid #e9ecef;
    }
    .experience-item:last-child, .education-item:last-child {
        border-bottom: none;
    }
    .footer {
        background-color: #333333;
        color: white;
        padding: 2rem;
        text-align: center;
        margin-top: 3rem;
    }
</style>
"""

# Create the UI
@ui.page('/')
def portfolio_page():
    # Add custom CSS
    ui.html(custom_css)
    
    # Navigation bar
    with ui.header().classes('navbar'):
        with ui.row().classes('container items-center justify-between'):
            ui.label(ml_engineer['name']).classes('text-xl font-bold')
            with ui.row():
                ui.link('About', '#about').classes('nav-link mx-2')
                ui.link('Skills', '#skills').classes('nav-link mx-2')
                ui.link('Projects', '#projects').classes('nav-link mx-2')
                ui.link('Experience', '#experience').classes('nav-link mx-2')
                ui.link('Education', '#education').classes('nav-link mx-2')
                ui.link('Contact', '#contact').classes('nav-link mx-2')
    
    # Main content
    with ui.column().classes('container'):
        # Hero section
        with ui.row().classes('hero-section w-full items-center') as hero:
            hero.style('background-image: url("/assets/hero-bg.jpg"); background-size: cover;')
            with ui.column().classes('w-1/3 items-center'):
                try:
                    ui.image(ml_engineer['profile_pic']).classes('profile-pic w-48 h-48 object-cover')
                except:
                    # Fallback if image is not available
                    with ui.element('div').classes('profile-pic w-48 h-48 flex items-center justify-center bg-blue-100'):
                        ui.icon('person', size='5em').classes('text-blue-500')
            
            with ui.column().classes('w-2/3 ml-8'):
                ui.label(ml_engineer['name']).classes('text-4xl font-bold mb-2')
                ui.label(ml_engineer['title']).classes('text-2xl mb-4')
                ui.label(ml_engineer['bio']).classes('text-lg')
                with ui.row().classes('mt-4'):
                    ui.link(target=ml_engineer['github'], new_tab=True).classes('social-icon').style('text-decoration: none;').tooltip('GitHub'):
                        ui.icon('code')
                    ui.link(target=ml_engineer['linkedin'], new_tab=True).classes('social-icon').style('text-decoration: none;').tooltip('LinkedIn'):
                        ui.icon('link')
                    ui.link(f'mailto:{ml_engineer["email"]}').classes('social-icon').style('text-decoration: none;').tooltip('Email'):
                        ui.icon('email')
        
        # About section
        with ui.column().classes('section') as about:
            about.props('id=about')
            ui.label('About Me').classes('section-title text-2xl')
            ui.label(ml_engineer['bio']).classes('text-lg')
        
        # Skills section
        with ui.column().classes('section') as skills:
            skills.props('id=skills')
            ui.label('Skills').classes('section-title text-2xl')
            with ui.grid(columns=2).classes('w-full gap-4'):
                for skill, proficiency in ml_engineer['skills'].items():
                    with ui.column().classes('mb-2'):
                        with ui.row().classes('justify-between w-full'):
                            ui.label(skill).classes('font-medium')
                            ui.label(f'{proficiency}%').classes('text-sm text-gray-600')
                        with ui.element('div').classes('skill-bar w-full'):
                            ui.element('div').classes('skill-progress').style(f'width: {proficiency}%')
        
        # Projects section
        with ui.column().classes('section') as projects:
            projects.props('id=projects')
            ui.label('Projects').classes('section-title text-2xl')
            with ui.grid(columns=2).classes('w-full gap-6'):
                for project in ml_engineer['projects']:
                    with ui.card().classes('project-card w-full'):
                        try:
                            ui.image(project['image']).classes('w-full h-48 object-cover')
                        except:
                            # Fallback if image is not available
                            with ui.element('div').classes('w-full h-48 flex items-center justify-center bg-blue-100'):
                                ui.icon('code', size='3em').classes('text-blue-500')
                        
                        with ui.card_section():
                            ui.label(project['title']).classes('text-xl font-bold mb-2')
                            ui.label(project['description']).classes('mb-3 text-gray-700')
                            
                            with ui.row().classes('flex-wrap mb-3'):
                                for tech in project['technologies']:
                                    ui.label(tech).classes('tech-tag')
                            
                            ui.link('View on GitHub', project['github_link'], new_tab=True).classes('text-blue-600 hover:text-blue-800')
        
        # Experience section
        with ui.column().classes('section') as experience:
            experience.props('id=experience')
            ui.label('Experience').classes('section-title text-2xl')
            for job in ml_engineer['experience']:
                with ui.column().classes('experience-item'):
                    with ui.row().classes('justify-between items-center'):
                        ui.label(job['role']).classes('text-xl font-bold')
                        ui.label(job['period']).classes('text-gray-600')
                    ui.label(job['company']).classes('text-lg text-blue-600 mb-2')
                    ui.label(job['description']).classes('text-gray-700')
        
        # Education section
        with ui.column().classes('section') as education:
            education.props('id=education')
            ui.label('Education').classes('section-title text-2xl')
            for edu in ml_engineer['education']:
                with ui.column().classes('education-item'):
                    ui.label(edu['degree']).classes('text-xl font-bold')
                    with ui.row().classes('justify-between items-center'):
                        ui.label(edu['institution']).classes('text-lg text-blue-600')
                        ui.label(edu['year']).classes('text-gray-600')
        
        # Certifications section
        with ui.column().classes('section'):
            ui.label('Certifications').classes('section-title text-2xl')
            with ui.column().classes('mt-2'):
                for cert in ml_engineer['certifications']:
                    with ui.row().classes('mb-2 items-center'):
                        ui.icon('verified', color=colors['accent']).classes('mr-2')
                        ui.label(cert)
        
        # Contact section
        with ui.column().classes('section') as contact:
            contact.props('id=contact')
            ui.label('Contact Me').classes('section-title text-2xl')
            ui.label('Feel free to reach out for collaboration or opportunities.').classes('mb-4')
            
            with ui.row().classes('items-center mb-3'):
                ui.icon('email', color=colors['primary']).classes('mr-2')
                ui.link(ml_engineer['email'], f'mailto:{ml_engineer["email"]}').classes('text-blue-600')
            
            with ui.row().classes('items-center mb-3'):
                ui.icon('link', color=colors['primary']).classes('mr-2')
                ui.link('LinkedIn Profile', ml_engineer['linkedin'], new_tab=True).classes('text-blue-600')
            
            with ui.row().classes('items-center mb-3'):
                ui.icon('code', color=colors['primary']).classes('mr-2')
                ui.link('GitHub Profile', ml_engineer['github'], new_tab=True).classes('text-blue-600')
            
            # Simple contact form
            ui.label('Send me a message:').classes('text-lg font-medium mt-4 mb-2')
            with ui.column().classes('w-full gap-4'):
                name_input = ui.input('Your Name').classes('w-full')
                email_input = ui.input('Your Email').classes('w-full')
                message_input = ui.textarea('Your Message').classes('w-full')
                
                def send_message():
                    if name_input.value and email_input.value and message_input.value:
                        ui.notify('Message sent successfully! (Demo only - no actual email sent)', type='positive')
                        name_input.value = ''
                        email_input.value = ''
                        message_input.value = ''
                    else:
                        ui.notify('Please fill in all fields', type='negative')
                
                ui.button('Send Message', on_click=send_message).classes('bg-blue-600 text-white')
        
        # Footer
        with ui.element('footer').classes('footer w-full'):
            ui.label(f'© {2023} {ml_engineer["name"]} | ML Engineer Portfolio').classes('mb-2')
            ui.label('Built with NiceGUI and Python').classes('text-sm text-gray-400')

# Create assets directory if it doesn't exist
os.makedirs('assets', exist_ok=True)

# Run the app
if __name__ == '__main__':
    ui.run(title=f"{ml_engineer['name']} - ML Engineer Portfolio", favicon='🤖', port=8080)