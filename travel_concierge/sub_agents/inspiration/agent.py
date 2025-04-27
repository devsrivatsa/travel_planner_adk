from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from travel_concierge.shared.types import DestinationIdeas, POISuggestions, json_response_config
from travel_concierge.sub_agents.inspiration import prompt
from travel_concierge.tools.places import map_tool



place_agent = Agent(
    model="gemeni-2.0-flash",
    name="place_agent",
    instruction=prompt.PLACE_AGENT_INSTRUCTION,
    description="This agent suggests few destinations based on some user preferences",
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=DestinationIdeas,
    output_key="place",
    generate_content_config=json_response_config
)

poi_agent = Agent(
    model="gemini-1.5-flash",
    name="poi_agent",
    description="This agent suggests few activities and points of interest given a destination",
    instruction=prompt.POI_AGENT_INSTRUCTION,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=POISuggestions,
    output_key="poi",
    generate_content_config=json_response_config
)

inspiration_agent = Agent(
    model="gemini-2.0-flash",
    name="inspiration_agent",
    description="A travel inspiration agent who inspires users, and discovers their next vacation destinations; Provides information about places, activities, and points of interests",
    instruction=prompt.INSPIRATION_AGENT_INSTRUCTION,
    tools=[
        AgentTool(agent=place_agent),
        AgentTool(agent=poi_agent),
        map_tool
    ]
)