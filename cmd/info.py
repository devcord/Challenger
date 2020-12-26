import discord
import db_init

def info(msg, args):
    challenge_id = args[0]

    def find_challenge(conn):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM challenges WHERE challenge_id = '{challenge_id}'")

        result = cur.fetchall()
            
        return result[0]

    challenge_info = find_challenge(db_init.db_conn)
    
    embed = discord.Embed(title=f"{challenge_info[2]} / id: {challenge_info[1]}",
                          description=f"```{challenge_info[3]}```",
                          color=0xff8ae8)
    
    return msg.channel.send(embed=embed)
