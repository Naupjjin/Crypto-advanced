from gmpy2 import gcdext
from Crypto.Util.number import *

e1 = 257
e2 = 65537
n = 107984125552565429663054372186495230124351130345608465380931041268073305908583805561833667111573963519030951139687252061926293112686471383006719215723394085297015158097094164886658894334255759014116833921891916288266262342803709278191924287818066509792029295844090166409801968471680897669457854584574184542551       
c1 = 69211662336569578115558268929241336604361048311798615310178171341548419068041314645881086501401867409289588912600400040604732401114597187206451992327236255487354452277955397645441001260301770967532594690008490623938856396261922818458236843801348376967944202140715181016613505402175105145050216008315692967555       
c2 = 44660353296784457219248172580070464765952167807477094927008743892660625160454581941198466797494547473023662029349531718044018672161977136521145062613334596249847870896102823283654893696735915688468889472140672424846797563413479146874362525604117142578458428223275298780028617444416299355195177836364608916708       

_, t, u = gcdext(e1, e2)
m = pow(c1, t, n) * pow(c2, u, n) % n
print(long_to_bytes(m))