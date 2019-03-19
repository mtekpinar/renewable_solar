
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
