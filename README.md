### Installation on Ubuntu

Install git:

```
sudo apt-get update
sudo apt-get install git
```

Install Pip (Ubuntu version has a bug):
```
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
rm get-pip.py
```

Clone repository:

```
git clone https://github.com/megastudio/twitter.git
```

Install required Python modules:

```
cd twitter
sudo pip install -r requirements.txt
```


### Running the scripts

First you [have to obtain login tokens](doc/tokens.md).
For the parameters of the scripts see the [details](doc/scripts.md).
