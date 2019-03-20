
import datetime


import math

an = datetime.datetime.now()

# datetime.datetime.strftime(an, '%d %B %Y')

print(datetime.datetime.strftime(an, '%d.%m.%Y tarihinde buluşalım.'))

timezone = int(input("Pleas insert your time zone"))

print(timezone)

print(an.year)

k = an.year

m = an.month

i = an.day

jd = 367 * k - (7 * (k + (m + 9) / 12)) / 4 + (275 * m) / 9 + i + 1721013.5 + timezone / 24

print("ilk",jd)

if ((100 * k + m) > 190002.5):

    jd = 367 * k - (7 * (k + (m + 9) / 12)) / 4 + (275 * m) / 9 + i + 1721013.5 + timezone / 24

    print("+ lı", jd)



else:

    jd = 367 * k - (7 * (k + (m + 9) / 12)) / 4 + (275 * m) / 9 + i + 1721013.5 + timezone / 24 + 1

    print("- li", jd)


print(jd)


########jullian century########



jc=(jd-2451545)/36525

print("jullian century",jc)


###### Geom Mean Long Sun (deg) ##########


gmls=(280.46646+jc*(36000.76983 + jc*0.0003032))%360

print("Geom Mean Long Sun deg",gmls)



##### Geom Mean Anom Sun (deg)#######

gmas=357.52911+jc*(35999.05029 - 0.0001537*jc)

print("Geom Mean Anom Sun (deg)",gmas)


#######Eccent Earth Orbit##########

eeo=(0.016708634-jc*(0.000042037+0.0000001267*jc))

print("Eccent Earth Orbit:",eeo)


###### Sun Eq of Ctr############

seoc=(math.sin((gmas))*(1.914602-jc*(0.004817+0.000014*jc))+math.sin((2*gmas))*(0.019993-0.000101*jc)+math.sin((3*gmas))*0.000289)

print("Sun Eq of Ctr:",seoc)


# bu niye yanlış ???

#########  Sun True Long (deg)  #######33


stl=gmls+seoc

print("Sun True Long (deg):",stl)

# tabi bu da yanlış oluyor

########## Sun True Anom (deg) ############


sta=gmas+seoc

print("Sun True Anom (deg)",sta)

# tabi bu da yanlış oluyor

#########  Sun Rad Vector (AUs) #########

srv=(1.000001018*(1-eeo*eeo))/(1+eeo*math.cos((sta)))

print("Sun Rad Vector (AUs):",sta)

# tabi bu da yanlış oluyor

####### Sun App Long (deg)  ##########

sal=(stl-0.00569-0.00478*math.sin((125.04-1934.136*jc)))

print("Sun App Long (deg):",sal)

# tabi bu da yanlış oluyor

####### Mean Obliq Ecliptic (deg) ##########

moe=23+(26+((21.448-jc*(46.815+jc*(0.00059-jc*0.001813))))/60)/60

print("Mean Obliq Ecliptic (deg):",moe)

######### Obliq Corr (deg) #########

oc=moe+0.00256*math.cos((125.04-1934.136*jc))

print("Obliq Corr (deg):",oc)

# tabi bu da yanlış oluyor

########### Sun Rt Ascen (deg)  ########

#srta=DERECE(ATAN2(COS(RADYAN(P225));COS(RADYAN(R225))*SİN(RADYAN(P225))))

#python koda bakılacak





