#%% 
import pygit2
username = input("Enter Username : ")
token = input("Enter Token : ")

r = pygit2.init_repository('/home/jovyan/QuantumLearning/.git')
index = r.index
index.add_all()
index.write()
author = pygit2.Signature("Aritra Ranjan Chowdhury", "aritra1393@gmail.com")
commiter = pygit2.Signature("Aritra Ranjan Chowdhury", "aritra1393@gmail.com")
tree = index.write_tree()
# oid = r.create_commit('refs/heads/main', author, commiter, "init commit",tree,[r.head.get_object().hex])
remote = r.remotes["origin"]
credentials = pygit2.UserPass(username, token)
remote.credentials = credentials

callbacks=pygit2.RemoteCallbacks(credentials=credentials)

remote.push(['refs/heads/main'],callbacks=callbacks)