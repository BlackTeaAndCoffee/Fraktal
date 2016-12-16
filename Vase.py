from __future__ import division
from pyx import *


def draw_Vase(vase,farbe):
    for i in range(len(vase)-1):
        #print koord_vase[i]#, *koord_vase[i+1]
        c.stroke(path.line(vase[i][0], vase[i][1],
            vase[i+1][0],vase[i+1][1]),[style.linewidth(0.01),farbe])

def vase_evolution(vase_eins, N):

    for j in range(N):
        len_vase_1 = len(vase_eins)
        vase_2 = []

        for i in range(len_vase_1 - 1):
            x_2 = vase_eins[i+1][0]
            x_1 = vase_eins[i][0]
            y_2 = vase_eins[i+1][1]
            y_1 = vase_eins[i][1]

            a = x_1 - x_2
            b = y_1 - y_2
            print a, b
            if a < 0:
                a = abs(a)
                vase_2.append([x_1,       y_1])
                vase_2.append([x_1 + a/3, y_1])
                vase_2.append([x_1 + a/3, y_1 - a/3])
                vase_2.append([x_1 + a*2/3, y_1 - a/3])
                vase_2.append([x_1 + a*2/3, y_2])
                vase_2.append([x_2, y_2])
            elif a  > 0:
                a = abs(a)
                vase_2.append([x_1,       y_1])
                vase_2.append([x_1 - a/3, y_1])
                vase_2.append([x_1 - a/3, y_1 + a/3])
                vase_2.append([x_1 - a*2/3, y_1 + a/3])
                vase_2.append([x_1 - a*2/3, y_2])
                vase_2.append([x_2, y_2])
            elif b  < 0:
                b = abs(b)
                vase_2.append([x_1,       y_1])
                vase_2.append([x_1, y_1 + b/3])
                vase_2.append([x_1 + b/3, y_1 + b/3])
                vase_2.append([x_1 + b/3, y_1 + b*2/3])
                vase_2.append([x_1, y_1 + b*2/3])
                vase_2.append([x_1, y_2])
            elif b  > 0:
                b = abs(b)
                vase_2.append([x_1,       y_1])
                vase_2.append([x_1, y_1 - b/3])
                vase_2.append([x_1 - b/3, y_1 - b/3])
                vase_2.append([x_1 - b/3, y_1 - b*2/3])
                vase_2.append([x_1, y_1 - b*2/3])
                vase_2.append([x_1, y_2])
        #print 'vase2',vase_2
        vase_eins = vase_2
        #zeichne_Vase(vase_eins, liste_farbe[j])

        #print 'vase1', vase_eins
    return vase_eins


if __name__ == "__main__":
    N = 5

    c = canvas.canvas()

    koord_vase = [[0,0], [1,0], [1,-1], [2,-1], [2,0], [3,0] ]
    draw_Vase(koord_vase, color.rgb.green)


    liste_farbe = [color.rgb.red, color.rgb.blue, color.rgb.green]



    vase_mase = vase_evolution(koord_vase, N)
    draw_Vase(vase_mase, color.rgb.blue)
    #zeichne_Vase(koord_vase, color.rgb.green)

    c.writePDFfile('Vase,N=%d' %(N))


