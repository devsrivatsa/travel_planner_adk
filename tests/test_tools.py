from google.adk.agents.invocation_context import InvocationContext
from google.adk.artifacts import InMemoryArtifactService
from google.adk.sessions import InMemorySessionService
from google.adk.tools import ToolContext
from dotenv import load_dotenv
import unittest
import pytest

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

session_service = InMemorySessionService()
artifact_service = InMemoryArtifactService()

class TestAgents(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.session = session_service.create_session(
            app_name="Travel_Concierge",
            user_id="digital_traveler",
        )
        self.user_id = "digital_traveler"
        self.session_id = self.session.id
        self.invocation_context = InvocationContext(
            session_service=session_service, 
            artifact_service=artifact_service,
            session=self.session,
            agent=root_agent,
        )
        self.tool_context = ToolContext(invocation_context=self.invocation_context)
        