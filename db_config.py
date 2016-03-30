import pymongo
# import smtplib


def get_client(mongo_db):
    try:
        client = pymongo.MongoClient(mongo_db)
        return client
    except pymongo.errors.ConnectionFailure, excpt:
        # smtpObj = smtplib.SMTP('localhost')
        # smtpObj.sendmail(
        #     "sk11juit@gmail.com",
        #     "sancheeta.kaushal@grofers.com",
        #     excpt
        # )
        return excpt


def get_database(client, database):
    return client[database]
