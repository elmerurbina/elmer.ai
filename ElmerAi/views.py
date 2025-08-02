from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

def index(request):
    context = {
        'projects': [
            {
                'title': _("Freud IA"),
                'desc': _("An AI-driven assistant for mental health, utilizing AI agents to manage different psychological problems and offer tailored support."),
                'image': "img/freudia.png",
            },
            {
                'title': _("SignBridge"),
                'desc': _("A computer vision project enabling communication through American Sign Language (ASL). It transcribes speech to signs and interprets signs to text in real-time."),
                'image': "img/signbrigde.jpeg",
            },
            {
                'title': _("HatoMaster"),
                'desc': _("A web system for Nicaraguan cattle ranchers. Features inventory, sales, accounting reports, and analytics dashboards."),
                'image': "img/hatomaster.png",
            },
            {
                'title': _("StockFlow"),
                'desc': _("A tool for real-time stock analysis and inventory management, developed collaboratively with a team."),
                'image': "img/stockflow.png",
            },
            {
                'title': _("Data Analysis Project"),
                'desc': _("An open-source project for statistical analysis, providing tools for solving specific statistical problems."),
                'image': "img/dataanalysis.png",
            },
        ],
        'achievements': [
            _("🥇 First Place – Rally Nacional de Innovación 2025 with EchoNic"),
            _("🥇 First Place – Rally Nacional 2024 with EcoNic"),
            _("🥇 First Place – Innovation UNI 2024"),
            _("🥉 Third Place – Rally Latinoamericano 2024"),
            _("🥈 Second Place – Feria de Ciencia y Tecnología 2023"),
        ],
    }
    return render(request, 'index.html', context)
