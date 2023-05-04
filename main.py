from flask import Flask, redirect,render_template,request 
 
app=Flask(__name__) 
 
result_list = list()
header = ['Name', 'Number', 'Major', 'Email', 'Gender', 'Languages'] 
def sort_list():                                        #추가부분
   result_list.sort(key = lambda x: x['Number'])        #추가부분


@app.route('/', methods = ['GET', 'POST'])  
def main():
   if request.method == 'POST':                      #추가부분
        result_list.clear()                           #추가부분
   return render_template('main.html')
 

@app.route('/result', methods = ['POST','GET']) 
def result(): 
   if request.method == 'POST': 
      result = dict()
      result['Name'] = request.form.get('name') 
      result['Number'] = request.form.get('number') 
      result['Major'] = request.form.get('major') 
      result['Email'] = request.form.get('email_id') + '@' + request.form.get('email_addr') 
      result['Gender'] = request.form.get('gender') 
      result['languages'] = ', '.join(request.form.getlist('chkbox')) 
      result_list.append(result) 
      sort_list()                                   #추가부분
      return render_template("result.html", result = result_list, header = header) 


 
if __name__ == '__main__': 
   app.run('0.0.0.0', port=8000, debug = True)