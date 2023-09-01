try:
    import youtube_transcript_api as yta
except ImportError:
    print(f"Error, Module required! try: pip install youtube_transcript_api")
import json
import re
import ast

def main():    
    videos = input("enter youtube videos id  (['AqwSJ5qYTbI','bh_zToOn7bs']): ")    

    nf = yta.YouTubeTranscriptApi.get_transcripts(ast.literal_eval(videos), languages=['en'])
    nf_data, nf_errors = nf
    len_nf_data = len(nf_data)
    print(f'Raw:{len_nf_data}')
    ###f = open('nf.txt','w')

    filter_string = input("Enter filter text: ")
    # Filter nodes that contain the filter_string
    filtered_data = {
        key: value
        for key, value in nf_data.items()
        if any(filter_string  in caption["text"] for caption in value)
    }
    len_f_data = len(filtered_data)
    channel_name = re.sub('\W+','', f'videos_{filter_string}')
    with open(f'{channel_name}_filtered.json', 'w') as fp:
        json.dump(filtered_data, fp, indent=4)
    print(f'Filtered:{len_f_data}')

if __name__ == "__main__":
    main()
