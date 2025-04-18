import base64
import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="")  # Replace with your actual key

# List of local image paths
image_paths = [
    "/Users/ellenhart/Desktop/University of Richmond/Research AI/image1.png"
]

# Loop through each image
for image_path in image_paths:
    if not os.path.exists(image_path):
        print(f"Image not found: {image_path}")
        continue

    # Guess the image type from the file extension
    ext = image_path.split('.')[-1].lower()
    mime_type = "image/png" if ext == "png" else "image/jpeg"

    # Read and encode the image
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

    # Try sending request to OpenAI
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": " Is this graph accessible to people with visual impairments or color blindness? What improvements could be made to ensure the data is more inclusive and easier to interpret for all users?"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:{mime_type};base64,{encoded_image}",
                            },
                        },
                    ],
                }
            ],
        )

        print(f"\n Analysis for: {image_path}")
        print(response.choices[0].message.content)

    except Exception as e:
        print(f"Error analyzing {image_path}: {e}")
        
        # Use fake response as fallback
        fake_response = {
            "choices": [
                {
                    "message": {
                        "content": "[Mocked] This is a placeholder description of the image."
                    }
                }
            ]
        }

        print(f"\nFallback analysis for: {image_path}")
        print(fake_response["choices"][0]["message"]["content"])

    print("-" * 60)
