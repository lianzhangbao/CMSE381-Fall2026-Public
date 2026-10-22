# CMSE 381 - Project description

## Project Overview

This project provides students with an opportunity to work on real-world datasets, fostering a broader understanding of data science applications.

You will work in **2-person groups** -- please decide soon who your project partner will be.

## Dataset

For this project, students can use the **Yahoo Finance** Python package (`yfinance`) to obtain their dataset. It provides free access to historical market data -- daily prices, trading volume, and related information for stocks, ETFs, indices, and more -- and loads directly into a pandas DataFrame.

Example usage:

```python
pip install yfinance

import yfinance as yf

# download daily price history for a ticker
data = yf.download("AAPL", start="2020-01-01")
data.head()
```

This data source offers sufficient complexity for the project: you can define your own response variable (for example, next-day return for a regression task, or whether the price moves up or down for a classification task) and engineer predictors from historical prices and volume.

Students also have the flexibility to choose their own dataset instead of using Yahoo Finance data. If you would like to use a different dataset, you will need to propose it to your section instructor, who will need to **approve** it for sufficient complexity before you begin developing your project.

**Disclaimer:** This project, including any trading strategies or backtests developed in the notebook, is for educational purposes only and does not constitute financial or investment advice. Past performance in a backtest does not guarantee future results, and the instructors, teaching staff, and Michigan State University assume no responsibility for financial losses resulting from applying these strategies to real markets.

## Project Requirements

Students need to apply the skills studied in CMSE 381 to construct strategies for stock trading or portfolio optimization. Ideas include using confidence intervals, cross-validation, classification, predictions from regression, and deep learning methods.

1. This is a collaborative project. So the two members of each group should discuss how they want to distribute the project responsibilities described below while at the same time collaborating with each other.
2. Explore and understand the selected dataset. Students have the flexibility to explore the dataset in whatever direction interests them -- for example, focusing on a particular ticker, sector, or time window -- as long as the analysis stays grounded in the course material.
3. Perform a regression or a classification task on the dataset, such as predicting a stock's future price or return (regression) or predicting the direction of price movement (classification). (You can assign one member of the group for this)
4. Choose another method (or more) learned in class on the dataset. (You can assign the other member of the group for this)
5. Each must include some additional improvement, such as constructing **confidence intervals** for your estimates or predictions, or using **K-fold cross-validation** for parameter selection or subset selection to decrease the number of parameters used in the model.
6. Analyze and interpret the results of both 2 and 3.
7. Present findings and insights in a Jupyter Notebook and a video recording (5 min). Both group members should speak, spending roughly even amount of time.

## Project Deliverables

For your semester project, **you'll be expected to turn in a Jupyter notebook, a 4-5 minute presentation (video recording), and slides used in the presentation**.

Your **Jupyter notebook** (see [Template](./ProjectTemplate.ipynb)) should contain the following:

* All of the code used to complete your project. The code should be documented so that the instructor can understand what you did and why you did it. This means including meaningful comments in the code itself! You should also use logical variable names to ease the reading of the code.
* Narrative text (using Markdown cells) that explains what you did, why you did it, and how you went about it. You should break the notebook up into the following meaningful sections so that the instructor can follow the logical flow of your work:

	- **Background and Motivation**: Provide some context for the problem and what question(s) you set out to answer.
	- **Methodology**: How did you go about answering your question(s)? Most of your code will be contained in this section.
	- **Results**: What did you find when you carried out your methods? Some of your code related to presenting results/figures/data may be replicated from the methods section or may only be present in this section. All of the plots that you plan on using for your presentation should be present in this section.
	- **Synthesis and Discussion**: What did you learn from your results? What obstacles did you run into? What would you do differently next time? What is the answer to your question(s) and why?
	- **Author Contribution**: You should summarized the contribution of each member of the group to the project, in terms of, e.g., contribution to writing text, code development, and providing critical feedback to the other member.

**The code, text, and visuals should be threaded together as coherent report of your work!**

