(TeX-add-style-hook
 "just_ene"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "12pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "latin9") ("babel" "spanish")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art12"
    "inputenc"
    "babel"
    "indentfirst"
    "eurosym"
    "fancyhdr"
    "graphicx")
   (TeX-add-symbols
    "baselinestretch"
    "logotipo"
    "poner"
    "certificado"
    "profesor"
    "centro"
    "asignatura"
    "examen"
    "fecha"
    "alumno"
    "DNI"))
 :latex)

