#!/usr/bin/env python3
"""Generate hero image for personal branding article using Runware AI."""
import os, sys, json, base64, requests

API_KEY = os.environ.get('RUNWARE_API_KEY')
if not API_KEY:
    print("ERROR: RUNWARE_API_KEY not set")
    sys.exit(1)

SLUG = "ai-personal-branding-pemilik-ukm"
OUTPUT = f"/home/wahyu/.hermes/workspace/maswahyu-blog/src/assets/hero-{SLUG}.jpg"

prompt = (
    "stickman character in warm orange suit standing confidently on a podium, "
    "minimal flat design, simple cartoon, clean white background, "
    "holding a megaphone with social media icons around, "
    "warm orange and brown color palette, no face details, silhouette style"
)
negative = "realistic, photorealistic, face details, woman, portrait, eyes, nose, mouth, text, watermark"

payload = {
    "taskType": "imageInference",
    "taskUUID": "hero-pb-ukm-001",
    "positivePrompt": prompt,
    "negativePrompt": negative,
    "model": "runware:100@cfQaBEaLSDMsXGZHbjKV",
    "CFGScale": 7,
    "steps": 20,
    "width": 1024,
    "height": 576,
    "outputFormat": "JPEG",
    "scheduler": "FlowMatchEulerDiscreteScheduler"
}

try:
    resp = requests.post(
        "https://api.runware.ai/v1",
        headers={"Content-Type": "application/json"},
        json=[payload],
        timeout=120
    )
    data = resp.json()
    if resp.status_code != 200:
        print(f"API error {resp.status_code}: {resp.text[:500]}")
        sys.exit(1)
    # Find the image data in response
    for item in data.get('data', []):
        if 'imageURL' in item:
            img_url = item['imageURL']
            print(f"Downloading from: {img_url}")
            img_resp = requests.get(img_url, timeout=60)
            with open(OUTPUT, 'wb') as f:
                f.write(img_resp.content)
            print(f"Saved to: {OUTPUT} ({len(img_resp.content)} bytes)")
            sys.exit(0)
    # Try alternate format
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and 'imageURL' in item:
                img_url = item['imageURL']
                print(f"Downloading from (list): {img_url}")
                img_resp = requests.get(img_url, timeout=60)
                with open(OUTPUT, 'wb') as f:
                    f.write(img_resp.content)
                print(f"Saved to: {OUTPUT} ({len(img_resp.content)} bytes)")
                sys.exit(0)
    print(f"Unexpected response: {json.dumps(data, indent=2)[:500]}")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
