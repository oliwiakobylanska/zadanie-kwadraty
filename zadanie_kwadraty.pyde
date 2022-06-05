class Kwadrat():
    def __init__(self, bok): 
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class PasiastyKwadrat(Kwadrat): 
    def sketchPasiasty(self, x, y, paski): 
        Kwadrat.sketch(self, x, y) 
        space = self.bok/paski 
        _xLinii_ = 0 
        fill(400,90,70,80)
        for pasek in range(0, paski): 
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
            
class KraciastyKwadrat(Kwadrat): 
    def sketchKraciasty(self, x, y, paski):  # nie tyle kraciasty, co w paski poziome zamiast pionowych
        Kwadrat.sketch(self, x, y) #gdybyś tu dałą pasiasty i odziedziczyłą z niego, wówczas mógłby wyjść kraciasty
        space = self.bok/paski 
        _yLinii_ = 0 
        fill(400,90,70,80)
        for pasek in range(0, paski): 
            line(x, y+_yLinii_, x+self.bok, y+_yLinii_)
            _yLinii_ += space

def setup():
    size(500, 500)
    malyKwadrat = Kwadrat(50.0) # obiekt typu kwardrat o wielkości 50
    malyKwadrat.sketch(200, 300) # rysujemy go w podanych wsółrzędnych
    fill(100,100,40,100) 
    duzyKwadrat = Kwadrat(200.0)
    duzyKwadrat.sketch(50, 75)
    fill(90,400,20,25)
    malyKwadrat.sketch(100, 200) # rysujemy kwadrat wielkości 50 również w innych współrzędnych
    malyPasiastyKwadrat = PasiastyKwadrat(30.0) # tu tworzymy obiekt typu pasiasty kwadrat korzystając z konstruktora klasy bazowej
    malyPasiastyKwadrat.sketchPasiasty(300, 300, 5) # umieszczamy stworzony kwadrat w 5 pasków w tych współrzędnych
    malyPasiastyKwadrat.sketchPasiasty(100,300, 8) # a teraz w 8 pasów w innych współrzędnych
    duzyPasiastyKwadrat  = PasiastyKwadrat(120.0)
    duzyPasiastyKwadrat.sketchPasiasty(300, 50, 12)
    duzyPasiastyKwadrat.sketch(350, 300) # na obiekcie typu klasy pochodnej można wywołać metodę klasy bazowej ( rysujemy kwadrat bez pasków )
    malyKraciastyKwadrat = KraciastyKwadrat(120.0) # miały być dwa obiekty
    malyKraciastyKwadrat.sketchKraciasty(300,50,12)
    malyKraciastyKwadrat.sketchKraciasty(50,360,10)#obiekt jest ten sam, tylko drugi raz narysowany
    
    #1,75 pkt
