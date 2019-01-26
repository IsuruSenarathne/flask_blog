from flask_blog import app

v1 = 2
v2 = 4
print (v1)

v3 = v1 + v2

for i in range(8):
    e = i + 3
    print (e)

print (v3)

if __name__ == "__main__":
    app.run(debug=True)