import discord
import db_init
import json

current_challenge = json.load(open("challenge_info.json", "r"))

def challenges(msg, args):
    embed = discord.Embed(title=f"Active Challenges for {current_challenge['title']}",
                          color=0xff8ae8)

    embed.set_footer(text=f"End Date: {current_challenge['end_date']}")
    
    challenges = db_init.get_challenges(db_init.db_conn)
    for row in challenges:
        # Row looks like:
        # [1, 'a01', 'First Challenge', 'This challenge is about counting flowers.', '2020-12-26 01:22:26.812362']
        embed.add_field(name=f"{row[2]} / id: {row[1]}", value=row[3])

    return msg.channel.send(embed=embed)