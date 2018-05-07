# VIBRATION FEEDBACK

Questa repository è un aggiornamento della seguente https://github.com/EmaroLab/mqtt_ros_bridge.

Rispetto alla versione precendente:

1. Si è creato un nuovo file python vib.py, finalizzato a ricevere i dati odometrici e pubblicare stringhe.
   Sono state importate le funzioni Odometry e PoseStamped, utilizzate per ricevere i dati odometrici, in particolare sulla                    
   posizione rispetto alle coordinate x,y. Si pubblica sul canale '/vibration_vel' una stringa per comunicare allo smartwatch la
   tipologia di vibrazione.
   
2. E' stata aggiunta al file bridge.py la funzione pub(), e al file imu_bridge.py un subscriber per permettere la sottoscrizione al 
   canale '/vibration_vel'
