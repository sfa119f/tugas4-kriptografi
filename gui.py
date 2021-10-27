from tkinter import *

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
    btnImport.config(state=DISABLED)
  else:
    btnSwap.config(text='Change to Decrypt')
    labelInput.config(text='Plain Text')
    labelOutput.config(text='Cipher Text')
    if isFile.get():
      btnImport.config(state=NORMAL)
  clearText()
  encrypt.set(not encrypt.get())

def copy():
# Melakukan copy pada output value
  root.clipboard_clear()
  root.clipboard_append(textOutput.get('1.0', 'end-1c'))
  root.update()

def convertText():
# Mengubah text untuk dienkripsi/dideskripsi
  print('convertText')

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
radioVCS = Radiobutton(root, text='RSA', variable=cipher, value='RSA')
radioVCS.place(x=90, y=5)
radioFVC = Radiobutton(root, text='ElGamal', variable=cipher, value='ElGamal')
radioFVC.place(x=90, y=25)
radioEVC = Radiobutton(root, text='Pailler', variable=cipher, value='Pailler')
radioEVC.place(x=260, y=5)
radioPFC = Radiobutton(root, text='ECC', variable=cipher, value='ECC')
radioPFC.place(x=260, y=25)

# Input key
keyLabel = Label(text='Key')
keyLabel = Label(text='Key')
keyLabel.place(x=5, y=50)
key = Entry(root, width=20)
key.place(x=90, y=50)
pkeyLabel = Label(text='p-value')
pkeyLabel.place(x=230, y=50)
pkey = Entry(root, width=20)
pkey.place(x=320, y=50)
qkeyLabel = Label(text='q-value')
qkeyLabel.place(x=460, y=50)
qkey = Entry(root, width=30)
qkey.place(x=540, y=50)

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