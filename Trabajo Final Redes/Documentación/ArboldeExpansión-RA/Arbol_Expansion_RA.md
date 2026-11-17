# Árbol de expansión de RA

### Matriz de costos (fila = desde, columna = hacia; ∞ = sin enlace directo)

| Desde \ Hacia | RA | RBC | RDE | RF | RG | RH | RI | RJ | RK | RL | RM | RN | RO | RP | RQ | RR | RS | RT | RU | RV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **RA** | 0 | 20 | 25 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| **RBC** | 30 | 0 | ∞ | 40 | 30 | ∞ | ∞ | ∞ | 35 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| **RDE** | 35 | ∞ | 0 | ∞ | ∞ | 24 | ∞ | ∞ | 33 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| **RF** | ∞ | 22 | ∞ | 0 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| **RG** | ∞ | 45 | ∞ | ∞ | 0 | ∞ | ∞ | 28 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| **RH** | ∞ | ∞ | 38 | ∞ | ∞ | 0 | 32 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| **RI** | ∞ | ∞ | ∞ | ∞ | ∞ | 48 | 0 | ∞ | ∞ | 27 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| **RJ** | ∞ | ∞ | ∞ | ∞ | 50 | ∞ | ∞ | 0 | ∞ | ∞ | 36 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| **RK** | ∞ | 21 | 26 | ∞ | ∞ | ∞ | ∞ | ∞ | 0 | ∞ | ∞ | 45 | 22 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| **RL** | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | 41 | ∞ | ∞ | 0 | ∞ | ∞ | ∞ | ∞ | 60 | ∞ | ∞ | ∞ | ∞ | ∞ |
| **RM** | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | 23 | ∞ | ∞ | 0 | ∞ | ∞ | ∞ | ∞ | 31 | ∞ | ∞ | ∞ | ∞ |
| **RN** | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | 29 | ∞ | ∞ | 0 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| **RO** | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | 34 | ∞ | ∞ | ∞ | 0 | 26 | ∞ | ∞ | ∞ | 29 | ∞ | ∞ |
| **RP** | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | 39 | 0 | 21 | ∞ | ∞ | ∞ | ∞ | ∞ |
| **RQ** | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | 55 | ∞ | ∞ | ∞ | 47 | 0 | ∞ | ∞ | ∞ | ∞ | ∞ |
| **RR** | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | 44 | ∞ | ∞ | ∞ | ∞ | 0 | ∞ | ∞ | ∞ | ∞ |
| **RS** | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | 0 | 37 | ∞ | 43 |
| **RT** | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | 52 | ∞ | ∞ | ∞ | 20 | 0 | 25 | ∞ |
| **RU** | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | 49 | 0 | 34 |
| **RV** | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | 28 | ∞ | 58 | 0 |

## 2. Tabla de iteraciones

### 2.1 Nodo incorporado en cada iteración

