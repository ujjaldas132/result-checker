def dobG(year):
                arr=[]
                for mon in range(1,13):
                                mon_str=str(mon)
                                if mon<10:
                                                mon_str='0'+mon_str
                                for day in range(1,32):
                                                day_str=str(day)
                                                if day<10:
                                                                day_str='0'+day_str
                                                arr.append(str(year)+'-'+mon_str+'-'+day_str)
                return arr
