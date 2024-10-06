from google.cloud import aiplatform


aiplatform.init(project='your-google-cloud-project-id', location='us-central1')


def generate_review(prompt):
    model = aiplatform.TextGenerationModel(model_name="text-bison")
    response = model.predict(
        content=prompt,
        temperature=0.7, 
        max_output_tokens=150 
    )
    return response.text


prompts = [
    "Write a short review for the product 'Vitamin D3 Supplement' in the category of 'Vitamins'. Make it positive and mention how it improved energy levels.",
    "Write a medium review for 'Magnesium Capsules' in the 'Supplements' category with a rating of 3. Mention average results and neutral feedback.",
    "Write a long review for 'Omega 3 Fish Oil' with a rating of 2. The review should highlight issues with taste and packaging. Make it critical.",
    "Write a short review for 'Calcium with Vitamin D'. Mention how easy the tablets were to take and how it improved health. Make it positive.",
    "Write a medium review for 'Herbal Vitamin C' mentioning the strong taste and moderate results. Make it neutral.",
    "Write a medium review for 'Multivitamin Gummies' with a rating of 5. Mention the taste and how it helped with energy levels.",
    "Write a medium review for 'Zinc Tablets'. Mention improvements in immunity but mention difficulty swallowing the tablets.",
    "Write a long review for 'Fish Oil Omega 3'. Mention benefits for joint pain but critique the taste.",
    "Write a short review for 'Vitamin B12 Supplement'. Mention increased energy levels. Make it positive.",
    "Write a medium review for 'Probiotic Capsules'. Mention how it helped digestion but state that results were moderate.",
    "Write a medium review for 'Iron Supplement'. Mention improvements in energy but some stomach discomfort.",
    "Write a short review for 'Elderberry Syrup'. Mention taste and immunity benefits. Make it positive.",
    "Write a short review for 'Glucosamine Chondroitin'. Mention joint pain relief. Make it positive.",
    "Write a medium review for 'Turmeric Curcumin'. Mention reduction in inflammation and knee pain. Make it positive.",
    "Write a short review for 'Vitamin K2 with D3'. Mention bone health improvements. Make it positive.",
    "Write a medium review for 'Collagen Peptides'. Mention skin hydration and ease of use in drinks.",
    "Write a short review for 'Biotin Hair Growth'. Mention stronger hair and nails. Make it positive.",
    "Write a medium review for 'Ashwagandha Capsules'. Mention reduced stress and improved focus. Make it positive.",
    "Write a medium review for 'Magnesium Glycinate'. Mention improved sleep quality. Make it positive.",
    "Write a short review for 'Vitamin C Gummies'. Mention immunity boost and great taste. Make it positive."
]

generated_reviews = []
for prompt in prompts:
    review = generate_review(prompt)
    generated_reviews.append(review)

import pandas as pd

data = {
    'Product Name': [
        'Vitamin D3 Supplement', 'Magnesium Capsules', 'Omega 3 Fish Oil', 'Calcium with Vitamin D', 'Herbal Vitamin C',
        'Multivitamin Gummies', 'Zinc Tablets', 'Fish Oil Omega 3', 'Vitamin B12 Supplement', 'Probiotic Capsules',
        'Iron Supplement', 'Elderberry Syrup', 'Glucosamine Chondroitin', 'Turmeric Curcumin', 'Vitamin K2 with D3',
        'Collagen Peptides', 'Biotin Hair Growth', 'Ashwagandha Capsules', 'Magnesium Glycinate', 'Vitamin C Gummies'
    ],
    'Generated Review': generated_reviews,
    'Rating': [5, 3, 2, 4, 3, 5, 4, 3, 5, 4, 4, 5, 5, 5, 4, 4, 5, 5, 4, 5],
    'Review Length': ['Short', 'Medium', 'Long', 'Short', 'Medium', 'Medium', 'Medium', 'Long', 'Short', 'Medium', 
                     'Medium', 'Short', 'Short', 'Medium', 'Short', 'Medium', 'Short', 'Medium', 'Medium', 'Short']
}

reviews_df = pd.DataFrame(data)
reviews_df.to_csv('synthetic_reviews_assignment.csv', index=False)

reviews_df
