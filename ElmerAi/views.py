from django.shortcuts import render

def index(request):
    context = {
        'projects': [
            {'title': "Freud IA",
             'desc': "An AI-driven assistant for mental health, utilizing AI agents to manage different psychological problems and offer tailored support."},
            {'title': "StockFlow",
             'desc': "A tool for real-time stock analysis and inventory management, developed collaboratively with a team. This open-source project is customizable for various statistical needs."},
            {'title': "Data Analysis Project",
             'desc': "An open-source project for statistical analysis, focusing on cost research in cattle production, providing tools for solving specific statistical problems."},
        ],
        'achievements': [
            "🥇 First Place – Rally Nacional 2024 with EcoNic",
            "🥇 First Place – Innovation UNI 2024",
            "🥉 Third Place – Rally Latinoamericano 2024",
            "🥈 Second Place – Feria de Ciencia y Tecnología 2023",
        ],
    }
    return render(request, 'index.html', context)
