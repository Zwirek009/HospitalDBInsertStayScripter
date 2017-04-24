#INSERT INTO POBYT (ID, CZAS_PRZYJECIA, CZAS_WYPISU, PACJENT_ID, ODDZIAL_ID, LEKARZ_ID) VALUES ('1', TO_DATE('20100120','YYYYMMDD'), TO_DATE('20100130','YYYYMMDD'), '1', '1', '1');

#INSERT INTO KONSULTACJA (ID, CZAS, POBYT_ID, LEKARZ_ID) VALUES ('1', TO_DATE('20100122','YYYYMMDD'), '1', '1');

#INSERT INTO ZLECENIE (ID, CZAS_WYSTAWIENIA, WYSTAWIAJACY_ID, POBYT_ID, STD_ZLECENIE_ID) VALUES ('1', TO_DATE('20100120','YYYYMMDD'), '1', '1', '1')

#INSERT INTO BADANIE (ID, CZAS_WYKNANIA, ZLECENIE_ID, WYKONUJACY_ID, STD_BADANIE_ID) VALUES ('1', TO_DATE('20100120','YYYYMMDD'), '1', '1', '1')

#INSERT INTO TEST (ID, WYNIK_NUMERYCZNY, BADANIE_ID, STD_TEST_ID) VALUES ('2', '1', '1', '1')

#INSERT INTO TEST (ID, WYNIK_BINARNY, BADANIE_ID, STD_TEST_ID) VALUES ('3', utl_raw.cast_to_raw('C:\szpital_db\test1.txt'), '1', '71');


import datetime
import random

sciezka_do_wynikow_binarnych = "C:\szpital_db\\test{}.txt"

# schematy INSERTów do poszczególnych tabel w bazie danych
schemat_pobyt = "INSERT INTO POBYT (ID, CZAS_PRZYJECIA, CZAS_WYPISU, PACJENT_ID, ODDZIAL_ID, LEKARZ_ID) VALUES ({}, TO_DATE('{}','YYYYMMDD'), TO_DATE('{}','YYYYMMDD'), '{}', '{}', '{}');"
schemat_konsultacja = "INSERT INTO KONSULTACJA (ID, CZAS, POBYT_ID, LEKARZ_ID) VALUES ({}, TO_DATE('{}','YYYYMMDD'), '{}', '{}');"
schemat_zlecenie = "INSERT INTO ZLECENIE (ID, CZAS_WYSTAWIENIA, WYSTAWIAJACY_ID, POBYT_ID, STD_ZLECENIE_ID) VALUES ({}, TO_DATE('{}','YYYYMMDD'), '{}', '{}', '{}');"
schemat_badanie = "INSERT INTO BADANIE (ID, CZAS_WYKNANIA, ZLECENIE_ID, WYKONUJACY_ID, STD_BADANIE_ID) VALUES ({}, TO_DATE('{}','YYYYMMDD'), '{}', '{}', '{}');"
schemat_test_numeryczny = "INSERT INTO TEST (ID, WYNIK_NUMERYCZNY, BADANIE_ID, STD_TEST_ID) VALUES ({}, '{}', '{}', '{}');"
schemat_test_binarny = "INSERT INTO TEST (ID, WYNIK_BINARNY, BADANIE_ID, STD_TEST_ID) VALUES ({}, utl_raw.cast_to_raw('{}'), '{}', '{}');"

# początkowe wartości inkrementerów generatora skryptów --> zależą od aktualnych maksymalnych ID w bazie danych
pobyt_id = 30297
zlecenie_id = 30297
badanie_id = 151484

# slownik zlecenia-badania
badania = {}

badania[1] = [1, 2, 4, 6, 3]
badania[2] = [1, 2, 4, 6, 7]
badania[3] = [1, 5, 8, 9, 10]
badania[4] = [1, 2, 3, 4, 5]

# slownik badania-testy -> ostatni [][7] test jest binarny
testy = {}

