import string

alphabets = string.ascii_lowercase + string.ascii_lowercase
sentence = list(input('Ketik Text Yang Ingin Di Proses :\n').lower())
pilihan = input('Masukan 1 untuk ENKRIPSI, 2 untuk DEKRIPSI dan 3 untuk KELUAR \n').lower()
shift_number = int(input('Masukan nilai pergeseran : \n'))
end_program = False

while not end_program:

    if pilihan == '1':
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new_letter = alphabets.index(sentence[i]) + shift_number
                sentence[i] = alphabets[new_letter]
        print(''.join(map(str, sentence)))
        end_program = True
    elif pilihan == '2':
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new_letter = alphabets.index(sentence[i]) - shift_number
                sentence[i] = alphabets[new_letter]
        print(''.join(map(str, sentence)))
        end_program = True
    else:
        decide = input(
            'Perintah anda salah, lanjut untuk Melanjutkan \n').lower()
        if decide == 'lanjut':
            sentence = list(input('Teks : \n').lower())
            pilihan = input(
                'Masukan 1 untuk ENKRIPSI, 2 untukDEKRIPSI dan 3 untuk Keluar \n').lower()
            shift_number = int(
                input('Masukan nilai pergeseran : \n'))
        else:
            end_program = True
