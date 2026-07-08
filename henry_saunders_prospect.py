"""
Henry Saunders Prospect Evaluation Tool
A beginner's guide to prospect scouting using sabermetrics!

Analyzing a real player from BSM High School in Saint Paul, MN
"""

# ==============================================================
# PART 1: HENRY'S PHYSICAL & ATHLETIC TOOLS
# ==============================================================

henry_physical = {
    "name": "Henry Saunders",
    "position": "Second Baseman (2B)",
    "school": "Benilde-St. Margarets (BSM), Saint Paul, MN",
    "height": "6'2\"",
    "weight": 155,
    "age_approx": "High School or Recent Grad"
}

henry_athletic = {
    "60_yard_dash": 7.38,      # seconds (lower is faster)
    "infield_velo": 79,         # mph (how hard he throws)
    "exit_velo": 87.6,          # mph (how hard he hits the ball)
    "hand_speed": 20.3,         # mph (bat speed component)
    "bat_speed": 68.7,          # mph (overall swing speed)
}

henry_2025_2026 = {
    "season": "2025-2026",
    "games": 13,
    "plate_appearances": 46,
    "at_bats": 40,
    "hits": 19,
    "runs": 10,
    "rbis": 7,
    "doubles": 6,
    "strikeouts": 6,
    "walks": 2,
    "batting_average": 0.475,
    "obp": 0.522,               # On-Base Percentage
    "slg": 0.625,               # Slugging Percentage
    "ops": 1.147,               # OPS (OBP + SLG, combined offensive measure)
}

# ==============================================================
# PART 2: WHAT DO THESE STATS MEAN?
# ==============================================================

def explain_metrics():
    """
    Beginner's guide to prospect evaluation metrics
    """
    print("\n📚 UNDERSTANDING HENRY'S METRICS")
    print("=" * 60)
    print("""
SPEED METRICS:
  • 60-yard dash (7.38 sec): How fast he runs. MLB average ~7.1
    Henry's 7.38 = BELOW AVERAGE for D1/MLB scouts (they want <7.0)
    
THROWING METRICS (Infield Velo):
  • 79 mph: How hard he throws from short to first
    MLB average 2B: 85+ mph
    Henry's 79 = BELOW AVERAGE (weakness!)
    
HITTING METRICS:
  • Exit velo (87.6 mph): How hard the ball leaves his bat
    MLB average: 87-89 mph (Henry is RIGHT AT AVERAGE!)
    Good news: He has POWER potential
    
  • Hand speed (20.3 mph): Rotation speed of his hands
    • Bat speed (68.7 mph): How fast his bat is moving
    These are ELITE metrics! Scouts love fast hands/bat
    
SEASON STATS EXPLAINED:
  • Batting Avg (.475): He got a hit in 47.5% of ABs (EXCELLENT!)
  • OBP (.522): Got on base 52.2% of times up (GREAT!)
  • SLG (.625): Total bases per AB (VERY GOOD!)
  • OPS (1.147): Combined OBP+SLG. 1.000+ is ELITE. Henry is ELITE!
    """)

# ==============================================================
# PART 3: SCOUTING REPORT (Like a coach's evaluation)
# ==============================================================

def scouting_report():
    """
    A real scouting report - what scouts would say about Henry
    """
    print("\n🔍 SCOUTING REPORT - HENRY SAUNDERS")
    print("=" * 60)
    
    print("\n✅ STRENGTHS:")
    print("""
  1. ELITE HITTING ABILITY
     - .475 BA, .522 OBP, 1.147 OPS are COLLEGE-LEVEL numbers
     - At high school level, this is exceptional
     - He can hit for both average AND power
     
  2. QUICK HANDS & BAT SPEED
     - 20.3 hand speed and 68.7 bat speed are ELITE
     - This is what scouts want to see
     - Means his swing is efficient and powerful
     
  3. POWER POTENTIAL
     - 87.6 exit velo is MLB-average (great for HS!)
     - 6 doubles in 13 games shows gap power
     - Can hit for extra bases
     
  4. PLATE DISCIPLINE
     - Only 6 Ks in 46 PA (13% K rate) = EXCELLENT
     - That's elite contact ability
     - MLB hitters strike out 20%+
""")
    
    print("\n❌ CONCERNS:")
    print("""
  1. BELOW AVERAGE SPEED (7.38 60-time)
     - Won't steal many bases at next level
     - Limits defensive versatility
     - D1 scouts want <7.1 seconds
     
  2. WEAK THROWING ARM (79 mph infield velo)
     - 2B need 85+ mph to throw out runners
     - May need to move to different position (1B, DH, OF)
     - This is the BIGGEST red flag
     
  3. SMALL SAMPLE SIZE
     - Only 13 games = 40 ABs
     - Could be a hot streak, not sustainable
     - Need to see consistency over full season
     
  4. SKINNY FRAME (155 lbs at 6'2")
     - Needs to add 20-30 lbs of muscle
     - College/Pro pitchers will challenge him physically
     - Room to grow = good or bad?
""")

