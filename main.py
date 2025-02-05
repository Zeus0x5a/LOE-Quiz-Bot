import discord
from discord.ext import commands
import datetime
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
print(f"Token loaded: {TOKEN}")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Define quiz questions and scoring
questions = [
    ("What is your approach to battle?\nA) I prefer to defend and counterattack. (3)\nB) I build a strategy based on terrain advantage. (2)\nC) I try to avoid fighting until I’m ready. (1)\nD) I aggressively attack the enemy. (4)", 
     {"A": 3, "B": 2, "C": 1, "D": 4}),

    ("Which type of hero appeals to you the most?\nA) Elf. (2)\nB) Warrior. (4)\nC) Something different every time. (1)\nD) Mage. (3)", 
     {"A": 2, "B": 4, "C": 1, "D": 3}),

    ("How do you react to unexpected events during the game?\nA) I adjust my plan. (3)\nB) I use pre-prepared resources. (2)\nC) I improvise on the spot. (4)\nD) I use elements of surprise. (1)", 
     {"A": 3, "B": 2, "C": 4, "D": 1}),

    ("What do you value most in gameplay?\nA) Predictability. (2)\nB) The element of surprise. (1)\nC) Stability. (3)\nD) Adrenaline. (4)", 
     {"A": 2, "B": 1, "C": 3, "D": 4}),

    ("How do you manage your resources during the game?\nA) I distribute them evenly. (2)\nB) I invest in key elements. (1)\nC) I spend everything to gain an advantage. (4)\nD) I save for difficult moments. (3)", 
     {"A": 2, "B": 1, "C": 4, "D": 3}),

    ("What do you do when the opponent is stronger than you?\nA) I retreat and look for opportunities. (1)\nB) I attack anyway. (4)\nC) I change my tactics. (2)\nD) I build a defense. (3)", 
     {"A": 1, "B": 4, "C": 2, "D": 3}),

    ("Which units are your priority?\nA) Supportive and tactical. (2)\nB) Strong and offensive. (4)\nC) Fast and agile. (1)\nD) Tough and defensive. (3)", 
     {"A": 2, "B": 4, "C": 1, "D": 3}),

    ("How do you approach risk?\nA) I avoid unnecessary risks. (3)\nB) I calculate every decision. (2)\nC) I take risks when I have an advantage. (1)\nD) I enjoy risking for big rewards. (4)", 
     {"A": 3, "B": 2, "C": 1, "D": 4}),

    ("What motivates you the most in the game?\nA) Executing a good plan. (3)\nB) Winning. (4)\nC) Fun and unpredictability. (1)\nD) Skill development. (2)", 
     {"A": 3, "B": 4, "C": 1, "D": 2}),

    ("How do you react to losing?\nA) I look for fun in the game itself. (1)\nB) I analyze my mistakes. (3)\nC) I try to get revenge immediately. (4)\nD) I learn new strategies. (2)", 
     {"A": 1, "B": 3, "C": 4, "D": 2}),

    ("Which card style do you choose?\nA) Durable units. (3)\nB) Fast abilities. (1)\nC) Surprising spells. (2)\nD) Strong units. (4)", 
     {"A": 3, "B": 1, "C": 2, "D": 4}),

    ("How do you handle time pressure?\nA) I calmly plan every step. (3)\nB) I act quickly and effectively. (4)\nC) I try to avoid such situations. (1)\nD) I use a pre-established strategy. (2)", 
     {"A": 3, "B": 4, "C": 1, "D": 2}),

    ("What is your favorite form of victory?\nA) Winning through strategy. (2)\nB) Surprising the opponent. (1)\nC) Dominating the opponent. (4)\nD) Long-term advantage. (3)", 
     {"A": 2, "B": 1, "C": 4, "D": 3}),

    ("What do you choose at the start of the game?\nA) Terrain advantage. (1)\nB) An aggressive unit. (4)\nC) Solid defense. (3)\nD) Spells. (2)", 
     {"A": 1, "B": 4, "C": 3, "D": 2}),

    ("How do you approach opponents?\nA) I wait for their move. (3)\nB) I manipulate their decisions. (2)\nC) I avoid clashes when I can. (1)\nD) I eliminate them quickly. (4)", 
     {"A": 3, "B": 2, "C": 1, "D": 4})
]

