"""Adding the docstring to test out pylint
- vaihtoehtoisesti voitaisiin lisätä .pylintrc:hen diasble = C0111 """


class Varasto:
    """ Adding the docstring to test out pylint """

    def check_tilavuus(self, tilavuus):
        """
        luotiin uusi metodi tarkistamaan tilavuuden posiviitisuus, jotta pystyyn kompleksisuus vaatimuksessa
        """
        if tilavuus > 0.0:
            return tilavuus

        return 0.0

    def __init__(self, tilavuus, alku_saldo=0):
        """
        Adding the docstring to test out pylint
        """
        self.tilavuus = self.check_tilavuus(tilavuus)

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa tms.

    def paljonko_mahtuu(self):
        """
        Adding the docstring to test out pylint
        """
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """
        Adding the docstring to test out pylint
        """
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """
        Adding the docstring to test out pylint
        """
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
