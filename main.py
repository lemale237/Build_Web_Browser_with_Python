import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineHistory
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class Browser(QMainWindow):
    def __init__(self):
        # Initialise la classe QMainWindow
        super().__init__()

        # Crée le QWebEngineView
        self.view = QWebEngineView(self)
        self.view.load(QUrl("https://www.google.com"))
        self.view.show()

        # Crée la barre d'adresse
        self.url_bar = QLineEdit(self)
        # Appelle la méthode navigate_to_url lorsque l'utilisateur appuie sur Entrée
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        # Crée les boutons Précédent et Suivant
        self.back_button = QPushButton("<", self)
        # Charge la page précédente lorsque le bouton est cliqué
        self.back_button.clicked.connect(self.view.back)
        self.forward_button = QPushButton(">", self)
        # Charge la page suivante lorsque le bouton est cliqué
        self.forward_button.clicked.connect(self.view.forward)

        # Crée le bouton Rafraîchir
        self.refresh_button = QPushButton("R", self)
        # Rafraîchit la page lorsque le bouton est cliqué
        self.refresh_button.clicked.connect(self.view.reload)

        # Ajoute les boutons à la barre d'outils
        self.toolbar = self.addToolBar("Navigation")
        self.toolbar.addWidget(self.back_button)
        self.toolbar.addWidget(self.forward_button)
        self.toolbar.addWidget(self.refresh_button)
        self.toolbar.addWidget(self.url_bar)

        # Définit les propriétés de la fenêtre principale
        self.setWindowTitle("Mon navigateur")
        self.setCentralWidget(self.view)

    def navigate_to_url(self):
        # Récupère l'URL entrée par l'utilisateur
        url = QUrl(self.url_bar.text())
        # Ajoute le schéma "http" si l'URL ne contient pas de schéma
        if url.scheme() == "":
            url.setScheme("http")
        # Charge l'URL dans le QWebEngineView
        self.view.load(url)

# Crée l'application et le navigateur
app = QApplication(sys.argv)
browser = Browser()
browser.show()
sys.exit(app.exec_())
