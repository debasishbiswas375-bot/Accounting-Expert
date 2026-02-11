# mysite/settings.py

INSTALLED_APPS = [
    'jazzmin',  # MUST be above django.contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'converter',
]

# Jazzmin UI Customization
JAZZMIN_SETTINGS = {
    "site_title": "Accounting Expert Admin",
    "site_header": "Accounting Expert",
    "site_brand": "Accounting Expert Portal",
    "welcome_sign": "Welcome to the Accounting Expert Admin Portal",
    "copyright": "Accounting Expert Ltd",
    "search_model": ["auth.User", "auth.Group"],
    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # UI Customizer
    "show_ui_builder": False, # Set to True to play with colors in real-time
}

# Optional: Dark mode/Blue theme preset
JAZZMIN_UI_TWEAKS = {
    "theme": "flatly", # Professional blue theme
    "dark_mode_theme": "darkly",
}
