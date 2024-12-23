from header import *
async def challenge(message, args):
  userid = message.author.id
  cursor.execute('SELECT * FROM betalp WHERE id=?', (userid,))
  result = cursor.fetchone()
  if result == None:
    msg = 'You do not have a league pass. Create one with !setlp'
  elif issingles(args):
    cursor.execute('SELECT badge FROM betachallenge WHERE id=? AND status="O"', (userid,))
    result = cursor.fetchone()
    if result == None:
      cursor.execute('INSERT INTO betachallenge (id, time, badge, status) VALUES (?,?,?,"O")', (userid, int(message.timestamp.timestamp()), args))
      connection.commit()
      msg = 'Challenge Submitted!'
    else:
      msg = 'You already have an open ' + result[0] + ' challenge'
  else:
    msg = args + ' is not a valid badge'
  await client.send_message(message.channel, msg)
