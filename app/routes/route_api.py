from src import Characters, Comics, Creators, Stories, Events, Series
from flask import Flask, jsonify
import time
from main import app

@app.route('/characters')
def characters():
    start_time = time.time()
    characters = Characters()
    characters.get_all_api()
    print(f'Length: {characters.len_character_list}')
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\n\n\nRuntime: {execution_time:.4f} seg\n\n\n")
    return jsonify(characters.character_list)

@app.route('/comics')
def comics():
    start_time = time.time()
    comics = Comics()
    comics.get_all_api()
    print(f'Length: {comics.len_comics_list}')
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\n\n\nRuntime: {execution_time:.4f} seg\n\n\n")
    return jsonify(comics.comics_list)

@app.route('/creators')
def creators():
    start_time = time.time()
    creators = Creators()
    creators.get_all_api()
    print(f'Length: {creators.len_creators_list}')
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\n\n\nRuntime: {execution_time:.4f} seg\n\n\n")
    return jsonify(creators.creators_list)

@app.route('/stories')
def stories():
    start_time = time.time()
    stories = Stories()
    stories.get_all_api()
    print(f'Length: {stories.len_stories_list}')
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\n\n\nRuntime: {execution_time:.4f} seg\n\n\n")
    return jsonify(stories.stories_list)

@app.route('/series')
def series():
    start_time = time.time()
    series = Series()
    series.get_all_api()
    print(f'Length: {series.len_series_list}')
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\n\n\nRuntime: {execution_time:.4f} seg\n\n\n")
    return jsonify(series.series_list)


@app.route('/events')
def events():
    start_time = time.time()
    events = Events()
    events.get_all_api()
    print(f'Length: {events.len_events_list}')
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\n\n\nRuntime: {execution_time:.4f} seg\n\n\n")
    return jsonify(events.events_list)