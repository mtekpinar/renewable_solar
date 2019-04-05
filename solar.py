
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

print("first julian day",jd)

if ((100 * k + m) > 190002.5):

    jd = 367 * k - (7 * (k + (m + 9) / 12)) / 4 + (275 * m) / 9 + i + 1721013.5 + timezone / 24

    print("+ lı", jd)



else:

    jd = 367 * k - (7 * (k + (m + 9) / 12)) / 4 + (275 * m) / 9 + i + 1721013.5 + timezone / 24 + 1

    print("- li", jd)


print("Bu da muhtemelen lı day ve tüm hesapta kullanılan",jd)


########jullian century########



jc=(jd-2451545)/36525

print("jullian century",jc)

#(F189-2451545)/36525


###### Geom Mean Long Sun (deg) ##########

#MOD(280,46646+G189*(36000,76983 + G189*0,0003032);360)

gmls=(280.46646+jc*(36000.76983 + jc*0.0003032))%360

print("Geom Mean Long Sun deg",gmls)



##### Geom Mean Anom Sun (deg)#######

#357,52911+G189*(35999,05029 - 0,0001537*G189)

gmas=357.52911+jc*(35999.05029 - 0.0001537*jc)

print("Geom Mean Anom Sun (deg)",gmas)


#######Eccent Earth Orbit##########

#0,016708634-G189*(0,000042037+0,0000001267*G189)

eeo=(0.016708634-jc*(0.000042037+0.0000001267*jc))

print("Eccent Earth Orbit:",eeo)


###### Sun Eq of Ctr############

#SİN(RADYAN(J189))*(1,914602-G189*(0,004817+0,000014*G189))+SİN(RADYAN(2*J189))*(0,019993-0,000101*G189)+SİN(RADYAN(3*J189))*0,000289

seoc=(math.sin(math.radians(gmas))*(1.914602-jc*(0.004817+0.000014*jc))+math.sin(math.radians(2*gmas))*(0.019993-0.000101*jc)+math.sin(math.radians(3*gmas))*0.000289)


print("Sun Eq of Ctr:",seoc)


# bu niye yanlış ???

#artık yanlış değil 05.04.2019

#########  Sun True Long (deg)  #######33


stl=gmls+seoc

print("Sun True Long (deg):",stl)

# tabi bu da yanlış oluyor

########## Sun True Anom (deg) ############


sta=gmas+seoc

print("Sun True Anom (deg)",sta)

# tabi bu da yanlış oluyor
#artık hemen hemen doğru 05.04.2019

#########  Sun Rad Vector (AUs) #########

#(1,000001018*(1-K131*K131))/(1+K131*COS(RADYAN(N131)))
srv=(1.000001018*(1-eeo*eeo))/(1+eeo*math.cos(math.radians(sta)))

print("Sun Rad Vector (AUs):",srv)



####### Sun App Long (deg)  ##########

#=M104-0,00569-0,00478*SİN(RADYAN(125,04-1934,136*G104))

sal=(stl-0.00569-0.00478*math.sin(math.radians(125.04-1934.136*jc)))

print("Sun App Long (deg):",sal)

# tabi bu da yanlış oluyor

####### Mean Obliq Ecliptic (deg) ##########

moe=23+(26+((21.448-jc*(46.815+jc*(0.00059-jc*0.001813))))/60)/60

print("Mean Obliq Ecliptic (deg):",moe)

######### Obliq Corr (deg) #########

oc=moe+0.00256*math.cos((125.04-1934.136*jc))

print("Obliq Corr (deg):",oc)

# tabi bu da yanlış oluyor düzeldi 05.04.2019

########### Sun Rt Ascen (deg)  ########

#05.04.2019



#srta=DERECE(ATAN2(COS(RADYAN(P225));COS(RADYAN(R225))*SİN(RADYAN(P225))))

#srtaatan2=ATAN2(COS(RADYAN(P225));COS(RADYAN(R225))*SİN(RADYAN(P225)))



#atan2(y, x) returns value of atan(y/x) in radians. The atan2() method returns a numeric value between –\pi and \pi representing the angle \theta of a (x, y) point and positive x-axis.

srtaatan2=math.atan2(math.cos(math.radians(sal)),math.cos(math.radians(oc))*math.sin(math.radians(sal)))

srta=math.degrees(math.atan2(math.cos(math.radians(sal)),math.cos(math.radians(oc))*math.sin(math.radians(sal))))

print("dereceye çevirmeden ki hala yanlış",math.degrees(srtaatan2),srtaatan2,math.degrees(srtaatan2),srta)
 
# Yanlış bu nedense



######### Sun Declin (deg) ################

#DERECE(ASİN(SİN(RADYAN(R110))*SİN(RADYAN(P110))))
#=DERECE(ASİN(SİN(RADYAN(R130))*SİN(RADYAN(P130))))

# öncelikle bu radian içine yazılınca ne oluyor degree yaılınca ne oluyor onu kesin bil

sdradian=math.asin(math.sin(math.radians(oc))*math.sin(math.radians(sal)))
sd=math.degrees(sdradian)

print("Sun Declin (deg):",sd)


##################  var y   ######################

#=TAN(RADYAN(R85/2))*TAN(RADYAN(R85/2))

vary=math.tan(math.radians(oc/2))*math.tan(math.radians(oc/2))

print("Var y:",vary)



###################  Eq of Time (minutes) #####################
#u=vary
#k=eeo
#I =gmls
#j=gmas

#=4*DERECE(U85*SİN(2*RADYAN(I85))-2*K85*SİN(RADYAN(J85))+4*K85*U85*SİN(RADYAN(J85))*COS(2*RADYAN(I85))-0,5*U85*U85*SİN(4*RADYAN(I85))-1,25*K85*K85*SİN(2*RADYAN(J85)))
eot=4*(math.degrees(vary*math.sin(2*math.radians(gmls))-(2*eeo*math.sin(math.radians(gmas)))+4*eeo*(math.sin(math.radians(gmas)))*(math.cos(2*(math.radians(gmls))))-0.5*vary*vary*(math.sin(4*(math.radians(gmls))))-1.25*eeo*eeo*(math.sin(2*(math.radians(gmas))))))

print("Eq of Time:",eot)

#yanlış oldu











"""
import math


print("ilk ve DOĞRU ",math.sin(math.pi/6))

print("ikinci ve YANLIŞ ",math.sin(math.degrees(math.pi/6)))
#Yukarıdaki print(math.sin(30)) ile aynı demek yani içine rakam yazınca önüne math.degrees yazmalısın
# bu da tüm hesaplamalarını değiştiririr 

# BUNU KULLANMA KESİNLİKLE


print("Radyanı dereceye Çivirir:",math.degrees((math.pi)/6))

# BU RADYAN CİNSİNDEN OLANI DERECEYE ÇEVİRİR SADECE DERECEYE İHTYANCIN VARSA KULLAN

print("üçüncü ve DOĞRU",math.sin(math.radians(30)))

# math.radians(30) dereceyi radyana çevirip yazınca DÜZGÜN OLUYOR

# !!!!! DERECE CİNSİNDEN GİRİLEN DEĞERLERİ BÖYLE YAZ !!!!!!!!!!!!



"""
