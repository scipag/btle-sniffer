# -*- coding: utf-8 -*-

"""
Provides constants common in the Bluetooth HCI protocol.
"""

import enum

HCI_MAX_EVENT_SIZE = 260


class Status(enum.IntEnum):
    """
    Collection of HCI return states.
    """
    Success = 0x00
    UnknownHciCommand = 0x01
    UnknownConnectionIdentifier = 0x02
    HardwareFailure = 0x03
    PageTimeout = 0x04
    AuthenticationFailure = 0x05
    PinOrKeyMissing = 0x06
    MemoryCapacityExceeded = 0x07
    ConnectionTimeout = 0x08
    ConnectionLimitExceeded = 0x09
    SynchronousConnectionLimitExceeded = 0x0a
    ACLConnectionAlreadyExists = 0x0b
    CommandDisallowed = 0x0c
    ConnectionRejectedLimitedResources = 0x0d
    ConnectionRejectedSecurityReasons = 0x0e
    ConnectionRejectedUnnacceptableBDAddr = 0x0f
    ConnectionAcceptTimeoutExceeded = 0x10
    UnsupportedFeatureOrParameterValue = 0x11
    InvalidHciCommandParameters = 0x12
    RemoteUserTerminatedConnection = 0x13
    RemoteDeviceTerminatedConnectionLowResources = 0x14
    RemoteDeviceTerminatedConnectionPowerOff = 0x15
    ConnectionTerminatedLocalHost = 0x16
    RepeatedAttempts = 0x17
    PairingNotAllowed = 0x18
    UnknownLmpPdu = 0x19
    UnsupportedRemoteFeature = 0x1a
    ScoOffsetRejected = 0x1b
    ScoIntervalRejected = 0x1c
    ScoAirModeRejected = 0x1d
    InvalidLmpParameters = 0x1e
    UnspecifiedError = 0x1f
    UnsupportedLmpParameterValue = 0x20
    RoleChangeNotAllowed = 0x21
    LmpResponseTimeout = 0x22
    LmpErrorTransactionCollision = 0x23
    LmpPduNotAllowed = 0x24
    EncryptionModeNotAcceptable = 0x25
    LinkKeyCannotChange = 0x26
    RequestedQosNotSupported = 0x27
    InstantPassed = 0x28
    PairingWithUnitKeyNotSupported = 0x29
    DifferentTransactionCollision = 0x2a
    QosUnnacceptableParameter = 0x2c
    QosRejected = 0x2d
    ChannelClassificationNotSupported = 0x2e
    InsufficientSecurity = 0x2f
    ParameterOutOfMandatoryRange = 0x30
    RoleSwitchPending = 0x32
    RoleSwitchFailed = 0x35
    ExtendedInquiryResponseTooLarge = 0x36
    SecureSimplePairingNotSupportedByHost = 0x37
    HostBusyPairing = 0x38
    ConnectionRejectedNoSuitableChannel = 0x39
    ControllerBusy = 0x3a
    UnacceptableConnectionParameters = 0x3b
    DirectedAdvertisingTimeout = 0x3c
    ConnectionTerminatedMicFailure = 0x3d
    ConnectionEstablishFailure = 0x3e
    MacConnectionFailed = 0x3f
    CoarseClockAdjustmentRejected = 0x40


class PacketType(enum.IntEnum):
    """
    Known HCI packet types.
    """
    Invalid = 0x00
    Command = 0x01
    Async = 0x02
    Sync = 0x03
    Event = 0x04


class Event(enum.IntEnum):
    """
    Common HCI event types.
    """
    CommandComplete = 0x0e
    CommandStatus = 0x0f
    HardwareError = 0x10
    DataBufferOverflow = 0x1a
    Le = 0x3e
    VendorSpecific = 0xff


class LeEvent(enum.IntEnum):
    """
    Common HCI LE event types.
    """
    LeAdvertisingReport = 0x02


class GapProfile(enum.IntEnum):
    """
    GAP communication roles/profiles.
    """
    Broadcaster = 0x01
    Observer = 0x02
    Peripheral = 0x04
    Central = 0x08


class DiscoveryType(enum.IntEnum):
    """
    LeAdvertisingReport message type.
    """
    ConnectableUndirectedAdvertising = 0x00
    ConnectableDirectedAdvertising = 0x01
    ScannableUndirectedAdvertising = 0x02
    NonConnectableUndirectedAdvertising = 0x03
    ScanResponse = 0x04


class AddressType(enum.IntEnum):
    """
    Device address type.
    """
    PublicDeviceAddress = 0x00
    RandomDeviceAddress = 0x01
    PublicIdentityAddress = 0x02
    RandomIdentityAddress = 0x03
    UnknownAddressType = 0x04


class ScanType(enum.IntEnum):
    """
    LE scan type.
    """
    PassiveScan = 0x00
    ActiveScan = 0x01


class FilterPolicy(enum.IntEnum):
    """
    LE scan filter policy.
    """
    UndirectedAdsOnly = 0x00
    WhitelistedOnly = 0x01
    ResolvableDirected = 0x02
    WhitelistedAndResolvableDirected = 0x03


class AdType(enum.IntEnum):
    """
    Advertisement data type.
    """
    Flags = 0x01
    IncompleteListOf16BitServiceClassUUIDs = 0x02
    CompleteListOf16BitServiceClassUUIDs = 0x03
    IncompleteListOf32BitServiceClassUUIDs = 0x04
    CompleteListOf32BitServiceClassUUIDs = 0x05
    IncompleteListOf128BitServiceClassUUIDs = 0x06
    CompleteListOf128BitServiceClassUUIDs = 0x07
    ShortenedLocalName = 0x08
    CompleteLocalName = 0x09
    TxPowerLevel = 0x0a
    ClassOfDevice = 0x0d
    SimplePairingHashC192 = 0x0e
    SimplePairingRandomizerR192 = 0x0f
    SecurityManagerTKValue = 0x10
    SecurityManagerOutOfBandFlags = 0x11
    SlaveConnectionIntervalRange = 0x12
    ListOf16BitServiceSolicitationUUIDs = 0x14
    ListOf32BitServiceSolicitationUUIDs = 0x1f
    ListOf128BitServiceSolicitationUUIDs = 0x15
    ServiceData16BitUUID = 0x16
    ServiceData32BitUUID = 0x20
    ServiceData128BitUUID = 0x21
    LeSecureConnectionsConfirmationValue = 0x22
    LeSecureConnectionsRandomValue = 0x23
    URI = 0x24
    IndoorPositioning = 0x25
    TransportDiscoveryData = 0x26
    PublicTargetAddress = 0x17
    RandomTargetAddress = 0x18
    Appearance = 0x19
    AdvertisingInterval = 0x1a
    LeBluetoothDeviceAddress = 0x1b
    LeRole = 0x1c
    SimplePairingHashC256 = 0x1d
    SimplePairingRandomizerR256 = 0x1e
    InformationData = 0x3d
    ManufacturerSpecificData = 0xff


