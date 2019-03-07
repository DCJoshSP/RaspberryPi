import sqlite3
#Connect to the database
conn = sqlite3.connect('databaseofneededstuff.db', check_same_thread=False)
#Some sort of abstract thing that acts as the link between database and program
c = conn.cursor()

class profile():
    """When the choose account function is done, the account detail/obect will become the one chosen 
    and its attributes will contain all those in the table for that profile
    This class contains all the functions needed to do stuff with the profile"""
    def __init__(self, username, email, emailtime, algtype):
        self.username = username
        self.email = email
        self.emailtime = emailtime
        self.algtype = algtype
    #endprocedure
    
    def getUsername(self):
        return self.username
    #endfunction

    def getEmail(self):
        return self.email
    #endfunction

    def getEmailTime(self):
        return self.emailtime
    #endfunction

    def getAlgType(self):
        return self.algtype
    #endfunction 

    def setUsername(self, username):
        c.execute("""UPDATE profiletable SET username = :newuser
                    WHERE username = :username""",
                  {'newuser': username, 'username': self.username})
        conn.commit()
        c.execute("""UPDATE itemtable SET username = :newuser
                    WHERE username = :username""",
                  {'newuser': username, 'username': self.username})
        conn.commit()
        c.execute("""UPDATE triptable SET username = :newuser
                    WHERE username = :username""",
                  {'newuser': username, 'username': self.username})
        conn.commit()
        self.username = username
        pass
    # go to updater()
    #endprocedure

    def setEmail(self, email):
        c.execute("""UPDATE profiletable SET email = :newemail
                    WHERE username = :username""",
                  {'newemail': email, 'username': self.username})
        conn.commit()
        pass
    # go to updater()
    #endprocedure

    def setEmailTime(self, emailtime):
        c.execute("""UPDATE profiletable SET emailtime = :emailtime
                    WHERE username = :username""",
                  {'emailtime': emailtime, 'username': self.username})
        conn.commit()
        pass
    # go to updater()
    #endprocedure

    def setAlgType(self, algtype):
        c.execute("""UPDATE profiletable SET algorithmtype = :newalg
                    WHERE username = :username""",
                  {'newalg': algtype, 'username': self.username})
        conn.commit()
        pass
    # go to updater()
    #endprocedure

    def deleteself(self, name):

        c.execute("""DELETE FROM profiletable
                    WHERE username = :username""",
                    {'username': self.username})
        conn.commit()
        c.execute("""DELETE FROM itemtable
                    WHERE username = :username""",
                    {'username': self.username})
        conn.commit()
        c.execute("""DELETE FROM triptable
                    WHERE username = :username""",
                    {'username': self.username})
        conn.commit()

        #c.execute("""UPDATE profiletable SET username = :newuser
        #            WHERE username = :username""",
        #          {'newuser': username, 'username': self.username})
        #conn.commit()
        #c.execute("""UPDATE itemtable SET username = :newuser
        #            WHERE username = :username""",
        #          {'newuser': username, 'username': self.username})
        #conn.commit()
        #c.execute("""UPDATE triptable SET username = :newuser
        #            WHERE username = :username""",
        #          {'newuser': username, 'username': self.username})
        #conn.commit()

        pass
    #need to return to start()
    #endprocedure

    def updater(self, field, newvalue):
        pass
    
    #Use same principal from clothing with un, em, emt and algt all pointing to updater
    #endprocedure 

#endclass


