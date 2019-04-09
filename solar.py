
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



#=4*DERECE(U92*SİN(2*RADYAN(I92))-2*K92*SİN(RADYAN(J92))+4*K92*U92*SİN(RADYAN(J92))*COS(2*RADYAN(I92))-0,5*U92*U92*SİN(4*RADYAN(I92))-1,25*K92*K92*SİN(2*RADYAN(J92)))


eot=4*math.degrees((vary*math.sin(math.radians(2*gmls))-2*eeo*math.sin(math.radians(gmas))+4*eeo*vary*math.sin(math.radians(gmas))*math.cos(math.radians(2*gmls))-0.5*vary*vary*math.sin(math.radians(4*gmls))-1.25*eeo*eeo*math.sin(math.radians(2*gmas))))





print("Eq of Time:",eot)


#yanlış oldu, artık doğru 09.04.2019



##############  HA Sunrise (deg)  #############

# =DERECE(ACOS(COS(RADYAN(90,833))/(COS(RADYAN($B$3))*COS(RADYAN(T131)))-TAN(RADYAN($B$3))*TAN(RADYAN(T131))))
latitute=40

has=math.degrees(math.acos(math.cos(math.radians(90.833))/(math.cos(math.radians(latitute))*math.cos(math.radians(sd)))-math.tan(math.radians(latitute))*math.tan(math.radians(sd))))


print("HA Sunrise (deg): ", has)



################## Solar Noon (LST)  ###################3


longitute= 30 

# =(720-4*$B$4-V7+$B$5*60)/1440

solnoon=((720-4*longitute-eot+timezone*60)/1440)

solnoontime=((720-4*longitute-eot+timezone*60)/1440)*24

# * 24 yapınca tuttu ya la :)


print("Solar Noon (LST) :",solnoontime)




#############  Sunrise Time (LST)  ##############


# =X2-W2*4/1440

srtime=solnoon-has*4/1440

srtime24=(solnoon-has*4/1440)*24

# 6,53 demek 6:32 demek

print("Sunrise Time (LST): ",srtime24)


############ Sunset Time (LST)  ###############

#X4+W4*4/1440

sstime=solnoon+has*4/1440

sstime24=(solnoon +has*4/1440)*24

# 6,53 demek 6:32 demek

print("Sunset Time (LST) : ",sstime24)

#################  Sunlight Duration (minutes)  ################


# =8*W132

sld=8*has

print("Sunlight Duration (minutes): ",sld)


############### True Solar Time (min)  ##################
# e= anlık zaman BUrada anlık zmaan nasıl girilicek 0.58 gibi yani 13:00
#v=eot
#b4=longitute
#b5=timezone

#=MOD(E6*1440+V6+4*$B$4-60*$B$5;1440)

tst=(((an.hour/24)*1440*eot*longitute-60*timezone)%1440)


print("True Solar Time (min)",tst)

print("saat:",an.hour/24)


#  Bu yanlış oldu



#############  Hour Angle (deg)  ##################


#=EĞER(AB9/4<0;AB9/4+180;AB9/4-180)










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