class CompanyId(enum.IntEnum):
    """
    Known company identifiers.
    """
    Racketrydoo =  0x0CB5
    EberspaecherClimateControlSystemsGmbH =  0x0CB4
    janovaGmbH =  0x0CB3
    SHINKAWASensorTechnologyInc =  0x0CB2
    RFCreations =  0x0CB1
    SwipeSenseInc =  0x0CB0
    NEURINNOV =  0x0CAF
    EvidentCorporation =  0x0CAE
    ShenzhenOpenhearingTechCOLTD =  0x0CAD
    ShenzhenShokzCoLtd =  0x0CAC
    HERUTUELECTRONICSCORPORATION =  0x0CAB
    ShenzhenPoseidonNetworkTechnologyCoLtd =  0x0CAA
    MievoTechnologiesPrivateLimited =  0x0CA9
    SonasInc =  0x0CA8
    VerveInfoTecPtyLtd =  0x0CA7
    MeggerLtd =  0x0CA6
    PrincessCruiseLinesLtd =  0x0CA5
    MITSUBISHIELECTRICLIGHTINGCOLTD =  0x0CA4
    MAQUETGmbH =  0x0CA3
    XSENSELTD =  0x0CA2
    YAMAHAMOTORCOLTD =  0x0CA1
    BIGBEN =  0x0CA0
    DragonflyEnergyCorp =  0x0C9F
    ECCELCORPORATIONSAS =  0x0C9E
    RibbiotINC =  0x0C9D
    SunstoneRTLSIpariSzolgaltatoKorlatoltFelelosseguTarsasag =  0x0C9C
    NTTsonorityInc =  0x0C9B
    ALFInc =  0x0C9A
    VireHealthOy =  0x0C99
    MiXTelematicsInternationalPTYLTD =  0x0C98
    Deako =  0x0C97
    HBHightechGmbH =  0x0C96
    GemstoneLightsCanadaLtd =  0x0C95
    BaxterHealthcareCorporation =  0x0C94
    MovesenseOy =  0x0C93
    KessebhmerErgonomietechnikGmbH =  0x0C92
    YashuSystems =  0x0C91
    WESCOAG =  0x0C90
    RadarAutomobileSalesShandongCoLtd =  0x0C8F
    TechnoconEngineeringLtd =  0x0C8E
    toniesGmbH =  0x0C8D
    TMobileUSA =  0x0C8C
    HeavysInc =  0x0C8B
    ARTISTICCOGLOBALLtd =  0x0C8A
    AGZZXOPTOELECTRONICSTECHNOLOGYCOLTD =  0x0C89
    NextivityInc =  0x0C88
    WeltekTechnologiesCompanyLimited =  0x0C87
    QingdaoEastsoftCommunicationTechnologyCoLtd =  0x0C86
    AmlogicInc =  0x0C85
    MAXONINDUSTRIESINC =  0x0C84
    WatchdogSystemsLLC =  0x0C83
    NACON =  0x0C82
    CarrierCorporation =  0x0C81
    CARDIOIDTECHNOLOGIESLDA =  0x0C80
    RochesterSensorsLLC =  0x0C7F
    BOOMINGOFTHINGS =  0x0C7E
    ThreeALogicsInc =  0x0C7D
    MopekaProductsLLC =  0x0C7C
    PTSADAMAYAGRAHATEKNOLOGI =  0x0C7B
    TriductorTechnologySuzhouInc =  0x0C7A
    ZhuhaiSmartlinkTechnologyCoLtd =  0x0C79
    CHARGTRONIOTPRIVATELIMITED =  0x0C78
    TEACCorporation =  0x0C77
    ShenzhenGwellTimesTechnologyCoLtd =  0x0C76
    EmbeddedEngineeringSolutionsLLC =  0x0C75
    yupiteru =  0x0C74
    TrumaGertetechnikGmbHCoKG =  0x0C73
    StreetCarORVLLC =  0x0C72
    BitGreenTechnolabzOPCPrivateLimited =  0x0C71
    SCARABSOLUTIONSLTD =  0x0C70
    ParakeyAB =  0x0C6F
    SensaLLC =  0x0C6E
    FidureCorp =  0x0C6D
    SNIFFLOGICLTD =  0x0C6C
    GILSONSAS =  0x0C6B
    CONSORCIOTRUSTCONTROLNETTEL =  0x0C6A
    BLITZelectricmotorsLTD =  0x0C69
    EmerjaCorporation =  0x0C68
    TRACKTINGSRL =  0x0C67
    DENSmartHomeBV =  0x0C66
    WAKOCOLTD =  0x0C65
    dormakabaHoldingAG =  0x0C64
    phgPeterHengstlerGmbHCoKG =  0x0C63
    PhiatonCorporation =  0x0C62
    NNOXXInc =  0x0C61
    KEBAEnergyAutomationGmbH =  0x0C60
    NanjingLinkpowerMicroelectronicsCoLtd =  0x0C5F
    BlueIDGmbH =  0x0C5E
    StepUpSolutionsApS =  0x0C5D
    MGMWIRELESSSHOLDINGSPTYLTD =  0x0C5C
    AlbanGiacomoSPA =  0x0C5B
    LockswitchSdnBhd =  0x0C5A
    CYBERDYNEInc =  0x0C59
    HyksoInc =  0x0C58
    UNEEGmedicalAS =  0x0C57
    RheemSalesCompanyInc =  0x0C56
    ZintouchBV =  0x0C55
    HiVizLightingInc =  0x0C54
    TacoInc =  0x0C53
    ESCEALIMITED =  0x0C52
    INNOVASRL =  0x0C51
    ImostarTechnologiesInc =  0x0C50
    SharkNinjaOperatingLLC =  0x0C4F
    TactileEngineeringInc =  0x0C4E
    SeekwaveTechnologyColtd =  0x0C4D
    OrpyxMedicalTechnologiesInc =  0x0C4C
    ADTRANInc =  0x0C4B
    atSpiroApS =  0x0C4A
    twopoundsgmbh =  0x0C49
    VALEOMANAGEMENTSERVICES =  0x0C48
    EpsilonElectronicslnc =  0x0C47
    GranwinIoTTechnologyGuangzhouCoLtd =  0x0C46
    BroseVerwaltungSEBamberg =  0x0C45
    ONCELABSLLC =  0x0C44
    BerlingerCoAG =  0x0C43
    HeathConsultantsInc =  0x0C42
    ControlSolutionsLLC =  0x0C41
    HORIBALtd =  0x0C40
    StingerEquipmentInc =  0x0C3F
    BELLDESIGNInc =  0x0C3E
    WrmthCorp =  0x0C3D
    ClassifiedCycling =  0x0C3C
    ORBInnovationsLtd =  0x0C3B
    EquinosisLLC =  0x0C3A
    TIGERCORPORATION =  0x0C39
    NoritzCorporation =  0x0C38
    SignalQuestLLC =  0x0C37
    CosmicnodeBV =  0x0C36
    ThermokonSensortechnikGmbH =  0x0C35
    BYDCompanyLimited =  0x0C34
    ExegerOperationsAB =  0x0C33
    XianYisuobaoElectronicTechnologyCoLtd =  0x0C32
    KINDOOLLP =  0x0C31
    McIntoshGroupInc =  0x0C30
    BEEHEROINC =  0x0C2F
    EaseeAS =  0x0C2E
    OTFProductSourcingLLC =  0x0C2D
    ZekuTechnologyShanghaiCorpLtd =  0x0C2C
    GigaDeviceSemiconductorInc =  0x0C2B
    CaresixInc =  0x0C2A
    DENSOAIRCOOLCORPORATION =  0x0C29
    EmbectaCorp =  0x0C28
    PalElectronics =  0x0C27
    PerformanceElectronicsLtd =  0x0C26
    JURAElektroapparateAG =  0x0C25
    SMARTDTECHNOLOGIESINC =  0x0C24
    KEYTECInc =  0x0C23
    GlamoInc =  0x0C22
    FoshanViomiElectricalTechnologyCoLtd =  0x0C21
    COMELITGROUPSPA =  0x0C20
    LVICo =  0x0C1F
    ECsensecoLtd =  0x0C1E
    OFFLineJapanCoLtd =  0x0C1D
    GEMU =  0x0C1C
    RockchipElectronicsCoLtd =  0x0C1B
    CatapultGroupInternationalLtd =  0x0C1A
    ArloTechnologiesInc =  0x0C19
    CORROHM =  0x0C18
    SomnoMedLimited =  0x0C17
    TYKEEPTYLTD =  0x0C16
    GevaSolBV =  0x0C15
    FasettoInc =  0x0C14
    ScandinavianHealthLimited =  0x0C13
    IoSA =  0x0C12
    GordonMurrayDesignLimited =  0x0C11
    Cosmedsrl =  0x0C10
    AETERLINK =  0x0C0F
    ALEXDENKOCOLTD =  0x0C0E
    Mereltronbv =  0x0C0D
    MendeltronInc =  0x0C0C
    aconnoGmbH =  0x0C0B
    AutomatedPetCareProductsLLC =  0x0C0A
    SenicInc =  0x0C09
    limitedliabilitycompanyRed =  0x0C08
    CONSTRUKTSINC =  0x0C07
    LEDSmartInc =  0x0C06
    MontageConnectInc =  0x0C05
    HappyHealthInc =  0x0C04
    PuffCorp =  0x0C03
    LoomanetInc =  0x0C02
    NEOWRKSISTEMASINTELIGENTESSA =  0x0C01
    MQALimited =  0x0C00
    RatioElectricBV =  0x0BFF
    MediaCartecGmbH =  0x0BFE
    EsmSolutions =  0x0BFD
    TAelektroakustikGmbHCoKG =  0x0BFC
    DodamEnersysCoLtd =  0x0BFB
    CleanBandsSystemsLtd =  0x0BFA
    AlioInc =  0x0BF9
    InnovacionnyeResheniya =  0x0BF8
    WackerNeusonSE =  0x0BF7
    greenTEGAG =  0x0BF6
    T5tekInc =  0x0BF5
    ERLabLLC =  0x0BF4
    PONEBIOMETRICSAS =  0x0BF3
    AngelMedicalSystemsInc =  0x0BF2
    SiteIQLLC =  0x0BF1
    KIDOSPORTSCOLTD =  0x0BF0
    SafetytestGmbH =  0x0BEF
    LINKSYSUSAINC =  0x0BEE
    CORALTAIYICoLtd =  0x0BED
    MiracleEarInc =  0x0BEC
    LunaHealthInc =  0x0BEB
    TwentyFiveSevenprodajainstoritvedoo =  0x0BEA
    ShindengenElectricManufacturingCoLtd =  0x0BE9
    SensormateAG =  0x0BE8
    FresnelTechnologiesInc =  0x0BE7
    PuratapPtyLtd =  0x0BE6
    ZWILLINGJAHenckelsAktiengesellschaft =  0x0BE5
    DeepfieldConnectGmbH =  0x0BE4
    ComtelSystemsLtd =  0x0BE3
    OTCengineering =  0x0BE2
    Back40Precision =  0x0BE1
    KoizumiLightingTechnologycorp =  0x0BE0
    WINKEYENTERPRISEHONGKONGLIMITED =  0x0BDF
    Yale =  0x0BDE
    CorofloLimited =  0x0BDD
    LedworksSrl =  0x0BDC
    CHARBROILLLC =  0x0BDB
    AardexLtd =  0x0BDA
    ElicsBasisLtd =  0x0BD9
    PURASCENTSINC =  0x0BD8
    VINFASTTRADINGANDPRODUCTIONJOINTSTOCKCOMPANY =  0x0BD7
    ShenzhenInjoinicTechnologyCoLtd =  0x0BD6
    SuperBLithiumPowerBV =  0x0BD5
    nddMedizintechnikAG =  0x0BD4
    ProconAnalyticsLLC =  0x0BD3
    IDEC =  0x0BD2
    HubeiYuanTimesTechnologyCoLtd =  0x0BD1
    DuragGmbH =  0x0BD0
    LLTecGroupLLC =  0x0BCF
    NeurosityInc =  0x0BCE
    Amikosrl =  0x0BCD
    Sylvacsa =  0x0BCC
    Divesoftsro =  0x0BCB
    PerimeterTechnologiesInc =  0x0BCA
    NeuvatekInc =  0x0BC9
    OTFDistributionLLC =  0x0BC8
    SigntleInc =  0x0BC7
    TCLCOMMUNICATIONEQUIPMENTCOLTD =  0x0BC6
    AperiaTechnologiesInc =  0x0BC5
    TECHTICSENGINEERINGBV =  0x0BC4
    MCOTINC =  0x0BC3
    EntWickCo =  0x0BC2
    MieleCieKG =  0x0BC1
    READYFORSKYLLP =  0x0BC0
    HIMSAIIKS =  0x0BBF
    SAABAktiebolag =  0x0BBE
    ETHEORYPTYLTD =  0x0BBD
    T2REALITYSOLUTIONSPRIVATELIMITED =  0x0BBC
    SWISSINNOSOLUTIONSAG =  0x0BBB
    HusoINC =  0x0BBA
    SaluStimGroupOy =  0x0BB9
    INNOVAGPTYLTD =  0x0BB8
    IONATechLLC =  0x0BB7
    BuildWithRobotsInc =  0x0BB6
    XirgoTechnologiesLLC =  0x0BB5
    NewCosmosUSAInc =  0x0BB4
    FlenderGmbH =  0x0BB3
    FjordenElectraAS =  0x0BB2
    BeijingranxinintelligencetechnologyCoLTD =  0x0BB1
    EcolabInc =  0x0BB0
    NITTOKOGYOCORPORATION =  0x0BAF
    SomaLabsLLC =  0x0BAE
    RoamboticsInc =  0x0BAD
    MachfuInc =  0x0BAC
    GrandexInternationalCorporation =  0x0BAB
    InfinitegraInc =  0x0BAA
    AlltercoRoboticsltd =  0x0BA9
    GLOWFORGEINC =  0x0BA8
    hearXGroupPtyLtd =  0x0BA7
    NissanMotorCoLtd =  0x0BA6
    SONICOSENTERPRISESLLC =  0x0BA5
    VerventAudioGroup =  0x0BA4
    SonovaConsumerHearingGmbH =  0x0BA3
    TireCheckGmbH =  0x0BA2
    BunnOMaticCorporation =  0x0BA1
    DataSciencesInternational =  0x0BA0
    GroupLotusLimited =  0x0B9F
    AudioPartnershipPlc =  0x0B9E
    SensoriaHoldingsLTD =  0x0B9D
    KomatsuLtd =  0x0B9C
    GISMAN =  0x0B9B
    BeijingWisepoolInfiniteIntelligenceTechnologyCoLtd =  0x0B9A
    TheGoodyearTireRubberCompany =  0x0B99
    GymstoryBV =  0x0B98
    SILVERTREELABSINC =  0x0B97
    TelecomDesign =  0x0B96
    NetwakeGmbH =  0x0B95
    DreemSAS =  0x0B94
    HangzhouBroadLinkTechnologyCoLtd =  0x0B93
    CitisendSolutionsSL =  0x0B92
    AlfenICUBV =  0x0B91
    IneosAutomotiveLimited =  0x0B90
    SenscommSemiconductorCoLtd =  0x0B8F
    GentleEnergyCorp =  0x0B8E
    PertechIndustriesInc =  0x0B8D
    MOTREX =  0x0B8C
    AmericanTechnologyComponentsIncorporated =  0x0B8B
    SeikoInstrumentsInc =  0x0B8A
    RotronicAG =  0x0B89
    MuguangGuangdongIntelligentLightingTechnologyCoLtd =  0x0B88
    AmpetronicLtd =  0x0B87
    TrekBicycle =  0x0B86
    VIMANATECHPTYLTD =  0x0B85
    PresidioMedicalInc =  0x0B84
    TaigaMotorsInc =  0x0B83
    MammutSportsGroupAG =  0x0B82
    SCMGroup =  0x0B81
    AXELIFE =  0x0B80
    ICUtechGmbH =  0x0B7F
    OffcodeOy =  0x0B7E
    FoundersLaneGmbH =  0x0B7D
    ScangripAS =  0x0B7C
    HardcoderOy =  0x0B7B
    ShenzhenKTCTechnologyCoLtd =  0x0B7A
    SankyoAirTechCoLtd =  0x0B79
    FIELDDESIGNINC =  0x0B78
    AixlinkChengduCoLtd =  0x0B77
    MAXcoltd =  0x0B76
    TripleWJapanInc =  0x0B75
    BQN =  0x0B74
    HARADAINDUSTRYCOLTD =  0x0B73
    GeeknetInc =  0x0B72
    lilbitODMAS =  0x0B71
    JDRFElectromagEngineeringInc =  0x0B70
    ShenzhenMalideTechnologyCoLtd =  0x0B6F
    ReactMobile =  0x0B6E
    SOLUMCOLTD =  0x0B6D
    SensitechInc =  0x0B6C
    SamsaraNetworksInc =  0x0B6B
    Dymo =  0x0B6A
    Addaday =  0x0B69
    Quhaoy =  0x0B68
    CleanSpaceTechnologyPtyLtd =  0x0B67
    MITSUBISHIELECTRICAUTOMATIONTHAILANDCOMPANYLIMITED =  0x0B66
    TheApacheSoftwareFoundation =  0x0B65
    NingBokliteElectricManufactureCoLTD =  0x0B64
    InnoluxCorporation =  0x0B63
    NOVEAENERGIES =  0x0B62
    SentekPtyLtd =  0x0B61
    RATOCSystemsInc =  0x0B60
    RiviehInc =  0x0B5F
    CELLCONTROLINC =  0x0B5E
    FujianNewlandAutoIDTechCoLtd =  0x0B5D
    ExponentialPowerInc =  0x0B5C
    ShenzhenImagineVisionTechnologyLimited =  0x0B5B
    HPShelbyManufacturingLLC =  0x0B5A
    VersaGroupBV =  0x0B59
    TOKAIDENSHIINC =  0x0B58
    CONVERTRONIXTECHNOLOGIESANDSERVICESLLP =  0x0B57
    BORAVertriebsGmbHCoKG =  0x0B56
    HGMAutomotiveElectronicsInc =  0x0B55
    EmotionFitnessGmbHCoKG =  0x0B54
    SHENZHENKAADASINTELLIGENTTECHNOLOGYCOLtd =  0x0B53
    ZIIPInc =  0x0B52
    FUNFACTORYGmbH =  0x0B51
    MeshSystemsLLC =  0x0B50
    BreeziioInc =  0x0B4F
    ICPSystemsBV =  0x0B4E
    AdamHallGmbH =  0x0B4D
    BiosBobBiz =  0x0B4C
    EMSIntegratorsLLC =  0x0B4B
    NomonoAS =  0x0B4A
    SkyHawkeTechnologies =  0x0B49
    NIOUSAInc =  0x0B48
    GentexCorporation =  0x0B47
    BirdRidesInc =  0x0B46
    ElectronicSensorsInc =  0x0B45
    nForeTechnologyCoLtd =  0x0B44
    INCITATENVIRONNEMENT =  0x0B43
    TSI =  0x0B42
    SentraxGmbH =  0x0B41
    HavellsIndiaLimited =  0x0B40
    MindRhythmInc =  0x0B3F
    ISEOSerratureSpa =  0x0B3E
    REALTIMEIDAS =  0x0B3D
    DodgeIndustrialInc =  0x0B3C
    AICsemiconductorShanghaiCoLtd =  0x0B3B
    ImpactBiosystemsInc =  0x0B3A
    Red100LightingColtd =  0x0B39
    WISYCOMSRL =  0x0B38
    OmnivoltaicEnergySolutionsLimitedCompany =  0x0B37
    SINTEF =  0x0B36
    BHSENS =  0x0B35
    CONZUMEXINDUSTRIESPRIVATELIMITED =  0x0B34
    ARMATURALLC =  0x0B33
    HalaSystemsInc =  0x0B32
    SilverWolfVehiclesInc =  0x0B31
    ARTSPA =  0x0B30
    DukeManufacturingCo =  0x0B2F
    MOCASystemInc =  0x0B2E
    REDARCELECTRONICSPTYLTD =  0x0B2D
    ILLUMAGEARInc =  0x0B2C
    MAINBOT =  0x0B2B
    ACLAirshopBV =  0x0B2A
    TechVenomEntertainmentPrivateLimited =  0x0B29
    CHACON =  0x0B28
    LumiUnitedTechnologyCoLtd =  0x0B27
    BaracodaDailyHealthtech =  0x0B26
    NIBROTECHLTD =  0x0B25
    BeiJingZiJieTiaoDongKeJiCoLtd =  0x0B24
    iRhythmTechnologiesInc =  0x0B23
    HygieneIQLLC =  0x0B22
    amsAG =  0x0B21
    TKHSecurityBV =  0x0B20
    BeijingESWINComputingTechnologyCoLtd =  0x0B1F
    PBINC =  0x0B1E
    AcceleratedSystems =  0x0B1D
    NanoleqAG =  0x0B1C
    EnerpacToolGroupCorp =  0x0B1B
    RocaSanitarioSA =  0x0B1A
    WBSPROJECTHPTYLTD =  0x0B19
    DECATHLONSE =  0x0B18
    SIGSAUERINC =  0x0B17
    GuardRFIDSolutionsInc =  0x0B16
    NAOSJAPANKK =  0x0B15
    Olumee =  0x0B14
    IOTOOLS =  0x0B13
    ToughBuiltIndustriesLLC =  0x0B12
    ThermoWorksInc =  0x0B11
    AlfaLavalCorporateAB =  0x0B10
    BEASA =  0x0B0F
    HondaLockMfgCoLtd =  0x0B0E
    SANYODENKOCoLtd =  0x0B0D
    BluPeak =  0x0B0C
    SanistaalAS =  0x0B0B
    BelunTechnologyCompanyLimited =  0x0B0A
    soonisys =  0x0B09
    ShenzhenQianfenyiIntelligentTechnologyCoLTD =  0x0B08
    WorkaroundGmbh =  0x0B07
    FAZUAGmbH =  0x0B06
    MarquardtGmbH =  0x0B05
    IPERCUT =  0x0B04
    PrecisionTriathlonSystemsLimited =  0x0B03
    IORATechnologyDevelopmentLtdSti =  0x0B02
    RESIDEOTECHNOLOGIESINC =  0x0B01
    FlaircommMicroelectronicsInc =  0x0B00
    FUSEAWARELIMITED =  0x0AFF
    EardaTechnologiesCoLtd =  0x0AFE
    WeberSensorsLLC =  0x0AFD
    CerebrumSensorTechnologiesInc =  0x0AFC
    SMTELEKTRONIKGmbH =  0x0AFB
    ChengduAmbitTechnologyCoLtd =  0x0AFA
    UnistoAG =  0x0AF9
    FirstDesignSystemInc =  0x0AF8
    Irdeto =  0x0AF7
    AMETEKInc =  0x0AF6
    UnitechElectronicInc =  0x0AF5
    RadioworksMicroelectronicsPTYLTD =  0x0AF4
    SevenZeroOnexInc =  0x0AF3
    ShanghaiAllLinkMicroelectronicsCoLtd =  0x0AF2
    CRADERSCOLTD =  0x0AF1
    LeupoldStevensInc =  0x0AF0
    GLPGermanLightProductsGmbH =  0x0AEF
    VelentiumLLC =  0x0AEE
    SaxonarGmbH =  0x0AED
    FUTEKADVANCEDSENSORTECHNOLOGYINC =  0x0AEC
    SquareInc =  0x0AEB
    BordaTechnology =  0x0AEA
    FLIRSystemsAB =  0x0AE9
    LEVELsro =  0x0AE8
    SunplusTechnologyCoLtd =  0x0AE7
    Hexology =  0x0AE6
    unuGmbH =  0x0AE5
    DALIAlliance =  0x0AE4
    GlobalMed =  0x0AE3
    IMATRIXSYSTEMSINC =  0x0AE2
    ChengDuForThinkTechnologyCoLtd =  0x0AE1
    ViceroyDevicesCorporation =  0x0AE0
    DouglasDynamicsLLC =  0x0ADF
    VoceraCommunicationsInc =  0x0ADE
    BossAudio =  0x0ADD
    DuravitAG =  0x0ADC
    ReelablesInc =  0x0ADB
    CodefabrikGmbH =  0x0ADA
    ShenzhenAimoreCoLtd =  0x0AD9
    FranzKaldeweiGmbHCoKG =  0x0AD8
    ALKOGeraeteGmbH =  0x0AD7
    nymeaGmbH =  0x0AD6
    StreamitBV =  0x0AD5
    ZhuhaiPantumElectroniscCoLtd =  0x0AD4
    SSVSoftwareSystemsGmbH =  0x0AD3
    LautsprecherTeufelGmbH =  0x0AD2
    EAGLEKINGDOMTECHNOLOGIESLIMITED =  0x0AD1
    NordicStrongApS =  0x0AD0
    CACITechnologies =  0x0ACF
    KOBATAGAUGEMFGCOLTD =  0x0ACE
    VisuallexSportInternationalLimited =  0x0ACD
    Nuvoton =  0x0ACC
    iseIndividuelleSoftwareundElektronikGmbH =  0x0ACB
    ShenzhenCoolKitTechnologyCoLtd =  0x0ACA
    SwedlockAB =  0x0AC9
    KeepinCoLtd =  0x0AC8
    ChengduAichTechnologyCoLtd =  0x0AC7
    BarnesGroupInc =  0x0AC6
    FlexoptixGmbH =  0x0AC5
    CODIUM =  0x0AC4
    KenzenInc =  0x0AC3
    RealMegaMicroelectronicstechnologyShanghaiCoLtd =  0x0AC2
    ShenzhenJingxunTechnologyCoLtd =  0x0AC1
    OmniIDUSAINC =  0x0AC0
    PAULHARTMANNAG =  0x0ABF
    RobkooInformationTechnologiesCoLtd =  0x0ABE
    InventasAS =  0x0ABD
    KCCSMobileEngineeringCoLtd =  0x0ABC
    RDASsro =  0x0ABB
    OpenBionicsLtd =  0x0ABA
    STL =  0x0AB9
    SensaiIncorporated =  0x0AB8
    LogTagNorthAmericaInc =  0x0AB7
    XenterInc =  0x0AB6
    ElstatElectronicsLtd =  0x0AB5
    EllenbyTechnologiesInc =  0x0AB4
    INNERRANGEPTYLTD =  0x0AB3
    TouchTronicsInc =  0x0AB2
    InVueSecurityProductsInc =  0x0AB1
    Visiontronicsro =  0x0AB0
    AIAIAIApS =  0x0AAF
    PSEngineeringInc =  0x0AAE
    AdevoConsultingAB =  0x0AAD
    OSMHKLimited =  0x0AAC
    AnhuiListenaiCo =  0x0AAB
    ComputimeInternationalLtd =  0x0AAA
    SpintlyInc =  0x0AA9
    ZencontrolPtyLtd =  0x0AA8
    UrbanistaAB =  0x0AA7
    Realityworksinc =  0x0AA6
    ShenzhenUascentTechnologyCoLtd =  0x0AA5
    FAZEPROLLC =  0x0AA4
    DICCorporation =  0x0AA3
    CareBloomLLC =  0x0AA2
    LINCOGNTECHNOLOGYCOLIMITED =  0x0AA1
    LoyTecelectronicsGmbH =  0x0AA0
    istaInternationalGmbH =  0x0A9F
    LifePlusInc =  0x0A9E
    CanonFinetechNiscaInc =  0x0A9D
    XianFengyuInformationTechnologyCoLtd =  0x0A9C
    EelloLLC =  0x0A9B
    TEMKINASSOCIATESLLC =  0x0A9A
    ShanghaihighflyingelectronicstechnologyCoLtd =  0x0A99
    FoilInc =  0x0A98
    SensTek =  0x0A97
    LightricityLtd =  0x0A96
    PamexInc =  0x0A95
    OOBIKInc =  0x0A94
    GiPStechSrl =  0x0A93
    CarestreamDentalLLC =  0x0A92
    MonarchInternationalInc =  0x0A91
    ShenzhenGrandsunElectronicCoLtd =  0x0A90
    TOTOLTD =  0x0A8F
    PerfectCompany =  0x0A8E
    JCMTECHNOLOGIESSA =  0x0A8D
    DelpSyssro =  0x0A8C
    SANlightGmbH =  0x0A8B
    HAINBUCHGMBHSPANNENDETECHNIK =  0x0A8A
    SESImagotag =  0x0A89
    PSAPeugeotCitroen =  0x0A88
    ShanghaiSmartSystemTechnologyCoLtd =  0x0A87
    ALIZENTInternational =  0x0A86
    SnowballTechnologyCoLtd =  0x0A85
    GreennoteInc =  0x0A84
    RivataInc =  0x0A83
    Corsair =  0x0A82
    UniversalBiosensorsPtyLtd =  0x0A81
    CleerLimited =  0x0A80
    IntuityMedical =  0x0A7F
    KEBAHandoverAutomationGmbH =  0x0A7E
    FreedmanElectronicsPtyLtd =  0x0A7D
    WAFERLOCK =  0x0A7C
    UniqAirOy =  0x0A7B
    EmlidLimited =  0x0A7A
    WebastoSE =  0x0A79
    ShenzhenSunricherTechnologyLimited =  0x0A78
    AXTROPTELTD =  0x0A77
    SynapticsIncorporated =  0x0A76
    DeltaCycleCorporation =  0x0A75
    MICROSONSA =  0x0A74
    InnohomeOy =  0x0A73
    JumoGmbHCoKG =  0x0A72
    SenquipPtyLtd =  0x0A71
    Ooma =  0x0A70
    WarnerBros =  0x0A6F
    PacSaneLimited =  0x0A6E
    KUUKANJYOKINCoLtd =  0x0A6D
    Pokkels =  0x0A6C
    OlympicOphthalmicsInc =  0x0A6B
    ScribbleDesignInc =  0x0A6A
    HAPPIESTBABYINC =  0x0A69
    FocusIngenieriaSRL =  0x0A68
    BeijingSuperHexaCenturyTechnologyCOLtd =  0x0A67
    JUSTMORPHPTELTD =  0x0A66
    LytxINC =  0x0A65
    GeopalsystemAS =  0x0A64
    GremsyJSC =  0x0A63
    MOKOTECHNOLOGYLtd =  0x0A62
    SmartParksBV =  0x0A61
    DATANGSEMICONDUCTORTECHNOLOGYCOLTD =  0x0A60
    stryker =  0x0A5F
    LaceClipsllc =  0x0A5E
    MGEnergySystemsBV =  0x0A5D
    InnovativeDesignLabsInc =  0x0A5C
    LEGICIdentsystemsAG =  0x0A5B
    SontheimIndustrieElektronikGmbH =  0x0A5A
    TourBuiltLLC =  0x0A59
    IndigoDiabetes =  0x0A58
    MeizhouGuoWeiElectronicsCoLtd =  0x0A57
    ambie =  0x0A56
    InugoSystemsLimited =  0x0A55
    SQLTechnologiesCorp =  0x0A54
    KKMCOMPANYLIMITED =  0x0A53
    FollowSenseEuropeBV =  0x0A52
    CSIRO =  0x0A51
    NextscapeInc =  0x0A50
    VANMOOFGlobalHoldingBV =  0x0A4F
    ToytecCorporation =  0x0A4E
    LocknTechnologiesPrivateLimited =  0x0A4D
    SiFliTechnologiesshanghaiInc =  0x0A4C
    MistyWestEnergyandTransportLtd =  0x0A4B
    MapLargeInc =  0x0A4A
    VentureResearchInc =  0x0A49
    JRCMobilityInc =  0x0A48
    TheWandCompanyLtd =  0x0A47
    BeijingHCInfiniteTechnologyLimited =  0x0A46
    ThreeSISecuritySystemsInc =  0x0A45
    NovidanInc =  0x0A44
    BuschSystemsInternationalInc =  0x0A43
    MotionalysisInc =  0x0A42
    OPEXCorporation =  0x0A41
    GEWISSSpA =  0x0A40
    ShenzhenYopeakOptoelectronicsTechnologyCoLtd =  0x0A3F
    HefeiYunlianSemiconductorCoLtd =  0x0A3E
    DELABIE =  0x0A3D
    SitecoGmbH =  0x0A3C
    GalileoTechnologyLimited =  0x0A3B
    IncotexCoLtd =  0x0A3A
    BLUETICKETINGSRL =  0x0A39
    BouffaloLabNanjingLtd =  0x0A38
    TwoFiveOntarioInc =  0x0A37
    NGKSPARKPLUGCOLTD =  0x0A36
    safectoryGmbH =  0x0A35
    LuxerCorporation =  0x0A34
    WMFAG =  0x0A33
    PinnacleTechnologyInc =  0x0A32
    NevroCorp =  0x0A31
    AirWeigh =  0x0A30
    InstamicInc =  0x0A2F
    ZumaArrayLimited =  0x0A2E
    ShenzhenFeasycomTechnologyCoLtd =  0x0A2D
    ShenzhenHTIntelligentControlCoLtd =  0x0A2C
    PaceBaitIVS =  0x0A2B
    YamahaCorporation =  0x0A2A
    WorthcloudTechnologyCoLtd =  0x0A29
    NanoFlexPowerCorporation =  0x0A28
    AYUDEVICESPRIVATELIMITED =  0x0A27
    LouisVuitton =  0x0A26
    EranFinancialServicesLLC =  0x0A25
    AtmosicTechnologiesInc =  0x0A24
    BIXOLONCOLTD =  0x0A23
    DAIICHIKOSHOCOLTD =  0x0A22
    ApollogicSpzoo =  0x0A21
    JiangxiInnotechTechnologyCoLtd =  0x0A20
    DeVilbissHealthcareLLC =  0x0A1F
    CombiQAB =  0x0A1E
    APIK =  0x0A1D
    INPEAKSC =  0x0A1C
    EmbravaPtyLtd =  0x0A1B
    LinkLabsInc =  0x0A1A
    MaxellLtd =  0x0A19
    CambridgeAnimalTechnologiesLtd =  0x0A18
    PlumeDesignInc =  0x0A17
    RIDEVISIONLTD =  0x0A16
    SyngInc =  0x0A15
    CROXELINC =  0x0A14
    Tec4medLifeScienceGmbH =  0x0A13
    DysonTechnologyLimited =  0x0A12
    Sensolus =  0x0A11
    SUBARUCorporation =  0x0A10
    LIXILCorporation =  0x0A0F
    RolandCorporation =  0x0A0E
    BluePeacockGmbH =  0x0A0D
    ShanghaiYidianIntelligentTechnologyCoLtd =  0x0A0C
    SIANASystems =  0x0A0B
    VolanTechnologyInc =  0x0A0A
    ECCT =  0x0A09
    OrasOy =  0x0A08
    ReflowPtyLtd =  0x0A07
    ShanghaiwuqimicroelectronicsCoLtd =  0x0A06
    SouthwireCompanyLLC =  0x0A05
    FlosonicsMedical =  0x0A04
    donutroboticsCoLtd =  0x0A03
    AyxonDynamicsGmbH =  0x0A02
    CleveronAS =  0x0A01
    AmplerBikesOU =  0x0A00
    AIRSTAR =  0x09FF
    LichtvisionEngineeringGmbH =  0x09FE
    KeepTechnologiesInc =  0x09FD
    Confidex =  0x09FC
    TOITUCOLTD =  0x09FB
    ListenTechnologiesCorporation =  0x09FA
    HangzhouYaguanTechnologyCoLTD =  0x09F9
    ROSRL =  0x09F8
    SENSATECCoLtd =  0x09F7
    MobileActionTechnologyInc =  0x09F6
    OKIElectricIndustryCoLtd =  0x09F5
    SpectrumTechnologiesInc =  0x09F4
    BeijingZeroZeroInfinityTechnologyCoLtd =  0x09F3
    AudearaPtyLtd =  0x09F2
    OMDigitalSolutionsCorporation =  0x09F1
    WatchGasBV =  0x09F0
    SteinelSolutionsAG =  0x09EF
    OJMARSA =  0x09EE
    SibelInc =  0x09ED
    YukonadvancedopticsworldwideUAB =  0x09EC
    KEANELECTRONICSPTYLTD =  0x09EB
    AthlosOy =  0x09EA
    LumenRadioAB =  0x09E9
    MelangeSystemsPvtLtd =  0x09E8
    KabushikigaishaHANERON =  0x09E7
    MasoniteCorporation =  0x09E6
    Mobilogix =  0x09E5
    CPSAS =  0x09E4
    FridayHomeAps =  0x09E3
    WuhanLinptechCoLtd =  0x09E2
    TagNTracInc =  0x09E1
    PreddioTechnologiesInc =  0x09E0
    MagnusTechnologySdnBhd =  0x09DF
    JLDTechnologySolutionsLLC =  0x09DE
    InnowareDevelopmentAB =  0x09DD
    AON2Ltd =  0x09DC
    BionicAvionicsInc =  0x09DB
    NagravisionSA =  0x09DA
    VivoSensMedicalGmbH =  0x09D9
    SynergyTecnologiaemSistemasLtda =  0x09D8
    Coyotta =  0x09D7
    EARTEKNIKISITMEVEODIOMETRICIHAZLARISANAYIVETICARETANONIMSIRKETI =  0x09D6
    GEARRADIOELECTRONICSCORP =  0x09D5
    ORBISInc =  0x09D4
    HeartHeroinc =  0x09D3
    TemperatureSensitiveSolutionsSystemsSwedenAB =  0x09D2
    ABLEPAYTECHNOLOGIESAS =  0x09D1
    ChessWiseBV =  0x09D0
    BlueStreakIoTLLC =  0x09CF
    JuliusBlumGmbH =  0x09CE
    Blyott =  0x09CD
    Senso4sdoo =  0x09CC
    HxEngineeringLLC =  0x09CB
    Mobitrace =  0x09CA
    CrowdGlowLtd =  0x09C9
    XUNTONG =  0x09C8
    CombustionLLC =  0x09C7
    HonorDeviceCoLtd =  0x09C6
    HungYiMicroelectronicsCoLtd =  0x09C5
    UVISIO =  0x09C4
    JAPANTOBACCOINC =  0x09C3
    UniversalAudioInc =  0x09C2
    Rosewill =  0x09C1
    AnotherBraininc =  0x09C0
    SpanIOInc =  0x09BF
    VesselLtd =  0x09BE
    CentreSuissedElectroniqueetdeMicrotechniqueSA =  0x09BD
    AerosensLLC =  0x09BC
    SkyStreamCorporation =  0x09BB
    ElimoEngineeringLtd =  0x09BA
    SAVOYELECTRONICLIGHTING =  0x09B9
    PlayerDataLimited =  0x09B8
    BoutLabsLLC =  0x09B7
    PegasusTechnologiesInc =  0x09B6
    AUTECGesellschaftfuerAutomationstechnikmbH =  0x09B5
    PentaLockAps =  0x09B4
    BlueXMicroelectronicsCorpLtd =  0x09B3
    DYPHI =  0x09B2
    BLINQY =  0x09B1
    DeublinCompanyLLC =  0x09B0
    ifLinkOpenCommunity =  0x09AF
    PozyxNV =  0x09AE
    NarhwallInc =  0x09AD
    Ambiq =  0x09AC
    DashLogicInc =  0x09AB
    PHOTODYNAMICINCORPORATED =  0x09AA
    NipponCeramicCoLtd =  0x09A9
    KHNSolutionsLLC =  0x09A8
    PaybuddyApS =  0x09A7
    BEIJINGELECTRICVEHICLECOLTD =  0x09A6
    SecurityEnhancementSystemsLLC =  0x09A5
    KUMHOELECTRICSINC =  0x09A4
    ARDUINOSA =  0x09A3
    ENGAGENOWDATASCIENCESPRIVATELIMITED =  0x09A2
    VOSSystemsLLC =  0x09A1
    ProofDiagnosticsInc =  0x09A0
    KoyaMedicalInc =  0x099F
    StepOneLimited =  0x099E
    YKKAPInc =  0x099D
    deisterelectronicGmbH =  0x099C
    SendumWirelessCorporation =  0x099B
    NewAudioLLC =  0x099A
    eTacticaehf =  0x0999
    PixieDustTechnologiesInc =  0x0998
    NextMind =  0x0997
    CEFeinGmbH =  0x0996
    BronkhorstHighTechBV =  0x0995
    VT42PtyLtd =  0x0994
    AbsoluteAudioLabsBV =  0x0993
    BigKaiserPrecisionToolingLtd =  0x0992
    TelenorASA =  0x0991
    AntonPaarGmbH =  0x0990
    AktiebolagetRegin =  0x098F
    ADVEEZ =  0x098E
    C3WIRELESSLLC =  0x098D
    bGridBV =  0x098C
    MequonicEngineeringSL =  0x098B
    Biovigil =  0x098A
    WIKAAlexanderWiegandSECoKG =  0x0989
    BHMTechProduktionsgesellschaftmbH =  0x0988
    TSEBRAKESINC =  0x0987
    CelloHillLLC =  0x0986
    LumosHealthInc =  0x0985
    TeraTronGmbH =  0x0984
    FeedbackSportsLLC =  0x0983
    ELPROBUCHSAG =  0x0982
    BernardKroneHoldingSECoKG =  0x0981
    DEKRATESTINGANDCERTIFICATIONSAU =  0x0980
    ISEMARSRL =  0x097F
    SonicSensoryInc =  0x097E
    CLBBV =  0x097D
    ThorleyIndustriesLLC =  0x097C
    CTEKSwedenAB =  0x097B
    CORECORPORATION =  0x097A
    BIOTRONIKSECoKG =  0x0979
    ZifferEinsGmbHCoKG =  0x0978
    TOYOTAmotorcorporation =  0x0977
    FaunaAudioGmbH =  0x0976
    BlueIOTBeijingTechnologyCoLtd =  0x0975
    ABEYE =  0x0974
    PopitOy =  0x0973
    ClosedJointStockCompanyZavodFlometrZavodFlometrCJSC =  0x0972
    GA =  0x0971
    IBADosimetryGmbH =  0x0970
    LundMotionProductsInc =  0x096F
    BandIndustriesinc =  0x096E
    GunwerksLLC =  0x096D
    NineThreeQuebecinc =  0x096C
    GuideIDBV =  0x096B
    dricosInc =  0x096A
    WoanTechnologyShenzhenCoLtd =  0x0969
    ActevMotorsInc =  0x0968
    NeoMaterialsandConsultingInc =  0x0967
    PointGuardLLC =  0x0966
    AsahiKaseiCorporation =  0x0965
    CountrymateTechnologyLimited =  0x0964
    MoonbirdBV =  0x0963
    GLSolutionsKK =  0x0962
    LinkuraAB =  0x0961
    SenaTechnologiesInc =  0x0960
    NUANCEHEARINGLTD =  0x095F
    BioEchoNetinc =  0x095E
    ElectronicTheatreControls =  0x095D
    LogiLubeLLC =  0x095C
    LismoreInstrumentsLimited =  0x095B
    SelektBilgisayarlletisimUrunlerilnsaatSanayiveTicaretLimitedSirketi =  0x095A
    HerdDoggInc =  0x0959
    ZTECorporation =  0x0958
    OhsungElectronics =  0x0957
    Kerlink =  0x0956
    BrevilleGroup =  0x0955
    Julbo =  0x0954
    LogiLubeLLC2 =  0x0953
    ApptricityCorporation =  0x0952
    PPRS =  0x0951
    Capetech =  0x0950
    LimitedLiabilityCompanyMikrotikls =  0x094F
    PassiveBoltInc =  0x094E
    tkLABSINC =  0x094D
    GimmiSysGmbH =  0x094C
    KindevaDrugDeliveryLP =  0x094B
    ZwiftInc =  0x094A
    MetronomHealthEurope =  0x0949
    WearableLinkLimited =  0x0948
    FirstLightTechnologiesLtd =  0x0947
    AMCInternationalAlfaMetalcraftCorporationAG =  0x0946
    GlobeJiangsuCoLtd =  0x0945
    Agitrondoo =  0x0944
    Reserved =  0x0943
    TRANSSIONHOLDINGSLIMITED =  0x0942
    RivianAutomotiveLLC =  0x0941
    HeroWorkoutGmbH =  0x0940
    JEPICOCorporation =  0x093F
    CatalyftLabsInc =  0x093E
    AdolfWuerthGmbHCoKG =  0x093D
    XenomaInc =  0x093C
    ENSESOLLC =  0x093B
    LinkedSemiMicroelectronicsXiamenCoLtd =  0x093A
    ASTEMCoLtd =  0x0939
    HenwayTechnologiesLTD =  0x0938
    RealThingksGmbH =  0x0937
    ElekonAG =  0x0936
    ReconnectInc =  0x0935
    KiteSpringInc =  0x0934
    SRAM =  0x0933
    BarVisionLLC =  0x0932
    BREATHINGSCoLtd =  0x0931
    JamesWalkerRotaBoltLimited =  0x0930
    COBOSpA =  0x092F
    PSGmbH =  0x092E
    LeggettPlattIncorporated =  0x092D
    PCIPrivateLimited =  0x092C
    TekHome =  0x092B
    SapplVerwaltungsundBetriebsGmbH =  0x092A
    QingdaoHaierTechnologyCoLtd =  0x0929
    AiRISTA =  0x0928
    ROOQGmbH =  0x0927
    GooligumTechnologiesPtyLtd =  0x0926
    YukaiEngineeringInc =  0x0925
    FundacionTecnaliaResearchandInnovation =  0x0924
    JSBTECHPTELTD =  0x0923
    ShanghaiMXCHIPInformationTechnologyCoLtd =  0x0922
    KAHAPTELTD =  0x0921
    OmnisenseLimited =  0x0920
    MyzeeTechnology =  0x091F
    MelbotStudiosSociedadLimitada =  0x091E
    InnokindInc =  0x091D
    OblamatikAG =  0x091C
    LuminosticsInc =  0x091B
    AlbertronicBV =  0x091A
    NOSMDLIMITED =  0x0919
    TechnosphereLabsPvtLtd =  0x0918
    ASRMicroelectronicsShenZhenCoLtd =  0x0917
    AmbientSensorsLLC =  0x0916
    HondaMotorCoLtd =  0x0915
    INEOSENSE =  0x0914
    BraveheartWirelessInc =  0x0913
    NerbioMedicalSoftwarePlatformsInc =  0x0912
    DouglasLightingControlsInc =  0x0911
    ASRMicroelectronicsShanghaiCoLtd =  0x0910
    VCInc =  0x090F
    OPTIMUSIOTTECHLLP =  0x090E
    IOTInventGmbH =  0x090D
    RadiawaveTechnologiesCoLtd =  0x090C
    EMBRlabsINC =  0x090B
    ZhuhaiHoksiTechnologyCOLTD =  0x090A
    SeventymaiCoLtd =  0x0909
    PinpointInnovationsLimited =  0x0908
    UserHelloLLC =  0x0907
    ScopeLogisticalSolutions =  0x0906
    YandexServicesAG =  0x0905
    SUNCORPORATION =  0x0904
    DATAMARSInc =  0x0903
    TSCAutoIDTechnologyCoLtd =  0x0902
    Lucimed =  0x0901
    BeijingZizaiTechnologyCoLTD =  0x0900
    PlastimoldProductsInc =  0x08FF
    KetronixsSdnBhd =  0x08FE
    BioIntelliSenseInc =  0x08FD
    HillRom =  0x08FC
    DarkglassElectronicsOy =  0x08FB
    TrooCorporation =  0x08FA
    SpacelabsMedicalInc =  0x08F9
    instagridGmbH =  0x08F8
    MTDProductsIncAffiliates =  0x08F7
    DermalPhotonicsCorporation =  0x08F6
    TymtixTechnologiesPrivateLimited =  0x08F5
    KodimoTechnologiesCompanyLimited =  0x08F4
    PSPPauliServicesProductsGmbH =  0x08F3
    Microoled =  0x08F2
    TheLSStarrettCompany =  0x08F1
    JoovvInc =  0x08F0
    CumulusDigitalSystemsInc =  0x08EF
    AskeyComputerCorp =  0x08EE
    IMIHydronicEngineeringInternationalSA =  0x08ED
    DensoCorporation =  0x08EC
    BeijingBigMomentTechnologyCoLtd =  0x08EB
    COWBELLENGINEERINGCOLTD =  0x08EA
    TaiwanIntelligentHomeCorp =  0x08E9
    Naonext =  0x08E8
    BarrotTechnologyCoLtd =  0x08E7
    EnesoTecnologiadeAdaptacionSL =  0x08E6
    CrowdConnectedLtd =  0x08E5
    Rashidovltd =  0x08E4
    RepublicWirelessInc =  0x08E3
    ShenzhenSimoTechnologycoLTD =  0x08E2
    KOZOKEIKAKUENGINEERINGInc =  0x08E1
    PhiliaTechnology =  0x08E0
    IRISOHYAMACOLTD =  0x08DF
    TEConnectivityCorporation =  0x08DE
    codeQ =  0x08DD
    SHENZHENAUKEYEBUSINESSCOLTD =  0x08DC
    TertiumTechnology =  0x08DB
    MiridiaTechnologyIncorporated =  0x08DA
    PointrLabsLimited =  0x08D9
    WARES =  0x08D8
    InovonicsCorp =  0x08D7
    NomeOy =  0x08D6
    KEYes =  0x08D5
    ADATATechnologyCoLTD =  0x08D4
    NovelBitsLLC =  0x08D3
    VirscientLimited =  0x08D2
    SensoviumInc =  0x08D1
    ESTOMInfotechKft =  0x08D0
    betternotstealmybikeUGwithlimitedliability =  0x08CF
    ZIMICORPORATION =  0x08CE
    ifly =  0x08CD
    TGMTECHNOLOGYCOLTD =  0x08CC
    JTINNOVATIONSLIMITED =  0x08CB
    NubiaTechnologyCoLtd =  0x08CA
    NoventaAG =  0x08C9
    LiteboxerTechnologiesInc =  0x08C8
    MonadnockSystemsLtd =  0x08C7
    IntegraOpticsInc =  0x08C6
    JWagnerGmbH =  0x08C5
    CellAssistLLC =  0x08C4
    CHIPOLOdoo =  0x08C3
    LindinventAB =  0x08C2
    RaydenEarthLTD =  0x08C1
    AccentAdvancedSystemsSLU =  0x08C0
    SIRCCoLtd =  0x08BF
    ubisystechnologiesGmbH =  0x08BE
    bf1systemslimited =  0x08BD
    PrevaylLimited =  0x08BC
    Tokairikacoltd =  0x08BB
    HYPERICEINC =  0x08BA
    UShinLtd =  0x08B9
    CheckTechnologySolutionsLLC =  0x08B8
    ABBInc =  0x08B7
    BoehringerIngelheimVetmedicaGmbH =  0x08B6
    TransferFi =  0x08B5
    SengledCoLtd =  0x08B4
    IONIQSkincareGmbHCoKG =  0x08B3
    PFSCHWEISSTECHNOLOGIEGMBH =  0x08B2
    COREvisionBV =  0x08B1
    TrivediAdvancedTechnologiesLLC =  0x08B0
    PolideaSpzoo =  0x08AF
    MoticonReGoAG =  0x08AE
    KayamaticsLimited =  0x08AD
    TopreCorporation =  0x08AC
    CoburnTechnologyLLC =  0x08AB
    SZDJITECHNOLOGYCOLTD =  0x08AA
    FraunhoferIIS =  0x08A9
    ShanghaiKfcubeInc =  0x08A8
    TGR1618Limited =  0x08A7
    IntelligenceworksInc =  0x08A6
    UMEHEALLtd =  0x08A5
    RealmeChongqingMobileTelecommunicationsCorpLtd =  0x08A4
    HoffmannSE =  0x08A3
    EpicSystemsCoLtd =  0x08A2
    EXEOTECHCORPORATION =  0x08A1
    AclaraTechnologiesLLC =  0x08A0
    WitschiElectronicLtd =  0x089F
    iSENSinc =  0x089E
    JJADEEnterpriseLLC =  0x089D
    EmbeddedDevicesCoCompany =  0x089C
    SauconTechnologies =  0x089B
    PrivatelimitedcompanyTeltonika =  0x089A
    SFSunimarketAG =  0x0899
    SensiboInc =  0x0898
    CurrentLightingSolutionsLLC =  0x0897
    NokianRenkaatOyj =  0x0896
    Gimermedical =  0x0895
    EPIFIT =  0x0894
    MaytronicsLtd =  0x0893
    IngenieurbueroBirnfeldUGhaftungsbeschraenkt =  0x0892
    SmartWirelessGmbHCoKG =  0x0891
    NICHIEIINTECCOLTD =  0x0890
    TaitInternationalLimited =  0x088F
    GIGATMSINC =  0x088E
    SolitonSystemsKK =  0x088D
    GBSolutioncoLtd =  0x088C
    TricorderArraayTechnologiesLLC =  0x088B
    sclaksrl =  0x088A
    XANTHIO =  0x0889
    EnPointeFencingPtyLtd =  0x0888
    HydroGearLimitedPartnership =  0x0887
    MovellaTechnologiesBV =  0x0886
    LEVOLORINC =  0x0885
    ControlidIndustriaComerciodeHardwareeServicosdeTecnologiaLtda =  0x0884
    WintersteigerAG =  0x0883
    PSYONICInc =  0x0882
    Optalert =  0x0881
    imagiLabsAB =  0x0880
    PhillipsConnectTechnologiesLLC =  0x087F
    OnebarnetLimited =  0x087E
    KonftelAB =  0x087D
    CrosscanGmbH =  0x087C
    BYSTAMP =  0x087B
    ZRFLLC =  0x087A
    MIZUNOCorporation =  0x0879
    TheChamberlainGroupInc =  0x0878
    TomeInc =  0x0877
    SmartResQApS =  0x0876
    BernerInternationalLLC =  0x0875
    TreegreenLimited =  0x0874
    InnophaseIncorporated =  0x0873
    ElevenHealthTechnologiesLimited =  0x0872
    DensionElektronikaiKft =  0x0871
    WyzeLabsInc =  0x0870
    TrackunitAS =  0x086F
    VorwerkElektrowerkeGmbHCoKG =  0x086E
    Biometrikadoo =  0x086D
    RevvoTechnologiesInc =  0x086C
    PacificTrackLLC =  0x086B
    OdicIncorporated =  0x086A
    EVVASicherheitstechnologieGmbH =  0x0869
    WIOsenseGmbHCoKG =  0x0868
    WesternDigitalTechologiesInc =  0x0867
    LAONZCoLtd =  0x0866
    EmergencyLightingProductsLimited =  0x0865
    Rafaelmicro =  0x0864
    YotronicsTechnologyCoLtd =  0x0863
    SmartDrive =  0x0862
    SmartSensorLabsLtd =  0x0861
    AlflexProductsBV =  0x0860
    COMPEGPSTEAMSOCIEDADLIMITADA =  0x085F
    KrogSystemsLLC =  0x085E
    GuilinZhishenInformationTechnologyCoLtd =  0x085D
    ACOSCOLTD =  0x085C
    NisshinboMicroDevicesInc =  0x085B
    DAKATECH =  0x085A
    BlueUp =  0x0859
    SOUNDBOKS =  0x0858
    ParsylInc =  0x0857
    CanopyGrowthCorporation =  0x0856
    HeliosSportsInc =  0x0855
    TapSoundSystem =  0x0854
    PektronGroupLimited =  0x0853
    CognososInc =  0x0852
    SubecaInc =  0x0851
    YealinkXiamenNetworkTechnologyCoLTD =  0x0850
    EmbeddedFitnessBV =  0x084F
    CarolColeCompany =  0x084E
    SafePort =  0x084D
    ORSOInc =  0x084C
    BiotechwareSRL =  0x084B
    ARCOM =  0x084A
    DoppleTechnologiesBV =  0x0849
    JUJUJOINTSCANADACORP =  0x0848
    DNANUDGELIMITED =  0x0847
    USoundGmbH =  0x0846
    DometicCorporation =  0x0845
    PepperlFuchsGmbH =  0x0844
    FRAGRANCEDELIVERYTECHNOLOGIESLTD =  0x0843
    TangshanHongJiaelectronictechnologycoLTD =  0x0842
    GeneralLuminaireShanghaiCoLtd =  0x0841
    DownRangeSystemsLLC =  0x0840
    DLinkCorp =  0x083F
    ZorachkaLTD =  0x083E
    TokenizeInc =  0x083D
    BeerTechLTD =  0x083C
    PiaggioFastForward =  0x083B
    BPWBergischeAchsenKommanditgesellschaft =  0x083A
    Apuissance3 =  0x0839
    EtymoticResearchInc =  0x0838
    vivoMobileCommunicationCoLtd =  0x0837
    BitwardsOy =  0x0836
    CanopyGrowthCorporation2 =  0x0835
    RIKENKEIKICOLTD =  0x0834
    ConneqtechBV =  0x0833
    IntermotiveInc =  0x0832
    FoxbleLLC =  0x0831
    CoreHealthandFitnessLLC =  0x0830
    BlippitAB =  0x082F
    ABBSpA =  0x082E
    INCUSPERFORMANCELTD =  0x082D
    INGICSTECHNOLOGYCOLTD =  0x082C
    shenzhenfitcareelectronicsCoLtd =  0x082B
    MitutoyoCorporation =  0x082A
    HEXAGONMETROLOGYDIVISIONROMER =  0x0829
    ShanghaiSuishengInformationTechnologyCoLtd =  0x0828
    Kickmaker =  0x0827
    HyundaiMotorCompany =  0x0826
    CMEPTELTD =  0x0825
    EightPowerLimited =  0x0824
    NexiteLtd =  0x0823
    adafruitindustries =  0x0822
    INOVAGeophysicalInc =  0x0821
    BrilliantHomeTechnologyInc =  0x0820
    eSenseLabLTD =  0x081F
    iNFORMTechnologyGmbH =  0x081E
    PotrykusHoldingsandDevelopmentLLC =  0x081D
    BobrickWashroomEquipmentInc =  0x081C
    DIM3 =  0x081B
    ShenzhenConex =  0x081A
    HunterDouglasInc =  0x0819
    tatwahSA =  0x0818
    WangsAllianceCorporation =  0x0817
    SPICASYSTEMSLLC =  0x0816
    SKCInc =  0x0815
    Ossurhf =  0x0814
    FlextronicsInternationalUSAInc =  0x0813
    MstreamTechnologiesInc =  0x0812
    BeckerAntriebeGmbH =  0x0811
    LECOCorporation =  0x0810
    ParadoxEngineeringSA =  0x080F
    TATTCOMLLC =  0x080E
    AzbilCo =  0x080D
    IngyBV =  0x080C
    NanoleafCanadaLimited =  0x080B
    Altaneos =  0x080A
    TrulliAudio =  0x0809
    SISTEMASKERNSOCIEDADANMINA =  0x0808
    ECDElectronicComponentsGmbHDresden =  0x0807
    TYRISwedenAB =  0x0806
    UrbanmindedLtd =  0x0805
    AndonHealthCoLtd =  0x0804
    Domintellsa =  0x0803
    NantSoundInc =  0x0802
    CRONUSELECTRONICSLTD =  0x0801
    Optek =  0x0800
    maxonmotorltd =  0x07FF
    BIROTA =  0x07FE
    JSKCOLTD =  0x07FD
    RenaultSA =  0x07FC
    AccessCoLtd =  0x07FB
    KlipschGroupInc =  0x07FA
    DirectCommunicationSolutionsInc =  0x07F9
    quipNYCInc =  0x07F8
    CesarSystemsLtd =  0x07F7
    ShenzhenTonliScienceandTechnologyDevelopmentCoLtd =  0x07F6
    BytonNorthAmericaCorporation =  0x07F5
    MEDIRLABOrvosbiologiaiFejlesztoKorlatoltFelelosseguTarsasag =  0x07F4
    DIGISINEENERGYTECHCOLTD =  0x07F3
    SERENEGROUPINC =  0x07F2
    ZimiInnovationsPtyLtd =  0x07F1
    emoolacomPtyLtd =  0x07F0
    AktiebolagetSandvikCoromant =  0x07EF
    KidzTekLLC =  0x07EE
    JouleIQINC =  0x07ED
    FrecceLLC =  0x07EC
    NOVABASESRL =  0x07EB
    ShapeLogInc =  0x07EA
    HfeleGmbHCoKG =  0x07E9
    PacketcraftInc =  0x07E8
    KomfortIQInc =  0x07E7
    WaybeyondLimited =  0x07E6
    MinutInc =  0x07E5
    GeeksmeSL =  0x07E4
    AirohaTechnologyCorp =  0x07E3
    AlfredKaercherSECoKG =  0x07E2
    LucieLabs =  0x07E1
    EdifierInternationalLimited =  0x07E0
    SnaponIncorporated =  0x07DF
    UnlimitedEngineeringSL =  0x07DE
    LinearCircuits =  0x07DD
    ThingOSGmbHCoKG =  0x07DC
    RemedeeLabs =  0x07DB
    STARLITECoLtd =  0x07DA
    MicroDesignInc =  0x07D9
    SOLUTIONSAMBRAINC =  0x07D8
    NanjingQinhengMicroelectronicsCoLtd =  0x07D7
    ecobeeInc =  0x07D6
    hootsclassicGmbH =  0x07D5
    KanoComputingLimited =  0x07D4
    LIVNEXCoLtd =  0x07D3
    ReactAccessibilityLimited =  0x07D2
    ShanghaiPanchipMicroelectronicsCoLtd =  0x07D1
    HangzhouTuyaInformationTechnologyCoLtd =  0x07D0
    NeoSensoryInc =  0x07CF
    ShanghaiTopChipMicroelectronicsTechCoLTD =  0x07CE
    SmartWaveTechnologiesCanadaInc =  0x07CD
    BarnacleSystemsInc =  0x07CC
    WestPharmaceuticalServicesInc =  0x07CB
    ModulSystemHHAB =  0x07CA
    SkullcandyInc =  0x07C9
    WRLDSCreationsAB =  0x07C8
    iaconicDesignInc =  0x07C7
    BlueneticsGmbH =  0x07C6
    JuneLifeInc =  0x07C5
    JohnsonHealthTechNA =  0x07C4
    CIMTechniquesInc =  0x07C3
    RadinnAB =  0x07C2
    AWChestertonCompany =  0x07C1
    BiralAG =  0x07C0
    REGULALtd =  0x07BF
    AxentiaTechnologiesAB =  0x07BE
    GenedriveDiagnosticsLtd =  0x07BD
    KDCIRCUITSLLC =  0x07BC
    EPICSRL =  0x07BB
    BatteryBizInc =  0x07BA
    EponaBiotecLimited =  0x07B9
    iSwip =  0x07B8
    ETABLISSEMENTSGEORGESRENAULT =  0x07B7
    SoundbrennerLimited =  0x07B6
    CRONOCHIPSL =  0x07B5
    HormannKGAntriebstechnik =  0x07B4
    TwoNTELEKOMUNIKACEas =  0x07B3
    MoecoIOTInc =  0x07B2
    ThomasDynamicsLLC =  0x07B1
    GVConceptsInc =  0x07B0
    HongKongBouffaloLabLimited =  0x07AF
    AureaSolucoesTecnologicasLtda =  0x07AE
    NewH3CTechnologiesCoLtd =  0x07AD
    LoupeDeckOy =  0x07AC
    GraniteRiverSolutionsInc =  0x07AB
    TheKrogerCo =  0x07AA
    BruelKjaerSoundVibration =  0x07A9
    conbeeGmbH =  0x07A8
    ZumeInc =  0x07A7
    MusenConnectInc =  0x07A6
    RABLightingInc =  0x07A5
    XiamenMageInformationTechnologyCoLtd =  0x07A4
    ComcastCable =  0x07A3
    RokuInc =  0x07A2
    ApolloNeuroscienceInc =  0x07A1
    RegentBeleuchtungskorperAG =  0x07A0
    PuneScientificLLP =  0x079F
    SmartloxxGmbH =  0x079E
    DigibalePtyLtd =  0x079D
    SkyUKLimited =  0x079C
    CSTELECTRONICSPROPRIETARYLIMITED =  0x079B
    GuangDongOppoMobileTelecommunicationsCorpLtd =  0x079A
    PlantChoirInc =  0x0799
    HoloKitInc =  0x0798
    WateridGmbH =  0x0797
    StarLeafLtd =  0x0796
    GASTECCORPORATION =  0x0795
    TheCocaColaCompany =  0x0794
    AEVspolsro =  0x0793
    CricutInc =  0x0792
    ScoscheIndustriesInc =  0x0791
    KOMPANAS =  0x0790
    HannaInstrumentsInc =  0x078F
    FUJIMICNIIGATAINC =  0x078E
    CybexGmbH =  0x078D
    MINIBREWHOLDINGBV =  0x078C
    OptikamTechInc =  0x078B
    TheWildflowerFoundation =  0x078A
    PCBPiezotronicsInc =  0x0789
    BubblyNetLLC =  0x0788
    PangaeaSolution =  0x0787
    HLPControlsPtyLimited =  0x0786
    O2MicroInc =  0x0785
    audifonGmbHCoKG =  0x0784
    ESEMBERLIMITEDLIABILITYCOMPANY =  0x0783
    DeviceDriveAS =  0x0782
    QingpingTechnologyBeijingCoLtd =  0x0781
    FinchTechnologiesLtd =  0x0780
    GlenviewSoftwareCorporation =  0x077F
    SparkageInc =  0x077E
    Sensoritysro =  0x077D
    radiuscoltd =  0x077C
    AmaterZInc =  0x077B
    NiruhaSystemsPrivateLimited =  0x077A
    LoopshoreOy =  0x0779
    KOAMTACINC =  0x0778
    Cue =  0x0777
    CyberTransportControlGmbH =  0x0776
    FoureBusinessGmbH =  0x0775
    CMAXAsiaLimited =  0x0774
    EchoflexSolutionsInc =  0x0773
    ThirdwayvInc =  0x0772
    CorvexConnectedSafety =  0x0771
    InnoConMedicalApS =  0x0770
    SuccessfulEndeavoursPtyLtd =  0x076F
    WuQitechnologiesInc =  0x076E
    GraesslinGmbH =  0x076D
    NoodleTechnologyinc =  0x076C
    EngineeredMedicalTechnologies =  0x076B
    DmacMobileDevelopmentsLLC =  0x076A
    ForceImpactTechnologies =  0x0769
    PelotonInteractiveInc =  0x0768
    NITTODENKOASIATECHNICALCENTREPTELTD =  0x0767
    ARTANDPROGRAMINC =  0x0766
    VoxxInternational =  0x0765
    WWZNInformationTechnologyCompanyLimited =  0x0764
    PIKOLINSL =  0x0763
    TerOptaLtd =  0x0762
    MantisTechLLC =  0x0761
    VimarSpA =  0x0760
    RemoteSolutionCoLTD =  0x075F
    KaterraInc =  0x075E
    RHOMBUSSYSTEMSINC =  0x075D
    AntitronicsInc =  0x075C
    SmartSensorDevicesAB =  0x075B
    HARMANCOLTD =  0x075A
    ShanghaiInGeekCyberSecurityCoLtd =  0x0759
    umanSenseAB =  0x0758
    ELAInnovation =  0x0757
    LumensForLessInc =  0x0756
    BrotherIndustriesLtd =  0x0755
    MichaelParkin =  0x0754
    JLGIndustriesInc =  0x0753
    ElatecGmbH =  0x0752
    ChangshaJEMOICDesignCoLtd =  0x0751
    HamiltonProfessionalServicesofCanadaIncorporated =  0x0750
    MEDIATECHSRL =  0x074F
    EAGLEDETECTIONSA =  0x074E
    AmtechSystemsLLC =  0x074D
    iopoolsa =  0x074C
    SarvavidSoftwareSolutionsLLP =  0x074B
    IllusoryStudiosLLC =  0x074A
    DIAODIAOBeijingTechnologyCoLtd =  0x0749
    GuangZhouKuGouComputerTechnologyCoLtd =  0x0748
    ORTechnologiesPtyLtd =  0x0747
    SeitecElektronikGmbH =  0x0746
    WIZNOVAInc =  0x0745
    SOCOMEC =  0x0744
    Sanofi =  0x0743
    DMLLLC =  0x0742
    MACSRL =  0x0741
    HITIQLIMITED =  0x0740
    BeijingUnisocTechnologiesCoLtd =  0x073F
    BluepackSRL =  0x073E
    BeijingHaoHengTianTechCoLtd =  0x073D
    AcubitApS =  0x073C
    FantiniCosmispa =  0x073B
    ChandlerSystemsInc =  0x073A
    JiangsuQinhengCoLtd =  0x0739
    GlassSecurityPteLtd =  0x0738
    LLCNavitek =  0x0737
    LunaXIOInc =  0x0736
    UpRightTechnologiesLTD =  0x0735
    DiUSComputingPtyLtd =  0x0734
    IguanavationInc =  0x0733
    DairyTechInc =  0x0732
    ABLICInc =  0x0731
    WildlifeAcousticsInc =  0x0730
    OnePlusElectronicsShenzhenCoLtd =  0x072F
    OpenPlatformSystemsLLC =  0x072E
    SaferaOy =  0x072D
    GWAHygieneGmbH =  0x072C
    BitkeyInc =  0x072B
    JMRembeddedsystemsGmbH =  0x072A
    SwaraLinkTechnologies =  0x0729
    EliLillyandCompany =  0x0728
    STALKITAS =  0x0727
    PHCCorporation =  0x0726
    TedeeSpzoo =  0x0725
    GuangzhouSuperSoundInformationTechnologyCoLtd =  0x0724
    FordMotorCompany =  0x0723
    XiamenEholderElectronicsCoLtd =  0x0722
    CloverNetworkInc =  0x0721
    OculeveInc =  0x0720
    DongguanLieshengElectronicCoLtd =  0x071F
    DONGGUANHELEELECTRONICSCOLTD =  0x071E
    exoTICSystems =  0x071D
    F5SportsInc =  0x071C
    Precor =  0x071B
    REVSMARTWEARABLEHKCOLTD =  0x071A
    COREIOTPTYLTD =  0x0719
    IDIBAIXenginneering =  0x0718
    iQsquareBV =  0x0717
    Altonics =  0x0716
    MBARCLABSInc =  0x0715
    MindPeaceSafetyLLC =  0x0714
    RespiriLimited =  0x0713
    BullGroupCompanyLimited =  0x0712
    ABAXAS =  0x0711
    AudiodoAB =  0x0710
    CaliforniaThingsInc =  0x070F
    FiveCoSarl =  0x070E
    SmartSnuggPtyLtd =  0x070D
    BeijingWinnerMicroelectronicsCoLtd =  0x070C
    ElementProductsInc =  0x070B
    HufHlsbeckFrstGmbHCoKG =  0x070A
    CarewearCorp =  0x0709
    BeInteractiveCoLtd =  0x0708
    EssityHygieneandHealthAktiebolag =  0x0707
    WernhervonBraunCenterforASdvancedResearch =  0x0706
    ABElectrolux =  0x0705
    JBXDesignsInc =  0x0704
    BeijingJingdongCenturyTradingCoLtd =  0x0703
    AkcijusabiedribaSAFTEHNIKA =  0x0702
    PAFERSTECH =  0x0701
    TraqFreqLLC =  0x0700
    RedpineSignalsInc =  0x06FF
    MahrGmbH =  0x06FE
    ESSEmbeddedSystemSolutionsInc =  0x06FD
    TomCommunicationIndustrialCoLtd =  0x06FC
    SartoriusAG =  0x06FB
    EnequiAB =  0x06FA
    happybrushGmbH =  0x06F9
    BodyPlusTechnologyCoLtd =  0x06F8
    WILKASchliesstechnikGmbH =  0x06F7
    VituloPlusBV =  0x06F6
    VigilTechnologiesInc =  0x06F5
    TouchTechnologyLtd =  0x06F4
    AlfredInternationalInc =  0x06F3
    TrapperDataAB =  0x06F2
    ShibutaniCoLtd =  0x06F1
    ChargyTechnologiesSL =  0x06F0
    ALCARECoLtd =  0x06EF
    AvantisSystemsLimited =  0x06EE
    JNeadesLtd =  0x06ED
    Sigur =  0x06EC
    HoustonRadarLLC =  0x06EB
    SafeLineSwedenAB =  0x06EA
    ZmartfunElectronicsInc =  0x06E9
    AlmendoTechnologiesGmbH =  0x06E8
    VELUXAS =  0x06E7
    NIHONDENGYOKOUSAKU =  0x06E6
    OPTEXCOLTD =  0x06E5
    Aluna =  0x06E4
    SpinlockLtd =  0x06E3
    AlangoTechnologiesLtd =  0x06E2
    MilestoneAVTechnologiesLLC =  0x06E1
    AvayaInc =  0x06E0
    HLISolutionsInc =  0x06DF
    NavcastInc =  0x06DE
    IntellithingsLtd =  0x06DD
    IndustrialNetworkControlsLLC =  0x06DC
    AutomaticLabsInc =  0x06DB
    ZliideTechnologiesApS =  0x06DA
    ShanghaiMountainViewSiliconCoLtd =  0x06D9
    AWCompany =  0x06D8
    FUBAAutomotiveElectronicsGmbH =  0x06D7
    JCTHealthcarePtyLtd =  0x06D6
    SensirionAG =  0x06D5
    DYNAKODETECHNOLOGYPRIVATELIMITED =  0x06D4
    TriTeqLockandSecurityLLC =  0x06D3
    CeoTronicsAG =  0x06D2
    MeyerSoundLaboratoriesIncorporated =  0x06D1
    EtekcityCorporation =  0x06D0
    BelpartsNV =  0x06CF
    FIORGENTZ =  0x06CE
    DIGCorporation =  0x06CD
    DongguanSmartActionTechnologyCoLtd =  0x06CC
    DyewareLLC =  0x06CB
    ShenzhenZhongguangInfotechTechnologyDevelopmentCoLtd =  0x06CA
    MYLAPSBV =  0x06C9
    StorzBickelGmbHCoKG =  0x06C8
    SomatixInc =  0x06C7
    SimmTronicLimited =  0x06C6
    UrbanCompassInc =  0x06C5
    DreamLabsGmbH =  0x06C4
    KingIElectronicsCoLtd =  0x06C3
    MeasurlogicInc =  0x06C2
    AlarmcomHoldingsInc =  0x06C1
    CAMESpA =  0x06C0
    DelcomProductsInc =  0x06BF
    HitSeedOy =  0x06BE
    ABBOy =  0x06BD
    TWSSrl =  0x06BC
    LeaftronixAnalogicSolutionsPrivateLimited =  0x06BB
    BeaconzoneLtd =  0x06BA
    BeflexInc =  0x06B9
    ShadeCraftInc =  0x06B8
    iCOGNIZEGmbH =  0x06B7
    SociometricSolutionsInc =  0x06B6
    WabilogicLtd =  0x06B5
    SencilionOy =  0x06B4
    TheHablabApS =  0x06B3
    TussockInnovation2013Limited =  0x06B2
    SimpliSafeInc =  0x06B1
    BRKBrandsInc =  0x06B0
    ShoofTechnologies =  0x06AF
    SenseQInc =  0x06AE
    InnovaSeaSystemsInc =  0x06AD
    IngchipsTechnologyCoLtd =  0x06AC
    HMSIndustrialNetworksAB =  0x06AB
    ProdualOy =  0x06AA
    SoundmaxElectronicsLimited =  0x06A9
    GDMideaAirConditioningEquipmentCoLtd =  0x06A8
    ChipseaTechnologiesShenZhenCorp =  0x06A7
    RoambeeCorporation =  0x06A6
    TEKZITELPTYLTD =  0x06A5
    LIMNOCoLtd =  0x06A4
    NymbusLLC =  0x06A3
    GlobalworxGmbH =  0x06A2
    CardoSystemsLtd =  0x06A1
    OBIQLocationTechnologyInc =  0x06A0
    FlowMotionTechnologiesAS =  0x069F
    DeltaElectronicsInc =  0x069E
    VakarosLLC =  0x069D
    NoomiAB =  0x069C
    DragonchipLimited =  0x069B
    AderoInc =  0x069A
    RandomLabSAS =  0x0699
    WoodITSecurityLLC =  0x0698
    StemcoProductsInc =  0x0697
    GunakarPrivateLimited =  0x0696
    KokiHoldingsCoLtd =  0x0695
    TALaboratoriesLLC =  0x0694
    HachDanaher =  0x0693
    GeorgFischerAG =  0x0692
    CuriePointAB =  0x0691
    EccrineSystemsInc =  0x0690
    JRMGroupLimited =  0x068F
    RazerInc =  0x068E
    JetBeepInc =  0x068D
    ChangzhouSoundDragonElectronicsandAcousticsCoLtd =  0x068C
    JiangsuTeranovoTechCoLtd =  0x068B
    RaytacCorporation =  0x068A
    Tacxbv =  0x0689
    AmstedDigitalSolutionsInc =  0x0688
    CherryGmbH =  0x0687
    inQsCoLtd =  0x0686
    GreenwaldIndustries =  0x0685
    DermalappsLLC =  0x0684
    EltakoGmbH =  0x0683
    PhotronLimited =  0x0682
    TradeFIDESas =  0x0681
    MannkindCorporation =  0x0680
    NETGRIDSNCDIBISSOLIMATTEOCAMPOREALESIMONETOGNETTIFEDERICO =  0x067F
    MbientLabInc =  0x067E
    FormAthleticaInc =  0x067D
    TileInc =  0x067C
    IFARMINC =  0x067B
    TheEnergyConservatoryInc =  0x067A
    FouriiiiInnovationsInc =  0x0679
    SABIKOffshoreGmbH =  0x0678
    InnovationFirstInc =  0x0677
    ExpaiSolutionsPrivateLimited =  0x0676
    DecoEnterprisesInc =  0x0675
    BeSpoon =  0x0674
    InnovaIdeasLimited =  0x0673
    Kopi =  0x0672
    BuzzProductsLtd =  0x0671
    GemaSwitzerlandGmbH =  0x0670
    HugTechnologyLtd =  0x066F
    EurotronikKranjdoo =  0x066E
    VensoEcoSolutionsAB =  0x066D
    ZtoveApS =  0x066C
    DewertOkinGmbH =  0x066B
    BradyWorldwideInc =  0x066A
    LivanovaUSAInc =  0x0669
    BlebTechnologysrl =  0x0668
    SparkTechnologyLabsInc =  0x0667
    WTOWerkzeugEinrichtungenGmbH =  0x0666
    PureInternationalLimited =  0x0665
    RHATECHNOLOGIESLTD =  0x0664
    AdvancedTelemetrySystemsInc =  0x0663
    ParticleIndustriesInc =  0x0662
    ModeLightingLimited =  0x0661
    RTCIndustriesInc =  0x0660
    RicohCompanyLtd =  0x065F
    AloAB =  0x065E
    PanduitCorp =  0x065D
    PixArtImagingInc =  0x065C
    SesamSolutionsBV =  0x065B
    ZoundIndustriesInternationalAB =  0x065A
    UnSeenTechnologiesOy =  0x0659
    PayexNorgeAS =  0x0658
    MeshtronixLimited =  0x0657
    ZhuHaiAdvanProTechnologyCompanyLimited =  0x0656
    RenishawPLC =  0x0655
    LedlenserGmbHCoKG =  0x0654
    MeggittSA =  0x0653
    ITZInnovationsundTechnologiezentrumGmbH =  0x0652
    StasisLabsInc =  0x0651
    CoravinInc =  0x0650
    DigitalMatterPtyLtd =  0x064F
    KRUXWorksTechnologiesPrivateLimited =  0x064E
    iLOQOy =  0x064D
    ZumtobelGroupAG =  0x064C
    ScaleTecLtd =  0x064B
    OpenResearchInstituteInc =  0x064A
    RyeexTechnologyCoLtd =  0x0649
    UltuneTechnologies =  0x0648
    MEDEL =  0x0647
    SGVGroupHoldingGmbHCoKG =  0x0646
    BM3 =  0x0645
    ApogeeInstruments =  0x0644
    makitacorporation =  0x0643
    BluetrumTechnologyCoLtd =  0x0642
    RevenueCollectionSystemsFRANCESAS =  0x0641
    DishNetworkLLC =  0x0640
    LDLTECHNOLOGY =  0x063F
    TheIndoorLabLLC =  0x063E
    XradioTechnologyCoLtd =  0x063D
    ContecMedicalSystemsCoLtd =  0x063C
    KromekGroupPlc =  0x063B
    ProlojikLimited =  0x063A
    ShenzhenMinewTechnologiesCoLtd =  0x0639
    LXSOLUTIONSPTYLIMITED =  0x0638
    GiPInnovationToolsGmbH =  0x0637
    ELECTRONICAINTEGRALDESONIDOSA =  0x0636
    Crookwood =  0x0635
    FanstelCorp =  0x0634
    WangiLaiPLT =  0x0633
    HugoMullerGmbHCoKG =  0x0632
    FortioriDesignLLC =  0x0631
    AsthreaDOO =  0x0630
    ONKYOCorporation =  0x062F
    Procept =  0x062E
    VosslohSchwabeDeutschlandGmbH =  0x062D
    ASPionGmbH =  0x062C
    MinebeaMitsumiInc =  0x062B
    LunaticoAstronomiaSL =  0x062A
    PHONEPEPVTLTD =  0x0629
    EnstoOy =  0x0628
    WEGSA =  0x0627
    Amplifico =  0x0626
    SquarePandaInc =  0x0625
    BiovotionAG =  0x0624
    PhiladelphiaScientificUKLimited =  0x0623
    BeamLabsLLC =  0x0622
    Noordungdoo =  0x0621
    ForciotOy =  0x0620
    PhrameInc =  0x061F
    DiamondKineticsInc =  0x061E
    SENSInnovationApS =  0x061D
    UnivationsLimited =  0x061C
    silextechnologyinc =  0x061B
    RWBeckettCorporation =  0x061A
    SixGuysLabssro =  0x0619
    AudioTechnicaCorporation =  0x0618
    WIZCONNECTEDCOMPANYLIMITED =  0x0617
    OS42UGhaftungsbeschraenkt =  0x0616
    INTERACTIONCorporation =  0x0615
    OnAssetIntelligenceInc =  0x0614
    HansDinslageGmbH =  0x0613
    PlayfinityAS =  0x0612
    BeurerGmbH =  0x0611
    ADHGUARDIANUSALLC =  0x0610
    SignifyNetherlandsBV =  0x060F
    BlueairAB =  0x060E
    TDKCorporation =  0x060D
    VuzixCorporation =  0x060C
    TriaxTechnologiesInc =  0x060B
    IQAirAG =  0x060A
    BUCHILabortechnikAG =  0x0609
    KeySafeCloud =  0x0608
    RookeryTechnologyLtd =  0x0607
    JohnDeere =  0x0606
    FMWelectronicFuttereruMaierWolfOHG =  0x0605
    Cell2JackLLC =  0x0604
    FourthEvolutionInc =  0x0603
    GeberitInternationalAG =  0x0602
    SchraderElectronics =  0x0601
    iRobotCorporation =  0x0600
    WellnomicsLtd =  0x05FF
    Nikonv =  0x05FE
    Innoseis =  0x05FD
    MasbandoGmbH =  0x05FC
    ArbletInc =  0x05FB
    KonamiSportsLifeCoLtd =  0x05FA
    HagleitnerHygieneInternationalGmbH =  0x05F9
    AnkiInc =  0x05F8
    TRACMOINC =  0x05F7
    DPTechnics =  0x05F6
    GSTAG =  0x05F5
    ClearityLLC =  0x05F4
    SeeScan =  0x05F3
    TryandECOLTD =  0x05F2
    TheLinuxFoundation =  0x05F1
    beken =  0x05F0
    SIKOMAS =  0x05EF
    WristcamInc =  0x05EE
    FujiXeroxCoLtd =  0x05ED
    GycomSvenskaAB =  0x05EC
    BayerischeMotorenWerkeAG =  0x05EB
    ACSControlSystemGmbH =  0x05EA
    iconmobileGmbH =  0x05E9
    COWBOY =  0x05E8
    PressurePro =  0x05E7
    MotionInstrumentsInc =  0x05E6
    INEOENERGYSYSTEMS =  0x05E5
    TaiyoYudenCoLtd =  0x05E4
    ElementalMachinesInc =  0x05E3
    stAPPtronicsGmbH =  0x05E2
    HumanIncorporated =  0x05E1
    ViperDesignLLC =  0x05E0
    VIRTUALCLINICDIRECTLIMITED =  0x05DF
    QTMedicalINC =  0x05DE
    essentimGmbH =  0x05DD
    PetronicsInc =  0x05DC
    AvidIdentificationSystemsInc =  0x05DB
    AppliedNeuralResearchCorp =  0x05DA
    ToyoElectronicsCorporation =  0x05D9
    FarmJennyLLC =  0x05D8
    modumioAG =  0x05D7
    ZhuhaiJielitechnologyCoLtd =  0x05D6
    TEGAMInc =  0x05D5
    LAMPLIGHTCoLtd =  0x05D4
    AcurableLimited =  0x05D3
    frogblueTECHNOLOGYGmbH =  0x05D2
    LindabAB =  0x05D1
    AnovaAppliedElectronics =  0x05D0
    BiowatchSA =  0x05CF
    VZUGLtd =  0x05CE
    RJBrandsLLC =  0x05CD
    WATTSELECTRONICS =  0x05CC
    LucentWearLLC =  0x05CB
    MHLCustomInc =  0x05CA
    TBSElectronicsBV =  0x05C9
    SOMFYSAS =  0x05C8
    LippertComponentsINC =  0x05C7
    SmartAnimalTrainingSystemsLLC =  0x05C6
    SELVEGmbHCoKG =  0x05C5
    Codecoupspzoospk =  0x05C4
    RuntimeInc =  0x05C3
    GroteIndustries =  0x05C2
    PIEngineering =  0x05C1
    NaluMedicalInc =  0x05C0
    RealWorldSystemsCorporation =  0x05BF
    RFIDGlobalbySoftworkSrL =  0x05BE
    ULCRoboticsInc =  0x05BD
    LevitonMfgCoInc =  0x05BC
    OxfordMetricsplc =  0x05BB
    igloohome =  0x05BA
    SuzhouPairlinkNetworkTechnology =  0x05B9
    AmbystomaLabsInc =  0x05B8
    BeijingPineconeElectronicsCoLtd =  0x05B7
    ElecsIndustryCoLtd =  0x05B6
    verisilicon =  0x05B5
    WhiteHorseScientificltd =  0x05B4
    ParabitSystemsInc =  0x05B3
    CARELINDUSTRIESSPA =  0x05B2
    MedallionInstrumentationSystems =  0x05B1
    NewTecGmbH =  0x05B0
    OVLOOPINC =  0x05AF
    CARMATEMFGCOLTD =  0x05AE
    INIA =  0x05AD
    GoerTekDynaudioCoLtd =  0x05AC
    NofenceAS =  0x05AB
    TramexLimited =  0x05AA
    Monidor =  0x05A9
    TomAllebrandiConsulting =  0x05A8
    SonosInc =  0x05A7
    TeleconMobileLimited =  0x05A6
    KiirooBV =  0x05A5
    OEMControlsInc =  0x05A4
    AxiomwareSystemsIncorporated =  0x05A3
    ADHERIUMNZLIMITED =  0x05A2
    ShanghaiXiaoyiTechnologyCoLtd =  0x05A1
    RCPSoftwareOy =  0x05A0
    FisherPaykelHealthcare =  0x059F
    PolycomInc =  0x059E
    TandemDiabetesCare =  0x059D
    MacrogigaElectronics =  0x059C
    DataflowSystemsLimited =  0x059B
    TeledyneLecroyInc =  0x059A
    Lazlo326LLC =  0x0599
    rapitagGmbH =  0x0598
    RadioPulseInc =  0x0597
    MySmartBlinds =  0x0596
    InorProcessAB =  0x0595
    KohlerCompany =  0x0594
    SpauldingClinicalResearch =  0x0593
    IZITHERM =  0x0592
    ViasatGroupSpA =  0x0591
    Pur3Ltd =  0x0590
    HENDONSEMICONDUCTORSPTYLTD =  0x058F
    MetaPlatformsTechnologiesLLC =  0x058E
    JungheinrichAktiengesellschaft =  0x058D
    FracarroRadioindustrieSRL =  0x058C
    MaximIntegratedProducts =  0x058B
    STARTTODAYCOLTD =  0x058A
    StarTechnologies =  0x0589
    ALTTEKNIKLLC =  0x0588
    DerichsGmbH =  0x0587
    LEGRAND =  0x0586
    HearingLabTechnology =  0x0585
    GiraGiersiepenGmbHCoKG =  0x0584
    CodeBlueCommunications =  0x0583
    BreakwallAnalyticsLLC =  0x0582
    LYSTECHNOLOGIESLTD =  0x0581
    ARANZMedicalLimited =  0x0580
    ScufGamingInternationalLLC =  0x057F
    BecoInc =  0x057E
    InstinctPerformance =  0x057D
    ToorTechnologiesLLC =  0x057C
    DuracellUSOperationsInc =  0x057B
    OMNIRemotes =  0x057A
    EnsembleTechPrivateLimited =  0x0579
    WellingtonDriveTechnologiesLtd =  0x0578
    TrueWearablesInc =  0x0577
    GlobalstarInc =  0x0576
    IntegralMemroyPlc =  0x0575
    AFFORDABLEELECTRONICSINC =  0x0574
    LightingScienceGroupCorp =  0x0573
    AntTailcom =  0x0572
    PSIKICKINC =  0x0571
    ConsumerSleepSolutionsLLC =  0x0570
    BikeFinderAS =  0x056F
    VIZPININC =  0x056E
    RedmondIndustrialGroupLLC =  0x056D
    LongRangeSystemsLLC =  0x056C
    RionCoLtd =  0x056B
    FlipnaviCoLtd =  0x056A
    AudionicsSystemINC =  0x0569
    BodyportInc =  0x0568
    XiamenEveresportsGoodsCoLtd =  0x0567
    CORETRANSPORTTECHNOLOGIESNZLIMITED =  0x0566
    BeijingSmartspaceTechnologiesInc =  0x0565
    BeghelliSpa =  0x0564
    SteinelVertriebGmbH =  0x0563
    ThalmicLabsInc =  0x0562
    FinderSpA =  0x0561
    SaritaCareTechAPS =  0x0560
    PROTECHSASDIGIRARDIANDREAC =  0x055F
    HekatronVertriebsGmbH =  0x055E
    ValveCorporation =  0x055D
    Lely =  0x055C
    FRANKLINTECHNOLOGYINC =  0x055B
    CANDYHOUSEInc =  0x055A
    NewconOptik =  0x0559
    benegearinc =  0x0558
    ArwinTechnologyLimited =  0x0557
    OtodynamicsLtd =  0x0556
    KROHNEMesstechnikGmbH =  0x0555
    NationalInstruments =  0x0554
    NintendoCoLtd =  0x0553
    AvempaceSARL =  0x0552
    Sylero =  0x0551
    VersaNetworksInc =  0x0550
    Sinnoz =  0x054F
    FORTRONIKstoritvedoo =  0x054E
    Sensome =  0x054D
    CarefreeScottFetzerCoInc =  0x054C
    AdvancedElectronicDesignsInc =  0x054B
    LinoughInc =  0x054A
    SmartTechnologiesandInvestmentLimited =  0x0549
    KnickElektronischeMessgeraeteGmbHCoKG =  0x0548
    LOGICDATAElectronicSoftwareEntwicklungsGmbH =  0x0547
    ApexarTechnologiesSA =  0x0546
    CandyHooverGroupsrl =  0x0545
    OrthoSensorInc =  0x0544
    MIWALOCKCOLtd =  0x0543
    MistSystemsInc =  0x0542
    Sharknetsrl =  0x0541
    SilverPlusInc =  0x0540
    SilergyCorp =  0x053F
    CLIM8LIMITED =  0x053E
    TESASA =  0x053D
    ScreenovateTechnologiesLtd =  0x053C
    prodigy =  0x053B
    SavitechCorp =  0x053A
    OPPLELightingCoLtd =  0x0539
    MedelaAG =  0x0538
    MetaLogicsCorporation =  0x0537
    ZTRControlSystemsLLC =  0x0536
    SmartComponentTechnologiesLimited =  0x0535
    FrontiergadgetInc =  0x0534
    NuraOperationsPtyLtd =  0x0533
    CRESCOWirelessInc =  0x0532
    DMHoldingsInc =  0x0531
    AdoleneInc =  0x0530
    CenterIDCorp =  0x052F
    LEDVANCEGmbH =  0x052E
    EXFOInc =  0x052D
    GeosatisSA =  0x052C
    NovartisAG =  0x052B
    KeynesControlsLtd =  0x052A
    LumenUAB =  0x0529
    LuneraLightingInc =  0x0528
    AlbrechtJUNG =  0x0527
    HoneywellInternationalInc =  0x0526
    HONGKONGNANOICTECHNOLOGIESCOLIMITED =  0x0525
    HangzhouiMagicTechnologyCoLtd =  0x0524
    MTGCoLtd =  0x0523
    NSTechInc =  0x0522
    IAICorporation =  0x0521
    TargetCorporation =  0x0520
    SetecPtyLtd =  0x051F
    DetectBlueLimited =  0x051E
    OFFLineCoLtd =  0x051D
    EDPS =  0x051C
    AngeeTechnologiesLtd =  0x051B
    LeicaCameraAG =  0x051A
    TytoLifeLLC =  0x0519
    MAMORIOinc =  0x0518
    AmtronicSverigeAB =  0x0517
    Footmarks =  0x0516
    RBControlsCoLtd =  0x0515
    FIBROGmbH =  0x0514
    NineNineCanadaInc =  0x0513
    SoprodSA =  0x0512
    BrookfieldEquinoxLLC =  0x0511
    UNIELECTRONICSINC =  0x0510
    FoundationEngineeringLLC =  0x050F
    YichipMicroelectronicsHangzhouCoLtd =  0x050E
    TRSystemsGmbH =  0x050D
    OSRAMGmbH =  0x050C
    VibrissaInc =  0x050B
    ShakeonBV =  0x050A
    GarageSmartInc =  0x0509
    AxesSystemspzoo =  0x0508
    Yellowcog =  0x0507
    Hager =  0x0506
    InPlayInc =  0x0505
    PHYPLUSInc =  0x0504
    LocorollInc =  0x0503
    SpecifiKaliLLC =  0x0502
    PolarisIND =  0x0501
    WiliotLTD =  0x0500
    MicrosemiCorporation =  0x04FF
    WoosimSystemsInc =  0x04FE
    TapkeyGmbH =  0x04FD
    SwingLyncLLC =  0x04FC
    BenchmarkDrivesGmbHCoKG =  0x04FB
    AndrotecGmbH =  0x04FA
    Interactio =  0x04F9
    ConvergenceSystemsLimited =  0x04F8
    ShenzhenGoodixTechnologyCoLtd =  0x04F7
    McLearLimited =  0x04F6
    PirelliTyreSPA =  0x04F5
    ZanComputeInc =  0x04F4
    CerevastMedical =  0x04F3
    InDreamerTechsolPrivateLimited =  0x04F2
    ThebenAG =  0x04F1
    KosiLimited =  0x04F0
    DaisyWorksInc =  0x04EF
    Auxivia =  0x04EE
    R9TechnologyInc =  0x04ED
    MotorolaSolutions =  0x04EC
    BirdHomeAutomationGmbH =  0x04EB
    PacificBioscienceLaboratoriesInc =  0x04EA
    BuschJaegerElektroGmbH =  0x04E9
    STABILOInternational =  0x04E8
    REHABTRONICSINC =  0x04E7
    SmartSolutionTechnologyInc =  0x04E6
    AvackOy =  0x04E5
    Woodenshark =  0x04E4
    UnderArmour =  0x04E3
    EllieGrid =  0x04E2
    REACTECLIMITED =  0x04E1
    GuardtecInc =  0x04E0
    EmersonElectricCo =  0x04DF
    LutronElectronicsCoInc =  0x04DE
    FourMODTechnology =  0x04DD
    IOTTIVEOPCPRIVATELIMITED =  0x04DC
    EngineeredAudioLLC =  0x04DB
    FranceschiMarinasnc =  0x04DA
    RMAcquisitionLLC =  0x04D9
    FUJIFILMCorporation =  0x04D8
    BlincamInc =  0x04D7
    LUGLOCLLC =  0x04D6
    GooeeLimited =  0x04D5
    FifthElementLtd =  0x04D4
    QueerconInc =  0x04D3
    AnloqTechnologiesInc =  0x04D2
    KTSGmbH =  0x04D1
    OlympusCorporation =  0x04D0
    DOMSicherheitstechnikGmbHCoKG =  0x04CF
    GOOOLEDSRL =  0x04CE
    SafetechProductsLLC =  0x04CD
    EnfluxInc =  0x04CC
    NovoNordiskAS =  0x04CB
    SteinerOptikGmbH =  0x04CA
    ThornwaveLabsInc =  0x04C9
    ShanghaiFlycoElectricalApplianceCoLtd =  0x04C8
    SvantekSpzoo =  0x04C7
    InstaGmbH =  0x04C6
    SeibertWilliamsGlassLLC =  0x04C5
    TeAMHutchinsAB =  0x04C4
    MantracourtElectronicsLimited =  0x04C3
    DmetProductsCorp =  0x04C2
    Sospitassro =  0x04C1
    StatsportsInternational =  0x04C0
    VITInitiativeLLC =  0x04BF
    AverosFZCO =  0x04BE
    AlbynMedical =  0x04BD
    DraegerwerkAGCoKGaA =  0x04BC
    NeateboxLtd =  0x04BB
    CrestronElectronicsInc =  0x04BA
    CSRBuildingProductsLimited =  0x04B9
    SoraaInc =  0x04B8
    AnalogDevicesInc =  0x04B7
    DiagnopticsTechnologies =  0x04B6
    SwiftronixAB =  0x04B5
    InuheatGroupAB =  0x04B4
    mobikeHongKongLimited =  0x04B3
    TheShadowontheMoon =  0x04B2
    KartographersTechnologiesPvtLtd =  0x04B1
    WebaSportundMedArtikelGmbH =  0x04B0
    BIOROWERHandelsagenturGmbH =  0x04AF
    ERMElectronicSystemsLTD =  0x04AE
    ShureInc =  0x04AD
    UndagridBV =  0x04AC
    HarbortronicsInc =  0x04AB
    LINKIOSAS =  0x04AA
    DISCOVERYSOUNDTECHNOLOGYLLC =  0x04A9
    BioTexInc =  0x04A8
    DallasLogicCorporation =  0x04A7
    VinetechCoLtd =  0x04A6
    GuangzhouFiiOElectronicsTechnologyCoLtd =  0x04A5
    HerbertWaldmannGmbHCoKG =  0x04A4
    GTtronicsHKLtd =  0x04A3
    ovrEngineeredLLC =  0x04A2
    PNISensorCorporation =  0x04A1
    VypinLLC =  0x04A0
    PopperPayAB =  0x049F
    ANDXORLLC =  0x049E
    UhlmannZacherGmbH =  0x049D
    DyOcean =  0x049C
    nVistiLLC =  0x049B
    SituneAS =  0x049A
    RuuviInnovationsLtd =  0x0499
    METERGroupIncUSA =  0x0498
    CochlearLimited =  0x0497
    PolymorphicLabsLLC =  0x0496
    LMTMercerGroupInc =  0x0495
    SENNHEISERelectronicGmbHCoKG =  0x0494
    LynxemiPteLtd =  0x0493
    ADCTechnologyInc =  0x0492
    SOREXWirelessSolutionsGmbH =  0x0491
    MattingAB =  0x0490
    BlueKitchenGmbH =  0x048F
    CompanionMedicalInc =  0x048E
    SLabsSpzoo =  0x048D
    VectronixAG =  0x048C
    CPElectronicsLimited =  0x048B
    TaelekOy =  0x048A
    IgarashiEngineering =  0x0489
    AutomotiveDataSolutionsInc =  0x0488
    CentricaConnectedHome =  0x0487
    DEVTECNOLOGIAINDUSTRIACOMERCIOEMANUTENCAODEEQUIPAMENTOSLTDAME =  0x0486
    SKIDATAAG =  0x0485
    RevolTechnologiesInc =  0x0484
    MultiCareSystemsBV =  0x0483
    POSTuningUdoVosshenrichGmbHCoKG =  0x0482
    QuintraxLimited =  0x0481
    DynometricsInc =  0x0480
    ProMarkInc =  0x047F
    OurHubDevIvS =  0x047E
    OcclyLLC =  0x047D
    POWERMATLTD =  0x047C
    MIYOSHIELECTRONICSCORPORATION =  0x047B
    SinosunTechnologyCoLtd =  0x047A
    mywerksystemGmbH =  0x0479
    FarSiteCommunicationsLimited =  0x0478
    BlueSparkTechnologies =  0x0477
    OxstrenWearableTechnologiesPrivateLimited =  0x0476
    Icominc =  0x0475
    iApartmentcoltd =  0x0474
    SteelcaseInc =  0x0473
    ControlJPtyLtd =  0x0472
    TiVoCorp =  0x0471
    iDesignsrl =  0x0470
    DevelcoProductsAS =  0x046F
    PamborLtd =  0x046E
    BEGAGantenbrinkLeuchtenKG =  0x046D
    QingdaoRealtimeTechnologyCoLtd =  0x046C
    PMDSolutions =  0x046B
    INSIGMAINC =  0x046A
    PalagoAB =  0x0469
    KynesimLtd =  0x0468
    CodenexOy =  0x0467
    CycleLabsSolutionsinc =  0x0466
    InternationalForteGroupLLC =  0x0465
    BellmanSymfon =  0x0464
    FathomSystemsInc =  0x0463
    BonsaiSystemsGmbH =  0x0462
    vhfelektronikGmbH =  0x0461
    Kolibree =  0x0460
    RealTimeAutomationInc =  0x045F
    NuvizInc =  0x045E
    BostonScientificCorporation =  0x045D
    DeltaTCorporation =  0x045C
    SPACEEKLTD =  0x045B
    TwoOFourOntarioInc =  0x045A
    LumenetixInc =  0x0459
    MiniSolutionCoLtd =  0x0458
    RFINNOVATION =  0x0457
    NemikConsultingInc =  0x0456
    Atomation =  0x0455
    SphinxElectronicsGmbHCoKG =  0x0454
    QorvoUtrechtBV =  0x0453
    SvepDesignCenterAB =  0x0452
    TunstallNordicAB =  0x0451
    TeenageEngineeringAB =  0x0450
    TTSTooltechnicSystemsAGCoKG =  0x044F
    XtravaInc =  0x044E
    VEGAGrieshaberKG =  0x044D
    LifeStyleLockLLC =  0x044C
    NainInc =  0x044B
    SHIMANOINC =  0x044A
    OneUPUSAcomllc =  0x0449
    GrandCentrixGmbH =  0x0448
    FabtronicsAustraliaPtyLtd =  0x0447
    NETGEARInc =  0x0446
    KobianCanadaInc =  0x0445
    MetanateLimited =  0x0444
    TuckerInternationalLLC =  0x0443
    SECOMCOLTD =  0x0442
    iProtoXiOy =  0x0441
    ValencellInc =  0x0440
    TentacleSyncGmbH =  0x043F
    ThermomedicsInc =  0x043E
    CoilerCorporation =  0x043D
    DeLaval =  0x043C
    Appsidecoltd =  0x043B
    NuhearaLimited =  0x043A
    RadianceTechnologies =  0x0439
    HelvarLtd =  0x0438
    eBestIOTInc =  0x0437
    DraysonTechnologiesEuropeLimited =  0x0436
    BlocksWearablesLtd =  0x0435
    HatchBabyInc =  0x0434
    PillsyInc =  0x0433
    SilkLabsInc =  0x0432
    AlticorInc =  0x0431
    SnapStykInc =  0x0430
    DanfossAS =  0x042F
    MemCachierInc =  0x042E
    MeshtechAS =  0x042D
    TictoNV =  0x042C
    iMicroMedIncorporated =  0x042B
    BDMedical =  0x042A
    ProlonInc =  0x0429
    SmallLoopLLC =  0x0428
    Focusfleetandfuelmanagementinc =  0x0427
    HusqvarnaAB =  0x0426
    UnifySoftwareandSolutionsGmbHCoKG =  0x0425
    TrainesenseLtd =  0x0424
    ChargifiLimited =  0x0423
    DELSEYSA =  0x0422
    BackboneLabsInc =  0x0421
    TecBakeryGmbH =  0x0420
    KopinCorporation =  0x041F
    DellComputerCorporation =  0x041E
    BenningElektrotechnikundElektronikGmbHCoKG =  0x041D
    WaterGuruInc =  0x041C
    OrthoAccelTechnologies =  0x041B
    FridayLabsLimited =  0x041A
    NovalogyLTD =  0x0419
    Reserved2 =  0x0418
    FatigueScience =  0x0417
    SODAGmbH =  0x0416
    UberTechnologiesInc =  0x0415
    LightningProtectionInternationalPtyLtd =  0x0414
    WirelessCablesInc =  0x0413
    SEFAM =  0x0412
    LuidiaInc =  0x0411
    FenderMusicalInstruments =  0x0410
    COAXTechnologyInc =  0x040F
    SKFUKLimited =  0x040E
    NorthStarBatteryCompanyLLC =  0x040D
    SenixCorporation =  0x040C
    JanaCareInc =  0x040B
    ZFOPENMATICSsro =  0x040A
    RYSEINC =  0x0409
    ToGetHomeInc =  0x0408
    SwissAudioSA =  0x0407
    Airtago =  0x0406
    VertexInternationalInc =  0x0405
    AuthomateInc =  0x0404
    GantnerElectronicGmbH =  0x0403
    SearsHoldingsCorporation =  0x0402
    RelationsInc =  0x0401
    ideveloperITBeratungUG =  0x0400
    Withings =  0x03FF
    Littelfuse =  0x03FE
    TrimbleInc =  0x03FD
    KimberlyClark =  0x03FC
    NoxMedical =  0x03FB
    VyassoftTechnologiesInc =  0x03FA
    BeconTechnologiesCoLtd =  0x03F9
    RockfordCorp =  0x03F8
    OwlLabsInc =  0x03F7
    ItonTechnologyCorp =  0x03F6
    WHEREInc =  0x03F5
    PALTechnologiesLtd =  0x03F4
    FlowscapeAB =  0x03F3
    WindowMasterAS =  0x03F2
    HestanSmartCookingInc =  0x03F1
    CLINK =  0x03F0
    foolographyGmbH =  0x03EF
    CUBETECHNOLOGIES =  0x03EE
    BASICMICROCOMINC =  0x03ED
    JigowattsInc =  0x03EC
    OzoEduInc =  0x03EB
    HelloInc =  0x03EA
    SHENZHENLEMONJOYTECHNOLOGYCOLTD =  0x03E9
    ReinerKartengeraeteGmbHCoKG =  0x03E8
    TRUEFitnessTechnology =  0x03E7
    IoTInstrumentsOy =  0x03E6
    ffly4u =  0x03E5
    ChipingAG =  0x03E4
    QualcommLifeInc =  0x03E3
    SensoanOy =  0x03E2
    SPDDevelopmentCompanyLtd =  0x03E1
    ActionsZhuhaiTechnologyCoLimited =  0x03E0
    GrobTechnologiesLLC =  0x03DF
    NathanRhoadesLLC =  0x03DE
    AndreasStihlAGCoKG =  0x03DD
    NimaLabs =  0x03DC
    InstabeatInc =  0x03DB
    EnOceanGmbH =  0x03DA
    ThreeIWareCoLtd =  0x03D9
    ZenMeLabsLtd =  0x03D8
    FINSECUR =  0x03D7
    YotaDevicesLTD =  0x03D6
    WyzelinkSystemsInc =  0x03D5
    PEGPEREGOSPA =  0x03D4
    SigmaConnectivityAB =  0x03D3
    IOTPotIndiaPrivateLimited =  0x03D2
    DensityInc =  0x03D1
    WatteamLtd =  0x03D0
    MIRAInc =  0x03CF
    CONTRINEXSA =  0x03CE
    WyndTechnologiesInc =  0x03CD
    VonkilTechnologiesLtd =  0x03CC
    SYSDEVSrl =  0x03CB
    In2thingsAutomationPvtLtd =  0x03CA
    GallagherGroup =  0x03C9
    AvvelInternational =  0x03C8
    StructuralHealthSystemsInc =  0x03C7
    Intricon =  0x03C6
    StJudeMedicalInc =  0x03C5
    PicoTechnologyInc =  0x03C4
    CasambiTechnologiesOy =  0x03C3
    SnapchatInc =  0x03C2
    EmberTechnologiesInc =  0x03C1
    ArchSystemsInc =  0x03C0
    iLumiSolutionsInc =  0x03BF
    AppliedScienceInc =  0x03BE
    amadas =  0x03BD
    ASBBankLtd =  0x03BC
    Abbott =  0x03BB
    MaxscendMicroelectronicsCompanyLimited =  0x03BA
    FREDERIQUECONSTANTSA =  0x03B9
    ASafeLimited =  0x03B8
    AirblyInc =  0x03B7
    Mattel =  0x03B6
    petPOMMInc =  0x03B5
    AlphaNodusinc =  0x03B4
    MidwestInstrumentsControls =  0x03B3
    PropagationSystemsLimited =  0x03B2
    OtodataWirelessNetworkInc =  0x03B1
    VIBRADORMGmbH =  0x03B0
    CommNSenseCorpDBAVerigo =  0x03AF
    AllswellInc =  0x03AE
    XiQ =  0x03AD
    SmabloLTD =  0x03AC
    MeizuTechnologyCoLtd =  0x03AB
    ExonSpzoo =  0x03AA
    THINKERLYSRL =  0x03A9
    EsrilleInc =  0x03A8
    AeroScout =  0x03A7
    MedelaInc =  0x03A6
    ACECADEnterpriseCoLtdACECAD =  0x03A5
    TokenZeroLtd =  0x03A4
    SmartMovtTechnologyCoLtd =  0x03A3
    CanduraInstruments =  0x03A2
    AlpineLabsLLC =  0x03A1
    IVTWirelessLimited =  0x03A0
    MolexCorporation =  0x039F
    SchoolBoardLimited =  0x039E
    CareViewCommunicationsInc =  0x039D
    ALEInternational =  0x039C
    SouthSiliconValleyMicroelectronics =  0x039B
    NeST =  0x039A
    NikonCorporation =  0x0399
    ThetatronicsLtd =  0x0398
    LEGOSystemAS =  0x0397
    BLOKSGmbH =  0x0396
    SDATAWAY =  0x0395
    NetclearanceSystemsInc =  0x0394
    LAVAZZASpA =  0x0393
    TD =  0x0392
    ThingsquareAB =  0x0391
    INFOTECHsro =  0x0390
    XiaomiInc =  0x038F
    CrownstoneBV =  0x038E
    ResmedLtd =  0x038D
    AppionInc =  0x038C
    Noke =  0x038B
    KohlerMiraLimited =  0x038A
    ActiveBluCorporation =  0x0389
    KapschTrafficComAB =  0x0388
    BluStorPMCInc =  0x0387
    AtericaInc =  0x0386
    EmbeddedElectronicSolutionsLtddbae2Solutions =  0x0385
    OCOSMOSCoLtd =  0x0384
    KronosIncorporated =  0x0383
    PrecisionOutcomesLtd =  0x0382
    SharpCorporation =  0x0381
    LLCMEGAFservice =  0x0380
    SocitdesProduitsNestlSA =  0x037F
    lulabytesSL =  0x037E
    MICRODIALtd =  0x037D
    CronologicsCorporation =  0x037C
    ApptionLabsInc =  0x037B
    Algoria =  0x037A
    ShenzheniMCOElectronicTechnologyCoLtd =  0x0379
    PropellerHealth =  0x0378
    PlejdAB =  0x0377
    ElectronicTemperatureInstrumentsLtd =  0x0376
    ExpainAS =  0x0375
    HolmanIndustries =  0x0374
    AppNearMeLtd =  0x0373
    NixieLabsInc =  0x0372
    ORBCOMM =  0x0371
    WazombiLabsO =  0x0370
    MotivInc =  0x036F
    MOTIVETECHNOLOGIESINC =  0x036E
    AirBoltPtyLtd =  0x036D
    Zipcar =  0x036C
    BRControlsProductsBV =  0x036B
    SetPointMedical =  0x036A
    littleBits =  0x0369
    MetormoteAB =  0x0368
    SapheInternational =  0x0367
    BOLTTSportstechnologiesPrivatelimited =  0x0366
    BioMechSensorLLC =  0x0365
    FaveroElectronicsSrl =  0x0364
    FREELAPSA =  0x0363
    ONSemiconductor =  0x0362
    WellinksInc =  0x0361
    InsuletCorporation =  0x0360
    Acromag =  0x035F
    NayaHealthInc =  0x035E
    KYS =  0x035D
    EatonCorporation =  0x035C
    MatrixInc =  0x035B
    PhillipsMedisizeAS =  0x035A
    NovotecMedicalGmbH =  0x0359
    MagniWareLtd =  0x0358
    PolymapWireless =  0x0357
    SpectrumBrandsInc =  0x0356
    SigmaDesignsInc =  0x0355
    TOPPANFORMSCOLTD =  0x0354
    AlphaAudiotronicsInc =  0x0353
    iRidingXiamenTechnologyCoLtd =  0x0352
    PiepsGmbH =  0x0351
    BitstrataSystemsInc =  0x0350
    HeartlandPaymentSystems =  0x034F
    SafeTrustInc =  0x034E
    TASERInternationalInc =  0x034D
    HMElectronicsInc =  0x034C
    LibratoneAS =  0x034B
    Vaddio =  0x034A
    VersaMe =  0x0349
    Arioneo =  0x0348
    PreventBiometrics =  0x0347
    AcuityBrandsLightingInc =  0x0346
    LocusPositioning =  0x0345
    WhirlInc =  0x0344
    DrekkerDevelopmentPtyLtd =  0x0343
    GERTECBRASILLTDA =  0x0342
    EtesianTechnologiesLLC =  0x0341
    Letsensesrl =  0x0340
    AutomationComponentsInc =  0x033F
    MonitraSA =  0x033E
    TPVTechnologyLimited =  0x033D
    Virtuosys =  0x033C
    CourtneyThorneLimited =  0x033B
    AppceptionInc =  0x033A
    BlueSkyScientificLLC =  0x0339
    COBIGmbH =  0x0338
    AJP2HoldingsLLC =  0x0337
    GISTIC =  0x0336
    EnlightedInc =  0x0335
    AirthingsASA =  0x0334
    MulTLock =  0x0333
    ElectrocompanietAS =  0x0332
    ThreeflaresTechnologiesInc =  0x0331
    NorthPoleEngineering =  0x0330
    OttoQInc =  0x032F
    indoormap =  0x032E
    BMinnovationsGmbH =  0x032D
    NIPPONSMTCOLtd =  0x032C
    ESYLUX =  0x032B
    ElectronicDesignLab =  0x032A
    EargoInc =  0x0329
    GrundfosAS =  0x0328
    EssexElectronics =  0x0327
    HealthwearTechnologiesChangzhouLtd =  0x0326
    AmotusSolutions =  0x0325
    AstroInc =  0x0324
    RotorBikeComponents =  0x0323
    CompumedicsLimited =  0x0322
    Jewelbots =  0x0321
    SONOELECTRONICSCOLTD =  0x0320
    MetaSystemSpA =  0x031F
    EyefiInc =  0x031E
    EnterlabApS =  0x031D
    LabSensorSolutions =  0x031C
    HQInc =  0x031B
    WurthElektronikeiSosGmbHCoKG =  0x031A
    EugsterFrismagAG =  0x0319
    AspentaInternational =  0x0318
    CHUOElectronicsCOLTD =  0x0317
    AGMeasurematicsPvtLtd =  0x0316
    ThermoFisherScientific =  0x0315
    RIIGAISpzoo =  0x0314
    DiveNavInc =  0x0313
    DucereTechnologiesPvtLtd =  0x0312
    PEEQDATA =  0x0311
    SGLItaliaSrl =  0x0310
    ShortcutLabs =  0x030F
    Deviceworx =  0x030E
    DevdataSrl =  0x030D
    HiltiAG =  0x030C
    MagnitudeLightingConverters =  0x030B
    Ellisys =  0x030A
    DolbyLabs =  0x0309
    SurefireLLC =  0x0308
    FUJIINDUSTRIALCOLTD =  0x0307
    LifeLaboratoryInc =  0x0306
    SwippApS =  0x0305
    ProxyTechnologiesInc =  0x0304
    IACAelectronique =  0x0303
    LoopDevicesInc =  0x0302
    GiatecScientificInc =  0x0301
    WorldMotoInc =  0x0300
    SiliconLaboratories =  0x02FF
    LierdaScienceTechnologyGroupCoLtd =  0x02FE
    UwannaInc =  0x02FD
    ShanghaiFrequenMicroelectronicsCoLtd =  0x02FC
    ClariusMobileHealthCorp =  0x02FB
    CoSTARTEchnologies =  0x02FA
    IMAGINATIONTECHNOLOGIESLTD =  0x02F9
    RunteqOyLtd =  0x02F8
    DreamVisionscoLtd =  0x02F7
    IntemoTechnologies =  0x02F6
    IndagemTechLLC =  0x02F5
    VensiInc =  0x02F4
    AuthAirInc =  0x02F3
    GoProInc =  0x02F2
    TheIdeaCaveLLC =  0x02F1
    BlackratSoftware =  0x02F0
    SMARTINNOVATIONinc =  0x02EF
    CitizenHoldingsCoLtd =  0x02EE
    HTCCorporation =  0x02ED
    DeltaSystemsInc =  0x02EC
    ArdicTechnology =  0x02EB
    FujitsuLimited =  0x02EA
    SensogramTechnologiesInc =  0x02E9
    AmericanMusicEnvironments =  0x02E8
    ConnectedYardInc =  0x02E7
    Unwire =  0x02E6
    EspressifSystemsShanghaiCoLtd =  0x02E5
    BytestormLtd =  0x02E4
    CarmanahTechnologiesCorp =  0x02E3
    NTTdocomo =  0x02E2
    VictronEnergyBV =  0x02E1
    UniversityofMichigan =  0x02E0
    BlurProductDevelopment =  0x02DF
    SamsungSDSCoLtd =  0x02DE
    FlintRehabilitationDevicesLLC =  0x02DD
    DeWalchTechnologiesInc =  0x02DC
    DigiInternationalIncR =  0x02DB
    Gilvader =  0x02DA
    FlieglAgrartechnikGmbH =  0x02D9
    Neosfar =  0x02D8
    NIPPONSYSTEMWARECOLTD =  0x02D7
    SendSolutions =  0x02D6
    OMRONCorporation =  0x02D5
    SecuyouApS =  0x02D4
    PowercastCorporation =  0x02D3
    AferoInc =  0x02D2
    EmpaticaSrl =  0x02D1
    ThreeM =  0x02D0
    Anima =  0x02CF
    TevaBrandedPharmaceuticalProductsRDInc =  0x02CE
    BMAergonomicsbv =  0x02CD
    EijkelkampSoilWater =  0x02CC
    AINAWirelessInc =  0x02CB
    ABOVSemiconductor =  0x02CA
    PayRangeInc =  0x02C9
    OneSpan =  0x02C8
    ElectronicsTomorrowLimited =  0x02C7
    AyatanSensors =  0x02C6
    LenovoSingaporePteLtd =  0x02C5
    WilsonSportingGoods =  0x02C4
    TechtronicPowerToolsTechnologyLimited =  0x02C3
    GuillemotCorporation =  0x02C2
    LINECorporation =  0x02C1
    DashRobotics =  0x02C0
    RedbirdFlightSimulations =  0x02BF
    SeguroTechnologySpzoo =  0x02BE
    Chemtronics =  0x02BD
    GenevacLtd =  0x02BC
    KohaCoLtd =  0x02BB
    SwissprimeTechnologiesAG =  0x02BA
    RinnaiCorporation =  0x02B9
    ChronoTherapeutics =  0x02B8
    OortTechnologiesLLC =  0x02B7
    SchneiderElectric =  0x02B6
    HANSHINELECTRICRAILWAYCOLTD =  0x02B5
    HyginexInc =  0x02B4
    CLABERSPA =  0x02B3
    OuraHealthOy =  0x02B2
    RadenInc =  0x02B1
    BestechnicShanghaiLtd =  0x02B0
    TechnicolorUSAInc =  0x02AF
    WeatherFlowInc =  0x02AE
    RxNetworksInc =  0x02AD
    RTBElektronikGmbHCoKG =  0x02AC
    BBPOSLimited =  0x02AB
    DopplerLab =  0x02AA
    Chargelib =  0x02A9
    miSportLtd =  0x02A8
    IlluxtroninternationalBV =  0x02A7
    RobertBoschGmbH =  0x02A6
    TendyronCorporation =  0x02A5
    PacificLockCompany =  0x02A4
    Itude =  0x02A3
    Sera4Ltd =  0x02A2
    InventureTrackSystems =  0x02A1
    ImpossibleCameraGmbH =  0x02A0
    AreusEngineeringGmbH =  0x029F
    Kupsonspolsro =  0x029E
    ALOTTAZSLABSLLC =  0x029D
    BlueSkyScientificLLC2 =  0x029C
    C2DevelopmentInc =  0x029B
    CurrantInc =  0x029A
    InexessTechnologySimmaKG =  0x0299
    EISSTLtd =  0x0298
    stormpowerltd =  0x0297
    Petzl =  0x0296
    SivantosGmbH =  0x0295
    ELIASGmbH =  0x0294
    BlueBite =  0x0293
    SwiftSensors =  0x0292
    CliniCloudInc =  0x0291
    MultibitOy =  0x0290
    ChurchDwightCoInc =  0x028F
    RFDigitalCorp =  0x028E
    IFLLC =  0x028D
    NANOLINKAPS =  0x028C
    CodeGearsLTD =  0x028B
    JetroAS =  0x028A
    SKTelecom =  0x0289
    WillowbankElectronicsLtd =  0x0288
    WallyVenturesSL =  0x0287
    RFCodeInc =  0x0286
    WOWTechCanadaLtd =  0x0285
    SynapseElectronics =  0x0284
    MavenMachinesInc =  0x0283
    SonovaAG =  0x0282
    StoneL =  0x0281
    ITECcorporation =  0x0280
    ruwidoaustriagmbh =  0x027F
    HabitAwareLLC =  0x027E
    HUAWEITechnologiesCoLtd =  0x027D
    AseptikaLtd =  0x027C
    DEFAAS =  0x027B
    Ekominiinc =  0x027A
    steuteSchaltgerateGmbHCoKG =  0x0279
    JohnsonOutdoorsInc =  0x0278
    bewhereinc =  0x0277
    EGOElektroGeraetebauGmbH =  0x0276
    Geotab =  0x0275
    MotsaiResearch =  0x0274
    OCEASOFT =  0x0273
    AlpsAlpineCoLtd =  0x0272
    AnimasCorp =  0x0271
    LSIADLTechnology =  0x0270
    AptcodeSolutions =  0x026F
    FLEURBAEYBVBA =  0x026E
    TechnogymSPA =  0x026D
    DomsterTadeuszSzydlowski =  0x026C
    DEKAResearchDevelopmentCorp =  0x026B
    Gemalto =  0x026A
    TorroxGmbHCoKG =  0x0269
    Cerevo =  0x0268
    XMISystemsSA =  0x0267
    SchawbelTechnologiesLLC =  0x0266
    SMKCorporation =  0x0265
    DDSInc =  0x0264
    IdentivInc =  0x0263
    GlacialRidgeTechnologies =  0x0262
    SECVREGmbH =  0x0261
    SensaRx =  0x0260
    YardarmTechnologies =  0x025F
    FlukeCorporation =  0x025E
    LexmarkInternationalInc =  0x025D
    NetEaseHangzhouNetworkcoLtd =  0x025C
    FiveInteractiveLLCdbaZendo =  0x025B
    UniversityofAppliedSciencesValaisHauteEcoleValaisanne =  0x025A
    ALTYOR =  0x0259
    DevialetSA =  0x0258
    AdBabbleLocalCommerceInc =  0x0257
    G24PowerLimited =  0x0256
    DaiNipponPrintingCoLtd =  0x0255
    Playbrush =  0x0254
    XicatoInc =  0x0253
    UKCTechnosolution =  0x0252
    LumoBodytechInc =  0x0251
    SapphireCircuitsLLC =  0x0250
    SchneiderSchreibgerteGmbH =  0x024F
    MicrotronicsEngineeringGmbH =  0x024E
    MWaySolutionsGmbH =  0x024D
    BlueCloverDevices =  0x024C
    OrlanLLC =  0x024B
    UwatecAG =  0x024A
    TranscranialLtd =  0x0249
    ParkerHannifinCorp =  0x0248
    FiftyThreeInc =  0x0247
    ACKmeNetworksInc =  0x0246
    EndressHauser =  0x0245
    IoteraInc =  0x0244
    MasimoCorp =  0x0243
    SixteenLabInc =  0x0242
    BragiGmbH =  0x0241
    ArgenoxTechnologies =  0x0240
    WaveWareTechnologiesInc =  0x023F
    RavenIndustries =  0x023E
    ViCentraBV =  0x023D
    Awarepoint =  0x023C
    BeijingCarePulseElectronicTechnologyCoLtd =  0x023B
    AlatechTehnology =  0x023A
    JINCOLtd =  0x0239
    Trakm8Ltd =  0x0238
    MSHelisrl =  0x0237
    PitpatpetLtd =  0x0236
    QrioInc =  0x0235
    FengFanBeiJingTechnologyCoLtd =  0x0234
    ShenzhenSuLongCommunicationLtd =  0x0233
    xSensoSolutionsKft =  0x0232
    ETASA =  0x0231
    FosterElectricCompanyLtd =  0x0230
    HuamiShanghaiCultureCommunicationCOLTD =  0x022F
    SiemensAG =  0x022E
    Lupine =  0x022D
    PharynksCorporation =  0x022C
    TeslaInc =  0x022B
    StamerMusikanlagenGMBH =  0x022A
    MuovertiLimited =  0x0229
    TwocanoesLabsLLC =  0x0228
    LifeBEAMTechnologies =  0x0227
    MerliniaAS =  0x0226
    NestlNespressoSA =  0x0225
    ComarchSA =  0x0224
    PhilipMorrisProductsSA =  0x0223
    PraxisDynamics =  0x0222
    MobiquityNetworksInc =  0x0221
    ManusMachinaBV =  0x0220
    LusterLeafProductsInc =  0x021F
    GoodnetLtd =  0x021E
    Edamic =  0x021D
    MobicommInc =  0x021C
    CiscoSystemsInc =  0x021B
    BlueSpeckLabsLLC =  0x021A
    DOTTLimited =  0x0219
    HiotechAB =  0x0218
    Tech4homeLda =  0x0217
    MTILtd =  0x0216
    LukotonExperienceOy =  0x0215
    IKMultimediaProductionsrl =  0x0214
    WylerAG =  0x0213
    InterplanCoLtd =  0x0212
    TelinkSemiconductorCoLtd =  0x0211
    ikeGPS =  0x0210
    ComoduleGMBH =  0x020F
    OmronHealthcareCoLTD =  0x020E
    SimploTechnologyCoLTD =  0x020D
    CoroWareTechnologiesInc =  0x020C
    JaguarLandRoverLimited =  0x020B
    MacnicaInc =  0x020A
    InvisionHeartInc =  0x0209
    LumiGeekLLC =  0x0208
    STEMPInc =  0x0207
    OtterProductsLLC =  0x0206
    SmartboticsInc =  0x0205
    TapcentiveInc =  0x0204
    KemppiOy =  0x0203
    RigadoLLC =  0x0202
    ARTiming =  0x0201
    VerifoneSystemsPteLtdTaiwanBranch =  0x0200
    FreescaleSemiconductorInc =  0x01FF
    RadioSystemsCorporation =  0x01FE
    KontaktMicroLocationSpzoo =  0x01FD
    WahooFitnessLLC =  0x01FC
    FormLiftingLLC =  0x01FB
    GozioInc =  0x01FA
    MedtronicInc =  0x01F9
    AnykaGuangzhouMicroelectronicsTechnologyCoLTD =  0x01F8
    GellinerLimited =  0x01F7
    DJOGlobal =  0x01F6
    CoolWebthingsLimited =  0x01F5
    UTCFireandSecurity =  0x01F4
    TheUniversityofTokyo =  0x01F3
    ItronInc =  0x01F2
    ZebraTechnologiesCorporation =  0x01F1
    KloudNation =  0x01F0
    FullpowerTechnologiesInc =  0x01EF
    ValeoService =  0x01EE
    CuteCircuitLTD =  0x01ED
    SpreadtrumCommunicationsShanghaiLtd =  0x01EC
    AutoMapLLC =  0x01EB
    AdvancedApplicationDesignInc =  0x01EA
    SanoInc =  0x01E9
    STIR =  0x01E8
    IPSGroupInc =  0x01E7
    TechnologySolutionsUKLtd =  0x01E6
    DynamicDevicesLtd =  0x01E5
    FreedomInnovations =  0x01E4
    CaterpillarInc =  0x01E3
    LectronixInc =  0x01E2
    JollaLtd =  0x01E1
    WidexAS =  0x01E0
    BisonGroupLtd =  0x01DF
    MinelabElectronicsPtyLimited =  0x01DE
    KoninklijkePhilipsNV =  0x01DD
    iParkingLtd =  0x01DC
    InnblueConsulting =  0x01DB
    LogitechInternationalSA =  0x01DA
    SavantSystemsLLC =  0x01D9
    CodeCorporation =  0x01D8
    SquadroneSystemsInc =  0x01D7
    Gwearablesinc =  0x01D6
    ELADsrl =  0x01D5
    NewlabSrl =  0x01D4
    SkyWaveDesign =  0x01D3
    GillElectronics =  0x01D2
    AugustHomeInc =  0x01D1
    PrimusInterParesLtd =  0x01D0
    BSH =  0x01CF
    HOUWASYSTEMDESIGNkk =  0x01CE
    ChengduSynwingTechnologyLtd =  0x01CD
    SamLabsLtd =  0x01CC
    FetchMyPet =  0x01CB
    LaerdalMedicalAS =  0x01CA
    Avion =  0x01C9
    PolyControlApS =  0x01C8
    AbiogenixInc =  0x01C7
    HASWAREInc =  0x01C6
    BitcrazeAB =  0x01C5
    DMEMicroelectronics =  0x01C4
    Bunch =  0x01C3
    TransenergooilAG =  0x01C2
    BRADATECHCorp =  0x01C1
    pironexGmbH =  0x01C0
    HongKongHunterSunElectronicLimited =  0x01BF
    PulsateMobileLtd =  0x01BE
    SyszoneCoLtd =  0x01BD
    SenionLabAB =  0x01BC
    CochlearBoneAnchoredSolutionsAB =  0x01BB
    StagesCyclingLLC =  0x01BA
    HANAMicron =  0x01B9
    iD3SL =  0x01B8
    GeneralElectricCompany =  0x01B7
    LMTechnologiesLtd =  0x01B6
    NestLabsInc =  0x01B5
    TrineoSpzoo =  0x01B4
    NytecInc =  0x01B3
    NymiInc =  0x01B2
    NetizensSpzoo =  0x01B1
    StarMicronicsCoLtd =  0x01B0
    SunriseMicroDevicesInc =  0x01AF
    EarlensCorporation =  0x01AE
    FlightSafetyInternational =  0x01AD
    TrividiaHealthInc =  0x01AC
    MetaPlatformsInc =  0x01AB
    GeophysicalTechnologyInc =  0x01AA
    CanonInc =  0x01A9
    Taobao =  0x01A8
    ENERGOUSCORPORATION =  0x01A7
    WilleEngineering =  0x01A6
    IconHealthandFitness =  0x01A5
    MSAInnovationLLC =  0x01A4
    EROAD =  0x01A3
    GIGALANECOLTD =  0x01A2
    FIAMM =  0x01A1
    ChannelEnterprisesHKLtd =  0x01A0
    StrainstallLtd =  0x019F
    Ceruus =  0x019E
    CVSHealth =  0x019D
    CokiyaIncorporated =  0x019C
    CUBETECHsro =  0x019B
    TRONForum =  0x019A
    SALTOSYSTEMSSL =  0x0199
    VENGITKorlatoltFelelosseguTarsasag =  0x0198
    WiSilicaInc =  0x0197
    PaxtonAccessLtd =  0x0196
    Zuli =  0x0195
    AcousticStreamCorporation =  0x0194
    MavericAutomationLLC =  0x0193
    CloudleafInc =  0x0192
    FDKCORPORATION =  0x0191
    IntellettoTechnologiesInc =  0x0190
    FirefliesSystems =  0x018F
    FitbitInc =  0x018E
    ExtronDesignServices =  0x018D
    WiloSE =  0x018C
    KonicaMinoltaInc =  0x018B
    AbleTrendTechnologyLimited =  0x018A
    PhysicalEnterprisesInc =  0x0189
    UnicoRBC =  0x0188
    SeraphimSenseLtd =  0x0187
    CORELightingLtd =  0x0186
    belappsLLC =  0x0185
    Nectar =  0x0184
    WaltDisney =  0x0183
    HOPUbiquitous =  0x0182
    GeckoHealthInnovationsInc =  0x0181
    GigasetCommunicationsGmbH =  0x0180
    XTelWirelessApS =  0x017F
    BluDotzLtd =  0x017E
    BatAndCat =  0x017D
    MercedesBenzGroupAG =  0x017C
    taskitGmbH =  0x017B
    TelemonitorInc =  0x017A
    LAPISSemiconductorCoLtd =  0x0179
    CASIOCOMPUTERCOLTD =  0x0178
    ISYSTinc =  0x0177
    SentriLock =  0x0176
    DynamicControls =  0x0175
    EverykeyInc =  0x0174
    KocomojoLLC =  0x0173
    ConnovateTechnologyPrivateLimited =  0x0172
    AmazoncomServicesLLC =  0x0171
    RocheDiabetesCareAG =  0x0170
    PodoLabsInc =  0x016F
    VolanticAB =  0x016E
    LifeScanInc =  0x016D
    MYSPHERA =  0x016C
    Qblinks =  0x016B
    EmersonDigitalColdChainInc =  0x016A
    emberlight =  0x0169
    SpiceboxLLC =  0x0168
    AscensiaDiabetesCareUSInc =  0x0167
    MISHIKPteLtd =  0x0166
    MilwaukeeElectricTools =  0x0165
    QingdaoYeelinkInformationTechnologyCoLtd =  0x0164
    PCHInternational =  0x0163
    MADSGlobalNZLtd =  0x0162
    yikes =  0x0161
    AwoX =  0x0160
    TimerCapCo =  0x015F
    UnikeyTechnologiesInc =  0x015E
    EstimoteInc =  0x015D
    PitiusTecSL =  0x015C
    BiomedicalResearchLtd =  0x015B
    micasAG =  0x015A
    ChefStepsInc =  0x0159
    Inmitesro =  0x0158
    AnhuiHuamiInformationTechnologyCoLtd =  0x0157
    AccumulateAB =  0x0156
    NETATMO =  0x0155
    PebbleTechnology =  0x0154
    ROLErgo =  0x0153
    VernierSoftwareTechnology =  0x0152
    OnBeep =  0x0151
    PioneerCorporation =  0x0150
    BWGroupLtd =  0x014F
    TangerineInc =  0x014E
    HUIZHOUDESAYSVAUTOMOTIVECOLTD =  0x014D
    MeshNetLtd =  0x014C
    MasterLock =  0x014B
    TivoliAudioLLC =  0x014A
    PerytonsLtd =  0x0149
    AmbimatElectronics =  0x0148
    MightyCastInc =  0x0147
    Ciright =  0x0146
    NovatelWireless =  0x0145
    LintechGmbH =  0x0144
    BkonConnect =  0x0143
    GrapeSystemsInc =  0x0142
    FedExServices =  0x0141
    AlpineElectronicsChinaCoLtd =  0x0140
    BBManufacturingCompany =  0x013F
    NodInc =  0x013E
    WirelessWERX =  0x013D
    MurataManufacturingCoLtd =  0x013C
    Allegion =  0x013B
    TencentHoldingsLtd =  0x013A
    FocusSystemsCorporation =  0x0139
    NTEOInc =  0x0138
    PrestigioPlazaLtd =  0x0137
    SilvairInc =  0x0136
    AirewareLLC =  0x0135
    ResolutionProductsLtd =  0x0134
    BlueMaestroLimited =  0x0133
    MADSInc =  0x0132
    CypressSemiconductor =  0x0131
    WarehouseInnovations =  0x0130
    ClarionCoInc =  0x012F
    ASSAABLOY =  0x012E
    SonyCorporation =  0x012D
    TEMECInstrumentsBV =  0x012C
    SportIQ =  0x012B
    ChangzhouYongseInfotechCoLtd =  0x012A
    NimbleDevicesOy =  0x0129
    GPSIGroupPtyLtd =  0x0128
    SaluticaAlliedSolutions =  0x0127
    PrometheanLtd =  0x0126
    SEATes =  0x0125
    HIDGlobal =  0x0124
    KinsaInc =  0x0123
    AirTurnInc =  0x0122
    SinoWealthElectronicLtd =  0x0121
    PorscheAG =  0x0120
    VolkswagenAG =  0x011F
    SkodaAutoas =  0x011E
    ArendiAG =  0x011D
    Baidu =  0x011C
    HewlettPackardEnterprise =  0x011B
    QualcommLabsInc =  0x011A
    WizeTechnologyCoLtd =  0x0119
    RadiusNetworksInc =  0x0118
    WimotoTechnologiesInc =  0x0117
    TenAKTechnologies =  0x0116
    esolutions =  0x0115
    Xensr =  0x0114
    OpenbrainTechnologiesCoLtd =  0x0113
    VisyblInc =  0x0112
    SteelseriesApS =  0x0111
    NipponSeikiCoLtd =  0x0110
    HiSiliconTechnologiesCOLIMITED =  0x010F
    AudiAG =  0x010E
    DENSOTENLimited =  0x010D
    TransducersDirectLLC =  0x010C
    ERiInc =  0x010B
    CodegateLtd =  0x010A
    AtusBV =  0x0109
    ChiconyElectronicsCoLtd =  0x0108
    DemantAS =  0x0107
    InnovativeYachtterSolutions =  0x0106
    UbiquitousComputingTechnologyCorporation =  0x0105
    PLUSLocationSystemsPtyLtd =  0x0104
    BangOlufsenAS =  0x0103
    KeiserCorporation =  0x0102
    FugooInc =  0x0101
    TomTomInternationalBV =  0x0100
    TypoProductsLLC =  0x00FF
    StanleyBlackandDecker =  0x00FE
    ValenceTechLimited =  0x00FD
    DelphiCorporation =  0x00FC
    KOUKAAMas =  0x00FB
    CrystalAlarmAB =  0x00FA
    StickNFind =  0x00F9
    AceUniCorpLtd =  0x00F8
    VSNTechnologiesInc =  0x00F7
    ElcometerLimited =  0x00F6
    SmartifierOy =  0x00F5
    NautilusInc =  0x00F4
    KentDisplaysInc =  0x00F3
    MorseProjectInc =  0x00F2
    WitronTechnologyLimited =  0x00F1
    PayPalInc =  0x00F0
    BitsplittersGmbH =  0x00EF
    AboveAverageOutcomesInc =  0x00EE
    JollyLogicLLC =  0x00ED
    BioResearchAssociates =  0x00EC
    ServerTechnologyInc =  0x00EB
    wwwvtracksystemscom =  0x00EA
    VtrackSystems =  0x00E9
    ACTSTechnologies =  0x00E8
    KSTechnologies =  0x00E7
    Freshtemp =  0x00E6
    EdenSoftwareConsultantsLtd =  0x00E5
    LSResearchInc =  0x00E4
    inMusicBrandsInc =  0x00E3
    SemilinkInc =  0x00E2
    DanlersLtd =  0x00E1
    Google =  0x00E0
    MisfitWearablesCorp =  0x00DF
    MuzikLLC =  0x00DE
    HosidenCorporation =  0x00DD
    ProcterGamble =  0x00DC
    SnuzaPtyLtd =  0x00DB
    txtrGmbH =  0x00DA
    VoyetraTurtleBeach =  0x00D9
    QualcommConnectedExperiencesInc =  0x00D8
    QualcommTechnologiesInc =  0x00D7
    TimexGroupUSAInc =  0x00D6
    AustcoCommunicationSystems =  0x00D5
    Kawantech =  0x00D4
    TaixingbangTechnologyHKCoLTD =  0x00D3
    DialogSemiconductorBV =  0x00D2
    PolarElectroEuropeBV =  0x00D1
    DexcomInc =  0x00D0
    ARCHOSSA =  0x00CF
    EveSystemsGmbH =  0x00CE
    MicrochipTechnologyInc =  0x00CD
    BeatsElectronics =  0x00CC
    BinauricSE =  0x00CB
    MC10 =  0x00CA
    Evluma =  0x00C9
    GeLoInc =  0x00C8
    QuuppaOy =  0x00C7
    SelflyBV =  0x00C6
    OnsetComputerCorporation =  0x00C5
    LGElectronics =  0x00C4
    adidasAG =  0x00C3
    GeneqInc =  0x00C2
    ShenzhenExcelsecuDataTechnologyCoLtd =  0x00C1
    AMICCOMElectronicsCorporation =  0x00C0
    StalmartTechnologyLimited =  0x00BF
    AAMPofAmerica =  0x00BE
    AplixCorporation =  0x00BD
    AceSensorInc =  0x00BC
    SPowerElectronicsLimited =  0x00BB
    StarkeyHearingTechnologies =  0x00BA
    JohnsonControlsInc =  0x00B9
    QualcommInnovationCenterIncQuIC =  0x00B8
    TreLabLtd =  0x00B7
    Mesointernational =  0x00B6
    SwirlNetworks =  0x00B5
    BDETechnologyCoLtd =  0x00B4
    ClarinoxTechnologiesPtyLtd =  0x00B3
    BekeyAS =  0x00B2
    SarisCyclingGroupInc =  0x00B1
    PassifSemiconductorCorp =  0x00B0
    Cinetix =  0x00AF
    OmegawaveOy =  0x00AE
    PeterSystemtechnikGmbH =  0x00AD
    GreenThrottleGames =  0x00AC
    IngenieurSystemgruppeZahnGmbH =  0x00AB
    CAENRFIDsrl =  0x00AA
    MARELLIEUROPESPA =  0x00A9
    ARPDevicesLimited =  0x00A8
    VisteonCorporation =  0x00A7
    PandaOceanInc =  0x00A6
    OTLDynamicsLLC =  0x00A5
    LINAKAS =  0x00A4
    MetaWatchLtd =  0x00A3
    VertuCorporationLimited =  0x00A2
    SRMedizinelektronik =  0x00A1
    KensingtonComputerProductsGroup =  0x00A0
    SuuntoOy =  0x009F
    BoseCorporation =  0x009E
    GeoforceInc =  0x009D
    ColorfyInc =  0x009C
    JiangsuToppowerAutomotiveElectronicsCoLtd =  0x009B
    Alpwise =  0x009A
    iTechDynamicGlobalDistributionLtd =  0x0099
    zero1tvGmbH =  0x0098
    ConnecteDeviceLtd =  0x0097
    ODMTechnologyInc =  0x0096
    NECLightingLtd =  0x0095
    AirohaTechnologyCorp2 =  0x0094
    UniversalElectronicsInc =  0x0093
    ThinkOpticsInc =  0x0092
    AdvancedPANMOBILsystemsGmbHCoKG =  0x0091
    FunaiElectricCoLtd =  0x0090
    TelitWirelessSolutionsGmbH =  0x008F
    QuinticCorp =  0x008E
    ZscanSoftware =  0x008D
    GimbalInc =  0x008C
    TopconPositioningSystemsLLC =  0x008B
    Jawbone =  0x008A
    GNHearingAS =  0x0089
    Ecotest =  0x0088
    GarminInternationalInc =  0x0087
    EquinuxAG =  0x0086
    BlueRadiosInc =  0x0085
    LudusHelsinkiLtd =  0x0084
    TimeKeepingSystemsInc =  0x0083
    DSEAAS =  0x0082
    WuXiVimicro =  0x0081
    DeLormePublishingCompanyInc =  0x0080
    AutonetMobile =  0x007F
    SportsTrackingTechnologiesLtd =  0x007E
    SeersTechnologyCoLtd =  0x007D
    ARCambridge =  0x007C
    HanlynnTechnologies =  0x007B
    MStarSemiconductorInc =  0x007A
    lesswireAG =  0x0079
    NikeInc =  0x0078
    LairdConnectivityLLC =  0x0077
    CreativeTechnologyLtd =  0x0076
    SamsungElectronicsCoLtd =  0x0075
    ZommLLC =  0x0074
    GroupSenseLtd =  0x0073
    ShangHaiSuperSmartElectronicsCoLtd =  0x0072
    connectBlueAB =  0x0071
    MonsterLLC =  0x0070
    SoundID =  0x006F
    SummitDataCommunicationsInc =  0x006E
    BriarTekInc =  0x006D
    BeautifulEnterpriseCoLtd =  0x006C
    PolarElectroOY =  0x006B
    MindTreeLtd =  0x006A
    ADEngineeringInc =  0x0069
    GeneralMotors =  0x0068
    GNAudioAS =  0x0067
    NineSolutionsOy =  0x0066
    HPInc =  0x0065
    BandXIInternationalLLC =  0x0064
    MiCommandInc =  0x0063
    GibsonGuitars =  0x0062
    RDAMicroelectronics =  0x0061
    RivieraWavesSAS =  0x0060
    WicentricInc =  0x005F
    StonestreetOneLLC =  0x005E
    RealtekSemiconductorCorporation =  0x005D
    BelkinInternationalInc =  0x005C
    RalinkTechnologyCorporation =  0x005B
    EMMicroelectronicMarinSA =  0x005A
    NordicSemiconductorASA =  0x0059
    VizioInc =  0x0058
    HarmanInternationalIndustriesInc =  0x0057
    SonyEricssonMobileCommunications =  0x0056
    PlantronicsInc =  0x0055
    ThreeDiJoyCorporation =  0x0054
    Free2moveAB =  0x0053
    JMCorporation =  0x0052
    TzeroTechnologiesInc =  0x0051
    SiRFTechnologyInc =  0x0050
    APTLtd =  0x004F
    AvagoTechnologies =  0x004E
    StaccatoCommunicationsInc =  0x004D
    AppleInc =  0x004C
    ContinentalAutomotiveSystems =  0x004B
    AccelSemiconductorLtd =  0x004A
    ThreeDSPCorporation =  0x0049
    MarvellTechnologyGroupLtd =  0x0048
    Bluegiga =  0x0047
    MediaTekInc =  0x0046
    AtherosCommunicationsInc =  0x0045
    SocketMobile =  0x0044
    PARROTAUTOMOTIVESAS =  0x0043
    CONWISETechnologyCorporationLtd =  0x0042
    IntegratedSiliconSolutionTaiwanInc =  0x0041
    SeikoEpsonCorporation =  0x0040
    BluetoothSIGInc =  0x003F
    SystemsandChipsInc =  0x003E
    IPextremeInc =  0x003D
    BlackBerryLimited =  0x003C
    GennumCorporation =  0x003B
    PanasonicHoldingsCorporation =  0x003A
    IntegratedSystemSolutionCorp =  0x0039
    SyntronixCorporation =  0x0038
    MobilianCorporation =  0x0037
    RenesasElectronicsCorporation =  0x0036
    EclipseHQEspanaSL =  0x0035
    ComputerAccessTechnologyCorporationCATC =  0x0034
    CommilLtd =  0x0033
    RedMCommunicationsLtd =  0x0032
    SynopsysInc =  0x0031
    STMicroelectronics =  0x0030
    MewTelTechnologyInc =  0x002F
    NorwoodSystems =  0x002E
    GCTSemiconductor =  0x002D
    MacronixInternationalCoLtd =  0x002C
    Tenovis =  0x002B
    SymbolTechnologiesInc =  0x002A
    HitachiLtd =  0x0029
    RFMicroDevices =  0x0028
    OpenInterface =  0x0027
    CTechnologies =  0x0026
    NXPBV =  0x0025
    Alcatel =  0x0024
    WavePlusTechnologyCoLtd =  0x0023
    NECCorporation =  0x0022
    MansellaLtd =  0x0021
    BandSpeedInc =  0x0020
    AVMBerlin =  0x001F
    Inventel =  0x001E
    Qualcomm =  0x001D
    ConexantSystemsInc =  0x001C
    SigniaTechnologiesInc =  0x001B
    TTPComLimited =  0x001A
    RohdeSchwarzGmbHCoKG =  0x0019
    TransilicaInc =  0x0018
    Newlogic =  0x0017
    KCTechnologyInc =  0x0016
    RTXAS =  0x0015
    MitsubishiElectricCorporation =  0x0014
    AtmelCorporation =  0x0013
    ZeevoInc =  0x0012
    WidcommInc =  0x0011
    MitelSemiconductor =  0x0010
    BroadcomCorporation =  0x000F
    ParthusTechnologiesInc =  0x000E
    TexasInstrumentsInc =  0x000D
    DigianswerAS =  0x000C
    SiliconWave =  0x000B
    QualcommTechnologiesInternationalLtdQTIL =  0x000A
    InfineonTechnologiesAG =  0x0009
    Motorola =  0x0008
    Lucent =  0x0007
    Microsoft =  0x0006
    ThreeCom =  0x0005
    ToshibaCorp =  0x0004
    IBMCorp =  0x0003
    IntelCorp =  0x0002
    NokiaMobilePhones =  0x0001
    EricssonAB =  0x0000

    RESERVED = 0xffff


