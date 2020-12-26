import db_init

def hello(msg, args):
    new_user = (msg.author.id,)
    db_init.create_user(db_init.db_conn, new_user)
    return msg.channel.send(f'Hello, you got saved to the database! {msg.author.mention}')