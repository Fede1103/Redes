# Esquema de conectividad — petas.izo

**Redes y Comunicación · Trabajo Final**

## Resumen

| Elemento | Dato |
|---|---|
| Routers | 20 (RA … RV) |
| Routers con 2 LAN | RBC (LB, LC) y RDE (LD, LE) |
| Redes LAN | 22 (LA … LV) |
| Enlaces entre routers | 22, en subredes /30 de 192.168.200.0/24 |
| Conexión a Internet | RA, eth3 · bridged (NAT) |
| Servidor DNS | HA1 — 192.168.100.1 (LA) |
| Servidor HTTP | HA2 — 192.168.100.2 (LA) |
| LAN con DHCP | LR (lease 5 min): HR1 y HR2 con IP fija, HR3 a HR5 con IP dinámica |
| Enrutamiento | OSPF, con una métrica por sentido en cada enlace |

## Referencias

- Enlaces: 192.168.200.0/24 en subredes /30.
- Cada enlace tiene 2 flechas, una por sentido, cada una con su métrica OSPF.
- Junto a cada router figura la etiqueta **IP@n** de su interfaz en el enlace.
- LAN: red y gateway (IP máxima asignable). Host: IP y etiqueta de interfaz.
- Colores: naranja = router conectado a Internet (RA) · violeta = router con 2 LAN (RBC, RDE) · amarillo = LAN con DHCP (LR).

## 1. Redes LAN

| LAN | Router | Red | Gateway | Etiqueta GW | Hosts máx. |
|---|---|---|---|---|---|
| LA | RA | 192.168.100.0/29 | 192.168.100.6 | 6@0 | 6 |
| LB | RBC | 10.0.0.0/15 | 10.1.255.254 | 1.255.254@0 | 131070 |
| LC | RBC | 10.2.0.0/18 | 10.2.63.254 | 63.254@1 | 16382 |
| LD | RDE | 10.3.0.0/19 | 10.3.31.254 | 31.254@0 | 8190 |
| LE | RDE | 10.4.0.0/21 | 10.4.7.254 | 7.254@1 | 2046 |
| LF | RF | 172.16.0.0/23 | 172.16.1.254 | 1.254@0 | 510 |
| LG | RG | 172.16.2.0/24 | 172.16.2.254 | 254@0 | 254 |
| LH | RH | 192.168.10.0/25 | 192.168.10.126 | 126@0 | 126 |
| LI | RI | 192.168.20.0/29 | 192.168.20.6 | 6@0 | 6 |
| LJ | RJ | 192.168.30.0/30 | 192.168.30.2 | 2@0 | 2 |
| LK | RK | 192.168.60.0/24 | 192.168.60.254 | 254@0 | 254 |
| LL | RL | 172.16.3.0/24 | 172.16.3.254 | 254@0 | 254 |
| LM | RM | 172.16.4.0/24 | 172.16.4.254 | 254@0 | 254 |
| LN | RN | 172.16.5.0/24 | 172.16.5.254 | 254@0 | 254 |
| LO | RO | 172.16.6.0/24 | 172.16.6.254 | 254@0 | 254 |
| LP | RP | 172.16.7.0/24 | 172.16.7.254 | 254@0 | 254 |
| LQ | RQ | 192.168.50.0/24 | 192.168.50.254 | 254@0 | 254 |
| LR | RR | 192.168.40.0/28 | 192.168.40.14 | 14@0 | 14 |
| LS | RS | 192.168.70.0/24 | 192.168.70.254 | 254@0 | 254 |
| LT | RT | 192.168.80.0/24 | 192.168.80.254 | 254@0 | 254 |
| LU | RU | 192.168.90.0/24 | 192.168.90.254 | 254@0 | 254 |
| LV | RV | 192.168.110.0/24 | 192.168.110.254 | 254@0 | 254 |

### Hosts

| Host | LAN | IP | Etiqueta | Detalle |
|---|---|---|---|---|
| HA1 | LA | 192.168.100.1 | 1@0 | DNS |
| HA2 | LA | 192.168.100.2 | 2@0 | HTTP |
| HB1 | LB | 10.0.0.1 | 0.0.1@0 | — |
| HC1 | LC | 10.2.0.1 | 0.1@0 | — |
| HD1 | LD | 10.3.0.1 | 0.1@0 | — |
| HE1 | LE | 10.4.0.1 | 0.1@0 | — |
| HF1 | LF | 172.16.0.1 | 0.1@0 | — |
| HG1 | LG | 172.16.2.1 | 1@0 | — |
| HH1 | LH | 192.168.10.1 | 1@0 | — |
| HI1 | LI | 192.168.20.1 | 1@0 | — |
| HJ1 | LJ | 192.168.30.1 | 1@0 | — |
| HK1 | LK | 192.168.60.1 | 1@0 | — |
| HL1 | LL | 172.16.3.1 | 1@0 | — |
| HM1 | LM | 172.16.4.1 | 1@0 | — |
| HN1 | LN | 172.16.5.1 | 1@0 | — |
| HO1 | LO | 172.16.6.1 | 1@0 | — |
| HP1 | LP | 172.16.7.1 | 1@0 | — |
| HQ1 | LQ | 192.168.50.1 | 1@0 | — |
| HR1 | LR | 192.168.40.1 | 1@0 | IP fija |
| HR2 | LR | 192.168.40.2 | 2@0 | IP fija |
| HR3 | LR | DHCP | — | IP dinámica |
| HR4 | LR | DHCP | — | IP dinámica |
| HR5 | LR | DHCP | — | IP dinámica |
| HS1 | LS | 192.168.70.1 | 1@0 | — |
| HT1 | LT | 192.168.80.1 | 1@0 | — |
| HU1 | LU | 192.168.90.1 | 1@0 | — |
| HV1 | LV | 192.168.110.1 | 1@0 | — |

