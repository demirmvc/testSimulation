#!/bin/bash

mkdir -p results

for i in 0.03125 0.015625 0.0078125 0.00390625; do
    echo "Running case with timestep: $i"
    mkdir -p results/$i
    sed -i "27 s/.*/deltaT    $i;/" system/controlDict

    # oderkFoam çalıştır, hata olursa döngüyü durdur
    if ! oderkFoam; then
        echo "oderkFoam failed for timestep $i"
        exit 1
    fi
    cp -r 0 results/$i
    cp -r 0.* results/$i
    cp -r 1   results/$i

    # Yalnızca başlangıç zaman adımı dosyalarını sil
    rm -r 0.*
    rm -r 1
    
    # Zaman adımına ait U değerlerini kaydetmek için bir dosya oluştur
    U_file="results/U_values_$i.txt"
    echo "U values for timestep: $i" > $U_file

    # Tüm zaman adımları için U dosyasını bul ve internalField değerini çekip dosyaya yazdır
for time_dir in results/$i/*; do
    if [ -f "$time_dir/U" ]; then
        time=$(basename $time_dir)
        U_value=$(awk '/^internalField/ {print $3}' "$time_dir/U" | tr -d ';')
        echo "Time: $time, U: $U_value" >> $U_file
    fi
done



    echo "U values for timestep $i written to $U_file"
done

