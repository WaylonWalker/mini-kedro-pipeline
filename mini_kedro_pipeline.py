"""
An example of a minimal kedro pipeline project
"""
from kedro.pipeline import Pipeline, node

__version__ = "0.1.0"
__author__ = "Waylon S. Walker"

nodes = []


def create_data():
    "creates a dictionary of sample data"
    return {"beans": range(10)}


nodes.append(node(create_data, None, "raw_data", name="create_raw_data"))


def mult_data(data):
    "multiplies each record of each item by 100"
    return {item: [i * 100 for i in data[item]] for item in data}


nodes.append(node(mult_data, "raw_data", "mult_data", name="create_mult_data"))

pipeline = Pipeline(nodes)
