import textract



chapter_names = [
    "02_search-fundamentals",
    "03_intelligent-search",
    "04_evolutionary-algorithms",
    "05_advanced-evolutionary-approaches",
    "06_swarm-intelligence_ants",
    "07_swarm-intelligence_particles",
    "08_machine-learning",
    "09_artificial-neural-networks",
    "10_reinforcement-learning-with-q-learning",
]



for chapter in chapter_names:
    path_file = f'/run/media/rafael/rafael03/ebooks/artificial-intelligence/grokking_artificial_intelligence_algorithm/{chapter}.pdf'
    text_bytes = textract.process(path_file)
    text = text_bytes.decode('utf-8')
    with open(f'{chapter}.txt', mode='w', encoding='utf-8', newline='') as file:
        file.write(text)