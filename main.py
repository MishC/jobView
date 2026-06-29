from services.api import get_feed

if __name__ == "__main__":
    data = get_feed()
    for item in data['items']:
        if item["_feed_entry"]["municipal"] == "BERGEN":
            print(item)
        