import timg
import time
import os

#initializers

frames = 6571
fps = 0.030
elapsed = 0
delay = [0.0] * frames

delaymaxint = 0
delaymax = 0
delaylowint = 99
delaylow = 99

debug = 1
error = 0

#main code
elapsedstart = time.time()
for num in range(6571):
    obj = timg.Renderer()

    starttime = time.time()

    filename = "images/badapple"
    filename = filename + str('{0:04}'.format(num)) + ".jpg"

    obj.load_image_from_file(filename)
    obj.resize(120,90)


    #obj.render(timg.Ansi24FblockMethod) #Fancy text, but slower and unstable
    obj.render(timg.ASCIIMethod) # Basic ASCII

    delay[num] = (time.time() - starttime)

    if((time.time()-starttime < fps-0.005)):
        print ((time.time() - starttime))
        time.sleep(fps - (time.time() - starttime))

    if(debug == 1):
        elapsed = (time.time() - elapsedstart)
        if(delay[num] > fps-0.005):
            error += 1
            print("FRAME TIME LONGER THAN EXPECTED")
        print("Frame:", num, "Frame time:", round(delay[num], 4), "Elapsed time:", elapsed)

    clear = lambda: os.system('cls')
    clear()


for i in range(0, len(delay)):
    if(delay[i] > delaymax):
        delaymax = delay[i]
        delaymaxint = i
    if(delay[i] < delaylow):
        delaylow = delay[i]
        delaylowint = i

print("Longest frame:", delaymaxint, "Frame time:", delaymax)
print("Shortest frame:", delaylowint, "Frame time:", delaylow)
print("Elapsed time:", elapsed)
if(error > 0):
    print("Frames too long:", error)