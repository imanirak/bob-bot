import os
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats


from dotenv import load_dotenv
load_dotenv()

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
    headers = stats['resultSets'][0]['headers']  # Column names
    rows = stats['resultSets'][0]['rowSet']  # Data rows
    stats_list = [dict(zip(headers, row)) for row in rows]

    season_stats = next((stat for stat in stats_list if stat['SEASON_ID'] == season), None)
    
    if not season_stats:
        return f'No stats found for {player_name} in the {season} season.'
    
    return season_stats


