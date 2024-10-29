harga_reguler = 50000
harga_vip = 100000

tipe_tiket = (input("Masukkan tipe tiket (reguler/VIP): "))
status_member = (input("Apakah Anda memiliki kartu member? (ya/tidak): "))


if tipe_tiket == "reguler":
    total_harga = harga_reguler
elif tipe_tiket == "vip":
     total_harga = harga_vip
else:
    print("Tipe tiket tidak valid.")
    exit()


if status_member == "ya":
        total_harga *= 0.8 
    
        print(f"Total harga yang harus dibayar: Rp{total_harga:.2f}")
elif status_member == "tidak":
            total_harga
            print(f"total harga yang harua dibayar: Rp{total_harga:.2f}")
else:
    print("Harga tidak dapat dihitung.")