In addition to the notebook, **you will recording a 4-5 minute presentation that you will turn in** using a short set of slides to share the results of your project with your instructors. Your presentation should include appropriate **visual aids**. The presentation should address:

* The **question(s)** you set out to answer.
* The **model** that you applied to your chosen data or chosen topic.
* The **computational techniques** that you used to analyze your data or run your model.
* The **answer(s)** you arrived at.

### Presentation slides

You can create your slides using the presentation software of your choosing (e.g. Google Slides, Powerpoint, Keynote). Once you've finished your slides, you should save a **PDF copy** that you can submit with your Jupyter notebook. You should aim for having a reasonable number of slides -- a good guideline is ~1 min of time per slide. For a presentation of this length, you probably wouldn't want to have more than 6-7 slides, but you should make sure that you have a sufficient number of slides to support your presentation.

**The slides should**:

* Address the above points in a logical order.
* Include a title slide with your project title, name, and course number (with section number).
* Effectively communicate information through a combination of text and figures. Text and figures should be clearly legible in your presentation.
* Only include text and figures that support the presentation (avoid including content "just because").
* Avoid large paragraphs of text, use bullet points instead.

### Additional details on Recording Presentations

You could use Zoom to record your presentation. You should be able to "Share Screen" in Zoom to share your slides and talk through the presentation as if you were giving it live. **You should make sure that your recording is no longer than 5 minutes, but it should be at least 4 minutes.** You will turn in the "mp4" file that Zoom produces when your record the Zoom session.

## Grading Rubric

The rubric below assumes both members of the group have contributed to the development of the project. If a member has not contributed anything, this member has **0 point** for the entire project.

The presentation/project will be graded as follows (**total: 100 points**):

* Oral presentation (**20 points**). Is it clear and well-structured? Does the student effectively communicate the key ideas about their results?
	* *Excellent presentation*: student speaks clearly and in a logical manner, and makes their key points clear. (**20 points**)
	* *Good presentation*: student speaks clearly and logically and conveys key points, but presentation is somewhat lacking (**15 points**)
	* *Fair presentation*: student's oral presentation is substantially lacking (speaking too quietly to be heard or with little inflection, clarity/logical flow in speaking is sub-par, etc.) (**10 points**)
	* *Poor presentation*: student's oral presentation is completely lacking (cannot be heard, there is no logical progression to the presentation) (**5 points**)

* Presentation slides (**20 points**). Do the slides complement their oral presentation, and conform to the guidelines?
	* *Excellent slides*: Slides conform to specifications in final presentation document, including number of slides, adequately addressing all points, legibility. Slides complement oral presentation. (**20 points**)
	* *Good slides*: Slides deviate from specifications in some minor way: too many or too few slides, not all points addressed, some slides hard to understand (poor graphics, too much or too little text, etc.) (**15 points**)
	* *Fair slides*: Slides deviate from specifications in some substantial way: too many or too few slides, half or fewer of points addressed, most slides hard to understand (poor graphics, too much or too little text, etc.) (**10 points**)
	* *Poor slides*: Slides do not conform to specifications in any meaningful way. (**5 points**)

* Final project content (**40 points**). This is a combination of the content in the student's presentation and in their Jupyter notebook. Does the student clearly and concisely address all off the points listed in the final project guidelines? Detailed rubrics are below:

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTVPKd8SghKdISy-oFlNJt5CsC3hqhhSuNJbs8tpFZvWvsGD7yq0xgILXso9JXBYdMhuCZv56gTP9pt/pubhtml?gid=0&amp;single=true&amp;widget=true&amp;headers=false" width = 100% height = "600"></iframe>

* Sufficient contribution (**20 points**). This assessment the individual specific contribution to the group project.
    * Substantial contribution to text writing, code development, video presentation, and providing critical feedback to the other member's work (**20 points**)
    * Minor contribution to the project. Clearly the other member had done more work. (**10 points**)
    * Minimal contribution to the project, when the work is mostly done by the other member. (**0 points**)
