try:
    import youtube_channel_transcript_api as ycta
except ImportError:
    print(f"Error, Module required! try: pip install youtube_channel_transcript_api")
import json

def main():    
    channel = input("enter youtube channel id  (@mychannel): ")
    yt_API = input("enter youtube API key: ")
    channel_get = ycta.YoutubeChannelTranscripts(channel, yt_API)

    nf = channel_get.get_transcripts()
    nf_data, nf_errors = nf
    len_nf_data = len(nf_data)
    print(f'Fenton Raw:{len_nf_data}')
    ###f = open('nf.txt','w')

    filter_string = input("Enter filter text: ")
    # Filter nodes that contain the filter_string
    filtered_data = {
        key: value
        for key, value in nf_data.items()
        if any(filter_string  in caption["text"] for caption in value["captions"])
    }
    len_nf_f_data = len(filtered_data)
    channel_name = re.sub('\W+','', f'{channel}_{filter_string}')
    with open(f'{channel_name}_filtered.json', 'w') as fp:
        json.dump(filtered_data, fp, indent=4)
    print(f'Fenton Filtered:{len_nf_f_data}')

if __name__ == "__main__":
    main()
