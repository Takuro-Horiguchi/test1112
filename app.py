import streamlitas st
from multiappimport MultiApp
from appsimport users, rooms, bookings# import your app modules here

app= MultiApp()

app.add_app("users", users.app)
app.add_app("rooms", rooms.app)
app.add_app("bookings", bookings.app)

app.run()