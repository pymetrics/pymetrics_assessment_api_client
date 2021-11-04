from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="MercuryErrorResponse")


@attr.s(auto_attribs=True)
class MercuryErrorResponse:
    """  """

    request_id: str
    recoverable: bool
    message: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id
        recoverable = self.recoverable
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {"request_id": request_id, "recoverable": recoverable, "message": message,}
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        request_id = d.pop("request_id")

        recoverable = d.pop("recoverable")

        message = d.pop("message")

        mercury_error_response = cls(request_id=request_id, recoverable=recoverable, message=message,)

        mercury_error_response.additional_properties = d
        return mercury_error_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
