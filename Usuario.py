from supabase import create_client
import hashlib


supabase = create_client("https://ylejvfogtxbebngaeubp.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlsZWp2Zm9ndHhiZWJuZ2FldWJwIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5Njg0NDg0OCwiZXhwIjoyMDEyNDIwODQ4fQ.QJHWLPJEJGh_iMRaFF2pZlO3I9mMqtX9mJ8Of0iFjJc")

def usuario(mail, userName, password):
    return {"correo_electronico": mail,"nombre_usuario": userName, "contrasena": password}
        
def createUser():    
    mail = input("Introduce tu correo electrónico ")
    userName = input("Introduce tu nombre de usuario ")
    password = input("Introduce tu contraseña ")
    
    user = usuario(mail, userName, password)    
    
    supabase.table("usuario").insert(user).execute()
    
def deleteUser():
    indexToRemove = input("¿Qué número de usuario quieres eliminar? ")
    
    if int(indexToRemove) < supabase.table("usuario").__sizeof__():
        supabase.table("usuario").delete().eq("id", indexToRemove).execute()
        
def updateUser():
    userToUpdate = input("¿Qué usuario desea actualizar? ")
    if int(userToUpdate) < supabase.table("usuario").__sizeof__():
        fieldToUpdate = input("¿Qué campo deseas actualizar? 1. correo_electronico 2. nombre_usuario 3. contrasena ")
        newValue = input("¿Cual es el nuevo valor que quieres introducir?")
    
        supabase.table("usuario").update({fieldToUpdate: newValue}).eq("id", userToUpdate).execute()
        
def readUser():
    userToShow = input("¿Qué usuario quieres mostrar?")
    if int(userToShow) < supabase.table("usuario").__sizeof__():
        data = supabase.table("usuario").select("*").eq("id", userToShow).execute()
        print(data)
        
def createTestUsers():
    for i in range(20, 40):
        userName = "usuario" + str(i)
        mail = userName + "@gmail.com"
        m = hashlib.sha256()
        contrasena = userName + "con"
        m.update(bytes(contrasena, encoding='utf8'))
        salida = m.hexdigest()
        supabase.table("usuario").insert(usuario(mail, userName, salida) ).execute()
def createTable():
    supabase.sql