# RESTful Web Service Implementation + Docker

## Team Members 
<p>Shubham Mishra</p>
<p>Rahul Mendes</p>

## Prerequisites
Install Docker and Python on your system
<pre>$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin</pre>
Once you have installed docker on your machine run command to check if it's working or not.
<pre>sudo docker run hello-world</pre>
<p>Now to install python</p>
<pre>sudo apt install python3.8</pre>


## Building the container
<p>To build the service</p>
<pre>docker build -t service .</pre>
<p>To build the client</p>
<pre>docker build -t client .</pre>


## Running
<p>To run the service </p>
<pre>docker run -p 4000:80 server</pre>
<p>To run the client</p> 
<pre>docker run -p 5000:8080 client</pre>
