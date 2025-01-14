import os
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats


from dotenv import load_dotenv
load_dotenv()


STAT_DESCRIPTIONS = {
    "SEASON_ID": "Season",
    "TEAM_ID": "Team ID",
    "TEAM_ABBREVIATION": "Team Abbreviation",
    "PLAYER_AGE": "Player Age",
    "GP": "Games Played",
    "GS": "Games Started",
    "MIN": "Minutes Per Game",
    "FGM": "Field Goals Made",
    "FGA": "Field Goals Attempted",
    "FG_PCT": "Field Goal Percentage",
    "3PM": "Three-Point Field Goals Made",
    "3PA": "Three-Point Field Goals Attempted",
    "3P_PCT": "Three-Point Field Goal Percentage",
    "FTM": "Free Throws Made",
    "FTA": "Free Throws Attempted",
    "FT_PCT": "Free Throw Percentage",
    "OREB": "Offensive Rebounds",
    "DREB": "Defensive Rebounds",
    "REB": "Total Rebounds",
    "AST": "Assists",
    "STL": "Steals",
    "BLK": "Blocks",
    "TO": "Turnovers",
    "PF": "Personal Fouls",
    "PTS": "Points",
    "PLUS_MINUS": "Plus/Minus"
}

def get_player_stats(player_name, season):
    # Search for the player by name
    player_list = players.get_players()
    player = next((player for player in player_list if player['full_name'].lower() == player_name.lower()), None)
    
    if not player:
        return f"Player '{player_name}' not found."
    
    player_id = player['id']
    
    # Fetch career stats
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    stats = career_stats.get_dict()
    
    # Extract the relevant data from the dictionary
    headers = stats['resultSets'][0]['headers']  
    rows = stats['resultSets'][0]['rowSet']  
    stats_list = [dict(zip(headers, row)) for row in rows]

    # filter by season
    season_stats = next((stat for stat in stats_list if stat['SEASON_ID'] == season), None)
    
    if not season_stats:
        return f'No stats found for {player_name} in the {season} season.'
    
    # Add full description instead of abbrv
    full_stats = {STAT_DESCRIPTIONS.get(key, key): value for key, value in season_stats.items()}
    
    return full_stats


