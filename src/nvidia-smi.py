import web
import subprocess

urls = (
  '/', 'index'
)

class index:
    def GET(self):
        p = subprocess.Popen(['nvidia-smi'], stdout=subprocess.PIPE,stderr=subprocess.PIPE) 
        out, err = p.communicate()
        frame='''
        <html>
            <META HTTP-EQUIV="REFRESH" CONTENT="5">
            <body>
                <pre> 
                    {} 
                <pre>
        '''
        return frame.format(out)

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()
