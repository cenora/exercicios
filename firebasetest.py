
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://prozfire2022-default-rtdb.firebaseio.com/'
})

ref = db.reference('py/')
users_ref = ref.child('users')
users_ref.set({
    'cenora': {
        'niver': '04/08/1988',
        'nome': 'Samuel',
        'idade': 34
    }
})
handle = db.reference('py/users/cenora')
print(ref.get())

# cenora = users_ref.child('cenora')
# cenora.update({'nome': 'Calvacante'})
