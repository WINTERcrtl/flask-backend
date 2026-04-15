# MD5: 263c356aba92b45953b171ce1b39e550


import os
import uuid
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from config import PORT, FILE_STORE_CONFIG
from routes.health import health_bp
from routes.file import file_bp
from routes.user import user_bp
from routes.dataset import dataset_bp
from routes.model import model_bp
from routes.detection import detection_bp
from routes.video_detection import video_detection_bp
from routes.realtime_detection import realtime_detection_bp

app = Flask(__name__)
CORS(app)

# 注册路由(注意：url前缀已经在路由文件中设置，无需重复设置)
app.register_blueprint(health_bp)  
app.register_blueprint(file_bp)
app.register_blueprint(user_bp)
app.register_blueprint(dataset_bp)
app.register_blueprint(model_bp)
app.register_blueprint(detection_bp)
app.register_blueprint(video_detection_bp)
app.register_blueprint(realtime_detection_bp)

if __name__ == '__main__':
    # 确保基础存储目录存在
    if not os.path.exists(FILE_STORE_CONFIG['base_path']):
        os.makedirs(FILE_STORE_CONFIG['base_path'])
    app.run(host='0.0.0.0', port=8080, debug=True) 