ALL_16BIT_UUIDS = {
    0x0001: "SDP",
    0x0003: "RFCOMM",
    0x0005: "TCS-BIN",
    0x0007: "ATT",
    0x0008: "OBEX",
    0x000f: "BNEP",
    0x0010: "UPNP",
    0x0011: "HIDP",
    0x0012: "Hardcopy Control Channel",
    0x0014: "Hardcopy Data Channel",
    0x0016: "Hardcopy Notification",
    0x0017: "AVCTP",
    0x0019: "AVDTP",
    0x001b: "CMTP",
    0x001e: "MCAP Control Channel",
    0x001f: "MCAP Data Channel",
    0x0100: "L2CAP",
    # 0x0101 to 0x0fff undefined */
    0x1000: "Service Discovery Server Service Class",
    0x1001: "Browse Group Descriptor Service Class",
    0x1002: "Public Browse Root",
    # 0x1003 to 0x1100 undefined */
    0x1101: "Serial Port",
    0x1102: "LAN Access Using PPP",
    0x1103: "Dialup Networking",
    0x1104: "IrMC Sync",
    0x1105: "OBEX Object Push",
    0x1106: "OBEX File Transfer",
    0x1107: "IrMC Sync Command",
    0x1108: "Headset",
    0x1109: "Cordless Telephony",
    0x110a: "Audio Source",
    0x110b: "Audio Sink",
    0x110c: "A/V Remote Control Target",
    0x110d: "Advanced Audio Distribution",
    0x110e: "A/V Remote Control",
    0x110f: "A/V Remote Control Controller",
    0x1110: "Intercom",
    0x1111: "Fax",
    0x1112: "Headset AG",
    0x1113: "WAP",
    0x1114: "WAP Client",
    0x1115: "PANU",
    0x1116: "NAP",
    0x1117: "GN",
    0x1118: "Direct Printing",
    0x1119: "Reference Printing",
    0x111a: "Basic Imaging Profile",
    0x111b: "Imaging Responder",
    0x111c: "Imaging Automatic Archive",
    0x111d: "Imaging Referenced Objects",
    0x111e: "Handsfree",
    0x111f: "Handsfree Audio Gateway",
    0x1120: "Direct Printing Refrence Objects Service",
    0x1121: "Reflected UI",
    0x1122: "Basic Printing",
    0x1123: "Printing Status",
    0x1124: "Human Interface Device Service",
    0x1125: "Hardcopy Cable Replacement",
    0x1126: "HCR Print",
    0x1127: "HCR Scan",
    0x1128: "Common ISDN Access",
    # 0x1129 and 0x112a undefined */
    0x112d: "SIM Access",
    0x112e: "Phonebook Access Client",
    0x112f: "Phonebook Access Server",
    0x1130: "Phonebook Access",
    0x1131: "Headset HS",
    0x1132: "Message Access Server",
    0x1133: "Message Notification Server",
    0x1134: "Message Access Profile",
    0x1135: "GNSS",
    0x1136: "GNSS Server",
    0x1137: "3D Display",
    0x1138: "3D Glasses",
    0x1139: "3D Synchronization",
    0x113a: "MPS Profile",
    0x113b: "MPS Service",
    # 0x113c to 0x11ff undefined */
    0x1200: "PnP Information",
    0x1201: "Generic Networking",
    0x1202: "Generic File Transfer",
    0x1203: "Generic Audio",
    0x1204: "Generic Telephony",
    0x1205: "UPNP Service",
    0x1206: "UPNP IP Service",
    0x1300: "UPNP IP PAN",
    0x1301: "UPNP IP LAP",
    0x1302: "UPNP IP L2CAP",
    0x1303: "Video Source",
    0x1304: "Video Sink",
    0x1305: "Video Distribution",
    # 0x1306 to 0x13ff undefined */
    0x1400: "HDP",
    0x1401: "HDP Source",
    0x1402: "HDP Sink",
    # 0x1403 to 0x17ff undefined */
    0x1800: "Generic Access Profile",
    0x1801: "Generic Attribute Profile",
    0x1802: "Immediate Alert",
    0x1803: "Link Loss",
    0x1804: "Tx Power",
    0x1805: "Current Time Service",
    0x1806: "Reference Time Update Service",
    0x1807: "Next DST Change Service",
    0x1808: "Glucose",
    0x1809: "Health Thermometer",
    0x180a: "Device Information",
    # 0x180b and 0x180c undefined */
    0x180d: "Heart Rate",
    0x180e: "Phone Alert Status Service",
    0x180f: "Battery Service",
    0x1810: "Blood Pressure",
    0x1811: "Alert Notification Service",
    0x1812: "Human Interface Device",
    0x1813: "Scan Parameters",
    0x1814: "Running Speed and Cadence",
    0x1815: "Automation IO",
    0x1816: "Cycling Speed and Cadence",
    # 0x1817 undefined */
    0x1818: "Cycling Power",
    0x1819: "Location and Navigation",
    0x181a: "Environmental Sensing",
    0x181b: "Body Composition",
    0x181c: "User Data",
    0x181d: "Weight Scale",
    0x181e: "Bond Management",
    0x181f: "Continuous Glucose Monitoring",
    0x1820: "Internet Protocol Support",
    0x1821: "Indoor Positioning",
    0x1822: "Pulse Oximeter",
    0x1823: "HTTP Proxy",
    0x1824: "Transport Discovery",
    0x1825: "Object Transfer",
    # 0x1824 to 0x27ff undefined */
    0x2800: "Primary Service",
    0x2801: "Secondary Service",
    0x2802: "Include",
    0x2803: "Characteristic",
    # 0x2804 to 0x28ff undefined */
    0x2900: "Characteristic Extended Properties",
    0x2901: "Characteristic User Description",
    0x2902: "Client Characteristic Configuration",
    0x2903: "Server Characteristic Configuration",
    0x2904: "Characteristic Format",
    0x2905: "Characteristic Aggregate Formate",
    0x2906: "Valid Range",
    0x2907: "External Report Reference",
    0x2908: "Report Reference",
    0x2909: "Number of Digitals",
    0x290a: "Value Trigger Setting",
    0x290b: "Environmental Sensing Configuration",
    0x290c: "Environmental Sensing Measurement",
    0x290d: "Environmental Sensing Trigger Setting",
    0x290e: "Time Trigger Setting",
    # 0x290f to 0x29ff undefined */
    0x2a00: "Device Name",
    0x2a01: "Appearance",
    0x2a02: "Peripheral Privacy Flag",
    0x2a03: "Reconnection Address",
    0x2a04: "Peripheral Preferred Connection Parameters",
    0x2a05: "Service Changed",
    0x2a06: "Alert Level",
    0x2a07: "Tx Power Level",
    0x2a08: "Date Time",
    0x2a09: "Day of Week",
    0x2a0a: "Day Date Time",
    # 0x2a0b undefined */
    0x2a0c: "Exact Time 256",
    0x2a0d: "DST Offset",
    0x2a0e: "Time Zone",
    0x2a0f: "Local Time Information",
    # 0x2a10 undefined */
    0x2a11: "Time with DST",
    0x2a12: "Time Accuracy",
    0x2a13: "Time Source",
    0x2a14: "Reference Time Information",
    # 0x2a15 undefined */
    0x2a16: "Time Update Control Point",
    0x2a17: "Time Update State",
    0x2a18: "Glucose Measurement",
    0x2a19: "Battery Level",
    # 0x2a1a and 0x2a1b undefined */
    0x2a1c: "Temperature Measurement",
    0x2a1d: "Temperature Type",
    0x2a1e: "Intermediate Temperature",
    # 0x2a1f and 0x2a20 undefined */
    0x2a21: "Measurement Interval",
    0x2a22: "Boot Keyboard Input Report",
    0x2a23: "System ID",
    0x2a24: "Model Number String",
    0x2a25: "Serial Number String",
    0x2a26: "Firmware Revision String",
    0x2a27: "Hardware Revision String",
    0x2a28: "Software Revision String",
    0x2a29: "Manufacturer Name String",
    0x2a2a: "IEEE 11073-20601 Regulatory Cert. Data List",
    0x2a2b: "Current Time",
    0x2a2c: "Magnetic Declination",
    # 0x2a2d to 0x2a30 undefined */
    0x2a31: "Scan Refresh",
    0x2a32: "Boot Keyboard Output Report",
    0x2a33: "Boot Mouse Input Report",
    0x2a34: "Glucose Measurement Context",
    0x2a35: "Blood Pressure Measurement",
    0x2a36: "Intermediate Cuff Pressure",
    0x2a37: "Heart Rate Measurement",
    0x2a38: "Body Sensor Location",
    0x2a39: "Heart Rate Control Point",
    # 0x2a3a to 0x2a3e undefined */
    0x2a3f: "Alert Status",
    0x2a40: "Ringer Control Point",
    0x2a41: "Ringer Setting",
    0x2a42: "Alert Category ID Bit Mask",
    0x2a43: "Alert Category ID",
    0x2a44: "Alert Notification Control Point",
    0x2a45: "Unread Alert Status",
    0x2a46: "New Alert",
    0x2a47: "Supported New Alert Category",
    0x2a48: "Supported Unread Alert Category",
    0x2a49: "Blood Pressure Feature",
    0x2a4a: "HID Information",
    0x2a4b: "Report Map",
    0x2a4c: "HID Control Point",
    0x2a4d: "Report",
    0x2a4e: "Protocol Mode",
    0x2a4f: "Scan Interval Window",
    0x2a50: "PnP ID",
    0x2a51: "Glucose Feature",
    0x2a52: "Record Access Control Point",
    0x2a53: "RSC Measurement",
    0x2a54: "RSC Feature",
    0x2a55: "SC Control Point",
    0x2a56: "Digital",
    # 0x2a57 undefined */
    0x2a58: "Analog",
    # 0x2a59 undefined */
    0x2a5a: "Aggregate",
    0x2a5b: "CSC Measurement",
    0x2a5c: "CSC Feature",
    0x2a5d: "Sensor Location",
    # 0x2a5e to 0x2a62 undefined */
    0x2a63: "Cycling Power Measurement",
    0x2a64: "Cycling Power Vector",
    0x2a65: "Cycling Power Feature",
    0x2a66: "Cycling Power Control Point",
    0x2a67: "Location and Speed",
    0x2a68: "Navigation",
    0x2a69: "Position Quality",
    0x2a6a: "LN Feature",
    0x2a6b: "LN Control Point",
    0x2a6c: "Elevation",
    0x2a6d: "Pressure",
    0x2a6e: "Temperature",
    0x2a6f: "Humidity",
    0x2a70: "True Wind Speed",
    0x2a71: "True Wind Direction",
    0x2a72: "Apparent Wind Speed",
    0x2a73: "Apparent Wind Direction",
    0x2a74: "Gust Factor",
    0x2a75: "Pollen Concentration",
    0x2a76: "UV Index",
    0x2a77: "Irradiance",
    0x2a78: "Rainfall",
    0x2a79: "Wind Chill",
    0x2a7a: "Heat Index",
    0x2a7b: "Dew Point",
    0x2a7c: "Trend",
    0x2a7d: "Descriptor Value Changed",
    0x2a7e: "Aerobic Heart Rate Lower Limit",
    0x2a7f: "Aerobic Threshold",
    0x2a80: "Age",
    0x2a81: "Anaerobic Heart Rate Lower Limit",
    0x2a82: "Anaerobic Heart Rate Upper Limit",
    0x2a83: "Anaerobic Threshold",
    0x2a84: "Aerobic Heart Rate Upper Limit",
    0x2a85: "Date of Birth",
    0x2a86: "Date of Threshold Assessment",
    0x2a87: "Email Address",
    0x2a88: "Fat Burn Heart Rate Lower Limit",
    0x2a89: "Fat Burn Heart Rate Upper Limit",
    0x2a8a: "First Name",
    0x2a8b: "Five Zone Heart Rate Limits",
    0x2a8c: "Gender",
    0x2a8d: "Heart Rate Max",
    0x2a8e: "Height",
    0x2a8f: "Hip Circumference",
    0x2a90: "Last Name",
    0x2a91: "Maximum Recommended Heart Rate",
    0x2a92: "Resting Heart Rate",
    0x2a93: "Sport Type for Aerobic/Anaerobic Thresholds",
    0x2a94: "Three Zone Heart Rate Limits",
    0x2a95: "Two Zone Heart Rate Limit",
    0x2a96: "VO2 Max",
    0x2a97: "Waist Circumference",
    0x2a98: "Weight",
    0x2a99: "Database Change Increment",
    0x2a9a: "User Index",
    0x2a9b: "Body Composition Feature",
    0x2a9c: "Body Composition Measurement",
    0x2a9d: "Weight Measurement",
    0x2a9e: "Weight Scale Feature",
    0x2a9f: "User Control Point",
    0x2aa0: "Magnetic Flux Density - 2D",
    0x2aa1: "Magnetic Flux Density - 3D",
    0x2aa2: "Language",
    0x2aa3: "Barometric Pressure Trend",
    0x2aa4: "Bond Management Control Point",
    0x2aa5: "Bond Management Feature",
    0x2aa6: "Central Address Resolution",
    0x2aa7: "CGM Measurement",
    0x2aa8: "CGM Feature",
    0x2aa9: "CGM Status",
    0x2aaa: "CGM Session Start Time",
    0x2aab: "CGM Session Run Time",
    0x2aac: "CGM Specific Ops Control Point",
    0x2aad: "Indoor Positioning Configuration",
    0x2aae: "Latitude",
    0x2aaf: "Longitude",
    0x2ab0: "Local North Coordinate",
    0x2ab1: "Local East Coordinate",
    0x2ab2: "Floor Number",
    0x2ab3: "Altitude",
    0x2ab4: "Uncertainty",
    0x2ab5: "Location Name",
    0x2ab6: "URI",
    0x2ab7: "HTTP Headers",
    0x2ab8: "HTTP Status Code",
    0x2ab9: "HTTP Entity Body",
    0x2aba: "HTTP Control Point",
    0x2abb: "HTTPS Security",
    0x2abc: "TDS Control Point",
    0x2abd: "OTS Feature",
    0x2abe: "Object Name",
    0x2abf: "Object Type",
    0x2ac0: "Object Size",
    0x2ac1: "Object First-Created",
    0x2ac2: "Object Last-Modified",
    0x2ac3: "Object ID",
    0x2ac4: "Object Properties",
    0x2ac5: "Object Action Control Point",
    0x2ac6: "Object List Control Point",
    0x2ac7: "Object List Filter",
    0x2ac8: "Object Changed",
    # vendor defined */
    0xfeff: "GN Netcom",
    0xfefe: "GN ReSound A/S",
    0xfefd: "Gimbal, Inc.",
    0xfefc: "Gimbal, Inc.",
    0xfefb: "Stollmann E+V GmbH",
    0xfefa: "PayPal, Inc.",
    0xfef9: "PayPal, Inc.",
    0xfef8: "Aplix Corporation",
    0xfef7: "Aplix Corporation",
    0xfef6: "Wicentric, Inc.",
    0xfef5: "Dialog Semiconductor GmbH",
    0xfef4: "Google",
    0xfef3: "Google",
    0xfef2: "CSR",
    0xfef1: "CSR",
    0xfef0: "Intel",
    0xfeef: "Polar Electro Oy",
    0xfeee: "Polar Electro Oy",
    0xfeed: "Tile, Inc.",
    0xfeec: "Tile, Inc.",
    0xfeeb: "Swirl Networks, Inc.",
    0xfeea: "Swirl Networks, Inc.",
    0xfee9: "Quintic Corp.",
    0xfee8: "Quintic Corp.",
    0xfee7: "Tencent Holdings Limited",
    0xfee6: "Seed Labs, Inc.",
    0xfee5: "Nordic Semiconductor ASA",
    0xfee4: "Nordic Semiconductor ASA",
    0xfee3: "Anki, Inc.",
    0xfee2: "Anki, Inc.",
    0xfee1: "Anhui Huami Information Technology Co.",
    0xfee0: "Anhui Huami Information Technology Co.",
    0xfedf: "Design SHIFT",
    0xfede: "Coin, Inc.",
    0xfedd: "Jawbone",
    0xfedc: "Jawbone",
    0xfedb: "Perka, Inc.",
    0xfeda: "ISSC Technologies Corporation",
    0xfed9: "Pebble Technology Corporation",
    0xfed8: "Google",
    0xfed7: "Broadcom Corporation",
    0xfed6: "Broadcom Corporation",
    0xfed5: "Plantronics Inc.",
    0xfed4: "Apple, Inc.",
    0xfed3: "Apple, Inc.",
    0xfed2: "Apple, Inc.",
    0xfed1: "Apple, Inc.",
    0xfed0: "Apple, Inc.",
    0xfecf: "Apple, Inc.",
    0xfece: "Apple, Inc.",
    0xfecd: "Apple, Inc.",
    0xfecc: "Apple, Inc.",
    0xfecb: "Apple, Inc.",
    0xfeca: "Apple, Inc.",
    0xfec9: "Apple, Inc.",
    0xfec8: "Apple, Inc.",
    0xfec7: "Apple, Inc.",
    0xfec6: "Kocomojo, LLC",
    0xfec5: "Realtek Semiconductor Corp.",
    0xfec4: "PLUS Location Systems",
    0xfec3: "360fly, Inc.",
    0xfec2: "Blue Spark Technologies, Inc.",
    0xfec1: "KDDI Corporation",
    0xfec0: "KDDI Corporation",
    0xfebf: "Nod, Inc.",
    0xfebe: "Bose Corporation",
    0xfebd: "Clover Network, Inc.",
    0xfebc: "Dexcom, Inc.",
    0xfebb: "adafruit industries",
    0xfeba: "Tencent Holdings Limited",
    0xfeb9: "LG Electronics",
    0xfeb8: "Facebook, Inc.",
    0xfeb7: "Facebook, Inc.",
    0xfeb6: "Vencer Co, Ltd",
    0xfeb5: "WiSilica Inc.",
    0xfeb4: "WiSilica Inc.",
    0xfeb3: "Taobao",
    0xfeb2: "Microsoft Corporation",
    0xfeb1: "Electronics Tomorrow Limited",
    0xfeb0: "Nest Labs Inc.",
    0xfeaf: "Nest Labs Inc.",
    0xfeae: "Nokia Corporation",
    0xfead: "Nokia Corporation",
    0xfeac: "Nokia Corporation",
    0xfeab: "Nokia Corporation",
    0xfeaa: "Google",
    0xfea9: "Savant Systems LLC",
    0xfea8: "Savant Systems LLC",
    0xfea7: "UTC Fire and Security",
    0xfea6: "GoPro, Inc.",
    0xfea5: "GoPro, Inc.",
    0xfea4: "Paxton Access Ltd",
    0xfea3: "ITT Industries",
    0xfea2: "Intrepid Control Systems, Inc.",
    0xfea1: "Intrepid Control Systems, Inc.",
    0xfea0: "Google",
    0xfe9f: "Google",
    0xfe9e: "Dialog Semiconductor B.V.",
    0xfe9d: "Mobiquity Networks Inc",
    0xfe9c: "GSI Laboratories, Inc.",
    0xfe9b: "Samsara Networks, Inc",
    0xfe9a: "Estimote",
    0xfe99: "Currant, Inc.",
    0xfe98: "Currant, Inc.",
    0xfe97: "Tesla Motor Inc.",
    0xfe96: "Tesla Motor Inc.",
    0xfe95: "Xiaomi Inc.",
    0xfe94: "OttoQ Inc.",
    0xfe93: "OttoQ Inc.",
    0xfe92: "Jarden Safety & Security",
    0xfe91: "Shanghai Imilab Technology Co.,Ltd",
    0xfe90: "JUMA",
    0xfe8f: "CSR",
    0xfe8e: "ARM Ltd",
    0xfe8d: "Interaxon Inc.",
    0xfe8c: "TRON Forum",
    0xfe8b: "Apple, Inc.",
    0xfe8a: "Apple, Inc.",
    0xfe89: "B&O Play A/S",
    0xfe88: "SALTO SYSTEMS S.L.",
    0xfe87: "Qingdao Yeelink Information Technology Co., Ltd. ( 青岛亿联客信息技术有限公司 )",
    0xfe86: "HUAWEI Technologies Co., Ltd. ( 华为技术有限公司 )",
    0xfe85: "RF Digital Corp",
    0xfe84: "RF Digital Corp",
    0xfe83: "Blue Bite",
    0xfe82: "Medtronic Inc.",
    0xfe81: "Medtronic Inc.",
    0xfe80: "Doppler Lab",
    0xfe7f: "Doppler Lab",
    0xfe7e: "Awear Solutions Ltd",
    0xfe7d: "Aterica Health Inc.",
    0xfe7c: "Stollmann E+V GmbH",
    0xfe7b: "Orion Labs, Inc.",
    0xfe7a: "Bragi GmbH",
    0xfe79: "Zebra Technologies",
    0xfe78: "Hewlett-Packard Company",
    0xfe77: "Hewlett-Packard Company",
    0xfe76: "TangoMe",
    0xfe75: "TangoMe",
    0xfe74: "unwire",
    0xfe73: "St. Jude Medical, Inc.",
    0xfe72: "St. Jude Medical, Inc.",
    0xfe71: "Plume Design Inc",
    0xfe70: "Beijing Jingdong Century Trading Co., Ltd.",
    0xfe6f: "LINE Corporation",
    0xfe6e: "The University of Tokyo",
    0xfe6d: "The University of Tokyo",
    0xfe6c: "TASER International, Inc.",
    0xfe6b: "TASER International, Inc.",
    0xfe6a: "Kontakt Micro-Location Sp. z o.o.",
    0xfe69: "Qualcomm Life Inc",
    0xfe68: "Qualcomm Life Inc",
    0xfe67: "Lab Sensor Solutions",
    0xfe66: "Intel Corporation",
    # SDO defined */
    0xfffe: "Alliance for Wireless Power (A4WP)",
    0xfffd: "Fast IDentity Online Alliance (FIDO)",
}

