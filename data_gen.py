import pandas as pd

# Create a DataFrame with the example resumes
data = {
    "Name": ["John Doe", "Jane Smith", "Michael Brown", "Emily Johnson", "Robert Davis", "Lisa Martinez", "David Wilson", "Sarah Lee"],
    "Resume": [
        "John Doe has over 10 years of experience in software development, specializing in web and mobile applications. He holds a Bachelor's degree in Computer Science from XYZ University. He has worked for ABC Corp, DEF Inc., and GHI Ltd., where he led numerous successful projects. He is proficient in Java, Python, and JavaScript.",
        "Jane Smith is a marketing professional with 8 years of experience in digital marketing and brand management. She has a Master’s degree in Business Administration from ABC University. She has worked with various companies to develop effective marketing strategies and campaigns. Her skills include SEO, content marketing, and social media management.",
        "Michael Brown is a certified project manager with 12 years of experience in managing large-scale projects in the construction industry. He holds a PMP certification and a degree in Civil Engineering from DEF University. He has successfully completed projects on time and within budget for several multinational companies.",
        "Emily Johnson has 6 years of experience in human resources management. She holds a Bachelor's degree in Human Resources from GHI University. She has worked in both corporate and non-profit sectors, focusing on employee relations, talent acquisition, and performance management. She is skilled in using various HR software and tools.",
        "Robert Davis is a financial analyst with 7 years of experience in investment banking and financial planning. He has a Master’s degree in Finance from JKL University. He has worked with top financial institutions to provide insightful analysis and recommendations. His expertise includes financial modeling, budgeting, and risk management.",
        "Lisa Martinez is a graphic designer with 5 years of experience in creating visual content for both print and digital media. She has a Bachelor’s degree in Graphic Design from MNO University. She has worked with various clients to produce logos, brochures, websites, and social media graphics. She is proficient in Adobe Creative Suite and other design tools.",
        "David Wilson is a data scientist with 8 years of experience in data analysis and machine learning. He holds a PhD in Computer Science from PQR University. He has worked on several high-impact projects, applying advanced statistical methods and algorithms to solve complex problems. His skills include Python, R, and SQL, as well as data visualization tools.",
        "Sarah Lee is a healthcare administrator with 10 years of experience in hospital management and healthcare policy. She holds a Master’s degree in Health Administration from STU University. She has worked in various healthcare settings to improve operational efficiency and patient care. Her skills include strategic planning, budgeting, and regulatory compliance."
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
file_path = "/mnt/data/resumes.csv"
df.to_csv(file_path, index=False)

file_path