# Keylogger avec Communication Serveur-Client

Ce projet est une implémentation de keylogger en Python qui capture les frappes de touches sur un client et les envoie à un serveur pour un enregistrement. Le serveur reçoit et stocke ces frappes dans un fichier dédié pour chaque client.

## Structure des Fichiers

- **`keylogger.py`** : Client qui capture les frappes de touches et les envoie au serveur.
- **`server.py`** : Serveur qui reçoit les frappes de touches et les enregistre dans un fichier de log.

## Prérequis

- Python 3.8 ou supérieur
- Les bibliothèques suivantes doivent être installées :
  - `pynput` (pour capturer les frappes de touches sur le client)
  - `socket` (bibliothèque standard pour la communication réseau)
  - `threading` (bibliothèque standard pour gérer plusieurs connexions)

Pour installer les dépendances, exécutez la commande suivante :

```bash
pip install pynput
```

## Fonctionnement
-**`Serveur (server.py)`**
Le serveur écoute les connexions TCP sur l'adresse IP et le port spécifiés.
Lorsqu'un client se connecte, un fichier de log est créé pour ce client, basé sur son adresse IP (par exemple, 192.168.0.103_keylogs.txt).
Le serveur enregistre toutes les frappes de touches reçues du client dans le fichier de log correspondant.
Le serveur peut gérer plusieurs clients simultanément grâce à l'utilisation des threads.

-**`Client (keylogger.py)`** : Le client utilise le module pynput pour écouter les frappes de touches sur le système.
Chaque frappe est envoyée au serveur via une connexion TCP.
