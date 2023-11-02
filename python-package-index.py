#pyhton package index

#pip list con questo comando vediamo l'ultima versione installata

# Cosa sono gli Ambienti Virtuali di Python?
# Gli Ambienti Virtuali o Virtual Environments di Python sono uno strumento che permette di creare degli spazi indipendenti dal resto del sistema in cui è possibile testare e lavorare con Python e pip.

#come creare un'ambiente vistuale di python?
# virtual environment di python

# vari strumenti per creare ambienti noi utilizziamo venv

python -m venv venv  # creamo una cartella venv con questo comando diciamo a python di utlizzare il modulo venv  
                    #per creare un abimento vistuale di python
                    
#come attivare un ambiente vistuale di python?
#spostiamoci nella cartella venv (o quella che abbiamo creato) e facciamo questo comando
# .\Script\Activate.ps1
# viceversa per disattivare un ambiente vistuale di python si usa questo comando
# deactivate

#per installare django su un ambiente vistuale di python
#lanciamo il comando 
pip install django