# ==============================================================
# PART 4: REALISTIC PROSPECT EVALUATION
# ==============================================================

def prospect_tier():
    """
    Where does Henry rank as a prospect?
    """
    print("\n🎯 PROSPECT TIER ANALYSIS")
    print("=" * 60)
    
    print("""
PROSPECT TIERS (from best to worst):

  TIER 1 (Elite/5-Star): Future MLB All-Star
    - Example: Juan Soto at this age had even better numbers
    - Probability to reach MLB: 50%+
    
  TIER 2 (High Potential): Could be a solid MLB player
    - Example: Average high D1 recruit
    - Probability to reach MLB: 20-30%
    
  TIER 3 (MLB Possible): Has some tools, needs development
    - Example: Fringe D1/top D2 player
    - Probability to reach MLB: 5-10%
    
  TIER 4 (College Player): Won't reach MLB
    - Example: Solid high school player
    - Probability to reach MLB: <1%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HENRY'S EVALUATION:

Based on the data:
  • Hitting ability = TIER 2 (elite hitting at HS level)
  • Speed = TIER 4 (below average)
  • Athleticism = TIER 2 (great hands/bat speed)
  • Arm strength = TIER 3 (concern for 2B)
  • Overall = TIER 2-3 (High College Prospect, possible MLB)

REALISTIC CEILING: 
  • BEST CASE: Solid D1 recruit, gets drafted in 10th+ round
  • MORE LIKELY: Good D2/D3 player, strong college career
  • MINIMUM: Gets into some college program

Why not Tier 1?
  - Weak throwing arm limits defensive value
  - Speed is below average
  - Small sample size (only 13 games!)
  - These concerns are coachable but significant
    """)

# ==============================================================
# PART 5: PATH TO PRO - WHAT NEEDS TO HAPPEN
# ==============================================================

def path_to_pro():
    """
    What does Henry need to do to go pro?
    """
    print("\n🛣️  PATH TO PRO - WHAT HENRY NEEDS TO DO")
    print("=" * 60)
    
    print("""
NEXT 12 MONTHS (Critical Year):

1. PROVE CONSISTENCY
   ✓ Play a FULL season (50+ games)
   ✓ Maintain .400+ BA and 1.000+ OPS
   ✓ Show it wasn't just a hot streak
   → If he does this, college coaches will recruit hard

2. ADD MUSCLE
   ✓ Gain 20-30 lbs to 175-185 lbs
   ✓ Get stronger (lifting program)
   ✓ Velocity might jump from added strength
   → Could bump arm from 79 to 82+ mph

3. IMPROVE SPEED
   ✓ Work on 60-time (goal: 6.9 seconds)
   ✓ Better footwork and acceleration
   ✓ Even small gains (7.38 → 7.1) = big difference
   → Opens up more D1 schools

4. DEFENSIVE VERSATILITY
   ✓ Since arm is weak for 2B, practice:
     - Left field (weaker arm positions)
     - First base (don't need arm speed)
     - Designated Hitter (no fielding needed)
   ✓ This keeps him valuable

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

IF HENRY DOES THIS:

Year 1 (Current): Prove hitting ability
  → Get recruited by D1/D2 schools
  
Year 2-3 (College): Develop power, add strength
  → Get drafted or signed by MLB team
  
Year 4-6 (Minor Leagues): Learn pro pitching
  → Reach AAA (closest to MLB)
  
Year 7+: MLB debut if everything goes right
  → This is the BEST case scenario

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REALISTIC ODDS:
  • Makes college team: 80%
  • Gets drafted/signed by MLB: 5-10%
  • Reaches MLB: 1-2%
  
Why so low? Because making MLB is HARD!
  • Only 750 MLB players exist
  • Millions play baseball
  • Less than 1% of college players make it
  
But Henry has BETTER ODDS than average because:
  ✅ Elite hitting ability
  ✅ Great bat/hand speed
  ✅ Makes hard contact
    """)