| Iter | Nodo agregado a T | L | T |
|---|---|---|---|
| 1 | RA | 0 | {RA} |
| 2 | RBC | 20 | {RA, RBC} |
| 3 | RDE | 25 | {RA, RBC, RDE} |
| 4 | RH | 49 | {RA, RBC, RDE, RH} |
| 5 | RG | 50 | {RA, RBC, RDE, RH, RG} |
| 6 | RK | 55 | {RA, RBC, RDE, RH, RG, RK} |
| 7 | RF | 60 | {RA, RBC, RDE, RH, RG, RK, RF} |
| 8 | RO | 77 | {RA, RBC, RDE, RH, RG, RK, RF, RO} |
| 9 | RJ | 78 | {RA, RBC, RDE, RH, RG, RK, RF, RO, RJ} |
| 10 | RI | 81 | {RA, RBC, RDE, RH, RG, RK, RF, RO, RJ, RI} |
| 11 | RN | 100 | {RA, RBC, RDE, RH, RG, RK, RF, RO, RJ, RI, RN} |
| 12 | RP | 103 | {RA, RBC, RDE, RH, RG, RK, RF, RO, RJ, RI, RN, RP} |
| 13 | RT | 106 | {RA, RBC, RDE, RH, RG, RK, RF, RO, RJ, RI, RN, RP, RT} |
| 14 | RL | 108 | {RA, RBC, RDE, RH, RG, RK, RF, RO, RJ, RI, RN, RP, RT, RL} |
| 15 | RM | 114 | {RA, RBC, RDE, RH, RG, RK, RF, RO, RJ, RI, RN, RP, RT, RL, RM} |
| 16 | RQ | 124 | {RA, RBC, RDE, RH, RG, RK, RF, RO, RJ, RI, RN, RP, RT, RL, RM, RQ} |
| 17 | RS | 126 | {RA, RBC, RDE, RH, RG, RK, RF, RO, RJ, RI, RN, RP, RT, RL, RM, RQ, RS} |
| 18 | RU | 131 | {RA, RBC, RDE, RH, RG, RK, RF, RO, RJ, RI, RN, RP, RT, RL, RM, RQ, RS, RU} |
| 19 | RR | 145 | {RA, RBC, RDE, RH, RG, RK, RF, RO, RJ, RI, RN, RP, RT, RL, RM, RQ, RS, RU, RR} |
| 20 | RV | 165 | {RA, RBC, RDE, RH, RG, RK, RF, RO, RJ, RI, RN, RP, RT, RL, RM, RQ, RS, RU, RR, RV} |

### 2.2 Distancias L(n) y caminos en cada iteración

| Iter | L(RBC) | Path | L(RDE) | Path | L(RF) | Path | L(RG) | Path | L(RH) | Path | L(RI) | Path | L(RJ) | Path |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 20 | A-BC | 25 | A-DE | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — |
| 2 | **20** | A-BC | 25 | A-DE | 60 | A-BC-F | 50 | A-BC-G | ∞ | — | ∞ | — | ∞ | — |
| 3 | 20 | A-BC | **25** | A-DE | 60 | A-BC-F | 50 | A-BC-G | 49 | A-DE-H | ∞ | — | ∞ | — |
| 4 | 20 | A-BC | 25 | A-DE | 60 | A-BC-F | 50 | A-BC-G | **49** | A-DE-H | 81 | A-DE-H-I | ∞ | — |
| 5 | 20 | A-BC | 25 | A-DE | 60 | A-BC-F | **50** | A-BC-G | 49 | A-DE-H | 81 | A-DE-H-I | 78 | A-BC-G-J |
| 6 | 20 | A-BC | 25 | A-DE | 60 | A-BC-F | 50 | A-BC-G | 49 | A-DE-H | 81 | A-DE-H-I | 78 | A-BC-G-J |
| 7 | 20 | A-BC | 25 | A-DE | **60** | A-BC-F | 50 | A-BC-G | 49 | A-DE-H | 81 | A-DE-H-I | 78 | A-BC-G-J |
| 8 | 20 | A-BC | 25 | A-DE | 60 | A-BC-F | 50 | A-BC-G | 49 | A-DE-H | 81 | A-DE-H-I | 78 | A-BC-G-J |
| 9 | 20 | A-BC | 25 | A-DE | 60 | A-BC-F | 50 | A-BC-G | 49 | A-DE-H | 81 | A-DE-H-I | **78** | A-BC-G-J |
| 10 | 20 | A-BC | 25 | A-DE | 60 | A-BC-F | 50 | A-BC-G | 49 | A-DE-H | **81** | A-DE-H-I | 78 | A-BC-G-J |
| 11 | 20 | A-BC | 25 | A-DE | 60 | A-BC-F | 50 | A-BC-G | 49 | A-DE-H | 81 | A-DE-H-I | 78 | A-BC-G-J |
| 12 | 20 | A-BC | 25 | A-DE | 60 | A-BC-F | 50 | A-BC-G | 49 | A-DE-H | 81 | A-DE-H-I | 78 | A-BC-G-J |
| 13 | 20 | A-BC | 25 | A-DE | 60 | A-BC-F | 50 | A-BC-G | 49 | A-DE-H | 81 | A-DE-H-I | 78 | A-BC-G-J |
| 14 | 20 | A-BC | 25 | A-DE | 60 | A-BC-F | 50 | A-BC-G | 49 | A-DE-H | 81 | A-DE-H-I | 78 | A-BC-G-J |
| 15 | 20 | A-BC | 25 | A-DE | 60 | A-BC-F | 50 | A-BC-G | 49 | A-DE-H | 81 | A-DE-H-I | 78 | A-BC-G-J |
| 16 | 20 | A-BC | 25 | A-DE | 60 | A-BC-F | 50 | A-BC-G | 49 | A-DE-H | 81 | A-DE-H-I | 78 | A-BC-G-J |
| 17 | 20 | A-BC | 25 | A-DE | 60 | A-BC-F | 50 | A-BC-G | 49 | A-DE-H | 81 | A-DE-H-I | 78 | A-BC-G-J |
| 18 | 20 | A-BC | 25 | A-DE | 60 | A-BC-F | 50 | A-BC-G | 49 | A-DE-H | 81 | A-DE-H-I | 78 | A-BC-G-J |
| 19 | 20 | A-BC | 25 | A-DE | 60 | A-BC-F | 50 | A-BC-G | 49 | A-DE-H | 81 | A-DE-H-I | 78 | A-BC-G-J |
| 20 | 20 | A-BC | 25 | A-DE | 60 | A-BC-F | 50 | A-BC-G | 49 | A-DE-H | 81 | A-DE-H-I | 78 | A-BC-G-J |

