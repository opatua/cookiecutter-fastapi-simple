from typing import Any, Dict, Optional

from fastapi import Request


class ResponseService:
    def to_response(self, request: Request, data: Optional[Any]) -> Dict[str, Any]:
        if not data:
            data = {}

        return {
            'data': data,
            'meta': {
                'query_params': request.query_params.multi_items(),
            },
        }
