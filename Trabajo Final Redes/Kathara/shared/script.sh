#!/bin/bash
# Prueba de conectividad: hace ping POR NOMBRE (usa el DNS) a todas las
# interfaces de la red. Uso: bash /shared/script.sh
ok=0; fallo=0
while read -r ip host; do
	[[ -z "$ip" || "$ip" =~ ^# ]] && continue
	ip a show | grep -qw "$ip" && continue
	if ping -c 1 -W 1 "$host" > /dev/null 2>&1; then
		echo "OK:    $host ($ip)"; ok=$((ok+1))
	else
		echo "Fallo: $host ($ip)"; fallo=$((fallo+1))
	fi
done < /shared/hosts.txt
echo "---- $(hostname): $ok OK, $fallo fallos"
