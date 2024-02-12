from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import JsonResponse
import json
from django.shortcuts import render
from .utils import calculate_learning_rate_from_survey
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
#from django.shortcuts import render



@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        # Extract the fields from the parsed data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
       
        
        # Validate the credentials or perform any additional checks
        
        # Create a new user profile
        #print(username)
        user_profile = UserProfile(username=username,email_id=email, password=password)
        user_profile.save()
        '''user_profile = User(username=username, email=email_id)
        user_profile.set_password(password)
        user_profile.save()
        '''
        emailuser = {
                    
                    'email_id': user_profile.email_id
                    
                }
        # Return a JSON response indicating successful signup
        #return JsonResponse({'message': 'Signup successful'})
        return JsonResponse({'message': 'Signup successful',"emailuser":emailuser}, status=201)
    # Return an error response for unsupported request methods or render a form for GET requests
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user_profiles = UserProfile.objects.filter(username=username, password=password)

        if user_profiles.exists():
            if user_profiles.count() == 1:
                user_profile = user_profiles.first()
                userlist = {
                    'username': user_profile.username,
                    'email_id': user_profile.email_id,
                    'phone_number': user_profile.phone_number,
                    'name': user_profile.name,
                }
                return JsonResponse({'message': 'Login successful', 'userlist': userlist})
            else:
                # Handle the case when multiple user profiles are found
                return JsonResponse({'error': 'Multiple user profiles found'}, status=500)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

# def Profile(request):
#     # Retrieve user data from the session
#     # phone_number = request.session.get('phone_number')
#     # username = request.session.get('username')
#     # email_id = request.session.get('email_id')
#     # name = request.session.get('name')

#     # # Check if the session key is None and save the session
#     # session_key = request.session.session_key
#     # if session_key is None:
#     #     request.session.save()
#     #     session_key = request.session.session_key
#     #     print(session_key)

#     # Retrieve any other user details stored in the session
#     user_data = {
#         'username': username,
#         'email': email_id,
#         'name': name,
#     }
    
#     return JsonResponse(user_data)

    # return render(request, 'LandingBeforeLogin.html')
'''
def Contact(request):
    return render(request, 'Contact.html')

def Dashboard(request):
    return render(request, 'Dashboard.html')

'''



def index(request):
    return render(request, 'react/index.html')


#@csrf_exempt
'''
def Signup(request):
    if request.method == 'POST':
        
        
        username = request.POST.get('username')
        email_id = request.POST['email_id']
        password = request.POST.get('password')
        
        # Validate the credentials or perform any additional checks
        
        # Create a new user profile
        #user_profile = UserProfile.objects.create(username=username, password=password)
        user_profile = UserProfile(username=username,email_id=email_id, password=password)
        user_profile.save()
        
        # Redirect the user to the landing page or any other desired page
        
        return render(request,'LandingAfterLogin.html')
        return redirect('LandingAfterLogin')
    
    return render(request, 'Signup.html')






def LandingBeforeLogin(request):
    # Handle the landing page logic here
    return render(request, 'LandingBeforeLogin.html')
''''''
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect(reverse('landingpage'))
        else:
            # Invalid credentials, handle the error or display a message
            
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})

            pass
    return render(request, 'login.html')

'''
'''
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_profiles = UserProfile.objects.all()
        
        
        for user_profile in user_profiles:
            un = user_profile.username
            pd = user_profile.password
            
            print(pd)
            if un == username and pd == password:
                
                
                request.session['username'] = user_profile.username
                request.session['email_id'] = user_profile.email_id 
                request.session['phone_number'] = user_profile.phone_number
                request.session['name'] = user_profile.name
                return redirect('LandingAfterLogin')
        
        #error_message = 'Invalid username or password.'
        messages.error(request, 'Invalid username or password.')
        return render(request, 'Login.html')   
    return render(request, 'Login.html')

def LandingAfterLogin(request):
    return render(request, 'LandingAfterLogin.html')

def Profile(request):
    return render(request, 'Profile.html')

def About(request):
    return render(request, 'About.html')

def Courses(request):
    return render(request, 'Courses.html')

def Cppcourse(request):
    return render(request, 'Cppcourse.html')

def Javacourse(request):
    return render(request, 'Javacourse.html')

def Pythoncourse(request):
    return render(request, 'Pythoncourse.html')
    ''' 
