from pathlib import Path


def project():
    return Path(__file__).parent  # Находит путь где лежит проект


def resources():
    return str(project().joinpath(f'resources/'))  # от проекта находит путь где лежит папка resources/
