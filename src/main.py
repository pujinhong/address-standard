from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json

from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

task = Tasks.token_classification
model = 'damo/mgeo_geographic_elements_tagging_chinese_base'
pipeline_ins = pipeline(task=task, model=model)

 
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    # 允许跨域的源列表，例如 ["http://www.example.org"] 等等，["*"] 表示允许任何源
    allow_origins=["*"],
    # 跨域请求是否支持 cookie，默认是 False，如果为 True，allow_origins 必须为具体的源，不可以是 ["*"]
    allow_credentials=False,
    # 允许跨域请求的 HTTP 方法列表，默认是 ["GET"]
    allow_methods=["*"],
    # 允许跨域请求的 HTTP 请求头列表，默认是 []，可以使用 ["*"] 表示允许所有的请求头
    # 当然 Accept、Accept-Language、Content-Language 以及 Content-Type 总之被允许的
    allow_headers=["*"],
    # 可以被浏览器访问的响应头, 默认是 []，一般很少指定
    # expose_headers=["*"]
    # 设定浏览器缓存 CORS 响应的最长时间，单位是秒。默认为 600，一般也很少指定
    # max_age=1000
) 

@app.get("/")
def home():
    return { "code": 200 , "message": "This`s MGEO!"}

@app.get("/address/")
def address(name: str):
    print(name)
    data=pipeline_ins(input=name)
    print(data)
    for ou in data['output']:
        ou['start']=int(ou['start'])
        ou['end']=int(ou['end'])
        ou['prob']=float(ou['end'])
    return JSONResponse(content=data['output'], status_code=status.HTTP_200_OK)


