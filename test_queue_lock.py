from fastapi import FastAPI, BackgroundTasks
import queue
import threading
import time

app = FastAPI()

# Create a shared queue
shared_queue = queue.Queue()

# Create a lock
lock = threading.Lock()


def process_queue():
    while True:
        # Acquire the lock
        lock.acquire()
        try:
            if not shared_queue.empty():
                item = shared_queue.get()
                # Simulate processing time
                time.sleep(2)
                print("Processed item:", item)
            else:
                break  # Exit the loop if the queue is empty
        finally:
            # Release the lock
            lock.release()


def add_to_queue(item):
    shared_queue.put(item)


@app.post("/add_item/{item}")
async def add_item(item: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(add_to_queue, item)
    return {"message": f"Item '{item}' added to the queue."}


@app.get("/process_queue")
async def process_queue_endpoint():
    thread = threading.Thread(target=process_queue)
    thread.start()
    return {"message": "Queue processing started."}
