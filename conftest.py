import pytest 
from pages.search_page import SearchPage 
from pages.profile_page import ProfilePage
from pages.issues_page import RepoPage

OWNER = "elkham07"
REPO = "EM-Apex"

@pytest.fixture
def profile_page(page):
    return ProfilePage(page)

@pytest.fixture
def search_page(page):
    return SearchPage(page)

@pytest.fixture
def issue_page(page):
    return RepoPage(page , OWNER , REPO)
