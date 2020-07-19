from tda_tabla_hash import crear_tabla, buscar_ta, agregar_ta, hash_cifrado, bernstein_palabra
from tda_lista import barrido
from math import sqrt

class Caracter(object):
    
    def __init__(self,caracter,codificacion):
        self.caracter = caracter
        self.codificacion = codificacion
        
    def __str__(self):
        return self.caracter + " " + self.codificacion


def decodificar(caract):
    res = ""     
    for e in range(0,4):
        res += str(int(sqrt(ord(caract[e])-ord(caract[4]))))
    return chr(int(int(res)/37))    

mensaje1 = "x}tFa=PP_OAx998SGDC;Kr2O?p??PP_OQBQQAPA@q@>f555?g?g6SGDCPP_OTH]]DCzzS:?g?g6N>GG>QBQQASGDC?g?g6PP_OByIy9;Kr2PP_OPA@q@@hhG7VOJFTH]]D=XX=4;Kr2>f555PA@q@PP_O;Kr2Fa=PP_OByIy9PA@q@N>GG><W7W3SGDC?g?g6PP_OQBQQASGDCCzzS:N>GG>CzzS:UIIECzzS:WPkkGPA@q@\_[PP_O{w3.{3*wts,#,3#tppPP_O?g?g6TH]]DUIIEò»¶Ë²PP_OSGDC?g?g6VOJFO?p??CzzS:?g?g6O?p??>f555PA@q@PP_OVOJFO?p??PP_O;Kr2SGDCTH]]D?g?g6O?p??;Kr2Fa=PP_OQBQQA;Kr2SGDC;Kr2PP_O>f555?g?g6TH]]DUIIESGDCVOJFCzzS:SGDCPP_O;Kr2PP_ON>GG>CzzS:TH]]DPP_O?g?g6O?p???g?g6N>GG>CzzS:Ax998PA@q@TH]]DPP_O>f555?g?g6PP_OVOJFO?p??PP_OTH]]DPA@q@Fa=PA@q@PP_OAx998PA@q@Fa=QBQQA?g?g6\_[PP_O?g?g6TH]]DUIIEúÞ¾»ºO?p??PP_O>f555PA@q@O?p??>f555?g?g6PP_O?g?g6TH]]DUIIEúÞ¾»ºO?p??PP_OTH]]DCzzS:O?p??PP_OCzzS:N>GG>QBQQAPA@q@SGDCUIIE;Kr2SGDCPP_OFa=PA@q@TH]]DPP_O?g?g6@hhG7?g?g6=XX=4UIIECzzS:WPkkGPA@q@TH]]DPP_ORCCBVOJF?g?g6PP_OQBQQAPA@q@TH]]D?g?g6;Kr2O?p??PP_OZZ{{JPP_O?g?g6O?p??PP_O=XX=4VOJF?g?g6TH]]DUIIECzzS:ĄĕĕÅÄO?p??PP_O>f555?g?g6PP_OByIy9PA@q@SGDC;Kr2TH]]D^]a]PP_OtppTH]]Dþïâď¾PP_O>f555?g?g6PP_OTH]]DCzzS:N>GG>QBQQAFa=?g?g6PP_O=XX=4;Kr2<W7W3;Kr2Fa=Fa=?g?g6SGDCPA@q@TH]]DPP_OByIy9?g?g6PP_OFa=PA@q@Ax998SGDC;Kr2>f555PA@q@PP_OUIIEPA@q@N>GG>;Kr2SGDCPP_O?g?g6Fa=PP_OQBQQAPA@q@>f555?g?g6SGDCPP_O>f555?g?g6PP_OFa=PA@q@TH]]DPP_OwtsCzzS:PA@q@TH]]D?g?g6TH]]D^]a]"
mensaje3 = "x}tFa=PP_ON>GG>CzzS:úÞ¾»ºSGDC=XX=4PA@q@Fa=?g?g6TH]]DPP_Oc¢¢bPP_O>f555?g?g6PP_O;Kr2Ax998PA@q@TH]]DUIIEPA@q@\_[PP_OQBQQA;Kr2SGDCUIIECzzS:SGDCò»¶Ë²PP_OVOJFO?p??PP_O=XX=4;Kr2SGDCAx998;Kr2N>GG>?g?g6O?p??UIIEPA@q@PP_O>f555?g?g6PP_OSGDCCzzS:@hhG7Fa=?g?g6TH]]DPP_O>f555?g?g6PP_O;Kr2TH]]D;Kr2Fa=UIIEPA@q@PP_O>f555?g?g6PP_O?g?g6O?p???g?g6SGDCAx998þïâď¾;Kr2\_[PP_O>f555?g?g6PP_OFa=PA@q@TH]]DPP_OeµedPP_O=XX=4;Kr2N>GG>CzzS:PA@q@O?p???g?g6TH]]DPP_OFa=PA@q@TH]]DPP_OUIIESGDC?g?g6TH]]DPP_OQBQQASGDCCzzS:N>GG>?g?g6SGDCPA@q@TH]]DPP_OTH]]D?g?g6SGDCò»¶Ë²O?p??PP_OQBQQA;Kr2SGDC;Kr2PP_O>f555CzzS:TH]]DUIIESGDC;Kr2?g?g6SGDCPP_O;Kr2PP_OFa=PA@q@TH]]DPP_O;Kr2Fa=CzzS:;Kr2>f555PA@q@TH]]D\_[PP_OFa=PA@q@TH]]DPP_O>f555PA@q@TH]]DPP_OĜÏäËËFa=UIIECzzS:N>GG>PA@q@TH]]DPP_OTH]]DCzzS:N>GG>VOJFFa=;Kr2SGDCò»¶Ë²O?p??PP_OQBQQASGDCPA@q@<W7W3Fa=?g?g6N>GG>;Kr2TH]]DPP_ON>GG>?g?g6=XX=4ò»¶Ë²O?p??CzzS:=XX=4PA@q@TH]]DPP_OZZ{{JPP_OTH]]D?g?g6PP_O>f555?g?g6TH]]DWPkkGCzzS:;Kr2SGDCò»¶Ë²O?p??PP_O?g?g6O?p??PP_OFa=;Kr2PP_OUIIE?g?g6SGDC=XX=4?g?g6SGDCPP_OTH]]D;Kr2Fa=CzzS:>f555;Kr2PP_OSGDCVOJFN>GG><W7W3PA@q@PP_O;Kr2Fa=PP_OO?p??PA@q@SGDCPA@q@?g?g6TH]]DUIIE?g?g6PP_OQTTQP{w;Kr2CzzS:Fa=PP_O{wZZ{{J>f555SGDC;Kr2QTTQP"

def mensaje(ab):
    tabla1 = crear_tabla(200)
    mensaje_final = ""
    #print(len(ab))
    a = 0
    x = int(len(ab) / 5)
    while a < x:
        caracter = ""
        for e in range(a,a+5):
            caracter += ab[e]
        #print(caracter)
        valor = buscar_ta(tabla1,bernstein_palabra,Caracter("",caracter),"codificacion")
        if valor is None:
            cifrado = decodificar(caracter)
            dato = Caracter(caracter,cifrado)
            agregar_ta(tabla1,bernstein_palabra,dato,"caracter")
        else:
            cifrado = valor.info.codificacion
        mensaje_final += cifrado
        a += 5
    print(mensaje_final)
    
mensaje(mensaje3)
