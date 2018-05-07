# Progetto App Android

L'applicazione android è un aggiornamento dell'app IMU Stream presente nella seguente repository https://github.com/EmaroLab/imu_stream.

Rispetto alla versione precedente:

(Smartwatch)

1. E' stata aggiunta una nuova classe DataListener, la cui funzione, è di ascoltare, in un nuovo thread, dati(stringhe) provenienti 
   dallo smartphone per l'attivazione della vibrazione, la struttura è molto simile alla classe DataListenerService dal lato mobile.

2. E' stata aggiornata la classe SendingActivity e relativo file xml, per adattare lo smartwatch alla vibrazione e e alla ricezione di        dati dallo smartwatch, sono stati aggiunti: un BroadcastReceiver e le funzioni vibration(), vib_sender() e syncSampleDataItemVib(). Il    BroadcastReceiver ha lo scopo di permettere alla classe di ricevere il messaggio, ascoltato dalla classe DataListener. La funzione        vibration() decide in base al messaggio ricevuto l'intervallo di durata della vibrazione. Le funzioni vib_sender() e
   syncSampleVib() servono per inviare un feedback allo smartphone indicante la tipologia di vibrazione scelta dalla funzione vibration().

(Smartphone/imustream)

1. E' stata aggiornata la classe DataLayerListenerService per adattare lo smartphone a ricevere dallo smartwatch un messaggio contente la    tipologia di vibrazione in corso su di esso.

2. E' stata aggiornata la classe PcCommunication, sono stati modificati il BroadcastReceiver e la funzione startMqtt(), e sono state          aggiunte le funzioni sender() e syncSampleDataItem(). 

3. E' stata aggiornata la classe MqttHelper, per permettere la subscribe al canale, con l'utilizzo della funzione subscribeToTopic()

4. E' stata aggiornata la classe MqttPublisher, per permettere di inviare anche i valori sulla vibrazione inviati dallo smartphone al pc,    oltre a quelli Imu.

