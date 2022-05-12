# Monthly Ritual Bot
A Discord bot made using Nextcord, PostgreSQL, and Heroku, for tracking all your monthly activities--both real and fictional. It is as HIPAA-compliant and anonymous as possible. Your data will never be sold or given without your consent, and you have the tools to completely erase or lock your data from access.

## 0. Table of Contents
1. Usage Instructions & Commands
2. Database Design
3. Hosting a Private Copy
4. Why did I make this?

## 1. Usage Instructions & Commands


## 2. Database Design
screenshots here

## 3. Hosting a Private Copy
To host a private copy, you'll need to have or make the following:
1. An email address.
2. A Discord account, if you don't have one already.
3. A Discord server. If privacy/anonymity is your concern, make a private server with only yourself in it.
4. A Heroku account.
5. A credit or debit card. This hasn't been tested with Visa gift cards; if you try, please let me know!
    1. YOU DO NOT NEED TO PAY ANYTHING. This is just Heroku's requirement for using a full 1000 hours per month.
6. A Discord developer account.
7. A Github account.

You will also need to install the following on your computer:
1. Git
2. Github Desktop
3. Heroku CLI

### Github Setup

### Discord Setup

### Heroku Setup

##4. Why did I make this?
In the United States, Roe v. Wade is a Supreme Court ruling from 1973 that ruled that the Constitution protects a person's right to access medical treatment and procedures within the privacy of their medical community, without outside interference or restriction. This most notably protects a female's right to obtain an abortion, no matter their reason.

Roe v. Wade is under threat of being overturned. If it is overturned, many laws across the country will immediately become active in multiple states, some allowing pregnant people to be criminally prosecuted should they miscarriage or need an abortion in order to save their life.

Many people with wombs are--understandably--distrustful that their period tracking apps may be used against them. It's already been found that [some period tracking apps share their data with Facebook](https://www.buzzfeednews.com/article/meghara/period-tracker-apps-facebook-maya-mia-fem). [Missouri officials have been found to track periods of patients](https://www.thecut.com/2019/10/missouri-official-tracked-womens-periods.html). Victims facing partner abuse may suffer from manipulation or even be forced to become pregnant through deceptive use of condoms should their partners have access to their period--and thus, ovulation--information.

