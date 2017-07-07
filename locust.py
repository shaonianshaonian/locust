from locust import HttpLocust,TaskSet,task
class web(TaskSet):
    @task
    def index(self):
        self.client.get("/baseInfo/getHomePageInfo")
    @task
    def about(self):
        self.client.post("/historicalquotation/nowDateTimeSharing?contractCode=Au(T%2BD)")

class Webyser(HttpLocust):
    task_set = web
    min_wait = 1000
    max_wait = 3000