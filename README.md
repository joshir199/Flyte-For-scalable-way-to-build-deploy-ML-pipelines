# Flyte: For Scalable and easier way to build & deploy ML pipelines
Understanding Flyte features and its use cases in ML pipeline building and deployment in Production Environment.

# Flyte
Flyte is a workflow orchestrator that seamlessly unifies data, machine learning, and analytics stacks for building robust and reliable applications.

Flyte consists of workflow which integrate various steps of ML process. Each workflow consists of small building blocks called tasks.
Tasks can be one of the steps of ML process like loading data, preprocessing data etc.

Constraints & Properties of Flyte :
1. Task and Workflow functions should be strongly typed, e.g : input & output data types should be explicitly mentioned in the function.
2. Task and Workflow functions should always be called using Keyword arguments (kwargs).

*******************************************
# Project
In this Project, We are building a simple Logistic Regression solution using proper Flyte workflow technique.

Logistic Regression model is used to classify wine data into two classes (0, 1).

![](https://github.com/joshir199/Flyte-For-scalable-way-to-build-deploy-ML-pipelines/blob/main/images/training_workflow_diagram.png)

---------------> ML workflow diagram


# Creating tasks and workflows in flyte
We use @task and @workflow decorators in each individual process function and training flow respectively.
 
Flyte @task and @workflow decorators are designed to work seamlessly with the code-base, provided that the decorated function is at the top-level scope of the module.

The whole Flyte workflow will run on running Docker daemon.

Running Script using pyflyte:
```bash
$ pyflyte run /pipelines/training.py run_training_workflow --hyperparameters '{"C": 0.15}'
```

or

Running Script using Python:

Note: First add following line in the training file and call run_training_workflow and receive argument.
```bash
if __name__ == "__main__":
   run_training_workflow(hyperparameters=args.hyperparameters)
```
and, later call final training script:
```bash
$ python3 /pipelines/training.py --hyperparameters 0.15
```
***********************************************
# Running Workflows in a Flyte Cluster

![](https://github.com/joshir199/Flyte-For-scalable-way-to-build-deploy-ML-pipelines/blob/main/images/running%20instances%20of%20flyte.jpg)

**************************************************
Above workflow can also be accessed using flyte UI.

# Comparision with Kubeflow
Both Flyte and Kubeflow are platforms designed for orchestrating ML workflows and infrastructure within Kubernetes.
But As compared with Kubeflow, Flyte is more easy to understand, build and integrate with working production environment.

Reference: https://flyte.org/