# Determine gamestyle based on total score
def get_gamestyle(score):
    if score >= 45:
        return "⚔️You are a born Conqueror! The Conqueror is an unyielding strategist, known for their ability to dictate the pace of battle through sheer aggression. You excel in fast-paced clashes where your powerful units quickly seize control of the battlefield, overwhelming opponents before they can react. With a sharp instinct for decisive action, you bolster your forces with offensive spells and take calculated risks to secure an immediate advantage. Your strength lies in swift, dominating victories, but your relentless approach requires careful resource management—lest you find yourself at a disadvantage in prolonged engagements. ⚔️"
    elif score >= 36:
        return "💥 Your alter ego is the Guardian – an unyielding defender, respected for mastery of control and endurance on the battlefield. Instead of rushing into combat, you methodically fortify your positions, patiently repelling enemy attacks until the perfect moment to strike. Your forces are built to endure, excelling in defense and resource management to outlast opponents in prolonged engagements. With a sharp tactical mind, you construct an impenetrable territory and dictate the flow of battle, ensuring no opponent can break through your meticulously crafted defenses. 💥"
    elif score >= 26:
        return "💡 Brilliant! The Strategist is your personality! You are a master tactician, renowned for your ability to outmaneuver opponents. Instead of relying on brute force, you meticulously analyze the battlefield, anticipate enemy moves, and adapt your plans to maintain control. Your strength lies in manipulation – disrupting enemy strategies, managing resources efficiently, and striking at the perfect moment to turn the tide of battle. With a sharp mind and a flexible approach, you ensure that no opponent can act without consequence, always staying one step ahead in the ever-changing flow of combat. 💡"
    else:
        return "🔥 Perfect! Trickster is your alter ego! You are like a cunning and elusive warrior who thrives on speed, deceit, and unpredictability. Instead of engaging in direct confrontations, you dance around your opponents, striking at their weak points before vanishing into the shadows. Your hit-and-run tactics and relentless adaptability make you a nightmare to pin down, always staying one step ahead. With lightning-fast reflexes and an ever-changing strategy, you ensure that no enemy can predict your next move, turning the chaos of battle into your most powerful weapon. 🔥"

# Function to log quiz results
def log_result(user, score, gamestyle):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | {user} | Score: {score} | Gamestyle: {gamestyle}\n"

    with open("quiz_results LOE-gamestyle.txt", "a") as file:
        file.write(log_entry)

@bot.command()
async def quiz(ctx):
    """Starts the quiz and logs results."""
    score = 0
    user = ctx.author

    try:
        await user.send(f"🎮 **Legends of Elysium** Playstyle Quiz starts now! - w DM. 📨")
    except discord.Forbidden:
        await ctx.send(f"{user.mention}, I can't send you a direct message (DM)! Please make sure your DMs are enabled for server members..")
        return

    def check(m):
        return m.author == user and isinstance(m.channel, discord.DMChannel)

    
    await ctx.send(f"{user.mention}, let's start the **Legends of Elysium** playstyle quiz! Your questions will be sent via DM! You have 60 seconds to answer each question 🎮" )

    for question, answers in questions:
        await user.send(question)
        try:
            msg = await bot.wait_for("message", check=check, timeout=60)
            answer = msg.content.upper()
            if answer in answers:
                score += answers[answer]
            else:
                await user.send("❌ Invalid response! Moving to the next question.")
        except:
            await user.send("⏳ Time's up! Moving to the next question.")
            

    gamestyle = get_gamestyle(score)

    try:
        await user.send(f"Your total score: **{score}**\nYour LoE playstyle is: **{gamestyle}**!")
    except:
        await ctx.send(f"{user.mention}, I couldn't DM you. Please check your privacy settings.")

    await ctx.send(f"{user.mention}, your results have been sent via DM! 🎮")

    # Log the results
    log_result(user, score, gamestyle)

bot.run(TOKEN)