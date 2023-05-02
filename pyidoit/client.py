


class IDoitClient(object):
    """_summary_

    Args:
        object (_type_): _description_
    """
    def __init__(
        self,
        host: str,
        port: str,
        apikey: str,
        username: str,
        password: str
    ) -> None:
        pass
    
    def _execute_request(self):
        pass
        
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

    def cmdb_object_read(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

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

    def cmdb_objects_read(self):
        """_summary_

        Args:
            object (_type_): _description_"""
        pass

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
