class DatabaseConstants:
    DATABASE_URI_TEMPLATE = "mysql://root:StartupLyfe2014@startuplinx2.chobzyje65oy.us-east-1.rds.amazonaws.com/%s?charset=utf8&init_command=set%%20character%%20set%%20utf8" # TODO CHANGE AND PUT IN ENV VARIABLE
    DATABASE_LOCAL_URI_TEMPLATE = "mysql://root@127.0.0.1:3307/%s?charset=utf8&init_command=set%%20character%%20set%%20utf8" # TODO CHANGE
    DATABASE_NAME = 'db' # TODO CHANGE
    DATABASE_URI = DATABASE_LOCAL_URI_TEMPLATE % DATABASE_NAME # TODO CHANGE
    DATABASE_LOCAL_URI = DATABASE_LOCAL_URI_TEMPLATE % DATABASE_NAME
