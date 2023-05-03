import enum
from typing import Literal


class CategoryField(enum.Enum):
    General = "C__CATG__GLOBAL"
    Model = "C__CATG__MODEL"
    FormFactor = "C__CATG__FORMFACTOR"
    CPU = "C__CATG__CPU"
    Memory = "C__CATG__MEMORY"
    Network = "C__CATG__NETWORK"
    PowerConsumer = "C__CATG__POWER_CONSUMER"
    InterfaceUniversal = "C__CATG__UNIVERSAL_INTERFACE"
    SoftwareAssignment = "C__CATG__APPLICATION"
    Access = "C__CATG__ACCESS"
    Backup = "C__CATG__BACKUP"
    EmergencyPlanAssignment = "C__CATG__EMERGENCY_PLAN"
    FilesCatg = "C__CATG__FILE"
    ContactAssignment = "C__CATG__CONTACT"
    Logbook = "C__CATG__LOGBOOK"
    Controller = "C__CATG__CONTROLLER"
    Location = "C__CATG__LOCATION"
    ObjectPicture = "C__CATG__IMAGE"
    ManualAssignment = "C__CATG__MANUAL"
    SoundCard = "C__CATG__SOUND"
    LocallyAssignedObjects = "C__CATG__OBJECT"
    GraphicCard = "C__CATG__GRAPHIC"
    VirtualMachine = "C__CATG__VIRTUAL_MACHINE"
    Accounting = "C__CATG__ACCOUNTING"
    Port = "C__CMDB__SUBCAT__NETWORK_PORT"
    InterfaceSubcat = "C__CMDB__SUBCAT__NETWORK_INTERFACE_P"
    LogicalPorts = "C__CMDB__SUBCAT__NETWORK_INTERFACE_L"
    Drive = "C__CATG__DRIVE"
    Device = "C__CMDB__SUBCAT__STORAGE__DEVICE"
    FCPort = "C__CATG__CONTROLLER_FC_PORT"
    HostAddress = "C__CATG__IP"
    Version = "C__CATG__VERSION"
    Connectors = "C__CATG__CONNECTOR"
    Invoice = "C__CATG__INVOICE"
    PowerSupplier = "C__CATG__POWER_SUPPLIER"
    RAIDArray = "C__CATG__RAID"
    LogicalDevicesLDEVServer = "C__CATG__LDEV_SERVER"
    LogicalDevicesClient = "C__CATG__LDEV_CLIENT"
    HostBusAdapterHBA = "C__CATG__HBA"
    ClusterRoot = "C__CATG__CLUSTER_ROOT"
    Cluster = "C__CATG__CLUSTER"
    Shares = "C__CATG__SHARES"
    ClusterServiceAssignment = "C__CATG__CLUSTER_SERVICE"
    ClusterMembers = "C__CATG__CLUSTER_MEMBERS"
    ClusterMemberships = "C__CATG__CLUSTER_MEMBERSHIPS"
    ComputingResources = "C__CATG__COMPUTING_RESOURCES"
    SNMP = "C__CATG__SNMP"
    VirtualHostRoot = "C__CATG__VIRTUAL_HOST_ROOT"
    VirtualHost = "C__CATG__VIRTUAL_HOST"
    GuestSystems = "C__CATG__GUEST_SYSTEMS"
    VirtualMachineRoot = "C__CATG__VIRTUAL_MACHINE__ROOT"
    VirtualSwitches = "C__CATG__VIRTUAL_SWITCH"
    VirtualDevices = "C__CATG__VIRTUAL_DEVICE"
    BackupAssignedObjects = "C__CATG__BACKUP__ASSIGNED_OBJECTS"
    GroupMemberships = "C__CATG__GROUP_MEMBERSHIPS"
    ServiceComponents = "C__CATG__IT_SERVICE_COMPONENTS"
    ServiceLogbook = "C__CATG__ITS_LOGBOOK"
    ServiceAssignment = "C__CATG__IT_SERVICE"
    Relationship = "C__CATG__RELATION"
    ServiceRelation = "C__CATG__IT_SERVICE_RELATIONS"
    DatabaseAssignment = "C__CATG__DATABASE_ASSIGNMENT"
    ServiceType = "C__CATG__ITS_TYPE"
    Passwords = "C__CATG__PASSWD"
    SOAStacks = "C__CATG__SOA_STACKS"
    StatusPlanning = "C__CATG__PLANNING"
    AssignedCards = "C__CATG__ASSIGNED_CARDS"
    SIMCard = "C__CATG__SIM_CARD"
    TSIService = "C__CATG__TSI_SERVICE"
    Audit = "C__CATG__AUDIT"
    LogicalLocation = "C__CATG__LOGICAL_UNIT"
    WorkplaceComponents = "C__CATG__ASSIGNED_LOGICAL_UNIT"
    AssignedWorkstation = "C__CATG__ASSIGNED_WORKSTATION"
    AssignedWorkplaces = "C__CATG__PERSON_ASSIGNED_WORKSTATION"
    ContractAssignment = "C__CATG__CONTRACT_ASSIGNMENT"
    Stacking = "C__CATG__STACKING"
    EMailAddresses = "C__CATG__MAIL_ADDRESSES"
    CUCMVoIPTelephone = "C__CATG__VOIP_PHONE"
    CUCMVoIPLine = "C__CATG__VOIP_PHONE_LINE"
    TelephoneFax = "C__CATG__TELEPHONE_FAX"
    SmartCardCertificate = "C__CATG__SMARTCARD_CERTIFICATE"
    ShareAccess = "C__CATG__SHARE_ACCESS"
    Certificate = "C__CATG__CERTIFICATE"
    SLA = "C__CATG__SLA"
    LDAP = "C__CATG__LDAP_DN"
    Hostdefinition = "C__CATG__NAGIOS"
    NagiosGroup = "C__CATG__NAGIOS_GROUP"
    NagiosService = "C__CATG__NAGIOS_SERVICE_FOLDER"
    NagiosServiceTPL = "C__CATG__NAGIOS_SERVICE_TPL_FOLDER"
    ServiceDefinition = "C__CATG__NAGIOS_SERVICE_DEF"
    BackwardsServiceAssignment = "C__CATG__NAGIOS_REFS_SERVICES_BACKWARDS"
    ServiceTemplateDefinition = "C__CATG__NAGIOS_SERVICE_TPL_DEF"
    AssignedObjects = "C__CATG__NAGIOS_SERVICE_REFS_TPL_BACKWARDS"
    NagiosHostTPL = "C__CATG__NAGIOS_HOST_TPL_FOLDER"
    HostTemplateDefinition = "C__CATG__NAGIOS_HOST_TPL_DEF"
    NagiosHost = "C__CATG__NAGIOS_HOST_FOLDER"
    AssignedObjectsCatg = "C__CATG__NAGIOS_HOST_TPL_ASSIGNED_OBJECTS"
    ServiceAssignmentRefsService = "C__CATG__NAGIOS_REFS_SERVICES"
    NagiosApplication = "C__CATG__NAGIOS_APPLICATION_FOLDER"
    ServiceAssignmentApplicationRef = "C__CATG__NAGIOS_APPLICATION_REFS_NAGIOS_SERVICE"
    ServiceDependencies = "C__CATG__NAGIOS_SERVICE_DEP"
    Address = "C__CATG__ADDRESS"
    Monitoring = "C__CATG__MONITORING"
    Livestatus = "C__CATG__LIVESTATUS"
    Vehicle = "C__CATG__VEHICLE"
    Aircraft = "C__CATG__AIRCRAFT"
    NetworkConnections = "C__CATG__NET_CONNECTIONS_FOLDER"
    Listener = "C__CATG__NET_LISTENER"
    Connection = "C__CATG__NET_CONNECTOR"
    AdministrationService = "C__CATG__CLUSTER_ADM_SERVICE"
    JDiscCustomAttributes = "C__CATG__JDISC_CA"
    LC__CATG__CMK_FOLDER = "C__CATG__CMK"
    LC__CATG__CMK_TAG = "C__CATG__CMK_TAG"
    LC__CATG__CMK_HOST_SERVICE = "C__CATG__CMK_HOST_SERVICE"
    LC__CATG__CMK_SERVICE = "C__CATG__CMK_SERVICE"
    LC__CATG__CMK_DEF = "C__CATG__CMK_DEF"
    NDO = "C__CATG__NDO"
    Cable = "C__CATG__CABLE"
    DataSource = "C__CATG__IDENTIFIER"
    ServicesCatg = "C__CATG__SERVICE"
    OperatingSystem = "C__CATG__OPERATING_SYSTEM"
    QinQSPVLAN = "C__CATG__QINQ_SP"
    FiberLead = "C__CATG__FIBER_LEAD"
    QinQCEVLAN = "C__CATG__QINQ_CE"
    Images = "C__CATG__IMAGES"
    WANConnection = "C__CATG__WAN"
    RemoteManagementController = "C__CATG__RM_CONTROLLER"
    ManagedDevices = "C__CATG__RM_CONTROLLER_BACKWARD"
    VirtualManagedObjects = "C__CATG__MANAGED_OBJECTS"
    VRRP = "C__CATG__VRRP"
    VRRPMember = "C__CATG__VRRP_MEMBER"
    StackMember = "C__CATG__STACK_MEMBER"
    LastLoginUser = "C__CATG__LAST_LOGIN_USER"
    NetZoneCatg = "C__CATG__NET_ZONE"
    Options = "C__CATG__NET_ZONE_OPTIONS"
    Scope = "C__CATG__NET_ZONE_SCOPES"
    SpecificCategories = "cats"
    Rack = "C__CATS__ENCLOSURE"
    Room = "C__CATS__ROOM"
    ServicesCats = "C__CATS__SERVICE"
    Switch = "C__CATS__SWITCH_NET"
    WAN = "C__CATS__WAN"
    EmergencyPlan = "C__CATS__EMERGENCY_PLAN"
    AirConditioning = "C__CATS__AC"
    WiFiDevice = "C__CATS__ACCESS_POINT"
    Monitor = "C__CATS__MONITOR"
    Desktop = "C__CATS__CLIENT"
    FCSwitch = "C__CATS__SWITCH_FC"
    Routing = "C__CATS__ROUTER"
    Printer = "C__CATS__PRT"
    FilesCats = "C__CATS__FILE"
    Applications = "C__CATS__APPLICATION"
    Net = "C__CATS__NET"
    MobileRadio = "C__CATS__CELL_PHONE_CONTRACT"
    ObjectGroup = "C__CATS__GROUP"
    LicenseKeys = "C__CMDB__SUBCAT__LICENCE_LIST"
    CurrentFile = "C__CMDB__SUBCAT__FILE_ACTUAL"
    FileVersions = "C__CMDB__SUBCAT__FILE_VERSIONS"
    AssignedObjectsFileObject = "C__CMDB__SUBCAT__FILE_OBJECTS"
    EmergencyPlanProperties = "C__CMDB__SUBCAT__EMERGENCY_PLAN"
    AssignedObjectsPlanLinked = "C__CMDB__SUBCAT__EMERGENCY_PLAN_LINKED_OBJECT_LIST"
    NetType = "C__CMDB__SUBCAT__WS_NET_TYPE"
    AssignedObjectsWs = "C__CMDB__SUBCAT__WS_ASSIGNMENT"
    WiringSystem = "C__CATS__WS"
    UninterruptiblePowerSupply  = "C__CATS__UPS"
    EmergencyPowerSupply = "C__CATS__EPS"
    SANZoning = "C__CATS__SAN_ZONING"
    Organization = "C__CATS__ORGANIZATION"
    MasterDataCatsOrganization = "C__CATS__ORGANIZATION_MASTER_DATA"
    PersonsOrganizations = "C__CATS__ORGANIZATION_PERSONS"
    Persons = "C__CATS__PERSON"
    MasterDataCats = "C__CATS__PERSON_MASTER"
    Login = "C__CATS__PERSON_LOGIN"
    PersonGroupMemberships = "C__CATS__PERSON_ASSIGNED_GROUPS"
    PersonGroups = "C__CATS__PERSON_GROUP"
    MasterData = "C__CATS__PERSON_GROUP_MASTER"
    Members = "C__CATS__PERSON_GROUP_MEMBERS"
    AssignedObjectsOrganization = "C__CATS__ORGANIZATION_CONTACT_ASSIGNMENT"
    AssignedObjectsPersons = "C__CATS__PERSON_CONTACT_ASSIGNMENT"
    AssignedObjectsPersonGroup  = "C__CATS__PERSON_GROUP_CONTACT_ASSIGNMENT"
    AssignedClusters = "C__CATS__CLUSTER_SERVICE"
    RelationDetails = "C__CATS__RELATION_DETAILS"
    DatabaseSchema = "C__CATS__DATABASE_SCHEMA"
    DatabaseLinks = "C__CATS__DATABASE_LINKS"
    DBMS = "C__CATS__DBMS"
    InstanceOracleDatabase = "C__CATS__DATABASE_INSTANCE"
    PDU = "C__CATS__PDU"
    Branch = "C__CATS__PDU_BRANCH"
    ParallelRelations = "C__CATS__PARALLEL_RELATION"
    DatabaseObjects = "C__CATS__DATABASE_OBJECTS"
    DatabaseAccess = "C__CATS__DATABASE_ACCESS"
    DatabaseGateway = "C__CATS__DATABASE_GATEWAY"
    Replication = "C__CATS__REPLICATION"
    ReplicationPartner = "C__CATS__REPLICATION_PARTNER"
    Installation = "C__CATS__APPLICATION_ASSIGNED_OBJ"
    Middleware = "C__CATS__MIDDLEWARE"
    CryptoCard = "C__CATS__KRYPTO_CARD"
    IPList = "C__CATS__NET_IP_ADDRESSES"
    DHCP = "C__CATS__NET_DHCP"
    Layer2Net = "C__CATS__LAYER2_NET"
    AssignedPorts = "C__CATS__LAYER2_NET_ASSIGNED_PORTS"
    Contract = "C__CATS__CONTRACT"
    ContractInformation = "C__CATS__CONTRACT_INFORMATION"
    AssignedObjectsContract = "C__CATS__CONTRACT_ALLOCATION"
    Chassis = "C__CATS__CHASSIS"
    Slots = "C__CATS__CHASSIS_SLOT"
    AssignedDevices = "C__CATS__CHASSIS_DEVICES"
    ChassisView = "C__CATS__CHASSIS_VIEW"
    Variants = "C__CATS__APPLICATION_VARIANT"
    Nagios = "C__CATS__PERSON_NAGIOS"
    NagiosPersonGroup = "C__CATS__PERSON_GROUP_NAGIOS"
    Type = "C__CATS__GROUP_TYPE"
    AssignedLogicalPorts = "C__CATS__LAYER2_NET_ASSIGNED_LOGICAL_PORTS"
    InstallationService = "C__CATS__APPLICATION_SERVICE_ASSIGNED_OBJ"
    InstallationDBMS = "C__CATS__APPLICATION_DBMS_ASSIGNED_OBJ"
    NetZoneCats = "C__CATS__NET_ZONE"
    OperatingSystems = "C__CATS__OPERATING_SYSTEM"


class ObjectStatusField(enum.Enum):
    C__RECORD_STATUS__BIRTH = 1
    C__RECORD_STATUS__NORMAL = 2
    C__RECORD_STATUS__ARCHIVED = 3
    C__RECORD_STATUS__DELETED = 4
    C__RECORD_STATUS__TEMPLATE = 6
    C__RECORD_STATUS__MASS_CHANGES_TEMPLATE = 7


class DeleteStatusField(enum.Enum):
    ArchiveObject = "C__RECORD_STATUS__ARCHIVED"
    MarkObjectAsDeleted = "C__RECORD_STATUS__DELETED"
    PurgeObjectFromDatabase = "C__RECORD_STATUS__PURGE"
