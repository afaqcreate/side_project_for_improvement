from logic import *

def main():
    while True:
        print('''
YouTube Manager | Select an option
    1. List all videos
    2. Add a YouTube video
    3. Update YouTube video details
    4. Delete a YouTube video
    5. Exit the app''')
        choice = input('\nEnter a number : ')

        videos = load_data()

        match choice:
            case '1':
                list_all_Videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_details_videos(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("-"* 80)
                print("Please Enter Given options Numbers")
                print("-"* 80)

if __name__ == "__main__":
    main()