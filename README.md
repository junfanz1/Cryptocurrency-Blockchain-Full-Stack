# Python-Blockchain

**Activate Virtual Environment**

```
source blockchain-env/bin/activate 
```

**Install All Packages**

```
pip3 install -r requirements.txt
```

**Run the Tests**

Make sure to activate the virtual environment.

```
python3 -m pytest backend/tests
```

**Run the Application and API**

Make sure to activate the virtual environment.

```
python3 -m backend.app
```

**Run a Peer Instance**

Make sure to activate the virtual environment.

```
export PEER=True && python3 -m backend.app
```

**Run the Frontend**

In the Frontend directory:

```
npm run start
```

**Seed the backend with data**

Make sure to activate the virtual environment.

```
export SEED_DATA=True && python3 -m backend.app
```