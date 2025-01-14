import pytest
from unittest.mock import MagicMock, AsyncMock
from notion_to_md import NotionToMarkdown, NotionToMarkdownAsync


def test_block_to_markdown_calls_custom_transformer():
    custom_transformer_mock = MagicMock()
    n2m = NotionToMarkdown(notion_client={})
    n2m.set_custom_transformer("test", custom_transformer_mock)

    n2m.block_to_markdown({
        "id": "test",
        "name": "test",
        "type": "test",
        "test": {"foo": "bar"},
    })

    custom_transformer_mock.assert_called_once_with({
        "id": "test",
        "name": "test",
        "type": "test",
        "test": {"foo": "bar"}
    })


def test_supports_only_one_custom_transformer_per_type():
    custom_transformer_mock1 = MagicMock()
    custom_transformer_mock2 = MagicMock()
    n2m = NotionToMarkdown(notion_client={})

    # Set two transformers for the same type
    n2m.set_custom_transformer("test", custom_transformer_mock1)
    n2m.set_custom_transformer("test", custom_transformer_mock2)

    n2m.block_to_markdown({
        "id": "test",
        "name": "test",
        "type": "test",
        "test": {"foo": "bar"},
    })

    custom_transformer_mock1.assert_not_called()
    custom_transformer_mock2.assert_called_once()


def test_custom_transformer_implementation_works():
    custom_transformer_mock = MagicMock()
    custom_transformer_mock.return_value = "hello"
    n2m = NotionToMarkdown(notion_client={})
    n2m.set_custom_transformer("divider", custom_transformer_mock)

    md = n2m.block_to_markdown({
        "id": "test",
        "type": "divider",
        "divider": {},
        "object": "block",
    })

    assert md == "hello"


def test_custom_transformer_default_implementation_works():
    custom_transformer_mock = MagicMock()
    custom_transformer_mock.return_value = False
    n2m = NotionToMarkdown(notion_client={})
    n2m.set_custom_transformer("divider", custom_transformer_mock)

    md = n2m.block_to_markdown({
        "id": "test",
        "type": "divider",
        "divider": {},
        "object": "block",
    })

    assert md == "---"


@pytest.mark.asyncio
async def test_block_to_markdown_calls_custom_transformer_async():
    custom_transformer_mock = AsyncMock()
    n2m = NotionToMarkdownAsync(notion_client={})
    n2m.set_custom_transformer("test", custom_transformer_mock)

    await n2m.block_to_markdown({
        "id": "test",
        "name": "test",
        "type": "test",
        "test": {"foo": "bar"},
    })

    custom_transformer_mock.assert_called_once_with({
        "id": "test",
        "name": "test",
        "type": "test",
        "test": {"foo": "bar"}
    })


@pytest.mark.asyncio
async def test_supports_only_one_custom_transformer_per_type_async():
    custom_transformer_mock1 = AsyncMock()
    custom_transformer_mock2 = AsyncMock()
    n2m = NotionToMarkdownAsync(notion_client={})

    # Set two transformers for the same type
    n2m.set_custom_transformer("test", custom_transformer_mock1)
    n2m.set_custom_transformer("test", custom_transformer_mock2)

    await n2m.block_to_markdown({
        "id": "test",
        "name": "test",
        "type": "test",
        "test": {"foo": "bar"},
    })

    custom_transformer_mock1.assert_not_called()
    custom_transformer_mock2.assert_called_once()


@pytest.mark.asyncio
async def test_custom_transformer_implementation_works_async():
    custom_transformer_mock = AsyncMock()
    custom_transformer_mock.return_value = "hello"
    n2m = NotionToMarkdownAsync(notion_client={})
    n2m.set_custom_transformer("divider", custom_transformer_mock)

    md = await n2m.block_to_markdown({
        "id": "test",
        "type": "divider",
        "divider": {},
        "object": "block",
    })

    assert md == "hello"


@pytest.mark.asyncio
async def test_custom_transformer_default_implementation_works_async():
    custom_transformer_mock = AsyncMock()
    custom_transformer_mock.return_value = False
    n2m = NotionToMarkdownAsync(notion_client={})
    n2m.set_custom_transformer("divider", custom_transformer_mock)

    md = await n2m.block_to_markdown({
        "id": "test",
        "type": "divider",
        "divider": {},
        "object": "block",
    })

    assert md == "---"
