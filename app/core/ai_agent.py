from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

from app.config.settings import settings


def get_response_from_ai_agents(llm_id, query, allow_search, system_prompt):

    llm = ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model=llm_id
    )

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(
        llm,
        tools
    )

    messages = []

    if system_prompt:
        messages.append(SystemMessage(content=system_prompt))

    for msg in query:
        messages.append(HumanMessage(content=msg["content"]))

    state = {"messages": messages}

    response = agent.invoke(state)

    final_messages = response.get("messages", [])

    ai_messages = [
        message.content
        for message in final_messages
        if isinstance(message, AIMessage)
    ]

    if not ai_messages:
        raise Exception("No AI response generated")

    return ai_messages[-1]