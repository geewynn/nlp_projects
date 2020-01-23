# Recommender_System
- Evaluation Metric - Root Mean Squared Error (RMSE)

# Data Preprocessing
- Data was gotten from lucid.blog, This data was released in the form of a dump.
- Meaningful column used was accessed using phpmyadmin and extracted to a csv file.
- Data was converted into SFRAME, required for turicreate to work with.

# Model
- Spilit the data into train and validation.
2 different models was built.
- 1 A rating model and an Item similarity model.
## Rating Model
- Ratings was decided by using the turicreate ranking factorization recommender method.
- Based on the evaluation metric, the rating model had a rsme of 0.56 on per user basis and rsme of 0.19 per item basis.

## Item Similarity Model
- Used the item similarity recommender method of turicreate to implement this model.
- Per user basis, the model scored 0.16 on the evaluation metric.
- Per Item basis, the model scored 0.16 on the evaluation metric.

- Based on the comparison, the item similarity model performed better than the rating model.

### Testing the Model
**First and most recommended step to try out the model is**
1. Go to the colab https://colab.research.google.com/drive/1yaUUM9aWt2fdwy0EH6C5va01yCxUTit1#scrollTo=exaELg8KZdHV
2.Download the data from https://drive.google.com/drive/folders/1BOKo2EeCRQ-Z85t5hzEtGz1svEYB6GmK?usp=sharing
3. Upload the data to your google drive 
4. Run the colab and set the path to the data on your google drive. There are instructions on the colab notebooks that you can also follow.

You can also find the colab notebook in the colab_notebook folder.

**For the second method, you can**
1. Clone the repo to your local repo using git clone repo_url
2. cd into the cloned directory and locate the jupyter_model folder.
3. If you are using linux. Install turicreate using pip install turicreate
4. Run and test the model.
5. For instruction on how to test the model. A simpler guide is written on the notebook.

**Lastly, the model was deployed using flask.**
Note. You have to have turicreate installed locally on your system.
1. You have to clone the repo. Same way as described above.
2. cd into the deploy model folder.
3. Run the deploy.py file. Make sure the files are kept in that folder. Do Not take any file out.
To check if the model is working
1. go to this url on your browser

**For the follower rec_sys http://127.0.0.1:5000/recomend/user_id**
**For the article rec_sys http://127.0.0.1:5000/articles/user_id**

Take note user_id is a number 1-infinity
	For example, Imagine we want to recommend users and articles for a user with user_id= 1.  		The main url for recommending followers will be http://127.0.0.1:5000/recomend/1
	The main url for recommending articles will be http://127.0.0.1:5000/articles/1 




**You are likely to run into issues with the turicreate package, it installs natively on the MacOs and Linux , it also does install on Windows 10 using WSL 
checkout https://pypi.org/project/turicreate/ for directions as to how to go about doing that #




 