| Iter | L(RK) | Path | L(RL) | Path | L(RM) | Path | L(RN) | Path | L(RO) | Path | L(RP) | Path |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — |
| 2 | 55 | A-BC-K | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — |
| 3 | 55 | A-BC-K | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — |
| 4 | 55 | A-BC-K | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — |
| 5 | 55 | A-BC-K | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — |
| 6 | **55** | A-BC-K | ∞ | — | ∞ | — | 100 | A-BC-K-N | 77 | A-BC-K-O | ∞ | — |
| 7 | 55 | A-BC-K | ∞ | — | ∞ | — | 100 | A-BC-K-N | 77 | A-BC-K-O | ∞ | — |
| 8 | 55 | A-BC-K | ∞ | — | ∞ | — | 100 | A-BC-K-N | **77** | A-BC-K-O | 103 | A-BC-K-O-P |
| 9 | 55 | A-BC-K | ∞ | — | 114 | A-BC-G-J-M | 100 | A-BC-K-N | 77 | A-BC-K-O | 103 | A-BC-K-O-P |
| 10 | 55 | A-BC-K | 108 | A-DE-H-I-L | 114 | A-BC-G-J-M | 100 | A-BC-K-N | 77 | A-BC-K-O | 103 | A-BC-K-O-P |
| 11 | 55 | A-BC-K | 108 | A-DE-H-I-L | 114 | A-BC-G-J-M | **100** | A-BC-K-N | 77 | A-BC-K-O | 103 | A-BC-K-O-P |
| 12 | 55 | A-BC-K | 108 | A-DE-H-I-L | 114 | A-BC-G-J-M | 100 | A-BC-K-N | 77 | A-BC-K-O | **103** | A-BC-K-O-P |
| 13 | 55 | A-BC-K | 108 | A-DE-H-I-L | 114 | A-BC-G-J-M | 100 | A-BC-K-N | 77 | A-BC-K-O | 103 | A-BC-K-O-P |
| 14 | 55 | A-BC-K | **108** | A-DE-H-I-L | 114 | A-BC-G-J-M | 100 | A-BC-K-N | 77 | A-BC-K-O | 103 | A-BC-K-O-P |
| 15 | 55 | A-BC-K | 108 | A-DE-H-I-L | **114** | A-BC-G-J-M | 100 | A-BC-K-N | 77 | A-BC-K-O | 103 | A-BC-K-O-P |
| 16 | 55 | A-BC-K | 108 | A-DE-H-I-L | 114 | A-BC-G-J-M | 100 | A-BC-K-N | 77 | A-BC-K-O | 103 | A-BC-K-O-P |
| 17 | 55 | A-BC-K | 108 | A-DE-H-I-L | 114 | A-BC-G-J-M | 100 | A-BC-K-N | 77 | A-BC-K-O | 103 | A-BC-K-O-P |
| 18 | 55 | A-BC-K | 108 | A-DE-H-I-L | 114 | A-BC-G-J-M | 100 | A-BC-K-N | 77 | A-BC-K-O | 103 | A-BC-K-O-P |
| 19 | 55 | A-BC-K | 108 | A-DE-H-I-L | 114 | A-BC-G-J-M | 100 | A-BC-K-N | 77 | A-BC-K-O | 103 | A-BC-K-O-P |
| 20 | 55 | A-BC-K | 108 | A-DE-H-I-L | 114 | A-BC-G-J-M | 100 | A-BC-K-N | 77 | A-BC-K-O | 103 | A-BC-K-O-P |

