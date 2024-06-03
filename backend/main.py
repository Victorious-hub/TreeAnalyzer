import base64
import io
import random
import time
from urllib import parse

from matplotlib import pyplot as plt
from avltree import AVLTree # type: ignore
from rbtree import RedBlackTree # type: ignore
from fastapi import FastAPI # type: ignore
from fastapi import FastAPI, Request  # type: ignore
from fastapi.responses import HTMLResponse # type: ignore
from fastapi.templating import Jinja2Templates  # type: ignore
from fastapi import Form  # type: ignore

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/main", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="main.html",
        context={}
    )

@app.post("/generate", response_class=HTMLResponse)
async def main(
                request: Request,
                operation: str = Form(...),
                num_keys: int = Form(...), 
                min_border: int = Form(...), 
                max_border: int = Form(...), 
    ):
    if operation == "randomized":
        num_list = [random.randint(min_border, max_border) for _ in range(num_keys)]
    elif operation == "ascending":
        num_list = list(range(1, num_keys+1))
    else:
        num_list = list(range(num_keys+1, 1,-1))
    # Red-Black Tree
    tree = RedBlackTree()
    avl_tree = AVLTree()

    insertion_times_rbtree = []
    deletion_times_rbtree = []
    search_times_rbtree = []

    insertion_times_avl_tree = []
    search_times_avl_tree = []
    deletion_times_avl_tree = []

    for key in num_list:
        start_time = time.time()
        tree.insert(key)
        end_time = time.time()
        insertion_times_rbtree.append(end_time - start_time)

        start_time = time.time()
        avl_tree.insert(key)
        end_time = time.time()
        insertion_times_avl_tree.append(end_time - start_time)

        start_time = time.time()
        tree.search(key)
        end_time = time.time()
        search_times_rbtree.append(end_time - start_time)

        start_time = time.time()
        avl_tree.search(key)
        end_time = time.time()
        search_times_avl_tree.append(end_time - start_time)
    

    for d_key in num_list:
        start_time = time.time()
        tree.delete(d_key)
        end_time = time.time()
        deletion_times_rbtree.append(end_time - start_time)

        start_time = time.time()
        avl_tree.delete_value(d_key)
        end_time = time.time()
        deletion_times_avl_tree.append(end_time - start_time)

    elems = [i for i in range(num_keys)]
    
    plt.figure(figsize=(15, 6))

    # Insert
    plt.subplot(1, 3, 1)
    plt.plot(elems, insertion_times_rbtree, label="Red-Black Tree")
    plt.plot(elems, insertion_times_avl_tree, label="AV-Tree)")
    plt.xlabel("Number of elements")
    plt.ylabel("Average time per element")
    plt.title("Insertion")
    plt.legend()

    # Search
    plt.subplot(1, 3, 2)
    plt.plot(elems, search_times_rbtree, label="Red-Black Tree")
    plt.plot(elems, search_times_avl_tree, label="AV-Tree)")
    plt.xlabel("Number of elements")
    plt.ylabel("Average time per element")
    plt.title("Search")
    plt.legend()

    plt.subplot(1, 3, 3)
    plt.plot(elems, deletion_times_rbtree, label="Red-Black Tree")
    plt.plot(elems, deletion_times_avl_tree, label="AV-Tree)")
    plt.xlabel("Number of elements")
    plt.ylabel("Average time per element")
    plt.title("Deletion")
    plt.legend()

    # Adjust layout
    plt.tight_layout()

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    url = parse.quote(string)

    return templates.TemplateResponse(
        request=request,
        name="analyzer.html",
        context={"url": url}
    )