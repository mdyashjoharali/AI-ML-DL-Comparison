# AI vs ML vs Deep Learning Comparison

comparison = {
    "Artificial Intelligence": {
        "Definition": "Machines performing tasks that normally require human intelligence.",
        "Example": "Chatbots, Virtual Assistants"
    },
    "Machine Learning": {
        "Definition": "Subset of AI that learns from data.",
        "Example": "Netflix Recommendations"
    },
    "Deep Learning": {
        "Definition": "Subset of ML using neural networks.",
        "Example": "Face Recognition"
    }
}

for tech, details in comparison.items():
    print(f"\n{tech}")
    for key, value in details.items():
        print(f"{key}: {value}")
      
