#!/bin/bash
# Prueba de DNS: resolucion directa e inversa de todos los nombres
# Uso: bash /shared/script2.sh
while read -r ip host; do
	[[ -z "$ip" || "$ip" =~ ^# ]] && continue
	a=$(dig +short "$host.petas.izo")
	p=$(dig +short -x "$ip")
	if [ "$a" == "$ip" ] && [ "$p" == "$host.petas.izo." ]; then
		echo "OK:    $host -> $a  |  $ip -> $p"
	else
		echo "Fallo: $host -> '$a'  |  $ip -> '$p'"
	fi
done < /shared/hosts.txt
