import json
import os
import openai

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

prompt = ChatPromptTemplate.from_template("{topic} 에 대해서 알려줘.")

model = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

result = chain.invoke({"topic": "손흥민"})


def lang(topic):
    return chain.invoke({"topic": topic})


def lambda_handler(event, context):
    return lang(event["topic"])