## 2. Enlaces entre routers y métricas

| Enlace | Red | Router 1 | Etiqueta | Router 2 | Etiqueta | Métrica 1 → 2 | Métrica 2 → 1 |
|---|---|---|---|---|---|---|---|
| EA_BC | 192.168.200.0/30 | RA | 1@1 | RBC | 2@2 | 20 | 30 |
| EA_DE | 192.168.200.4/30 | RA | 5@2 | RDE | 6@2 | 25 | 35 |
| EBC_F | 192.168.200.8/30 | RBC | 9@3 | RF | 10@1 | 40 | 22 |
| EBC_G | 192.168.200.12/30 | RBC | 13@4 | RG | 14@1 | 30 | 45 |
| EBC_K | 192.168.200.16/30 | RBC | 17@5 | RK | 18@1 | 35 | 21 |
| EDE_H | 192.168.200.20/30 | RDE | 21@3 | RH | 22@1 | 24 | 38 |
| EDE_K | 192.168.200.24/30 | RDE | 25@4 | RK | 26@2 | 33 | 26 |
| EG_J | 192.168.200.28/30 | RG | 29@2 | RJ | 30@1 | 28 | 50 |
| EH_I | 192.168.200.32/30 | RH | 33@2 | RI | 34@1 | 32 | 48 |
| EI_L | 192.168.200.36/30 | RI | 37@2 | RL | 38@1 | 27 | 41 |
| EJ_M | 192.168.200.40/30 | RJ | 41@2 | RM | 42@1 | 36 | 23 |
| EK_N | 192.168.200.44/30 | RK | 45@3 | RN | 46@1 | 45 | 29 |
| EK_O | 192.168.200.48/30 | RK | 49@4 | RO | 50@1 | 22 | 34 |
| EL_Q | 192.168.200.52/30 | RL | 53@2 | RQ | 54@1 | 60 | 55 |
| EM_R | 192.168.200.56/30 | RM | 57@2 | RR | 58@1 | 31 | 44 |
| EO_P | 192.168.200.60/30 | RO | 61@2 | RP | 62@1 | 26 | 39 |
| EO_T | 192.168.200.64/30 | RO | 65@3 | RT | 66@1 | 29 | 52 |
| EP_Q | 192.168.200.68/30 | RP | 69@2 | RQ | 70@2 | 21 | 47 |
| ES_T | 192.168.200.72/30 | RS | 73@1 | RT | 74@2 | 37 | 20 |
| ES_V | 192.168.200.76/30 | RS | 77@2 | RV | 78@1 | 43 | 28 |
| ET_U | 192.168.200.80/30 | RT | 81@3 | RU | 82@1 | 25 | 49 |
| EU_V | 192.168.200.84/30 | RU | 85@2 | RV | 86@2 | 34 | 58 |

## 3. Interfaces por router

| Router | eth0 | eth1 | eth2 | eth3 | eth4 | eth5 |
|---|---|---|---|---|---|---|
| RA | LA 6@0 | EA_BC 1@1 | EA_DE 5@2 | Internet · bridged (NAT) | | |
| RBC | LB 1.255.254@0 | LC 63.254@1 | EA_BC 2@2 | EBC_F 9@3 | EBC_G 13@4 | EBC_K 17@5 |
| RDE | LD 31.254@0 | LE 7.254@1 | EA_DE 6@2 | EDE_H 21@3 | EDE_K 25@4 | |
| RF | LF 1.254@0 | EBC_F 10@1 | | | | |
| RG | LG 254@0 | EBC_G 14@1 | EG_J 29@2 | | | |
| RH | LH 126@0 | EDE_H 22@1 | EH_I 33@2 | | | |
| RI | LI 6@0 | EH_I 34@1 | EI_L 37@2 | | | |
| RJ | LJ 2@0 | EG_J 30@1 | EJ_M 41@2 | | | |
| RK | LK 254@0 | EBC_K 18@1 | EDE_K 26@2 | EK_N 45@3 | EK_O 49@4 | |
| RL | LL 254@0 | EI_L 38@1 | EL_Q 53@2 | | | |
| RM | LM 254@0 | EJ_M 42@1 | EM_R 57@2 | | | |
| RN | LN 254@0 | EK_N 46@1 | | | | |
| RO | LO 254@0 | EK_O 50@1 | EO_P 61@2 | EO_T 65@3 | | |
| RP | LP 254@0 | EO_P 62@1 | EP_Q 69@2 | | | |
| RQ | LQ 254@0 | EL_Q 54@1 | EP_Q 70@2 | | | |
| RR | LR 14@0 | EM_R 58@1 | | | | |
| RS | LS 254@0 | ES_T 73@1 | ES_V 77@2 | | | |
| RT | LT 254@0 | EO_T 66@1 | ES_T 74@2 | ET_U 81@3 | | |
| RU | LU 254@0 | ET_U 82@1 | EU_V 85@2 | | | |
| RV | LV 254@0 | ES_V 78@1 | EU_V 86@2 | | | |
