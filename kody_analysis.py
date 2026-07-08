"""
Kody Funderburk Analysis Tool
A beginner's guide to baseball sabermetrics and Python!

This script analyzes Kody Funderburk's pitching statistics
to understand his performance and what needs to improve.
"""

# ==============================================================
# PART 1: STORE KODY'S STATS (2024-2026)
# ==============================================================

# We use a DICTIONARY (think of it like a labeled spreadsheet row)
# Each stat has a name (key) and a value (the number)

kody_2024 = {
    "year": 2024,
    "games": 27,
    "innings_pitched": 34.2,
    "era": 6.49,           # ERA = Earned Run Average (lower is better!)
    "whip": 1.62,          # WHIP = Walks + Hits per IP (lower is better!)
    "strikeouts": 32,
    "wins": 1,
    "losses": 0,
    "saves": 1
}

kody_2025 = {
    "year": 2025,
    "games": 39,
    "innings_pitched": 41.0,
    "era": 3.51,
    "whip": 1.51,
    "strikeouts": 40,
    "wins": 4,
    "losses": 1,
    "saves": 1
}

kody_2026 = {
    "year": 2026,
    "games": 23,
    "innings_pitched": 20.0,  # partial season
    "era": 3.72,
    "whip": 1.52,
    "strikeouts": 12,
    "wins": 1,
    "losses": 1,
    "saves": 1
}

# ==============================================================
# PART 2: CREATE FUNCTIONS (reusable tools)
# ==============================================================

def print_season_stats(season_dict):
    """
    This function takes a season's stats and prints them nicely.
    
    Think of it like: "Hey Python, take these stats and make them pretty!"
    """
    print(f"\n📊 {season_dict['year']} Season Stats")
    print("=" * 40)
    print(f"ERA (Earned Run Avg):  {season_dict['era']}")
    print(f"WHIP (Hits+Walks/IP):  {season_dict['whip']}")
    print(f"Strikeouts:            {season_dict['strikeouts']}")
    print(f"Wins-Losses:           {season_dict['wins']}-{season_dict['losses']}")
    print(f"Innings Pitched:       {season_dict['innings_pitched']}")
    print(f"Games Appeared:        {season_dict['games']}")


def calculate_strikeout_rate(season_dict):
    """
    Calculate K/9 = Strikeouts per 9 innings
    This shows how good his strikeout stuff is!
    
    Formula: (Strikeouts / Innings Pitched) * 9
    """
    k_per_9 = (season_dict['strikeouts'] / season_dict['innings_pitched']) * 9
    return round(k_per_9, 2)


def compare_two_seasons(season1, season2):
    """
    Compare two seasons and show what changed.
    This helps us see if Kody is improving!
    """
    year1 = season1['year']
    year2 = season2['year']
    
    print(f"\n🔄 Comparison: {year1} vs {year2}")
    print("=" * 40)
    
    # Calculate changes
    era_change = season2['era'] - season1['era']
    whip_change = season2['whip'] - season1['whip']
    k_change = season2['strikeouts'] - season1['strikeouts']
    
    # Show if it improved (negative = better for ERA/WHIP)
    print(f"ERA:        {season1['era']} → {season2['era']} ({era_change:+.2f}) {'✅ BETTER' if era_change < 0 else '❌ WORSE'}")
    print(f"WHIP:       {season1['whip']} → {season2['whip']} ({whip_change:+.2f}) {'✅ BETTER' if whip_change < 0 else '❌ WORSE'}")
    print(f"Strikeouts: {season1['strikeouts']} → {season2['strikeouts']} ({k_change:+}) {'✅ BETTER' if k_change > 0 else '❌ WORSE'}")


# ==============================================================
# PART 3: RUN THE ANALYSIS!
# ==============================================================

print("🎩 KODY FUNDERBURK - THE HAIR, THE NAME, THE PITCHER")
print("=" * 50)

# Print each season's stats
print_season_stats(kody_2024)
print_season_stats(kody_2025)
print_season_stats(kody_2026)

# Calculate strikeout rates
print("\n⚾ STRIKEOUT RATES (K/9)")
print("=" * 40)
k9_2024 = calculate_strikeout_rate(kody_2024)
k9_2025 = calculate_strikeout_rate(kody_2025)
k9_2026 = calculate_strikeout_rate(kody_2026)

print(f"2024: {k9_2024} K/9")
print(f"2025: {k9_2025} K/9")
print(f"2026: {k9_2026} K/9")

# Compare seasons
compare_two_seasons(kody_2024, kody_2025)
compare_two_seasons(kody_2025, kody_2026)

# ==============================================================
# PART 4: THE DIAGNOSIS
# ==============================================================

print("\n\n🔍 WHAT'S KODY'S DEAL?")
print("=" * 50)
print("""
✅ STRENGTHS:
   - Great strikeout stuff (9+ K/9 is elite!)
   - Big improvement from 2024 → 2025
   - Reliable arm for the bullpen

❌ WEAKNESSES:
   - HIGH WHIP: Gives up too many hits & walks
   - ERA still above 3.5 (league average for relievers ~3.8, elite <3.0)
   - Inconsistent season-to-season

🎯 TO BECOME GREAT, KODY NEEDS:
   1. BETTER CONTROL: Reduce walks (get that WHIP under 1.20)
   2. KEEP STRIKEOUTS: Maintain 10+ K/9
   3. CONSISTENCY: Avoid the 2024 regression
   4. ERA under 3.00: That's elite reliever territory
""")

print("\n" + "=" * 50)
print("💡 Next step: Scrape real Statcast data for deeper analysis!")
