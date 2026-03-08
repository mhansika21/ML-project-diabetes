from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Serve static files (Tailwind, icons, etc.)
app.mount(static, StaticFiles(directory=static), name=static)

# Templates folder
templates = Jinja2Templates(directory=templates)

# Dashboard data
modules = [
    {
        title Diabetes Prediction,
        description Supervised classification using Pima Indians Diabetes Dataset. Compare Logistic Regression, Decision Tree, and Random Forest.,
        href diabetes,
        color text-blue-500,
        bg bg-blue-50010,
        icon brain-circuit  # map to SVG in staticicons
    },
    {
        title Advertising vs Sales,
        description Simple Linear Regression demo showing the relationship between advertising spend and product sales.,
        href advertising,
        color text-emerald-500,
        bg bg-emerald-50010,
        icon bar-chart-2
    },
    {
        title Titanic Data Cleaning,
        description Explore data preprocessing, handling missing values, and feature engineering on the classic Titanic dataset.,
        href titanic-cleaning,
        color text-amber-500,
        bg bg-amber-50010,
        icon database
    },
    {
        title Titanic Supervised,
        description Apply classification models to the cleaned Titanic dataset to predict passenger survival.,
        href titanic-supervised,
        color text-purple-500,
        bg bg-purple-50010,
        icon git-branch
    },
    {
        title Titanic Unsupervised,
        description Discover hidden patterns using K-means clustering and PCA dimensionality reduction.,
        href titanic-unsupervised,
        color text-pink-500,
        bg bg-pink-50010,
        icon layers
    }
]

@app.get(, response_class=HTMLResponse)
async def dashboard(request Request)
    return templates.TemplateResponse(dashboard.html, {request request, modules modules})