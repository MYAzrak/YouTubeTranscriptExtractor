# Modules imported
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs


# Functions defined
def extract_transcript(youtube_url):
    try:
        # Parse the YouTube video ID from the URL
        parsed_url = urlparse(youtube_url)
        video_id = parse_qs(parsed_url.query).get("v")

        if not video_id:
            return "Invalid YouTube URL."

        video_id = video_id[0]

        # Get the transcript for the video
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Format the transcript
        formatted_transcript = ""
        for entry in transcript:
            formatted_transcript += f"{entry['start']:.2f} - {entry['text']}\n"

        return formatted_transcript

    except Exception as e:
        return f"Error: {str(e)}"


def format_transcript(transcript):
    new_text = []

    try:
        # Filter out non-characters
        for char in transcript:
            if char.isnumeric() or char == ":" or char == "." or char == "-":
                continue
            else:
                new_text.append(char)

        # Join the list back into a string
        new_text = "".join(new_text)

        # Write the cleaned text to a text file
        with open("transcript.txt", mode="w", encoding="utf-8") as file:
            file.write(new_text)
        print("Text has been written to output.txt")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    youtube_url = input("Enter YouTube URL: ")
    transcript = extract_transcript(youtube_url)
    format_transcript(transcript)


# Starting point
if __name__ == "__main__":
    main()