Privacy of health information such as your menstrual cycle is of [the utmost importance now more than ever](https://www.theguardian.com/world/2019/apr/13/theres-a-dark-side-to-womens-health-apps-menstrual-surveillance). Using a Discord bot is not the most convenient, compared to an app or even a calendar. But you can type a simple command and delete all of your data. You do not have an obvious app on your phone.

The bot automatically deletes your messages when you type a command, so there will not be an obvious record of what you have input. The terminology the bot uses is not obviously indicative of being related to menstruation.

And, most importantly: ***anyone can, and should, use it.*** This isn't period specific. You can get reminders to drink water, or take your meds. You can track other monthly appointments; maybe you want to record your monthly therapy sessions, or log your D&D sessions, or record your HRT shots.

The more people who use this bot for things other than period tracking, the more there is plausible deniability for those who do.

### Legal Disclaimer
This bot does not assist people in getting abortions. It does not provide information on how to get an abortion.

***DO NOT*** store any personally-identifying information in this app! It uses only your Discord user ID to identify you--keep it that way! While Heroku is HIPAA-compliant, Discord is not. Therefore, *please do not* record information such as what medications you are taking, who your doctor is, where you go for medical procedures, or even what medical procedures you have.

While this bot provides labels that can easily be used to track specific activities such as period, menstruation, and engaging in sex, users are not required to use the correct label for the information they are recording. Therefore, as the creator, I have no way to verify that user information is accurately logged.






## 1. Main References
* [Heroku database webUI](https://data.heroku.com/)
* [Postgresql Add-on Page](https://elements.heroku.com/addons/heroku-postgresql)
* [Discord Developer Portal](https://discord.com/developers/applications)

## 2. Essential Commands
### Matching user IDs to table IDs
```python
userID = ctx.author.id
tableID = await dbName.fetchval("SELECT * FROM table WHERE user_id = $1;", userID)

# check if the user has ever sent command before, if not, add them to our table
if tableID is None:
    await dbName.execute("INSERT INTO table(user_id) VALUES($1);", userID)
```

### Fetching a value
```python
# by name
pythonVar = await dbName.fetchval("SELECT column FROM table WHERE user_ID = $1;", userID)

# by column
pythonVar = await dbName.fetchval("SELECT * FROM table WHERE user_id = $1;", userID, column=1)
```

### Updating a value
```python
await dbName.execute("UPDATE table SET column = $1 WHERE user_id = $2;",newValue,userID)
```

### Pinging me when online
```python
hostChannelID = os.environ.get('HOST_CHANNEL')
kchilID = os.environ.get('CREATOR_ID')

@bot.event
async def on_ready():
    hostChannel = bot.get_channel(int(hostChannelID))
    kchil = bot.get_user(kchilID)
    kchilPing = kchil.mention
    await hostChannel.send(kchilPing + " I am online.")
```

### Random activities
```python
activitiesList = []
listeningList = []
watchingList = []
streamingList = []
playingList = []
activitiesList.extend(listeningList)
activitiesList.extend(watchingList)
activitiesList.extend(streamingList)
activitiesList.extend(playingList)
currentActivitiesList = []
currentActivitiesList.extend(activitiesList)

async def status_task():
    global activitiesList
    global currentActivitiesList
    global activityChoice
    global listeningList
    global watchingList
    global playingList
    global streamingList
    
    while True:
        activityChoice = random.choice(currentActivitiesList)
        currentActivitiesList.clear()
        currentActivitiesList.extend(activitiesList)
        currentActivitiesList.remove(activityChoice)
        # listening
        if activityChoice in listeningList:
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activityChoice))
        # watching
        elif activityChoice in watchingList:
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=activityChoice))
        # streaming
        elif activityChoice in streamingList:
            await bot.change_presence(activity=discord.Streaming(name=activityChoice,url="url here"))
        # playing
        elif activityChoice in playingList:
            await bot.change_presence(activity=discord.Game(name=activityChoice)) 
        await asyncio.sleep(60)
        
    @bot.event
    async def on_ready():
        bot.loop.create_task(status_task())
```


## 3. Repository Directory
* bot (folder): the folder for the python files
  * bot.py (python file): the file for our python bot
* Procfile (file with **no extension**): the process file Heroku refers to when knowing what commands to run to start your bot
* README.md (markdown file): the readme
* requirements.txt (plain-text file): lists the package requirements for our bot
* runtime.txt (plain-text file): lists the buildpack requirements for our bot

## 4. Deployment Steps
1. Create Discord app
2. Create bot for our app
3. Set profile pic & name
4. Copy bot token
5. Create/login Heroku
6. Create new app
7. Install postgresql add-on
7. Configure environment variable(s)
8. Connect to GitHub
9. Select repository
10. Turn on auto-deployments
11. Manually deploy
12. Turn on worker dyno


## 5. Additional References

Postgresql free account limits:
* 10,000 rows/records
* Estimated downtime 4 hours/month
* 1 GB storage
* Maximum 50 schemas

Useful links:
* [Heroku's docs for Deploying Python and Django Apps on Heroku](https://devcenter.heroku.com/articles/deploying-python)
* [Heroku's Python Support docs](https://devcenter.heroku.com/categories/python-support)
* [Heroku's article "How Heroku Works"](https://devcenter.heroku.com/articles/how-heroku-works)
* [Heroku's guide for deploying Python apps](https://devcenter.heroku.com/articles/getting-started-with-python) *\*Note: these instructions are for CLI/Console deployment
* [Heroku CLI Package](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
* [Which versions of Python/PyPy Heroku supports](https://devcenter.heroku.com/articles/python-support#specifying-a-python-version)
* [Heroku's dynos](https://www.heroku.com/dynos)
* [Postgres Guidelines](https://devcenter.heroku.com/articles/heroku-postgres-plans)
* [PostgreSQL add-on](https://elements.heroku.com/addons/heroku-postgresql)
* [Heroku PostgreSQL](https://devcenter.heroku.com/articles/heroku-postgresql)
  * From the same article as above, [Connecting in Python](https://devcenter.heroku.com/articles/heroku-postgresql#connecting-in-python)
* Heroku's Postgres Backups](https://devcenter.heroku.com/articles/heroku-postgres-backups)
* [Connecting to Heroku Postgres Databases from outside Heroku](https://devcenter.heroku.com/articles/connecting-to-heroku-postgres-databases-from-outside-of-heroku)
* [Monitoring Heroku Postgres](https://devcenter.heroku.com/articles/monitoring-heroku-postgres)
* [Heroku's Python connection guide](https://devcenter.heroku.com/articles/python-concurrency-and-database-connections).
* [PgBouncer Configuration](https://devcenter.heroku.com/articles/best-practices-pgbouncer-configuration)
* [Postgres Over Plan Capacity](https://devcenter.heroku.com/articles/heroku-postgres-over-plan-capacity)
* [Heroku Postgres Database Tuning](https://devcenter.heroku.com/articles/heroku-postgres-database-tuning)
* [Connection Pooling for Heroku Postgres](https://devcenter.heroku.com/articles/postgres-connection-pooling)
* [Heroku PGBackups](https://devcenter.heroku.com/articles/heroku-postgres-backups)

Code examples and references:
* [jegfish's example database connection](https://gist.github.com/jegfish/cfc7b22e72426f5ced6f87caa6920fd6)
* [Discord.py connection Stack Overflow](https://stackoverflow.com/questions/64271688/my-discord-py-bot-always-loses-connection-to-my-mysql-database-on-heroku)
