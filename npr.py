def get_npr_data():
    import feedparser
    import pandas as pd
    from dateutil import parser

    # URL of the RSS feed
    rss_url = "https://feeds.npr.org/1001/rss.xml"  # Replace with the actual RSS feed URL

    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    # Initialize an empty list to store the extracted data
    data = []

    # Iterate through each entry in the feed
    for entry in feed.entries:
        # Extract the required fields
        publish_date = parser.parse(entry.published)  # Convert the publish date to a datetime object
        title = entry.title
        description = entry.description
        link = entry.link

        # Append the extracted data to the list
        data.append({
            "publish date": publish_date,
            "title": title,
            "description": description,
            "link": link
        })

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data)

    # Sort the DataFrame by publish date in descending order and get the top 5 rows
    df = df.sort_values(by='publish date', ascending=False).head(5)

    return df