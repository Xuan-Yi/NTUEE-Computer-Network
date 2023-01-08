# NTUEE-Computer-Network

## HW#1_SocketProgramming

* required folder structure

  ```
  // Folder Stucture

  student_ID_hw1
  |--p1
  |  |--socket_client.py
  |  |--socket_server.py
  |--p2
  |  |--helloworld.html
  |  |--index.html
  |  |--web_server.py
  |--p3
  |  |-proxy_server.py
  |--studentID_hw1.pdf
  ```

### p1 - Socket Programming - TCP

* Default
  * Host - **127.0.0.1** (localhost)
  * PORT - **2103**
* Usage
  1. ```python socket_server.py``` Run **socket_server.py** first.
  2. ```python socket_client.py``` Run **socket_client.py** to send the formulas read from **p1_testcase** to socket_server.
  3. After some simple calculation, socket_server will sent the result back to socket_client, messages will be record in **b09901080_p1_client_log.txt** and **b09901080_p1_server_log.txt**.

### p2 - Web Server

* Default
  * Host - **127.0.0.1** (localhost)
  * PORT - **2103**
* Usage
  1. ```python web_server.py``` Run **web_server.py** first.
  2. Go to any browser and key in ```http://localhost:2103/index.html```.
  3. You can also access this web_server from other devices if you use **your localhost IP**. You can get your localhost IP address by running ```utility/get_host.py```.

### p3 - Proxy Server

* Mind, we use **web_server.py** of p2 as web_server here.
* Default
  * Host (proxy_server & web_server) - **127.0.0.1**
  * PORT (proxy_server) - **2104**
  * PORT (web_server) - **2103**
* Usage
  1. ```python  ../p2/web_server.py``` Run **web_server.py** first.
  2. ```python proxy_server.py``` Run **proxy_server.py**.
  3. Go to any browser and key in ```http://localhost:2104/index.html```. Be careful tat you need to access the **IP of proxy_server** but not that of web_server.
  4. If **index.html** isn't in proxy_server, proxy_server will request to web_server for **index.html** and save cache(copy of index.html) in proxy_server.

## HW#2_Link-State Routing Protocol

* Just implement Dijkstra algorithm. Much easier than HW#1.