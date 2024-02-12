import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Load the dataset
dataset = pd.read_csv(r'D:\gpt\copy.csv')

# Encode the 'Difficulty' column
difficulty_encoder = LabelEncoder()
dataset['Difficulty'] = difficulty_encoder.fit_transform(dataset['Difficulty'])

# Encode the 'Links' column
links_encoder = LabelEncoder()
dataset['Link'] = links_encoder.fit_transform(dataset['Link'])

# Encode the 'Topics' Column
topics_encoder=LabelEncoder()
dataset['Topics'] = topics_encoder.fit_transform(dataset['Topics'])

# Separate the features (Learning Rate and Difficulty) and the target (Link)
X = dataset[['Learning Rate', 'Difficulty', 'Topics']]
y = dataset['Link']

# Initialize a logistic regression model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X, y)

# Take user input for learning rate and difficulty
user_learning_rate = int(input("Enter your learning rate: "))
user_difficulty = input("Enter the difficulty level: ")
user_topic = input("Enter the topic: ")

# Encode the user difficulty and topic input
if user_topic not in topics_encoder.classes_:
    print("Unseen topic. Please choose a different topic.")
else:
    # Encode the user difficulty and topic input
    user_difficulty_encoded = difficulty_encoder.transform([user_difficulty])
    user_topic_encoded = topics_encoder.transform([user_topic])

    # Predict the probabilities of each link based on user input
    filtered_dataset = dataset[
    (dataset['Learning Rate'] == user_learning_rate) &
    (dataset['Difficulty'] == user_difficulty_encoded[0]) &
    (dataset['Topics'] == user_topic_encoded[0])
    ]

    # Check if any matching links are found
    if len(filtered_dataset) == 0:
        print("No matching links found.")
    else:
        # Get the maximum of 3 links or all available links
        num_links = min(3, len(filtered_dataset))

        # Decode and print the links
        predicted_links = links_encoder.inverse_transform(filtered_dataset['Link'])
        if num_links == 1:
            print("Predicted Link:")
            print(predicted_links[0])
        else:
            print("Predicted Links:")
            for link in predicted_links[:num_links]:
                print(link)