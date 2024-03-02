from diagrams import Cluster, Diagram
from diagrams.custom import Custom
from diagrams.generic.place import Datacenter

with Diagram("Secondary Tools"):

    hotjar = Custom("Session Recording/Feedback:\n Hotjar", ".\\img\\hotjar.png")
    optimizely = Custom("AB Testing:\n Optimizely", ".\\img\\optimizely.png")