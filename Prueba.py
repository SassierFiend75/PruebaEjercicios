from supabase import create_client, Client

supabase: Client  = create_client("https://dxgayxbnfgtlywtmmerr.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR4Z2F5eGJuZmd0bHl3dG1tZXJyIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTYzMTgwNDAsImV4cCI6MjAxMTg5NDA0MH0.KBKe4uw_UugytAFRzmXztI0OCFCFYKbblexOF0NC1Pw")
print(supabase.table("prueba").select("*").execute())