import pytest

@pytest.fixture
def setup(request):
    # setup code

    def cleanup():
        # teardown code
        pass


    request.addfinalizer(cleanup)

    return some_value
