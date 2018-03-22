# -*- coding: utf-8 -*-
'''
Created on 19 mar. 2018

@author: Carla
'''

import unittest
from selenium import webdriver

from src.pages.alojamientos import Alojamientos
from src.pages.vuelos import Vuelos
from src.pages.cruceros import Cruceros
from src.pages.paquetes import Paquetes
from src.pages.actividades import Actividades
from src.pages.autos import Autos
from src.pages.disney import Disney 
from src.pages.seguros import Seguros
from src.pages.traslados import Traslados
from src.pages.micros import Micros
from src.pages.alquileres import Alquileres
from src.pages.ventana_dialogo import VentanaDialogo 
from src.pages.menu import Menu
import time

class Test_001(unittest.TestCase):
    '''
    classdocs
    '''
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)
        #VISITANDO PAGINA DESPEGAR
        self.browser.get('https://www.despegar.com.ar/')
        time.sleep(2)
        self.browser.find_element_by_xpath(VentanaDialogo.boton_cerrar_ventana_dialogo_xpath).click()
        
    def test_001A(self):
        
        time.sleep(2)
        self.browser.find_element_by_xpath(Menu.menu_alojamiento_xpath).click()
        time.sleep(2)
        titulo_busqueda = self.browser.find_element_by_xpath(Alojamientos.titulo_xpath).text
        print("Verificando titulo de la seccion alojamiento")
        print(titulo_busqueda)
        self.assertIn(u"""Buscá tu Alojamiento""", titulo_busqueda)
        print("fin del test_006A")
        
    def test_001B(self):
        
        time.sleep(2)
        self.browser.find_element_by_xpath(Menu.menu_vuelos_xpath).click()
        time.sleep(2)
        #Verificacion de titulo
        titulo_busqueda = self.browser.find_element_by_xpath(Vuelos.titulo_xpath).text
        print("Verificando titulo de la seccion vuelos")
        print(titulo_busqueda)
        self.assertIn(u"""Encontrá tu Vuelo""", titulo_busqueda)
        print("fin del test_006B")
        
    def test_001C(self):
        
        time.sleep(2)
        self.browser.find_element_by_xpath(Menu.menu_paquetes_xpath).click()
        time.sleep(2)
        #Verificacion de titulo
        titulo_busqueda = self.browser.find_element_by_xpath(Paquetes.titulo_xpath).text
        print("Verificando titulo de la seccion paquetes")
        print(titulo_busqueda)
        self.assertIn(u"""Comprá tu Paquete""", titulo_busqueda)
        print("fin del test_006C")
        
    def test_001D(self):
        
        time.sleep(2)
        self.browser.find_element_by_xpath(Menu.menu_actividades_xpath).click()
        time.sleep(2)
        #Verificacion de titulo
        titulo_busqueda = self.browser.find_element_by_xpath(Actividades.titulo_xpath).text
        print("Verificando titulo de la seccion actividades")
        print(titulo_busqueda)
        self.assertIn(u"""Encontrá las mejores Actividades""", titulo_busqueda)
        print("fin del test_006D")
        
    def test_001E(self):
        
        time.sleep(2)
        self.browser.find_element_by_xpath(Menu.menu_autos_xpath).click()
        time.sleep(2)
        #Verificacion de titulo
        titulo_busqueda = self.browser.find_element_by_xpath(Autos.titulo_xpath).text
        print("Verificando titulo de la seccion autos")
        print(titulo_busqueda)
        self.assertIn(u"""Alquilá tu Auto""", titulo_busqueda)
        print("fin del test_006E")    
        
    def test_001F(self):
        
        time.sleep(2)
        self.browser.find_element_by_xpath(Menu.menu_disney_xpath).click()
        time.sleep(2)
        #Verificacion de titulo
        titulo_busqueda = self.browser.find_element_by_xpath(Disney.titulo_xpath).text
        print("Verificando titulo de la seccion disney")
        print(titulo_busqueda)
        self.assertIn(u"""Adquiera sus tickets para Walt Disney World""", titulo_busqueda)
        print("fin del test_006F")    
        
    def test_001G(self):
        
        time.sleep(2)
        self.browser.find_element_by_xpath(Menu.menu_seguros_xpath).click()
        time.sleep(2)
        #Verificacion de titulo
        titulo_busqueda = self.browser.find_element_by_xpath(Seguros.titulo_xpath).text
        print("Verificando titulo de la seccion seguros")
        print(titulo_busqueda)
        self.assertIn(u"""Asistencia al viajero""", titulo_busqueda)
        print("fin del test_006G") 
        
    def test_001H(self):
        
        time.sleep(2)
        self.browser.find_element_by_xpath(Menu.menu_traslados_xpath).click()
        time.sleep(2)
        #Verificacion de titulo
        titulo_busqueda = self.browser.find_element_by_xpath(Traslados.titulo_xpath).text
        print("Verificando titulo de la seccion traslados")
        print(titulo_busqueda)
        self.assertIn(u"""Organizá tu Traslado""", titulo_busqueda)
        print("fin del test_006H") 
        
    def test_001I(self):
        
        time.sleep(2)
        self.browser.find_element_by_xpath(Menu.menu_micros_xpath).click()
        time.sleep(2)
        #Verificacion de titulo
        titulo_busqueda = self.browser.find_element_by_xpath(Micros.titulo_xpath).text
        print("Verificando titulo de la seccion micros")
        print(titulo_busqueda)
        self.assertIn(u"""Elegí tu Micro""", titulo_busqueda)
        print("fin del test_006I")
        
    def test_001J(self):
        
        time.sleep(2)
        self.browser.find_element_by_xpath(Menu.menu_alquileres_xpath).click()
        time.sleep(2)
        #Verificacion de titulo
        titulo_busqueda = self.browser.find_element_by_xpath(Alquileres.titulo_xpath).text
        print("Verificando titulo de la seccion alquileres")
        print(titulo_busqueda)
        self.assertIn(u"""Alquileres temporarios""", titulo_busqueda)
        print("fin del test_006J")
        
    def test_001K(self):
        
        time.sleep(2)
        self.browser.find_element_by_xpath(Menu.menu_cruceros_xpath).click()
        time.sleep(2)
        #Verificacion de titulo
        titulo_busqueda = self.browser.find_element_by_xpath(Cruceros.titulo_xpath).text
        print("Verificando titulo de la seccion cruceros")
        print(titulo_busqueda)
        self.assertIn(u"""Disfrutá tu Crucero""", titulo_busqueda)
        print("fin del test_006K")
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
    