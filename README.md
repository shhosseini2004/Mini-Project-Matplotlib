# 📊 Mini Project — Google Play Store Data Visualization

🧠 Project Overview
This project is part of the Machine Learning in Python (ML0101EN) course, focusing heavily on Exploratory Data Analysis (EDA) and Visualization techniques. The primary tools utilized for visualization are the powerful Python libraries Matplotlib and Seaborn.

The core resource for this investigation is the dataset named googleplaystore.csv. This file contains rich, detailed information pertaining to a vast array of Android applications currently available on the Google Play Store. The scope of the project is broad, encompassing application metadata, user feedback statistics, and commercial aspects (like pricing).

The overarching goal of this entire exercise is twofold: first, to meticulously clean and prepare the raw, messy dataset for quantitative analysis; and second, to leverage visual methods to extract meaningful, actionable insights regarding app performance, user engagement patterns, and overall market segmentation within the Android ecosystem.

🧾 Dataset Description
The googleplaystore.csv file is substantial and offers a deep dive into application characteristics. Understanding each field is crucial for meaningful analysis.

The dataset comprises several key columns, detailed below:

Column NameDescriptionData Type (Initial)AppThe official, unique name of the application.StringCategoryThe broad classification of the app (e.g., GAME, TOOLS, BUSINESS).StringRatingThe average user rating assigned to the app, typically ranging from 1 to 5 stars.Float/StringReviewsThe total count of user reviews submitted for that application.String (needs conversion)InstallsThe reported number of times the application has been installed. This is stored in a non-numeric format (containing symbols like '+' and ',').StringTypeIndicates the pricing model: whether the app is designated as 'Free' or 'Paid'.StringPriceThe cost of the application if it is a Paid app. Free apps will typically have a price of '0'.StringContent RatingSpecifies the target audience based on Google's content guidelines (e.g., Everyone, Teen, Mature 17+).StringGenresA more specific classification within the broader Category (e.g., Action, Productivity).StringCurrent VerThe latest version number released for the application.StringAndroid VerThe minimum required version of the Android operating system needed to run the app.String

🧹 Data Cleaning and Preparation
Real-world data, especially scraped datasets, rarely arrive in a pristine state ready for modeling or visualization. A significant portion of this mini-project was dedicated to rigorous data preprocessing to ensure the integrity of the subsequent visual analysis.

The following critical steps were executed:

1. Handling Invalid Rating Entries
Initial exploration revealed spurious entries in the Rating column that did not conform to the expected 1-5 scale. Specifically, entries such as Rating = 19 were identified. These were treated as errors and removed entirely from the dataset, as they skew the central tendency measures.

2. Normalizing the Rating Range
After removing outright errors, a second filtering pass was performed. We retained only those rows where the Rating value was strictly within the permissible range: between 0 and 5.0, inclusive.

3. Imputing Missing Rating Values
The Rating column is central to our analysis, yet missing values (NaN) were present. Since removing too many rows can lead to loss of valuable information, we chose an imputation strategy. Missing Rating values were filled using the median rating of the entire dataset. The median is preferred over the mean in this context because user ratings are often skewed by a few very low or very high ratings.

4. Imputing Version Information
The version columns (Current Ver and Android Ver) contained missing values. These fields are generally categorical or version strings that do not lend themselves well to mean/median imputation. Therefore, we filled these missing entries using the mode (the most frequently occurring value) for each respective column.

5. Converting to Numeric Format
The Installs column was fundamentally unusable in its string form (e.g., "1,000,000+"). To perform any quantitative analysis (like summing or plotting distributions), it needed transformation:

Removal of Symbols: All commas (,) and plus signs (+) were stripped from the strings.

Type Casting: The resulting clean string was then successfully converted into a numeric type (integer or float), allowing for mathematical operations.

📊 Data Visualization & Insights
The cleaned data was then transformed into various visual representations using Matplotlib and Seaborn to uncover patterns related to app success factors.

1. Distribution of Ratings
Visualization Type: Histogram combined with a Kernel Density Estimate (KDE) plot.

Insight: The visualization clearly indicates a left-skewed distribution. The vast majority of applications cluster tightly around the higher end of the scale. Specifically, the peak of the distribution, representing the most common rating, falls between 4.0 and 4.5. This suggests a generally high level of user satisfaction across the ecosystem, or perhaps an inherent bias in users reviewing highly successful apps.

The mathematical representation of the distribution's shape (skewness) helps confirm this visual observation.

2. Boxplot of Ratings by Category
Visualization Type: Boxplot, with categories sorted by median rating.

Insight: This plot is excellent for comparing variances and central tendencies across different groups. It reveals significant disparities:

Categories such as Education, Events, and Art & Design often exhibit higher median ratings and tighter interquartile ranges (IQR), indicating consistent high performance.

Conversely, categories like Finance or Tools sometimes show lower medians or much larger outliers (apps with extremely low ratings), suggesting more polarizing user experiences in those segments.

3. Total Installs by Category
Visualization Type: Horizontal Barplot (due to many categories).

Insight: By summing the total (numeric) installations per Category, we identify the market leaders in terms of user adoption:

GAME: Consistently shows the highest absolute number of installs.

COMMUNICATION: High volume driven by essential utility apps (e.g., messaging).

TOOLS: Significant user base reflecting utility and system applications.

