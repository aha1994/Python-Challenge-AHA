import csv
import os
path = os.path.join("Resources", "election_data.csv")
with open(path, 'r') as pdata:
    csvreader = csv.reader(pdata, delimiter=',')
    csv_head = next(csvreader)
    voter_ids = []
    votes_received = []
    for each in csvreader:
        voter_ids.append(each[0])
        votes_received.append(each[2])
    ovotes = 0
    kvotes = 0
    lvotes = 0
    cvotes = 0
    for vote in votes_received:
        if vote == "O'Tooley":
            ovotes += 1
        elif vote == 'Khan':
            kvotes += 1
        elif vote == 'Li':
            lvotes += 1
        elif vote == 'Correy':
            cvotes += 1
    results = {
        "O'Tooley": ovotes,
        'Khan': kvotes,
        'Li': lvotes,
        'Correy': cvotes,
    }
    num_votes = len(voter_ids)
    candidates = set(votes_received)
    per_otooley = round(((ovotes/num_votes)*100), 4)
    per_khan = round(((kvotes/num_votes)*100), 4)
    per_li = round(((lvotes/num_votes)*100), 4)
    per_correy = round(((cvotes/num_votes)*100), 4)
    winner = ''
    if ovotes > kvotes and ovotes > lvotes and ovotes >cvotes:
        winner = "O'Tooley"
    elif kvotes > ovotes and kvotes > lvotes and kvotes > cvotes:
        winner = 'Khan'
    elif lvotes > ovotes and lvotes > kvotes and lvotes > cvotes:
        winner = 'Li'
    else:
        winner = 'Correy'
    print('Election Results\n----------------------------')
    print('Total Votes: %s\n----------------------------' % num_votes)
    print('Khan: {}% ({})'.format(per_khan, kvotes))
    print('Correy: {}% ({})'.format(per_correy, cvotes))
    print('Li: {}% ({})'.format(per_li, lvotes))
    print("O'Tooley: {}% ({})".format(per_otooley, ovotes))
    print("----------------------------\nWinner: %s\n----------------------------" % winner)
    with open("election_results.txt", 'w') as results:
        results.write('Election Results\n----------------------------\n')
        results.write('Total Votes: %s\n----------------------------\n' % num_votes)
        results.write('Khan: {}% ({})\n'.format(per_khan, kvotes))
        results.write('Correy: {}% ({})\n'.format(per_correy, cvotes))
        results.write('Li: {}% ({})\n'.format(per_li, lvotes))
        results.write("O'Tooley: {}% ({})\n".format(per_otooley, ovotes))
        results.write("----------------------------\nWinner: %s\n----------------------------" % winner)