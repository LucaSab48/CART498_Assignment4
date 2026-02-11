# Lynch's Dream Machine

For assignment 4, we were tasked with creating a live website that has a chatbot where users can enter their dreams and the bot will interpret the dream using Jungian psychology and an image would generate depicting the inputted dream. We were also tasked with making the website more navigable for the user. For the framework, I am using Flask as backend to handle routing, user input processing, and template rendering. For the server, I am using the free version of Render to host the site and I am using OpenAI's API model GPT-4.1 and gpt-image-1. 
I decided for my website to make it David Lynch themed because I consider him the master of creating dreamscapes and utilizing dream logic in his films. He is my favourite director of all time and I found that this assignment could be a great way to pay homage to him. 
To implement this theme, I decided to modify the image generation prompt to be inspired by the works of David Lynch, and I made the text generation prompt seem like a Jungian psychologist trapped in a David Lynch dream. I ran into difficulties with the image generation because of OpenAI's safety guidelines. Since Lynch's work is scary and unsettling, I had to modify the prompt to avoid an error 401 (safety guideline issue). I had to implement a third prompt that modifies the users inputted dream into key symbols and atmosphere in a neutral tone. This seemed to work very well. I think my favourite part of this assignment is the Jungian-Lynchian interpretations of the dreams. Instead of a clinical interpretation, the output is a poetic ambiguous examination of the meaning of the users dream. 

## Jungian Interpretation Strategy

The models interpretive logic is grounded in Jung's analytical psychology, which analyses dreams symbolically rather than treating them as a narrative. The system is guided to focus on archetypal figures, emotional tone, unconscious tensions, and themes related to individuation. This is all achieved through the prompt design to shape its behaviour. Since I am combining Jungian psychology with Lynch's world, I constrained the model to focus on symbolism, ambiguity, and speculative meaning. This was done in an effort to avoid the responses being overly clinical or diagnostic.

## Image Generation Pipeline

As explained before, this application generates images using OpenAI's image model gpt-image-1. A core issue I had was safely translating the user's dream description into a visual prompt. 
Initially, using the user's input as part of the prompt would trigger moderation blocks. So, the solution was to add an intermediary abstraction layer that would extract symbolic cues, mood and setting. 
This step serves multiple purposes:
- Reduced moderation conflicts
- Prevents unsafe imagery
- Preserves conceptual tone

## User Interaction Flow

1. User enters the website
2. The application then prompts the user to write a description (displays example text)
3. User enters a description of their dream. 
4. System generates a Jungian-Lynchian interpretation of that dream. 
5. User's input is abstracted into neutral tone visual cues. 
6. Image model generates a dreamlike representation.
7. Both outputs are displayed below. 

## Technical Reflections

This assignment highlights the importance of prompt design on how it shapes the model. Even small tweaks to the models prompt can change its responses vastly. 
A major technical insight for me is the safety constraints with image generation. Unlike the text based models, the image system requires much more moderation with prompts. Another insight was learning how to attach a github repo to a server. This was much more involved than I thought, but very useful to know. 
For improvements, I would like to spend more time designing the application to be more presentable and fluid, and I would really like to cut down on the time it takes for the application to process a users prompt. 



