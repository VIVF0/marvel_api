from src import Characters, Comics, Creators, Stories, Events, Series
from flask import Flask
import time
import json 
from main import app

@app.route('/characters_json')
def characters_json():
    start_time = time.time()
    characters = Characters()
    characters.get_all_api()
    print(f'Length: {characters.len_character_list}')
    json_object = json.dumps(characters.character_list, indent = 4) 
    with open("characters.json", "w") as outfile: 
        outfile.write(json_object) 
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\n\n\nRuntime: {execution_time:.4f} seg\n\n\n")
    return 'Gerado'

@app.route('/comics_json')
def comics_json():
    start_time = time.time()
    comics = Comics()
    comics.get_all_api()
    print(f'Length: {comics.len_comics_list}')
    json_object = json.dumps(comics.comics_list, indent = 4) 
    with open("comics.json", "w") as outfile: 
        outfile.write(json_object) 
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\n\n\nRuntime: {execution_time:.4f} seg\n\n\n")
    return 'Gerado'

@app.route('/creators_json')
def creators_json():
    start_time = time.time()
    creators = Creators()
    creators.get_all_api()
    print(f'Length: {creators.len_creators_list}')
    json_object = json.dumps(creators.creators_list, indent = 4) 
    with open("creators.json", "w") as outfile: 
        outfile.write(json_object) 
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\n\n\nRuntime: {execution_time:.4f} seg\n\n\n")
    return 'Gerado'

@app.route('/stories_json')
def stories_json():
    start_time = time.time()
    stories = Stories()
    stories.get_all_api()
    print(f'Length: {stories.len_stories_list}')
    json_object = json.dumps(stories.stories_list, indent = 4) 
    with open("stories.json", "w") as outfile: 
        outfile.write(json_object) 
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\n\n\nRuntime: {execution_time:.4f} seg\n\n\n")
    return 'Gerado'

@app.route('/series_json')
def series_json():
    start_time = time.time()
    series = Series()
    series.get_all_api()
    print(f'Length: {series.len_series_list}')
    json_object = json.dumps(series.series_list, indent = 4) 
    with open("series.json", "w") as outfile: 
        outfile.write(json_object) 
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\n\n\nRuntime: {execution_time:.4f} seg\n\n\n")
    return 'Gerado'

@app.route('/events_json')
def events_json():
    start_time = time.time()
    events = Events()
    events.get_all_api()
    print(f'Length: {events.len_events_list}')
    json_object = json.dumps(events.events_list, indent = 4) 
    with open("events.json", "w") as outfile: 
        outfile.write(json_object) 
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\n\n\nRuntime: {execution_time:.4f} seg\n\n\n")
    return 'Gerado'