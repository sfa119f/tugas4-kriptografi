from tkinter import *
import tkinter.messagebox
from rsa import *
from paillier import *

def clearKeyBox():
  keyLabel.place_forget()
  key.place_forget()
  gkeyLabel.place_forget()
  gkey.place_forget()
  pkeyLabel.place_forget()
  pkey.place_forget()
  qkeyLabel.place_forget()
  qkey.place_forget()
  rkeyLabel.place_forget()
  rkey.place_forget()
  xkeyLabel.place_forget()
  xkey.place_forget()
  kkeyLabel.place_forget()
  kkey.place_forget()

def changeCipher():
# Mengubah input tiap cipher
  if cipher.get() == 'X' or cipher.get() == 'ECC':
    clearKeyBox()
  elif cipher.get() == 'RSA':
    clearKeyBox()
    keyLabel.place(x=5, y=50)
    key.place(x=90, y=50)
    pkeyLabel.place(x=230, y=50)
    pkey.place(x=320, y=50)
    qkeyLabel.place(x=460, y=50)
    qkey.place(x=540, y=50)
  elif cipher.get() == 'ElGamal':
    clearKeyBox()
    gkeyLabel.place(x=5, y=50)
    gkey.place(x=90, y=50)
    pkeyLabel.place(x=230, y=50)
    pkey.place(x=320, y=50)
    xkeyLabel.place(x=460, y=50)
    xkey.place(x=540, y=50)
    kkeyLabel.place(x=680, y=50)
    kkey.place(x=760, y=50)
  elif cipher.get() == 'Paillier':
    clearKeyBox()
    gkeyLabel.place(x=5, y=50)
    gkey.place(x=90, y=50)
    pkeyLabel.place(x=230, y=50)
    pkey.place(x=320, y=50)
    qkeyLabel.place(x=460, y=50)
    qkey.place(x=540, y=50)
    rkeyLabel.place(x=680, y=50)
    rkey.place(x=760, y=50)

def clearKey():
# Menghapus key yang ada di layar
  key.delete(0, 'end')
  pkey.delete(0, 'end')
  qkey.delete(0, 'end')

def downloadKey():
# Mendownload public key dan private key
  print('downloadKey')

def clearText():
# Menghapus text yang ada di layar
  textInput.delete('1.0', END)
  textOutput.config(state=NORMAL)
  textOutput.delete('1.0', END)
  textOutput.config(state=DISABLED)

def swapFunction():
# Mengubah fungsi enkripsi menjadi dekripsi dan begitu sebaliknya
  if encrypt.get():
    btnSwap.config(text='Change to Encrypt')
    labelInput.config(text='Cipher Text')
    labelOutput.config(text='Plain Text')
  else:
    btnSwap.config(text='Change to Decrypt')
    labelInput.config(text='Plain Text')
    labelOutput.config(text='Cipher Text')
  clearText()
  encrypt.set(not encrypt.get())

def copy():
# Melakukan copy pada output value
  root.clipboard_clear()
  root.clipboard_append(textOutput.get('1.0', 'end-1c'))
  root.update()

def showOutput(outputValue):
# Menampilkan hasil ke layar
  textOutput.config(state=NORMAL)
  textOutput.delete('1.0', END)
  textOutput.insert(tkinter.END, outputValue)
  textOutput.config(state=DISABLED)

