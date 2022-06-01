from scamp import *
from math import lcm
from os import system

sieves=[]
list_of_mods=[]

def my_range(a,b,step):
    ruler=[a]
    start=a
    stop=b
    while a<=b:
        a+=step
        ruler.append(round(a, 3))
    return ruler

def deltas(listt):
    out=[]
    for i in range(len(listt)-1):
        out.append(listt[i+1]-listt[i])
    return out

def unique(listt):
    out=[]
    for i in range(len(listt)):
        if not out.count(listt[i])>0:
            out.append(listt[i])
    return out

def union(*lists):
    out=[]
    for i in lists:
        out=out+i
    out.sort()
    out=unique(out)
    return out

def sieve(mod=2, start=0, stop=5000):
    out=[]
    for i in range(start, stop, mod):
        out.append(i)
    return out

def concatenate(list_of_lists):
    out=[]
    for l in list_of_lists:
        for r in l:
            out.append(r)
    return out

def cond_ret(listt, threshold): #returns elements smaller than threshold
    out=[]
    for i in listt:
        if i< threshold:
            out.append(i)
    return out

def multi_sieve(nr_of_sieves):



    # ask sieve details
    for _ in range(nr_of_sieves):
        sieve_nr=_+1
        print("SIEVE " + str(sieve_nr) + " MOD.? : eg. for [0, 2, 4, 6] give 2")
        mod_of_sieve=input()
        mod_of_sieve=int(mod_of_sieve)
        list_of_mods.append(mod_of_sieve)
        # print('type start of sieve: eg. 0')
        # start_of_sieve=input()
        # print('type end of sieve: eg. 50')
        # end_of_sieve=input()
        # sieves.append(my_range(start_of_sieve, end_of_sieve, mod_of_sieve))
        sieves.append(sieve(mod_of_sieve))
        # print(sieves)



print('how many sieve layer you want?')
number_of_sieves=input()
number_of_sieves=int(number_of_sieves)

print('amount of SUBDIVISION for a quarter note: eg. for 16th note give 4')
subdivions=input()
subdivions=int(subdivions)


multi_sieve(number_of_sieves)

print("give a name to .xml file")
name_of_file=input()

period=lcm(*list_of_mods)
print('list_of_mods', list_of_mods, period)

sorted_sieves=concatenate(sieves)
sorted_sieves.sort()
sorted_sieves=unique(sorted_sieves)
sorted_sieves=cond_ret(sorted_sieves, period)

print(sorted_sieves)

sorted_sieves.append(period)
durations=deltas(sorted_sieves)

s=Session()
s.fast_forward_in_beats(float("inf"))
violin=s.new_part("Xylophon")
s.start_transcribing()
for rhy in durations:
    violin.play_note(67, 1, rhy/subdivions)

performance=s.stop_transcribing()
performance.to_score(title="Sieve", composer='Xenakis').export_music_xml(name_of_file+".xml")
system("open "+name_of_file+".xml")


# print(sieves)

# print('deltas', deltas([1,2,5,7,7,9]))
# print('unique', unique([1,1,2,3,4,4,5,6,7,7,7,7]))
# print('sieve', sieve(3, 0, 21))
# print('union', union([1,2,3, 88], [56,67,88,86,4], [3], [9,25,7]))
