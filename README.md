clone repo
`cd flask-heroku-backend`

-- To run locally:

`virtualenv venv` (`sudo pip install virtualenv` if you don't have it)
`source venv/bin/activate`
`pip install -r requirements.txt`

Make sure you have MySQL running locally on port 3307. Follow this: https://www.linode.com/docs/databases/mysql/how-to-install-mysql-on-ubuntu-14-04
Create a database `db`.

`export DATABASE_URL=mysql://root@127.0.0.1:3307/db?charset=utf8&init_command=set%%20character%%20set%%20utf8`
`python run.py`

-- To deploy on heroku:

Make sure you have a Heroku account and follow steps here: https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app

Follow the steps on https://devcenter.heroku.com/articles/cleardb#provisioning-the-add-on to set up a MySQL add-on.
