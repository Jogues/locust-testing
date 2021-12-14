# locust-testing

This is a small load test hitting http://reqres.in endpoint

## Installation

Make sure you have python and locust install in your device
```bash
pip3 install locust
```

## Usage

### Headless
All you need to do is go to the test directory and run 
```bash
locust -f locust.py --host https://reqres.in/ --users 10 --spawn-rate 1 --run-time 120 --headless
```
or just run the loadtesting.sh 

### With web UI
Go to the test directory and run
```bash
locust -f locust.py --host https://reqres.in/ --users 10 --spawn-rate 1
```
once its done, you can open your http://localhost:8089/ and click start swarming

Note: I've set the test with 10 Vus with spawn rate 1 user every 1 second. If you run the headless one it will also run for 120 seconds.
