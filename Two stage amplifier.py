import schemdraw
import schemdraw.elements as element

ground = element.Ground().color('indigo')

with schemdraw.Drawing() as d:
    mini = d.unit*0.1   # for minimizing element size

    # Input source terminal    
    d += ground
    d += element.Line().up(d.unit*0.7)
    d += (Vg:= element.SourceSin().up(mini).scale(1.3).color('blue').label('$V_g$'))
    d += element.Line().up(d.unit*0.8)
    d += element.Line().right(d.unit*0.5)
    d += (Rg:= element.Resistor().right(mini).color('violet').label("$R_G$"))
    d += element.Line().right(d.unit*0.6)
    d += (Cg:= element.Capacitor2().right(mini).color('cyan').scale(1.5))
    d += element.Line().right(d.unit*0.5).dot()
    
    # 1st stage loop
    d += element.Line().up(d.unit*0.5)
    d += (R1:= element.Resistor().up(mini).color('violet').label("$R_1$",loc ='bot'))
    d += element.Line().up(d.unit*0.5)
    d += element.Line().right(d.unit*1.2)
    d.push()
    d += element.Line().down(d.unit*0.5).idot()
    d += (Rc:= element.Resistor().down(mini).dot().color('violet').label("$R_C$",loc ='bot'))
    d += (RcL:= element.Line().down(d.unit*0.5))
    d += (Q1:= element.BjtNpn(circle = True).right().anchor('collector').scale(1.5).color('blue').label('$Q_1$'))
    d += (ReL:= element.Line().down(d.unit*0.5).at(Q1.emitter))
    d += (Re:= element.Resistor().down(mini).color('violet').label('$R_E$',loc ='bot'))
    d += element.Line().down(d.unit*0.4)
    d += element.Ground().color('indigo')
    d += element.Line().down(d.unit*1.5).at(R1.start)
    d += (R2:= element.Resistor().down(mini).color('violet').label('$R_2$',loc ='bot'))
    d += element.Line().down(d.unit*0.6)
    d += element.Ground()
    d += element.Line().left().at(Q1.base).tox(R2.start).dot()
    d += element.Line().right(d.unit*0.8).idot().at(ReL.center)
    d += element.Line().down(d.unit*0.5)
    d += (CE1:= element.Capacitor2().down(mini).color('cyan').scale(1.5))
    d += element.Line().down(d.unit*0.4)
    d += element.Ground().color('indigo')
    
    d.pop()
    d += element.Line().right(d.unit*1.5)
    d.push()

    #2nd stage loop 
    d += element.Line().down(d.unit*0.5).idot()
    d += (R12:= element.Resistor().down(mini).color('violet').label("$R_1$",loc ='bot'))
    d += (R12L:= element.Line().down(d.unit*1.5))
    d += (R22:= element.Resistor().down(mini).color('violet').label("$R_2$",loc ='bot'))
    d += element.Line().down(d.unit*0.6)
    d += element.Ground()
    d.pop()
    d += element.Line().right(d.unit*1.2)
    d.push()
    d += element.Line().down(d.unit*0.5)
    d += (Rc2:= element.Resistor().down(mini).color('violet').label("$R_C$",loc ='bot'))
    d += (Rc2L:= element.Line().down(d.unit*0.5))
    d += (Q2:= element.BjtNpn(circle = True).right().anchor('collector').color('blue').scale(1.5).label("$Q_2$"))
    d += (ReL:= element.Line().down(d.unit*0.5).at(Q2.emitter))
    d += (Re2:= element.Resistor().down(mini).color('violet').label("$R_E$",loc ='bot'))
    d += element.Line().down(d.unit*0.4)
    d += element.Ground().color('indigo')
    d += element.Line().left().at(Q2.base).tox(R22.start).dot()
    d += element.Line().right(d.unit*0.8).idot().at(ReL.center)
    d += element.Line().down(d.unit*0.5)
    d += (CE2:= element.Capacitor2().down(mini).color('cyan').scale(1.5))
    d += element.Line().down(d.unit*0.4)
    d += element.Ground().color('indigo')
    d += element.Line().right(d.unit*0.7).at(RcL.center).idot()
    d += element.Capacitor2().right(mini).color('cyan').scale(1.5)
    d += element.Line().tox(R12L.center).dot()

    d.pop()
    d += element.Line().idot().dot(open=True).scale(2).label('$+V_{CC}$',loc = 'right') # Vcc

    # output terminal
    d += element.Line().right(d.unit*0.8).idot().at(Rc2L.center)
    d += (CL:= element.Capacitor2().right(mini).color('cyan').scale(1.5))
    d += element.Line().right(d.unit*0.8)
    d += element.Line().down()
    d += (RL:= element.Resistor().down(mini).color('violet').label("$R_L$",loc ='bot'))
    d += element.Line().down(d.unit*0.85)
    d += element.Ground().color('indigo')
    