ALL_128BIT_UUIDS = {
    "a3c87500-8ed3-4bdf-8a39-a01bebede295": "Eddystone Configuration Service",
    "a3c87501-8ed3-4bdf-8a39-a01bebede295": "Capabilities",
    "a3c87502-8ed3-4bdf-8a39-a01bebede295": "Active Slot",
    "a3c87503-8ed3-4bdf-8a39-a01bebede295": "Advertising Interval",
    "a3c87504-8ed3-4bdf-8a39-a01bebede295": "Radio Tx Power",
    "a3c87505-8ed3-4bdf-8a39-a01bebede295": "(Advanced) Advertised Tx Power",
    "a3c87506-8ed3-4bdf-8a39-a01bebede295": "Lock State",
    "a3c87507-8ed3-4bdf-8a39-a01bebede295": "Unlock",
    "a3c87508-8ed3-4bdf-8a39-a01bebede295": "Public ECDH Key",
    "a3c87509-8ed3-4bdf-8a39-a01bebede295": "EID Identity Key",
    "a3c8750a-8ed3-4bdf-8a39-a01bebede295": "ADV Slot Data",
    "a3c8750b-8ed3-4bdf-8a39-a01bebede295": "(Advanced) Factory reset",
    "a3c8750c-8ed3-4bdf-8a39-a01bebede295": "(Advanced) Remain Connectable",
    # BBC micro:bit Bluetooth Profiles */
    "e95d0753-251d-470a-a062-fa1922dfa9a8": "MicroBit Accelerometer Service",
    "e95dca4b-251d-470a-a062-fa1922dfa9a8": "MicroBit Accelerometer Data",
    "e95dfb24-251d-470a-a062-fa1922dfa9a8": "MicroBit Accelerometer Period",
    "e95df2d8-251d-470a-a062-fa1922dfa9a8": "MicroBit Magnetometer Service",
    "e95dfb11-251d-470a-a062-fa1922dfa9a8": "MicroBit Magnetometer Data",
    "e95d386c-251d-470a-a062-fa1922dfa9a8": "MicroBit Magnetometer Period",
    "e95d9715-251d-470a-a062-fa1922dfa9a8": "MicroBit Magnetometer Bearing",
    "e95d9882-251d-470a-a062-fa1922dfa9a8": "MicroBit Button Service",
    "e95dda90-251d-470a-a062-fa1922dfa9a8": "MicroBit Button A State",
    "e95dda91-251d-470a-a062-fa1922dfa9a8": "MicroBit Button B State",
    "e95d127b-251d-470a-a062-fa1922dfa9a8": "MicroBit IO PIN Service",
    "e95d8d00-251d-470a-a062-fa1922dfa9a8": "MicroBit PIN Data",
    "e95d5899-251d-470a-a062-fa1922dfa9a8": "MicroBit PIN AD Configuration",
    "e95dd822-251d-470a-a062-fa1922dfa9a8": "MicroBit PWM Control",
    "e95dd91d-251d-470a-a062-fa1922dfa9a8": "MicroBit LED Service",
    "e95d7b77-251d-470a-a062-fa1922dfa9a8": "MicroBit LED Matrix state",
    "e95d93ee-251d-470a-a062-fa1922dfa9a8": "MicroBit LED Text",
    "e95d0d2d-251d-470a-a062-fa1922dfa9a8": "MicroBit Scrolling Delay",
    "e95d93af-251d-470a-a062-fa1922dfa9a8": "MicroBit Event Service",
    "e95db84c-251d-470a-a062-fa1922dfa9a8": "MicroBit Requirements",
    "e95d9775-251d-470a-a062-fa1922dfa9a8": "MicroBit Event Data",
    "e95d23c4-251d-470a-a062-fa1922dfa9a8": "MicroBit Client Requirements",
    "e95d5404-251d-470a-a062-fa1922dfa9a8": "MicroBit Client Events",
    "e95d93b0-251d-470a-a062-fa1922dfa9a8": "MicroBit DFU Control Service",
    "e95d93b1-251d-470a-a062-fa1922dfa9a8": "MicroBit DFU Control",
    "e95d6100-251d-470a-a062-fa1922dfa9a8": "MicroBit Temperature Service",
    "e95d1b25-251d-470a-a062-fa1922dfa9a8": "MicroBit Temperature Period",
    # Nordic UART Port Emulation */
    "6e400001-b5a3-f393-e0a9-e50e24dcca9e": "Nordic UART Service",
    "6e400002-b5a3-f393-e0a9-e50e24dcca9e": "Nordic UART TX",
    "6e400003-b5a3-f393-e0a9-e50e24dcca9e": "Nordic UART RX",
}


def uuid_to_string(uuid):
    """
    For a given UUID string, try to determine the textual equivalent
    of the GATT service or characteristic.
    """
    if not isinstance(uuid, str):
        raise TypeError("Expected a UUID string.")

    if len(uuid) != 36:
        raise ValueError("Expected the UUID string to be 36 characters long.")

    uuid_text = ALL_128BIT_UUIDS.get(uuid, None)
    if uuid_text is not None:
        return uuid_text
    else:
        if uuid.endswith("-0000-1000-8000-00805f9b34fb"):
            uuid_service = int(uuid[:8], 16)
            return ALL_16BIT_UUIDS.get(uuid_service, None)
        else:
            return None