def convertText():
# Mengubah text untuk dienkripsi/dideskripsi
  if cipher.get() == 'X':
    tkinter.messagebox.showinfo('Error', 'Cipher type not selected')
  elif textInput.get('1.0', 'end-1c') == '':
    tkinter.messagebox.showinfo('Error', 'No input available')
  else:
    if encrypt.get():
      msg = ''.join(filter(str.isalpha, textInput.get('1.0', 'end-1c'))).upper()
    else:
      msg = textInput.get('1.0', 'end-1c')
    if cipher.get() == 'RSA':
      try:
        int(key.get())
        int(pkey.get())
        int(qkey.get())
      except ValueError:
        tkinter.messagebox.showinfo('Error', 'Key or P-key or Q-key only accept integer value')
      else:
        if not isRsaValidatePQ(int(pkey.get()), int(qkey.get())):
          tkinter.messagebox.showinfo('Error', 'P-key or Q-key only accept prime value')
        elif not isRsaValidateEkey(int(key.get()), int(pkey.get()), int(qkey.get())):
          tkinter.messagebox.showinfo('Error', 'Key must be relatively prime with phi value')
        else:
          if encrypt.get():
            keyValue, nValue = makePbKeyRsa(int(pkey.get()), int(qkey.get()), int(key.get()))
          else:
            keyValue, nValue = makePvKeyRsa(int(pkey.get()), int(qkey.get()), int(key.get()))
          output = methodRsa(nValue, keyValue, msg, encrypt.get())
          showOutput(output)

    elif cipher.get() == 'ElGamal':
      print('ElGamal')

    elif cipher.get() == 'Paillier':
      try:
        int(gkey.get())
        int(pkey.get())
        int(qkey.get())
        if encrypt.get(): int(rkey.get())
      except ValueError:
        tkinter.messagebox.showinfo('Error', 'Key or P-key or Q-key or R-key only accept integer value')
      else:
        if not isPaillierValidatePQ(int(pkey.get()), int(qkey.get())):
          tkinter.messagebox.showinfo('Error', 'P-key or Q-key must meet the requirements GCD(pq, (p-1)*(q-1)) = 1')
        elif not isPaillierValidateG(int(gkey.get()), int(pkey.get()) * int(qkey.get())):
          tkinter.messagebox.showinfo('Error', 'Key must meet the requirements Key < n^2')
        elif encrypt.get() and not isPaillierValidateR(int(rkey.get()), int(pkey.get()) * int(qkey.get())):
          tkinter.messagebox.showinfo('Error', 'R-Key must meet the requirement 0 <= r < n and GCD(r, n) = 1')
        else:
          if encrypt.get():
            keyA, keyB = makePbKeyPaillier(int(pkey.get()), int(qkey.get()), int(gkey.get()))
          else:
            keyA, keyB = makePvKeyPaillier(int(pkey.get()), int(qkey.get()), int(gkey.get()))
          output = methodPaillier(keyA, keyB, msg, encrypt.get(), rValue=int(rkey.get()), nValue=int(pkey.get()) * int(qkey.get()))
          showOutput(output)

    elif cipher.get() == 'ECC':
      ptkinter.messagebox.showinfo('Error', 'ECC algorithm not implemented')

root = Tk()
root.title('Cipher')
root.geometry('905x505')
root.geometry("+{}+{}".format(
  int((root.winfo_screenwidth()-905) / 2), int((root.winfo_screenheight()-505) / 2)
))
root.resizable(0,0)
isConvertFile = BooleanVar(root, False)

# Radio button pilihan cipher
Label(root, text='Choose Cipher:').place(x=5, y=5)
cipher = StringVar(root, 'X')
radioVCS = Radiobutton(root, text='RSA', variable=cipher, value='RSA', command=changeCipher)
radioVCS.place(x=90, y=5)
radioFVC = Radiobutton(root, text='ElGamal', variable=cipher, value='ElGamal', command=changeCipher)
radioFVC.place(x=90, y=25)
radioEVC = Radiobutton(root, text='Paillier', variable=cipher, value='Paillier', command=changeCipher)
radioEVC.place(x=260, y=5)
radioPFC = Radiobutton(root, text='ECC', variable=cipher, value='ECC', command=changeCipher)
radioPFC.place(x=260, y=25)

# Input key
keyLabel = Label(text='Key')
key = Entry(root, width=20)
gkeyLabel = Label(text='g-value')
gkey = Entry(root, width=20)
pkeyLabel = Label(text='p-value')
pkey = Entry(root, width=20)
qkeyLabel = Label(text='q-value')
qkey = Entry(root, width=20)
xkeyLabel = Label(text='x-value')
xkey = Entry(root, width=20)
rkeyLabel = Label(text='r-value')
rkey = Entry(root, width=20)
kkeyLabel = Label(text='k-value')
kkey = Entry(root, width=20)

# Button delete key dan download key
btnClearKey = Button(root, text='Clear Key', command=clearKey, bg='grey85')
btnClearKey.place(x=90, y=75)
btnDownloadKey = Button(root, text='Download Key', command=downloadKey, bg='grey85')
btnDownloadKey.place(x=160, y=75)

# Input text yang akan diolah
labelInput = Label(text='Plain Text:')
labelInput.place(x=5, y=115)
btnClearText = Button(root, text='Clear Text', command=clearText, fg='red', bg='grey85', width=8)
btnClearText.place(x=5, y=135)
textInput = Text(root, height=10, width=100)
textInput.place(x=90, y=115)

# Button enkripsi/deskripsi
encrypt = BooleanVar(root, True)
btnSwap = Button(root, text='Change to Decrypt', command=swapFunction, bg='grey85')
btnSwap.place(x=90, y=285)
btnConvert = Button(root, text='Convert', command=convertText, bg='grey85')
btnConvert.place(x=210, y=285)

# Output text hasil olahan
labelOutput = Label(root, text='Cipher Text:')
labelOutput.place(x=5, y=330)
btnCopy = Button(root, text='Copy', command=copy, bg='grey85', width=8)
btnCopy.place(x=5, y=350)
textOutput = Text(root, height=10, width=100, state=DISABLED)
textOutput.place(x=90, y=330)

mainloop()