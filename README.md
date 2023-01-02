# rsa_512
Karatsuba.py là chương trình thực hiện phép nhân số lớn với thuật toán Karatsuba độ phức tạp O(n^1.52).
 Sử dụng MillerRabin.py để xét số nguyên tố 512 bit, từ đó in ra PaQ.txt chứa P và Q.
 Timcaccap.py thực hiện đọc file PaQ.txt, sau đó tính giá trị n =q*p, phi(n) = (q-1)*(p-1). Rồi chọn ngẫu nhiên 10 căp e,d. In vào Caccapkey.txt.
 Rsa.py thực hiện mã hóa Rsa cho message 128bit (Mes.txt) theo 1 cặp e,d. In kết quả mã hóa và giải mã vào Result.txt
