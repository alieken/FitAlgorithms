out = open("output.txt", "w")

def first_fit(mem,pro):
    #fonksiyon içinden eriştiğimiz için out'u global tanımladık 12. satıra kadar da dosyaya yazma işlemleri
    global out
    out.write("First-Fit Memory Allocation\n\n")
    out.write("------------------------------------\n\n")
    out.write("start =>")
    for i in mem:
        out.write(" "+str(i))
    out.write("\n\n")
    for i in range(0,len(pro)):
        #bu kontrol ise eğer hiç uygun bulamazsa not allocated kısmını yazdırmak için
        kontrol=False
        for j in range(0,len(mem)):
            if(mem[j]>pro[i]):
                kontrol=True
                #burada diziye 1 eleman ekliyorum. Sebebi ise bulduğu yerden itibaren hepsini sağa doğru taşıyorum. İndex hatası vermemesi için ekleme yaptım.
                mem.append(-1)
                mem[j+1:len(mem)]=mem[j:len(mem)-1]
                mem[j+1]=mem[j]-pro[i]
                #sağa taşıdığımızda 1 eleman boşta kaldı o kalan yere de processin negatif halini aldım ki dosyaya yazdırırken farkı görebilelim.
                mem[j]=-1*pro[i]
                out.write(str(pro[i])+" =>")
                #her process için işlem bittiğinde dosyaya yazdırma işlemi
                for i in mem:
                    if i < 0:
                        #allocated işlemi için yıldızlı yazdırma
                        out.write(" "+str((-1*i))+"*")
                    elif i==0:
                        continue
                    else:
                        out.write(" "+str(i))
                #bu \n ise dosyada satır atlamamızı sağlar. 2 tane konulursa 2 satır atlar
                out.write("\n\n")
                break
        if kontrol==False:
            out.write(str(pro[i])+" => not allocated, must wait")
            out.write("\n\n")


def best_fit(mem,pro):
    global out
    out.write("Best-Fit Memory Allocation\n\n")
    out.write("------------------------------------\n\n")
    out.write("start =>")
    for i in mem:
        out.write(" "+str(i))
    out.write("\n\n")
    for i in range(0,len(pro)):
        #burada farkı büyük tanımladım istersen daha da arttırabilirsin.
        fark=100000
        index=-1
        for j in range(0,len(mem)):
            #en küçük farkı bulma işlemi
            islem=mem[j]-pro[i]
            if islem >= 0 and islem<fark:
                fark=islem
                index=j
        #eğer uygun bulamazsa not allocated
        if index==-1:
            out.write(str(pro[i])+" => not allocated, must wait")
            out.write("\n\n")
            continue
        #first fit ile aynı şeyler
        mem.append(-1)
        mem[index+1:len(mem)]=mem[index:len(mem)-1]
        mem[index+1]=mem[index]-pro[i]
        #sağa taşıdığımızda 1 eleman boşta kaldı o kalan yere de processin negatif halini aldım ki dosyaya yazdırırken farkı görebilelim.
        mem[index]=-1*pro[i]
        out.write(str(pro[i])+" =>")
        #her process için işlem bittiğinde dosyaya yazdırma işlemi
        for i in mem:
            if i < 0:
                out.write(" "+str((-1*i))+"*")
            elif i ==0:
                continue
            else:
                out.write(" "+str(i))
        
        #bu \n ise dosyada satır atlamamızı sağlar. 2 tane konulursa 2 satır atlar
        out.write("\n\n") 

#worst fit tamamen best fitle aynı diyebiliriz. Sadece 98.satır ve 94.satır farklı yani fark=0 ve islem>fark oldu
def worst_fit(mem,pro):
    global out
    out.write("Worst-Fit Memory Allocation\n\n")
    out.write("------------------------------------\n\n")
    out.write("start =>")
    for i in mem:
        out.write(" "+str(i))
    out.write("\n\n")
    for i in range(0,len(pro)):
        fark=0
        index=-1
        for j in range(0,len(mem)):
            islem=mem[j]-pro[i]
            if islem >= 0 and islem>fark:
                fark=islem
                index=j
        if index==-1:
            out.write(str(pro[i])+" => not allocated, must wait")
            out.write("\n\n")
            continue
        mem.append(-1)
        mem[index+1:len(mem)]=mem[index:len(mem)-1]
        mem[index+1]=mem[index]-pro[i]
        #sağa taşıdığımızda 1 eleman boşta kaldı o kalan yere de processin negatif halini aldım ki dosyaya yazdırırken farkı görebilelim.
        mem[index]=-1*pro[i]
        out.write(str(pro[i])+" =>")
        #her process için işlem bittiğinde dosyaya yazdırma işlemi
        for i in mem:
            if i < 0:
                out.write(" "+str((-1*i))+"*")
            elif i ==0:
                continue
            else:
                out.write(" "+str(i))
        
        #bu \n ise dosyada satır atlamamızı sağlar. 2 tane konulursa 2 satır atlar
        out.write("\n\n") 
    
#Dosyayı okuma işlemi
f = open("input.txt", "r")
#tüm dosyayı ayıklamak durumunda kalmamak için 1 satır okuyup gerekli eşleştirmeyi yapıyoruz
memory=f.readline()
process=f.readline()
#dosya kapatma
f.close()
#her satırın sonunda \n karakteri bulunduğu için bunu çıkarıyoruz. Bu karakter satır atlamak için bulunur.9 ve 10. satırları yorum satırına alıp çıktıdaki farkı görebilirsiniz
memory=memory.replace("\n","")
process=process.replace("\n","")
print(memory)
print(process)
#alt 2 satırda string halde bulunan iki değişkeni dizi haline çeviriyoruz ki içlerinde gezmemiz daha kolay olsun
memories=memory.split(",")
processes=process.split(",")
print(memories)
print(processes)
#ekleme çıkarma gibi işlemler olduğu için dizileri int haline çevirdik
for i in range(0,len(memories)):
    memories[i]=int(memories[i])
for i in range(0,len(processes)):
    processes[i]=int(processes[i])
orjmem=[]
#memories kopyalandı
orjmem[:]=memories
first_fit(memories,processes)
memories[:]=orjmem
best_fit(memories,processes)
memories[:]=orjmem
worst_fit(memories,processes)