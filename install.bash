echo "Installing Web UI Node Modules..."
cd ui
npm install
cd ..
cd core
echo "Installing Core requirements.txt"
pip install requirements.txt