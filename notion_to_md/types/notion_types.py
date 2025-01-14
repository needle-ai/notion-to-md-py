from typing import TypedDict, Union, Literal, Optional, Callable, Dict, Any, List
from notion_client import Client

# Type definitions
Color = Literal[
    "default", "gray", "brown", "orange", "yellow", "green", "blue", 
    "purple", "pink", "red", "gray_background", "brown_background", 
    "orange_background", "yellow_background", "green_background", 
    "blue_background", "purple_background", "pink_background", "red_background"
]

class Annotations(TypedDict):
    bold: bool
    italic: bool
    strikethrough: bool
    underline: bool
    code: bool
    color: Color

class TextContent(TypedDict):
    content: str
    link: Optional[Dict[str, str]]

class Text(TypedDict):
    type: Literal["text"]
    text: TextContent
    annotations: Annotations
    plain_text: str
    href: Optional[str]

class Equation(TypedDict):
    type: Literal["equation"]
    equation: Dict[str, str]
    annotations: Annotations
    plain_text: str
    href: None

class CalloutIcon(TypedDict, total=False):
    type: Literal["emoji", "external", "file"]
    emoji: Optional[str]
    external: Optional[Dict[str, str]]
    file: Optional[Dict[str, str]]

class ConfigurationOptions(TypedDict, total=False):
    separateChildPage: bool
    convertImagesToBase64: bool
    parseChildPages: bool

class NotionToMarkdownOptions(TypedDict):
    notionClient: Client
    config: Optional[ConfigurationOptions]

class MdBlock(TypedDict):
    type: Optional[str]
    blockId: str
    parent: str
    children: List['MdBlock']

# Type aliases
BlockType = Literal[
    "image", "video", "file", "pdf", "table", "bookmark", "embed", 
    "equation", "divider", "toggle", "to_do", "bulleted_list_item", 
    "numbered_list_item", "synced_block", "column_list", "column", 
    "link_preview", "link_to_page", "paragraph", "heading_1", "heading_2", 
    "heading_3", "quote", "template", "child_page", "child_database", 
    "code", "callout", "breadcrumb", "table_of_contents", "audio", 
    "unsupported"
]

MdStringObject = Dict[str, str]
CustomTransformer = Callable[[Dict[str, Any]], Union[str, bool, None]] 