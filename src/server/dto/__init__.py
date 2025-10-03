"""
Data Transfer Objects (DTOs) for API request/response validation
"""

from .request_dto import (
    AskQuestionDTO,
    ConversationQueryDTO,
    CreateQuestionResponseDTO,
    CreateUserDTO,
    UpdateUserDTO,
)
from .response_dto import (
    AssistantStatusDTO,
    ConversationResponseDTO,
    ExampleQuestionDTO,
    QuestionResponseDTO,
    UserResponseDTO,
)

__all__ = [
    # Request DTOs
    "AskQuestionDTO",
    "CreateUserDTO",
    "UpdateUserDTO",
    "CreateQuestionResponseDTO",
    "ConversationQueryDTO",
    # Response DTOs
    "UserResponseDTO",
    "QuestionResponseDTO",
    "ConversationResponseDTO",
    "AssistantStatusDTO",
    "ExampleQuestionDTO",
]
