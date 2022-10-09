class Schema:

    __user_schema = {
        "_id": int,
        "url": str,
        "external_id": str,
        "name": str,
        "alias": str,
        "created_at": str,
        "active": bool,
        "verified": bool,
        "shared": bool,
        "locale": str,
        "timezone": str,
        "last_login_at": str,
        "email": str,
        "phone": str,
        "signature": str,
        "organization_id": int,
        "tags": list,
        "suspended": bool,
        "role": str,
    }

    __organization_schema = {
        "_id": int,
        "url": str,
        "external_id": str,
        "name": str,
        "domain_names": list,
        "created_at": str,
        "details": str,
        "shared_tickets": bool,
        "tags": list,
    }

    __tickets_schema = {
        "_id": str,
        "url": str,
        "external_id": str,
        "created_at": str,
        "type": str,
        "subject": str,
        "description": str,
        "priority": str,
        "status": str,
        "submitter_id": int,
        "assignee_id": int,
        "organization_id": int,
        "tags": list,
        "has_incidents": bool,
        "due_at": str,
        "via": str,
    }

    __map_schema_with_file_name = {
        "users": __user_schema,
        "tickets": __tickets_schema,
        "organizations": __organization_schema,
    }

    @classmethod
    def get_schema(cls, file_name: str):
        return cls.__map_schema_with_file_name[file_name]
