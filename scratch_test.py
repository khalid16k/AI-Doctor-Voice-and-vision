from brain_of_the_doctor import analyze_image_with_query, encode_image
import os

system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""

def main():
    encoded = encode_image("dandruff-optimized.webp")
    response = analyze_image_with_query(
        query=system_prompt + "\nhey doctor could you please check what's wrong with my scalp",
        model="qwen/qwen3.6-27b",
        encoded_image=encoded
    )
    print("--- RESPONSE ---")
    print(response)
    print("----------------")

if __name__ == "__main__":
    main()
