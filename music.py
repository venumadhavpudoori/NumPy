from functools import wraps
from typing import List, Dict, Any

class RowLevelSecurity:
    def __init__(self, user_id: str, user_roles: List[str]):
        self.user_id = user_id
        self.user_roles = user_roles
    
    def can_access_row(self, row: Dict[str, Any], required_role: str = None) -> bool:
        """Check if user can access a specific row"""
        if "admin" in self.user_roles:
            return True
        
        if row.get("owner_id") == self.user_id:
            return True
        
        if required_role and required_role in self.user_roles:
            return True
        
        return False
    
    def filter_rows(self, rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filter rows based on user permissions"""
        return [row for row in rows if self.can_access_row(row)]


def require_rls(func):
    """Decorator for row-level security checks"""
    @wraps(func)
    def wrapper(rls: RowLevelSecurity, rows: List[Dict[str, Any]], *args, **kwargs):
        filtered_rows = rls.filter_rows(rows)
        return func(filtered_rows, *args, **kwargs)
    return wrapper


@require_rls
def get_user_data(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Retrieve accessible rows only"""
    return rows


# Example usage
rls = RowLevelSecurity(user_id="user123", user_roles=["editor"])
data = [
    {"id": 1, "owner_id": "user123", "content": "My data"},
    {"id": 2, "owner_id": "user456", "content": "Other data"},
]
result = get_user_data(rls, data)
print(result)