| Iter | L(RQ) | Path | L(RR) | Path | L(RS) | Path | L(RT) | Path | L(RU) | Path | L(RV) | Path |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — |
| 2 | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — |
| 3 | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — |
| 4 | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — |
| 5 | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — |
| 6 | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — |
| 7 | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — | ∞ | — |
| 8 | ∞ | — | ∞ | — | ∞ | — | 106 | A-BC-K-O-T | ∞ | — | ∞ | — |
| 9 | ∞ | — | ∞ | — | ∞ | — | 106 | A-BC-K-O-T | ∞ | — | ∞ | — |
| 10 | ∞ | — | ∞ | — | ∞ | — | 106 | A-BC-K-O-T | ∞ | — | ∞ | — |
| 11 | ∞ | — | ∞ | — | ∞ | — | 106 | A-BC-K-O-T | ∞ | — | ∞ | — |
| 12 | 124 | A-BC-K-O-P-Q | ∞ | — | ∞ | — | 106 | A-BC-K-O-T | ∞ | — | ∞ | — |
| 13 | 124 | A-BC-K-O-P-Q | ∞ | — | 126 | A-BC-K-O-T-S | **106** | A-BC-K-O-T | 131 | A-BC-K-O-T-U | ∞ | — |
| 14 | 124 | A-BC-K-O-P-Q | ∞ | — | 126 | A-BC-K-O-T-S | 106 | A-BC-K-O-T | 131 | A-BC-K-O-T-U | ∞ | — |
| 15 | 124 | A-BC-K-O-P-Q | 145 | A-BC-G-J-M-R | 126 | A-BC-K-O-T-S | 106 | A-BC-K-O-T | 131 | A-BC-K-O-T-U | ∞ | — |
| 16 | **124** | A-BC-K-O-P-Q | 145 | A-BC-G-J-M-R | 126 | A-BC-K-O-T-S | 106 | A-BC-K-O-T | 131 | A-BC-K-O-T-U | ∞ | — |
| 17 | 124 | A-BC-K-O-P-Q | 145 | A-BC-G-J-M-R | **126** | A-BC-K-O-T-S | 106 | A-BC-K-O-T | 131 | A-BC-K-O-T-U | 169 | A-BC-K-O-T-S-V |
| 18 | 124 | A-BC-K-O-P-Q | 145 | A-BC-G-J-M-R | 126 | A-BC-K-O-T-S | 106 | A-BC-K-O-T | **131** | A-BC-K-O-T-U | 165 | A-BC-K-O-T-U-V |
| 19 | 124 | A-BC-K-O-P-Q | **145** | A-BC-G-J-M-R | 126 | A-BC-K-O-T-S | 106 | A-BC-K-O-T | 131 | A-BC-K-O-T-U | 165 | A-BC-K-O-T-U-V |
| 20 | 124 | A-BC-K-O-P-Q | 145 | A-BC-G-J-M-R | 126 | A-BC-K-O-T-S | 106 | A-BC-K-O-T | 131 | A-BC-K-O-T-U | **165** | A-BC-K-O-T-U-V |

