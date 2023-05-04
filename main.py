from flask import Flask, redirect,render_template,request 
 
app=Flask(__name__) 
 
result_list = list()#추가부분 
header = ['Name', 'Number', 'Major', 'Email', 'Gender', 'Languages']#추가부분 
 
@app.route('/', methods = ['GET', 'POST'])  #추가부분 
def main():#추가부분 
   return render_template('main.html')#추가부분 
 
#추가부분 
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
      return render_template("result.html", result = result_list, header = header) 
#추가부분 
 
if __name__ == '__main__': 
   app.run('0.0.0.0', port=8000, debug = True)#변경부분