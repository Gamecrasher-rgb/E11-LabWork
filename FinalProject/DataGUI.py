from guizero import *
def DAQGUI():
    def fileName():
        app.destroy()
    app = App(title='Data Acquisition',width='600',height='600')
    file_message = Text(app, text="Enter what you wish for the data file to be called")
    file_name = TextBox(app)
    run_time = Text(app,text="Enter the Run Time")
    run_box = TextBox(app)
    sleep_time = Text(app,text="Enter the Sleep Time")
    sleep_box = TextBox(app)
    ready_time = Text(app,text="Enter the Ready Time")
    ready_box = TextBox(app)
    SendFileName = PushButton(app, command=fileName, text="Enter")
    app.display()
    return str(file_name.value),int(run_box.value),int(sleep_box.value),int(ready_box.value)