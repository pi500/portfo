from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/templates/<page_name>')
def html_page(page_name):
    return render_template(page_name)  

def write_file(deta):
    with open("database.txt", mode='a') as database:
        email = deta['email']
        subject = deta['subject']
        message = deta['message']
        file = database.write(f'\n{email}, {subject}, {message}')

def write_csv(deta):
    with open("database2.csv", newline='', mode='a') as database2:
        email = deta['email']
        subject = deta['subject']
        message = deta['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL) 
        csv_writer.writerow([email, subject,message])      

@app.route('/templates/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_csv(data)
            return redirect("../templates/thank.html")
        except:
            return'couldnt save'
    else:
        return 'errror'    

app.run(debug=True)    