'''def Profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'Profile': user_profile}
    return render(request, 'Profile.html', context)
'''




# def submit_survey(request):
#     if request.method == 'POST':
#         # Access the form data sent from the React app
#         form_data = request.POST

#         # Process the form data as needed
#         # ...

#         # Return a JSON response if desired
#         return JsonResponse({'message': 'Survey submitted successfully'})

#     # Handle GET requests or other HTTP methods if needed
#     return JsonResponse({'message': 'Method not allowed'}, status=405)


@csrf_exempt
def submit_survey(request):
    if request.method == 'POST':
        # Retrieve the survey responses from the request payload
        try:
            form_data = json.loads(request.body)
            print(form_data)
            email = form_data.get('email')  # Retrieve the email from the form data
            print(email)            # Access the form data using the appropriate keys
            knowledge_level = form_data.get('knowledgeLevel')
            motivation = form_data.get('motivation')
            weekly_time = form_data.get('weeklyTime')
            prior_knowledge = form_data.get('priorKnowledge')
            self_paced_learning = form_data.get('selfPacedLearning')
            learning_style = form_data.get('learningStyle')
            approach_challenges = form_data.get('approachChallenges')
            comfortable_online_learning = form_data.get('comfortableOnlineLearning')
            pace_of_learning = form_data.get('paceOfLearning')
            long_term_goals = form_data.get('longTermGoals')
            # Perform the calculation to determine the learning rate based on the survey responses
            learning_rate = calculate_learning_rate_from_survey(form_data)
            print(learning_rate)
            # Update the user's profile with the learning rate if needed
            # Retrieve the user's profile based on the email ID
            user_profile = UserProfile.objects.get(email_id=email)
            #print(user_profile.email_id)
            user_profile.learningRate = learning_rate
            user_profile.save()

            # Return the learning rate in the API response
            return JsonResponse({'learningRate': learning_rate})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    # Handle GET requests or other HTTP methods if needed
    return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        # Retrieve the user input from the form
        dataset = pd.read_csv("C:\\Users\\HP\\OneDrive\\Desktop\\django-reactapp\\copy.csv")

        # Encode the 'Difficulty' column
        difficulty_encoder = LabelEncoder()
        dataset['Difficulty'] = difficulty_encoder.fit_transform(dataset['Difficulty'])

        # Encode the 'Links' column
        links_encoder = LabelEncoder()
        dataset['Link'] = links_encoder.fit_transform(dataset['Link'])

        # Encode the 'Topics' Column
        topics_encoder = LabelEncoder()
        dataset['Topics'] = topics_encoder.fit_transform(dataset['Topics'])

        # Separate the features (Learning Rate, Difficulty, and Topics) and the target (Link)
        X = dataset[['Learning Rate', 'Difficulty', 'Topics']]
        y = dataset['Link']

        # Initialize a logistic regression model
        model = LogisticRegression(max_iter=1000)
        print("hi")
        
        # Train the model
        model.fit(X, y)
        
        # Parse the JSON data from request body
        json_data = json.loads(request.body)
        
        user_difficulty = json_data.get('difficulty')
        user_topic = json_data.get('topic')
        email = json_data.get('email')
        
        #user_profile = UserProfile.objects.get(email_id=email)
        user_learning_rate = 8#user_profile.learningRate
        print(user_learning_rate, user_topic, user_difficulty)
        
        # Encode the user difficulty and topic input
        if user_topic not in topics_encoder.classes_:
            error_message = "Unseen topic. Please choose a different topic."
            return JsonResponse({'error_message': error_message})
        else:
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
                error_message = "No matching links found."
                return JsonResponse({'error_message': error_message})
            else:
                # Get the maximum of 3 links or all available links
                num_links = min(3, len(filtered_dataset))

                # Decode the predicted links and convert to list
                predicted_links = links_encoder.inverse_transform(filtered_dataset['Link']).tolist()
                if num_links == 1:
                    print("Predicted Link:")
                    print(predicted_links[0])
                else:
                    print("Predicted Links:")
                for link in predicted_links[:num_links]:
                    print(link)
                print("hi")    
                return JsonResponse({'predicted_links': predicted_links[:num_links]})
   
    return JsonResponse({})