testy[1] = [1, 2, 3, 4, 5, 6, 7, 71]
testy[2] = [8, 9, 10, 11, 12, 13, 14, 71]
testy[3] = [15, 16, 17, 18, 19, 20, 21, 71]
testy[4] = [22, 23, 24, 25, 26, 27, 28, 74]
testy[5] = [29, 30, 31, 32, 33, 34, 35, 72]
testy[6] = [36, 37, 38, 39, 40, 41, 42, 73]
testy[7] = [43, 44, 45, 46, 47, 48, 49, 71]
testy[8] = [50, 51, 52, 53, 54, 55, 56, 72]
testy[9] = [57, 58, 59, 60, 61, 62, 63, 72]
testy[10] = [64, 65, 66, 67, 68, 69, 70, 72]

# określenie prawidłowych zakresów wyników badań zmiennych alfanumerycznych
min_max_test = {}

min_max_test[1] = {min: 3.9, max: 6.5}
min_max_test[2] = {min: 6.8, max: 9.3}
min_max_test[3] = {min: 37, max: 47}
min_max_test[4] = {min: 0.6, max: 4.1}
min_max_test[5] = {min: 140, max: 440}
min_max_test[6] = {min: 4.1, max: 10.9}
min_max_test[7] = {min: 2, max: 7}
min_max_test[8] = {min: 70, max: 100}
min_max_test[9] = {min: 10.6, max: 28.3}
min_max_test[10] = {min: 2.1, max: 2.6}
min_max_test[11] = {min: 60, max: 80}
min_max_test[12] = {min: 0, max: 5.2}
min_max_test[13] = {min: 0, max: 3.4}
min_max_test[14] = {min: 0.92, max: 10}
min_max_test[15] = {min: 5, max: 40}
min_max_test[16] = {min: 3.42, max: 20.6}
min_max_test[17] = {min: 20, max: 70}
min_max_test[18] = {min: 18, max: 100}
min_max_test[19] = {min: 6, max: 28}
min_max_test[20] = {min: 120, max: 240}
min_max_test[21] = {min: 0, max: 0}
min_max_test[22] = {min: 10, max: 12}
min_max_test[23] = {min: 10, max: 13}
min_max_test[24] = {min: 0, max: 0}
min_max_test[25] = {min: 0, max: 0}
min_max_test[26] = {min: 1.5, max: 2.5}
min_max_test[27] = {min: 0, max: 0}
min_max_test[28] = {min: 300, max: 600}
min_max_test[29] = {min: 0, max: 0}
min_max_test[30] = {min: 0, max: 0}
min_max_test[31] = {min: 0, max: 0}
min_max_test[32] = {min: 0, max: 0}
min_max_test[33] = {min: 0, max: 0}
min_max_test[34] = {min: 0, max: 0}
min_max_test[35] = {min: 0, max: 0}
min_max_test[36] = {min: 1, max: 6}
min_max_test[37] = {min: 1, max: 1}
min_max_test[38] = {min: 1.005, max: 1.03}
min_max_test[39] = {min: 4.6, max: 8}
min_max_test[40] = {min: 0, max: 0}
min_max_test[41] = {min: 0, max: 0}
min_max_test[42] = {min: 0, max: 0}
min_max_test[43] = {min: 135, max: 145}
min_max_test[44] = {min: 3.5, max: 5}
min_max_test[45] = {min: 2, max: 6.7}
min_max_test[46] = {min: 7, max: 18}
min_max_test[47] = {min: 62, max: 124}
min_max_test[48] = {min: 0.15, max: 0.45}
min_max_test[49] = {min: 2.1, max: 2.6}
min_max_test[50] = {min: 0, max: 0}
min_max_test[51] = {min: 0, max: 0}
min_max_test[52] = {min: 0, max: 0}
min_max_test[53] = {min: 0, max: 0}
min_max_test[54] = {min: 0, max: 0}
min_max_test[55] = {min: 0, max: 0}
min_max_test[56] = {min: 0, max: 0}
min_max_test[57] = {min: 0, max: 0}
min_max_test[58] = {min: 0, max: 0}
min_max_test[59] = {min: 0, max: 0}
min_max_test[60] = {min: 0, max: 0}
min_max_test[61] = {min: 0, max: 0}
min_max_test[62] = {min: 0, max: 0}
min_max_test[63] = {min: 0, max: 0}
min_max_test[64] = {min: 0, max: 0}
min_max_test[65] = {min: 0, max: 0}
min_max_test[66] = {min: 0, max: 0}
min_max_test[67] = {min: 0, max: 0}
min_max_test[68] = {min: 0, max: 0}
min_max_test[69] = {min: 0, max: 0}
min_max_test[70] = {min: 0, max: 0}

