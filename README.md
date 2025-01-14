# BOB-BOT

## Get Started

Required: must have [docker](https://docs.docker.com/desktop/setup/install/mac-install/) installed in order to run discord bot with appropriate dependencies. 

run:

```
docker build -t discord-bot . && docker run --env-file .env -d --name discord-bot discord-bot
```

##### HOW TO GIT:

[https://www.atlassian.com/git/glossary#commands]()

`git status - track whats happening`

`git add . - save your changes`

`git commit -m """ - add a message describing the changes`

`git push - push changes to github repo for everyone`

## Bob features coming soon:

### **NBA Updates Features**

1. **Game Schedules** :

* Daily schedule of NBA games (`!nba schedule`).
* Set reminders for upcoming games involving favorite teams (`!nba remind <team>`).

1. **Live Scores and Highlights** :

* Provide live score updates during ongoing games (`!nba live`).
* Send game highlights or top plays of the day (`!nba highlights`).

1. **Player Stats** :

* Query specific player stats for the season or a particular game (`!nba stats <player>`).
* Compare players (`!nba compare <player1> <player2>`).

1. **Team Standings** :

* Post the current standings for the Eastern and Western Conferences (`!nba standings`).
* Update rankings after each game day.

1. **Breaking News** :

* Share important updates like trades, injuries, or major announcements (`!nba news`).

1. **Fantasy Basketball Integration** :

* Track fantasy points for key players.
* Suggest waiver wire pickups or trades.

1. **Trivia and Fun Facts** :

* NBA-themed trivia games (`!nba trivia`).
* Fun facts about teams, players, or the league's history (`!nba fact`).

1. **Customizable Alerts** :

* Let users subscribe to updates for specific teams or players.
* Notify users when their favorite team starts or finishes a game.

### **Implementation Ideas**

* **Data Source** : Integrate with APIs like [NBA API](https://nba.com/stats) or [SportsRadar](https://developer.sportradar.com/).
* **Webhook Updates** : Use webhooks to push live updates into a specific channel automatically.
* **Polls and Predictions** : Allow users to vote on game outcomes or create prediction challenges (`!nba predict <game>`).

Let me know if you need help with implementation, and I can guide you through setting up these features! 🏀
