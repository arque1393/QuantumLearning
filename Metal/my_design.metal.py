
from qiskit_metal import designs, MetalGUI

design = designs.DesignPlanar()

gui = MetalGUI(design)

gui.rebuild()
gui.autoscale()
        