## 3. Árbol de expansión resultante

| Router | L (costo desde RA) | Camino | Predecesor | Enlace del árbol | Primer salto desde RA |
|---|---|---|---|---|---|
| RBC | 20 | RA → RBC | RA | EA_BC (20) | RBC (192.168.200.2, eth1) |
| RDE | 25 | RA → RDE | RA | EA_DE (25) | RDE (192.168.200.6, eth2) |
| RH | 49 | RA → RDE → RH | RDE | EDE_H (24) | RDE (192.168.200.6, eth2) |
| RG | 50 | RA → RBC → RG | RBC | EBC_G (30) | RBC (192.168.200.2, eth1) |
| RK | 55 | RA → RBC → RK | RBC | EBC_K (35) | RBC (192.168.200.2, eth1) |
| RF | 60 | RA → RBC → RF | RBC | EBC_F (40) | RBC (192.168.200.2, eth1) |
| RO | 77 | RA → RBC → RK → RO | RK | EK_O (22) | RBC (192.168.200.2, eth1) |
| RJ | 78 | RA → RBC → RG → RJ | RG | EG_J (28) | RBC (192.168.200.2, eth1) |
| RI | 81 | RA → RDE → RH → RI | RH | EH_I (32) | RDE (192.168.200.6, eth2) |
| RN | 100 | RA → RBC → RK → RN | RK | EK_N (45) | RBC (192.168.200.2, eth1) |
| RP | 103 | RA → RBC → RK → RO → RP | RO | EO_P (26) | RBC (192.168.200.2, eth1) |
| RT | 106 | RA → RBC → RK → RO → RT | RO | EO_T (29) | RBC (192.168.200.2, eth1) |
| RL | 108 | RA → RDE → RH → RI → RL | RI | EI_L (27) | RDE (192.168.200.6, eth2) |
| RM | 114 | RA → RBC → RG → RJ → RM | RJ | EJ_M (36) | RBC (192.168.200.2, eth1) |
| RQ | 124 | RA → RBC → RK → RO → RP → RQ | RP | EP_Q (21) | RBC (192.168.200.2, eth1) |
| RS | 126 | RA → RBC → RK → RO → RT → RS | RT | ES_T (20) | RBC (192.168.200.2, eth1) |
| RU | 131 | RA → RBC → RK → RO → RT → RU | RT | ET_U (25) | RBC (192.168.200.2, eth1) |
| RR | 145 | RA → RBC → RG → RJ → RM → RR | RM | EM_R (31) | RBC (192.168.200.2, eth1) |
| RV | 165 | RA → RBC → RK → RO → RT → RU → RV | RU | EU_V (34) | RBC (192.168.200.2, eth1) |

**Enlaces que no forman parte del árbol:**

- **EDE_K:** por RDE llegaría a RK con 25 + 33 = 58 (contra 55); por RK llegaría a RDE con 55 + 26 = 81 (contra 25).
- **EL_Q:** por RL llegaría a RQ con 108 + 60 = 168 (contra 124); por RQ llegaría a RL con 124 + 55 = 179 (contra 108).
- **ES_V:** por RS llegaría a RV con 126 + 43 = 169 (contra 165); por RV llegaría a RS con 165 + 28 = 193 (contra 126).

