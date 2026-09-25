import json

YTfile = "youtube videos detail.txt"


def load_data():

    try:
        with open(YTfile, "r") as file:
            print_json = json.load(file)
            return print_json
    except FileNotFoundError:
        return []


def save_helper(videos):

    with open(YTfile, "w") as file:
        json.dump(videos, file)


def list_all_Videos(videos):

    print("\n")
    print("*"* 90)

    for index , vide in enumerate(videos, start=1):
        # index += 1
        print(f"{index}, Video name | {vide.get('Name')}.\n\tVideo time | {vide.get('Time')}\n")

    print("*" *90)

def add_video(videos):

    video_name = input("Enter video name : ")
    video_time = input("Enter video time : ")
    videos.append({'Name': video_name, 'Time': video_time})
    save_helper(videos)


def update_details_videos(videos):
    list_all_Videos(videos)
    index = int(input("You selected “Update Video.” Can you tell me which video number you want to update? : "))

    if 1 <= index <= len(videos):
        name = input("Enter the update video name : ")
        time = input("Enter the update video time : ")
        Iindex = videos[index-1]
        Iindex['Name'] = name
        Iindex['Time'] = time
        save_helper(videos)
        print("*"* 90)

    else:
        print("Invaled Prompt")

def delete_video(videos):
    list_all_Videos(videos)
    index = int(input("You selected “Delete Video.” Can you tell me which video number you want to delete? : "))

    if 1 <= index <= len(videos):
        
        del videos[index - 1]
        save_helper(videos)
        print("Sucessefully completed.")
        print("*"* 90)
    
    else:
        print("Invaled Prompt")