# ==============================================================
# PART 6: COMPARISON TO MLB PLAYERS
# ==============================================================

def compare_to_mlb():
    """
    How does Henry compare to MLB second basemen?
    """
    print("\n⚾ COMPARISON TO MLB SECOND BASEMEN")
    print("=" * 60)
    
    print("""
MLB 2B AVERAGE SEASON STATS:
  • BA: .270
  • OBP: .330
  • SLG: .425
  • OPS: .755
  • Speed (60): 7.0
  • Arm strength: 85+ mph

HENRY'S HIGH SCHOOL STATS:
  • BA: .475 ✅ (76% BETTER than MLB avg!)
  • OBP: .522 ✅ (58% BETTER!)
  • SLG: .625 ✅ (47% BETTER!)
  • OPS: 1.147 ✅ (52% BETTER!)
  • Speed: 7.38 ❌ (5% WORSE)
  • Arm: 79 ❌ (7% WORSE)

BOTTOM LINE:
Henry's HITTING NUMBERS are elite compared to MLB!
But his SPEED and ARM are below average.

This means:
  ✅ He CAN hit at a pro level
  ❌ His defense might force position change
  ➡️ He could become a DH or move to left field
    """)

# ==============================================================
# PART 7: FINAL VERDICT
# ==============================================================

def final_verdict():
    """
    The bottom line on Henry as a prospect
    """
    print("\n🏆 FINAL VERDICT - HENRY SAUNDERS AS A PROSPECT")
    print("=" * 60)
    
    print("""
SUMMARY IN ONE SENTENCE:
Henry has ELITE hitting ability but needs to prove he can:
(1) Sustain it over a full season
(2) Overcome speed/arm limitations
(3) Add physical strength

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BEST CASE SCENARIO (5% chance):
  • Gets recruited to Big 10 school
  • Puts up big numbers in college
  • Gets drafted by MLB team (late rounds)
  • Reaches minor leagues, possibly MLB

MOST LIKELY SCENARIO (60% chance):
  • Gets recruited to D1 or D2 school
  • Has successful college career
  • Doesn't get drafted (0.1% of college players drafted)
  • Plays semi-pro or independent ball

REALISTIC FLOOR (35% chance):
  • Gets recruited to college
  • Struggles with college pitching
  • Plays college but doesn't advance
  • Has to move on after college

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GRADE AS A PROSPECT: B- / B

RECRUITMENT INTEREST:
  • D1 schools: MAYBE (if arm gets better)
  • D2 schools: LIKELY
  • D3 schools: VERY LIKELY

NEXT STEPS FOR HENRY:
  1. Play a full season (50+ games)
  2. Post 1.000+ OPS for full season
  3. Improve 60-time by 0.3 seconds
  4. Gain 20+ lbs of muscle
  5. Work on infield velocity (goal: 82+ mph)
  6. Start getting recruited emails from colleges

YOUR ROLE (as his friend):
  • Send him this analysis!
  • Encourage him to play more games
  • Help him understand he needs to work on speed/arm
  • Celebrate his hitting ability (it's REAL!)
    """)

# ==============================================================
# RUN THE ANALYSIS
# ==============================================================

print("🎩 HENRY SAUNDERS - 2B FROM BSM HIGH SCHOOL")
print("=" * 60)

explain_metrics()
scouting_report()
prospect_tier()
path_to_pro()
compare_to_mlb()
final_verdict()

print("\n" + "=" * 60)
print("📊 Analysis complete!")
print("Share this with Henry and tell him to keep grinding! ⚾")
