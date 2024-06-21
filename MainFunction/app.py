from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0, max_tokens=1000)


class Response(BaseModel):
    title: str = Field(description="title of an Article")
    content: str = Field(description="summarization of an Article")
    category: str = Field(description="category of an Article")


output_parser = JsonOutputParser(pydantic_object=Response)

format_instructions = output_parser.get_format_instructions()

prompt = PromptTemplate(
    template="""Answer the user query. 
    {format_instructions}
    Write a concise summary of the following article in Korean:
    {text}"
    CONSICE SUMMARY:""",
    input_variables={"text"},
    partial_variables={"format_instructions": format_instructions}
)

chain = prompt | model | output_parser


def lambda_handler(event, context):
    return chain.invoke({"text": event["article"]})
