import notify2
from pycricbuzz import Cricbuzz
import time
import os
c = Cricbuzz()

def all_matches():
    match_data = c.matches()
    matches = []
    for match in match_data:
        matches.append(match['id'])
    return matches


def live_score(id):
    data = c.livescore(id)
    
    notify2.init('Cricket Score')
    ICON_PATH = os.getcwd() + "/image/cric.png"
    score = "{}, {} lose of {} wicket in {} overs".format(data['batting']['team'], data['batting']['score'][0]['runs'], data['batting']['score'][0]['wickets'], data['batting']['score'][0]['overs'])
    print(score)

    n = notify2.Notification('Cricket Score', score, icon=ICON_PATH )

    n.set_urgency(notify2.URGENCY_NORMAL)
    n.show()

    return score



def main():
    matches =all_matches()

    while True:
        score = live_score(matches[0])
        time.sleep(60)

if __name__ == '__main__':
    main()

