# flask_app
This is API to get serial values from RPI using pyserial and use flask to output to web

# Build container
cd flask_app
docker build -t flask_app .

# Run the container
docker run -p 80:80 -v /home/gerson/scripts/flask_app/app:/app --device /dev/serial0 -it -d <IMAGE_ID> '/app/start.sh'

# Run logs
docker logs <CONTAINER_ID>
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: xxx-xxx-xxx