# początkowa data określająca początek okresu, w którym skrypty będą generowane
schemat_czas_przyjecia = datetime.date(2007, 1, 1)

# inserty pobytow z danego roku --> liczność zakresu oznacza liczbę generowanych pobytów w ciągu najbliższych 10. lat
for i in range(0,2000):

	# wymuszenie zapisu w bazie co 500 pobytów
	if (i % 500) == 0:
		print("commit;")

	# inkrementacje zmiennych dotyczacych id
	pobyt_id += 1
	zlecenie_id += 1

	czas_przyjecia = schemat_czas_przyjecia + datetime.timedelta(days = random.randint(0, 3632))
	czas_wypisu = czas_przyjecia + datetime.timedelta(days = random.randint(0, 20))
	dlugosc_pobytu = (czas_wypisu - czas_przyjecia).days

	pobyt_insert = schemat_pobyt.format('pobyt_seq.nextval', czas_przyjecia.strftime("%Y%m%d"), czas_wypisu.strftime("%Y%m%d"), random.randint(1,50000), random.randint(1, 14), random.randint(1,1000))
	print(pobyt_insert)

	# inserty konsultacji
	for j in range(0, random.randint(0,3)):
		czas_konsultacji = czas_przyjecia + datetime.timedelta(random.randint(0, dlugosc_pobytu))
		
		konsultacja_insert = schemat_konsultacja.format('konsultacja_seq.nextval', czas_konsultacji.strftime("%Y%m%d"), pobyt_id, random.randint(1,1000))
		print(konsultacja_insert)

	# insert zlecenia (kazdy pacjent ma jedno zlecenie)
	numer_zlecenia = random.randint(1, 4)
	czas_zlecenia = czas_przyjecia + datetime.timedelta(random.randint(0, dlugosc_pobytu))
	czas_na_badania = (czas_wypisu - czas_zlecenia).days

	zlecenie_insert = schemat_zlecenie.format('zlecenie_seq.nextval', czas_zlecenia.strftime("%Y%m%d"), random.randint(1,1000), pobyt_id, numer_zlecenia)
	print(zlecenie_insert)

	# insert badań (każde zlecenie ma 5 badań)
	for k in range(0, 5):

		badanie_id += 1
		numer_badania = badania[numer_zlecenia][k]
		czas_badania = czas_zlecenia + datetime.timedelta(random.randint(0, czas_na_badania))

		badanie_insert = schemat_badanie.format('badanie_seq.nextval', czas_badania.strftime("%Y%m%d"), zlecenie_id, random.randint(1,1000), numer_badania)
		print(badanie_insert)

		# insert testów numerycznych(każde badanie ma 7 testów numerycznych i jeden binarny)
		for m in range(0, 7):
			aktualny_test = testy[numer_badania][m]

			if min_max_test[aktualny_test][min] == 0 and min_max_test[aktualny_test][max] == 0:
				wynik_testu = random.randint(0, 1)
			elif min_max_test[aktualny_test][min] == 1 and min_max_test[aktualny_test][max] == 1:
				wynik_testu = random.randint(0, 1)
			else:
				wynik_testu = random.triangular(0.0, (1.4 * min_max_test[aktualny_test][max]), (min_max_test[aktualny_test][max] - min_max_test[aktualny_test][min]))

			wynik_testu = str("%.3f" % wynik_testu)
			wynik_testu = wynik_testu.replace('.', ',')
			#print(wynik_testu)
			#print(wynik_testu.replace('.', ','))

			test_numeryczny_insert = schemat_test_numeryczny.format('test_seq.nextval', wynik_testu, badanie_id, testy[numer_badania][m])
			print(test_numeryczny_insert)

		#insert testu binarnego
		test_binarny_insert = schemat_test_binarny.format('test_seq.nextval', sciezka_do_wynikow_binarnych.format(badanie_id), badanie_id, testy[numer_badania][7])
		print(test_binarny_insert)

	print('\n')

# wymuszenie zapisu insertów w bazie
print("commit;")
print('\n')
