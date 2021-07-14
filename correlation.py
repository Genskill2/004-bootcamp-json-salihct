# Add the functions in this file
import json
import math

def load_journal(path):
    f = open(path)
    journal = json.load(f)
    f.close()
    return journal

# print(load_journal('journal.json'))

def compute_phi(path,event):
    journal = load_journal(path)
    n11, n00, n10, n01 = 0, 0, 0, 0
    for item in journal:
        if event in item['events']:
            if item['squirrel'] == True:
                n11 += 1 
            else:
                n10 += 1
        elif item['squirrel'] == True:
            n01 += 1
        else:
            n00 += 1
    n1p = n11 + n10
    n0p = n01 + n00
    np0 = n00 + n10
    np1 = n11 + n01
    corr = (n11 * n00 - n10 * n01) / math.sqrt(n1p * n0p * np1 * np0)
    return corr


def compute_correlations(path):
    corr = {}
    journal = load_journal(path)
    for item in journal:
        for e in item["events"]:
            if e not in corr:
                corr[e] = compute_phi(path,e)
    return corr


def diagnose(path):
    corr = compute_correlations(path)
    key_list = list(corr.keys())
    val_list = list(corr.values())
    hp = val_list.index(max(val_list))
    hp_event = key_list[hp]
    hn = val_list.index(min(val_list))
    hn_event = key_list[hn]
    return hp_event, hn_event
