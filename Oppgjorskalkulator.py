"""
Script for oppgjør. Regne ut kvitteringer.
    
"""

class Oppgjor:
    def __init__(self, antall_personer, mat = 0, transport = 0, annet = 0, ):
        self.antall_personer = antall_personer
        self.mat = mat
        self.transport = transport
        self.annet = annet

    def total_kostnad(self):
        """Regner ut den totale kostnaden for hele turen med alt inkludert.

        Returns:
            float: Totalt beløp i kr
        """
        total_kostnad = self.mat + self.transport + self.annet
        return total_kostnad
    
    def kostnad_per_person(self):
        """Regner ut for mye det blir for hver person å betale

        Returns:
            float: Hver enkelt sitt beløp
        """
        per_person = self.total_kostnad() / self.antall_personer
        return per_person

    # def transportutgift(self, kilometer, pris_per_kilometer, bomstasjoner):
    #     total_bomkostnad = sum(bomstasjoner)
    #     self.transport += (kilometer * pris_per_kilometer) + total_bomkostnad
        
    def kilometer_godtgjorelse(self, liter_per_km, kr_per_kilometer, km):
        """Regner ut kilometergodtgjørelsen. Metoden tar parametrene liter per km, kr per km, 
        og hvor langt i km.

        Args:
            liter_per_km (float): ex.: 0.06
            kr_per_kilometer (float): ex.: 18
            km (float): ex.: 100
        """
        #kostnad = (liter_per_km * kr_per_kilometer) * km
        steg_1 = liter_per_km * kr_per_kilometer
        steg_2 = steg_1 * km
        self.transport += steg_2
        #self.transport += kostnad
        
    def mat_utgifter(self, belop):
        self.mat += belop
        
    def vis_oppgjoret(self):
        return f"""
        kilometergodtgjørelse: {self.transport} kr
        Matutgifter: {self.mat} kr
        Total kostnad: {self.total_kostnad()} kr
        Kostnad per person: {self.kostnad_per_person()} kr
        """

if __name__ == "__main__":
    from gui import start_gui
    start_gui()
    


        #print(f"Transportutgift med bompasseringer: {self.transport} kr")
        # print(f"Kilometergodtgjørelse: {self.transport} kr")
        # print(f"Matutgifter: {self.mat} kr")
        # print(f"Total kostnad: {self.total_kostnad()} kr")
        # print(f"Kostnad per person: {self.kostnad_per_person()} kr")
        
# oppgjor = Oppgjor(2)
# #oppgjor.transportutgift(400, 3.4, [40, 30, 30, 40, 50, 60])
# oppgjor.kilometer_godtgjorelse(0.06, 18, 400)
# oppgjor.mat_utgifter(2000)
# oppgjor.vis_oppgjoret()
