from flask import Flask, redirect, url_for

@app.route('/redirect')
def reroute():
    return redirect(url_for('target_function'))