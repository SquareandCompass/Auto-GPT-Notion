import datetime
from pprint import pprint

from .notion import (
    append_page,
    create_page,
    get_all_pages,
    retrieve_page,
    update_page_properties,
)

# Integration tests


def create_test_page() -> str:
    return create_page(
        title="test_create_page",
        summary="pytest test_create_page()",
        tags=["test"],
        content=f"running test_create_page() on {datetime.datetime.now()}",
    )


def test_create_page():
    pprint(create_test_page())


def test_get_all_pages():
    pprint(get_all_pages())


def test_append_page():
    output = create_test_page()
    page_id = output[output.find("page_id: ") + len("page_id: ") :]
    pprint(
        append_page(
            page_id=page_id,
            content=f"running test_append_page() on {datetime.datetime.now()}",
        )
    )


def test_retrieve_page():
    pass


def test_update_page_properties():
    pass
