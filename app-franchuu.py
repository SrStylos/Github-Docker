from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def inicio_franchuu():
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>SrStylos by franchuu</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background: #f0f0f0; }}
            .container {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #333; }}
            .badge {{ background: #007bff; color: white; padding: 5px 10px; border-radius: 5px; font-size: 14px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🏪 SrStylos Store</h1>
            <p class="badge">by franchuu</p>
            <p>🚀 Proyecto: Github-Docker</p>
            <p>📍 Directorio: Github-Docker</p>
            
            <h3>🌐 Rutas disponibles:</h3>
            <ul>
                <li><a href="/productos">📦 Nuestros Productos</a></li>
                <li><a href="/docker-info">🐳 Info Docker</a></li>
                <li><a href="/github-info">📚 Info GitHub</a></li>
                <li><a href="/sobre-franchuu">👨‍💻 Sobre franchuu</a></li>
            </ul>
            
            <div style="margin-top: 20px; padding: 15px; background: #e9ecef; border-radius: 5px;">
                <strong>📁 Directorio Actual:</strong> Github-Docker<br>
                <strong>👤 Usuario:</strong> franchuu<br>
                <strong>🐳 Container:</strong> SrStylos-Store
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/productos')
def productos_franchuu():
    return '''
    <div style="margin: 40px;">
        <h1>📦 Productos SrStylos</h1>
        <p>Catálogo exclusivo de franchuu desde Github-Docker</p>
        <ul>
            <li>🛍️ Ropa estilo único franchuu</li>
            <li>👟 Zapatos personalizados</li>
            <li>🎒 Accesorios SrStylos</li>
            <li>⌚ Ediciones limitadas</li>
        </ul>
        <a href="/">← Volver al inicio</a>
    </div>
    '''

@app.route('/docker-info')
def info_docker():
    return '''
    <div style="margin: 40px;">
        <h1>🐳 Información Docker</h1>
        <p><strong>Proyecto:</strong> Github-Docker</p>
        <p><strong>Usuario:</strong> franchuu</p>
        <p><strong>Imagen:</strong> franchuu/srstylos-store</p>
        <p><strong>Directorio:</strong> Github-Docker</p>
        <p><strong>Puerto:</strong> 8080</p>
        <a href="/">← Volver al inicio</a>
    </div>
    '''

@app.route('/github-info')
def info_github():
    return '''
    <div style="margin: 40px;">
        <h1>📚 Información GitHub</h1>
        <p><strong>Usuario:</strong> franchuu</p>
        <p><strong>Repositorio:</strong> Github-Docker</p>
        <p><strong>Proyecto:</strong> SrStylos Store</p>
        <p><strong>Integración:</strong> Docker + GitHub</p>
        <a href="/">← Volver al inicio</a>
    </div>
    '''

@app.route('/sobre-franchuu')
def sobre_franchuu():
    return '''
    <div style="margin: 40px;">
        <h1>👨‍💻 Acerca de franchuu</h1>
        <p><strong>Desarrollador:</strong> franchuu</p>
        <p><strong>Proyecto:</strong> SrStylos Store</p>
        <p><strong>Directorio:</strong> Github-Docker</p>
        <p><strong>Especialidad:</strong> Docker + GitHub + Python</p>
        <p><strong>Contacto:</strong> franchuu en GitHub</p>
        <a href="/">← Volver al inicio</a>
    </div>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)