This visual helps business analysts understand where the bulk of user attention is concentrated.

4. Relationship Between Installs and Ratings
Visualization Type: Scatterplot, utilizing a logarithmic scale for the 'Installs' axis.

Insight: Since the number of installs spans several orders of magnitude, a standard linear plot would obscure lower-install apps. Using a log scale ($\log_{10}(\text{Installs})$) reveals the underlying trend:

There is a positive correlation: Apps that achieve higher levels of installation generally maintain better average ratings.

However, the scatter also shows outliers: some apps with astronomically high installs still possess middling or low ratings. This often points to established, legacy applications that maintain high download counts due to necessity or pre-installation, regardless of recent user satisfaction.

5. Count of Apps by Type
Visualization Type: Count Plot (Bar Chart showing frequency).

Insight: This simple comparison definitively illustrates the economic structure of the Play Store: Free applications overwhelmingly dominate the landscape in sheer volume compared to Paid applications. This highlights the common "freemium" model strategy prevalent in the mobile market.

6. Correlation Heatmap
Visualization Type: Heatmap using Seaborn's heatmap function applied to the correlation matrix of numeric features (Rating, Reviews, Installs, Price converted to numeric).

Insight: The heatmap visually quantifies linear relationships. Key takeaways include:

A very strong positive correlation ($r \approx 0.9$ or higher) is observed between Reviews and Installs. This is expected: the more users who install an app, the more likely they are to leave a review.

The correlation between Price (when converted numerically) and Rating is often weak or slightly negative, indicating that simply charging more money does not guarantee a higher average user rating.

🧰 Technologies Used
The execution of this project relied on a standard, powerful stack for data science in Python:

Python 3: The foundational programming language.

Pandas: Essential for data loading, complex filtering, grouping, aggregation, and restructuring the raw CSV data.

Matplotlib & Seaborn: The core libraries used to generate all visualizations, from basic histograms to complex bivariate plots and heatmaps. Seaborn was particularly useful for enhancing aesthetic appeal and statistical visualization complexity.

NumPy: Used implicitly by Pandas and explicitly for underlying numerical computations, especially when dealing with arrays and mathematical transformations (like the log scaling).

Scikit-learn: Although the primary focus was EDA, a minor extension exercise might involve fitting a simple model. For instance, the Iris dataset was often used alongside this project as a brief foray into classification, utilizing components like sklearn.model_selection or a basic LogisticRegression model to contrast the EDA findings with predictive modeling techniques.

▶️ How to Run the Project Locally
To reproduce the analysis and visualizations presented here, follow these standard steps:

1. Clone the Repository
If the project code is hosted on a version control system like Git (recommended):

git clone https://github.com/shhosseini2004/MiniProject-GooglePlaystore.git
cd MiniProject-GooglePlaystore

(Note: Replace shhosseini2004 with the actual repository owner.)

2. Install Dependencies
All necessary Python packages must be installed in your environment. It is best practice to use a requirements.txt file listing dependencies:

pip install -r requirements.txt

The requirements.txt file would typically contain entries such as:

pandas
matplotlib
seaborn
numpy
jupyter

3. Run the Jupyter Notebook File
The complete workflow, combining data cleaning steps and visualization code blocks, is usually encapsulated within a Jupyter Notebook:

jupyter notebook "Session 03 - Mini Project Matplotlib.ipynb"

This command launches a local web server, allowing you to interact with the code cells, execute them sequentially, and view the generated plots immediately within the notebook interface.

📈 Results Summary
The exploratory data analysis successfully navigated significant data quality hurdles to yield concrete findings regarding the Google Play Store ecosystem:

Data Volume: The final, cleaned dataset contained processed records representing over 10,000+ distinct applications.

Rating Tendency: The distribution analysis confirmed a positive bias, with the majority of apps scoring highly (median rating between 4.0 and 4.5).

Category Popularity: Analysis clearly identified Game and Communication as the categories dominating user attention (highest installs).

Core Correlations: A strong, positive relationship was established between user engagement metrics (Reviews) and adoption metrics (Installs).

Business Model: The visualization confirmed the overwhelming market preference for Free apps over Paid ones.

🔮 Future Improvements
While the current visualizations provide a robust snapshot, the project offers several pathways for future enhancement and deeper investigation:

Interactive Dashboards: Transitioning static Matplotlib/Seaborn charts into interactive components using libraries like Plotly or building a simple web application using Streamlit would allow users to filter data dynamically (e.g., by selecting a specific price range).

Textual Feature Integration: The raw text data (App Description, Reviews) was ignored due to scope limitations. Integrating Natural Language Processing (NLP) techniques, such as sentiment analysis on user reviews, would provide deeper insights into why apps are rated a certain way.

Real-Time Data Sourcing: Currently, the data is static (a CSV file). Integrating with third-party Play Store APIs (where permissible) or web scraping techniques could be employed to update the dataset periodically, allowing for trend analysis over time.

Advanced Statistical Modeling: Beyond correlation, a more sophisticated regression model could be built to predict an app's Rating based on its Category, Price, and the initial volume of Reviews.

✍️ Author Information
This mini-project serves as a practical application exercise completed within the curriculum structure.

Course Context: Developed as part of Machine Learning in Python (ML0101EN) — Session 03 Mini Project.

Author: [shhosseini2004]

GitHub Profile: https://github.shhosseini2004)
