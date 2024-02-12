def calculate_learning_rate_from_survey(form_data):
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

    # Assign numerical values to the options
    knowledge_level_values = {
        'beginner': 1,
        'intermediate': 2,
        'advanced': 3
    }

    motivation_values = {
        'Personal interest': 1,
        'Career advancement': 2,
        'Academic requirement': 3
    }

    weekly_time_values = {
        'Less than 5 hours': 1,
        '5-10 hours': 2,
        '10-20 hours': 3,
        #'More than 20 hours': 9
    }

    prior_knowledge_values = {
        'Yes': 3,
        'No': 2,
        'little':1
    }

    self_paced_learning_values = {
        'Very comfortable': 3,
        'Somewhat comfortable': 2,
        'Not comfortable': 1
    }

    learning_style_values = {
        'Visual (e.g., diagrams, charts)': 1,
        #'Auditory (e.g., lectures, discussions)': 6,
        'Read/Write (e.g., textbooks, written materials)': 2,
        'Kinesthetic (e.g., hands-on activities, practical, exercises)': 3
    }

    approach_challenges_values = {
        'I persist until I understand them fully.': 3,
        'I seek assistance or additional resources when needed.': 2,
        'I tend to avoid them or lose motivation.': 1
    }

    comfortable_online_learning_values = {
        'Yes, I am very comfortable': 3,
        'I am somewhat comfortable': 2,
        'No, I prefer traditional in-person learning': 1
    }

    pace_of_learning_values = {
        'Fast-paced, with a focus on completing courses quickly': 3,
        'Moderate pace, balancing comprehension and progress': 2,
        'Slow-paced, with a strong emphasis on deep understanding': 1
    }

    long_term_goals_values = {
        'Mastery and expertise': 3,
        'Applying knowledge in practical settings': 1,
        'Exploring new areas and expanding horizons': 2
    }

    # Calculate the learning rate based on the survey responses
    learning_rate = (
        (knowledge_level_values[knowledge_level] +
         motivation_values[motivation] +
         weekly_time_values[weekly_time] +
         prior_knowledge_values[prior_knowledge] +
         self_paced_learning_values[self_paced_learning] +
         learning_style_values[learning_style] +
         approach_challenges_values[approach_challenges] +
         comfortable_online_learning_values[comfortable_online_learning] +
         pace_of_learning_values[pace_of_learning] +
         long_term_goals_values[long_term_goals]
         ) // 3
    )
    #learning_rate = learning_rate *0.9+0.1
    return learning_rate