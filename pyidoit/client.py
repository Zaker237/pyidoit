import requests
import random
from typing import Union, List, Literal
from pyidoit.utils import DeleteStatusField

class IDoitClient(object):
    """_summary_

    Args:
        object (_type_): _description_
    """
    def __init__(
        self,
        host: str,
        apikey: str,
        username: str,
        password: str,
        language: str = "en"
    ) -> None:
        self.url = host
        self.apikey = apikey
        self.username = username
        self.password = password
        self.language = language
        self.headers = {
            "Content-Type":"application/json",
            "Accept": "application/json"
        }
    
    def _execute_request(self, body):
        print(body)
        try:
            data = requests.post(
                self.url,
                json=body,
                headers=self.headers,
                auth=(self.username, self.password)
            )
        except:
            data = None

        return data.json()
        
    # idoit methods
    def idoit_search(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def idoit_version(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def idoit_constants(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def idoit_login(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def idoit_logout(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    # cmdb objects methods
    def cmdb_object_create(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_object_read(self, object_id: int):
        """Get a specific object from i-doit with its id.

        Args:
            object_id (int): The id of the object."""
        body = {
            "jsonrpc": "2.0",
            "method" :"cmdb.object.read",
            "params": {
                "apikey": self.apikey,
                "id": object_id
            },
            "id": 1
        }

        data = self._execute_request(body)
        # print(data)
        return data

    def cmdb_object_update(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_object_delete(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_object_recycle(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_object_archive(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_object_purge(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_object_mark_as_template(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_object_mark_as_mass_change_template(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_objects_read(
        self,
        limit: Union[int, None] = None,
        categories: Union[List[str], None] = None,
        order_by: Union[str, None] = None,
        sort: Union[Literal["ASC", "DESC"], None] = "ASC",
        ids: Union[List[int], None] = None,
        type: Union[int, str, None] = None,
        title: Union[str, None] = None,
        type_title: Union[str, None] = None,
        sysid: Union[str, None] = None,
        first_name: Union[str, None] = None,
        last_name: Union[str, None] = None,
        email: Union[str, None] = None,
        type_group: Union[str, None] = None,
        status: Union[DeleteStatusField, None] = None
    ):
        """Get the list of all available objects.

        Args:
            limit (int | int): Maximum amount of objects Combine this limit with an offset (as string),
                               for example, fetch the next thousand of objects: "1000,1000".
            categories (List[str]): The list of categories to filter on.
            order_by (str): Order result set by.
            sort (str): Only useful in combination with key order_by; allowed values are either
                        "ASC" (ascending) or "DESC" (descending).
            ids: (List[int]): List of object identifiers to filter on.
            type (int | str): Object type identifier to filter on.
            title (str): Object title (see attribute Title in category Global).
            type_title (str): Translated name of object type, for example: 'Server'.
            sysid (str): System's id (see category Global), for example: "SRV_101010".
            first_name (str): First name of an object of type Persons.
            last_name (str): Last name of an object of type Persons.
            email (str): e-mail address of an object of type Persons, Person groups or Organization.
            type_group (str): Filters by the object type group e.g. Infrastructure or Other.
            status (DeleteStatusField): Filter by status of the objects e.g. Normal or Archived.
        """
        body = {
            "jsonrpc": "2.0",
            "method" :"cmdb.objects.read",
            "params": {
                "apikey": self.apikey,
                "language": self.language,
                "filter": {}
            },
            "id": random.randint(1, 200)
        }

        if limit:
            body["params"]["limit"] = limit
        if categories:
            body["params"]["categories"] = categories
        if order_by:
            body["params"]["order_by"] = order_by
        if sort:
            body["params"]["sort"] = sort
        if ids:
            body["params"]["filter"]["ids"] = ids
        if type:
            body["params"]["filter"]["type"] = type
        if title:
            body["params"]["filter"]["title"] = title
        if type_title:
            body["params"]["filter"]["type_title"] = type_title
        if sysid:
            body["params"]["filter"]["sysid"] = sysid
        if first_name:
            body["params"]["filter"]["first_name"] = first_name
        if last_name:
            body["params"]["filter"]["last_name"] = last_name
        if email:
            body["params"]["filter"]["email"] = email
        if type_group:
            body["params"]["filter"]["type_group"] = type_group
        if status:
            body["params"]["filter"]["status"] = status

        data = self._execute_request(body)
        # print(data)
        return data

    # cmdb category methods

    def cmdb_category_save(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_category_create(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_category_read(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_category_update(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_category_delete(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_category_quickpurge(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_category_purge(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_category_recycle(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_category_archive(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    # cmdb dialog methods

    def cmdb_dialog_read(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_dialog_create(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_dialog_update(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    def cmdb_dialog_delete(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

    # cmdb reports methods
    def cmdb_reports_read(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass
