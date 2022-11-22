from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from binary import *


class BinaryWidgets(GridLayout):
    answer = StringProperty("Waiting for calculation")
    def ask_question(self, widget):
        calc = self.ids.binary_calculation.text
        try:
            if calc == "Too twos complement":
                self.answer = str(twos_complement_ten(widget.text))
            elif calc == "From twos comlement":
                self.answer = str(from_twos_complement(int(widget.text)))
            elif calc == "Too Binary":
                self.answer = str(binary_two(int(widget.text)))
            elif calc == "From Binary":
                self.answer = str(binary_ten(int(widget.text)))
            elif calc == "Decimalpoint Binary":
                self.answer = decimalpoint_binary(widget.text)
            elif calc == "Flydende Decimalpoint":
                self.answer = flydende_decimalpunkt(widget.text)
            elif calc == "Binary Plus":
                txt = widget.text
                txt = txt.replace(" ", "").split("+")
                self.answer = binaer_plus(2, txt[0], txt[1])
            elif calc == "Binary Minus":
                txt = widget.text
                txt = txt.replace(" ", "").split("-")
                self.answer = binaer_minus(2, txt[0], txt[1])
            elif calc == "From Base 10 Too S":
                txt = widget.text
                txt = txt.replace(" ", "").split(",")
                self.answer = from_base_10_binaer(int(txt[0]), int(txt[1]))
            elif calc == "From S Too Base 10":
                txt = widget.text
                txt = txt.replace(" ", "").split(",")
                print(txt, to_base_10_binaer(int(txt[0]), str(txt[1])))
                self.answer = str(to_base_10_binaer(int(txt[0]), str(txt[1])))
        except:
            self.answer = "ERROR!"
class TheBinaryCalculaterApp(App):
    pass

if __name__ == "__main__":
    TheBinaryCalculaterApp().run()