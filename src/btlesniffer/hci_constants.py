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
    EricssonTechnologyLicensing = 0x0000
    NokiaMobilePhones = 0x0001
    IntelCorp = 0x0002
    IBMCorp = 0x0003
    ToshibaCorp = 0x0004
    ThreeCom = 0x0005
    Microsoft = 0x0006
    Lucent = 0x0007
    Motorola = 0x0008
    InfineonTechnologiesAG = 0x0009
    CambridgeSiliconRadio = 0x000a
    SiliconWave = 0x000b
    DigianswerAS = 0x000c
    TexasInstrumentsInc = 0x000d
    CevaInc = 0x000e
    BroadcomCorporation = 0x000f
    MitelSemiconductor = 0x0010
    WidcommInc = 0x0011
    ZeevoInc = 0x0012
    AtmelCorporation = 0x0013
    MitsubishiElectricCorporation = 0x0014
    RTXTelecomAS = 0x0015
    KCTechnologyInc = 0x0016
    NewLogic = 0x0017
    TransilicaInc = 0x0018
    RohdeSchwarzGmbHCoKG = 0x0019
    TTPComLimited = 0x001a
    SigniaTechnologiesInc = 0x001b
    ConexantSystemsInc = 0x001c
    Qualcomm = 0x001d
    Inventel = 0x001e
    AVMBerlin = 0x001f
    BandSpeedInc = 0x0020
    MansellaLtd = 0x0021
    NECCorporation = 0x0022
    WavePlusTechnologyCoLtd = 0x0023
    Alcatel = 0x0024
    NXPSemiconductors = 0x0025
    CTechnologies = 0x0026
    OpenInterface = 0x0027
    RFMicroDevices = 0x0028
    HitachiLtd = 0x0029
    SymbolTechnologiesInc = 0x002a
    Tenovis = 0x002b
    MacronixInternationalCoLtd = 0x002c
    GCTSemiconductor = 0x002d
    NorwoodSystems = 0x002e
    MewTelTechnologyInc = 0x002f
    STMicroelectronics = 0x0030
    Synopsis = 0x0031
    RedMLtd = 0x0032
    CommilLtd = 0x0033
    ComputerAccessTechnologyCorporation = 0x0034
    EclipseSL = 0x0035
    RenesasElectronicsCorporation = 0x0036
    MobilianCorporation = 0x0037
    Terax = 0x0038
    IntegratedSystemSolutionCorp = 0x0039
    MatsushitaElectricIndustrialCoLtd = 0x003a
    GennumCorporation = 0x003b
    BlackBerryLimited = 0x003c
    IPextremeInc = 0x003d
    SystemsandChipsInc = 0x003e
    BluetoothSIGInc = 0x003f
    SeikoEpsonCorporation = 0x0040
    IntegratedSiliconSolutionTaiwanInc = 0x0041
    CONWISETechnologyCorporationLtd = 0x0042
    PARROTSA = 0x0043
    SocketMobile = 0x0044
    AtherosCommunicationsInc = 0x0045
    MediaTekInc = 0x0046
    Bluegiga = 0x0047
    MarvellTechnologyGroupLtd = 0x0048
    ThreeDSPCorporation = 0x0049
    AccelSemiconductorLtd = 0x004a
    ContinentalAutomotiveSystems = 0x004b
    AppleInc = 0x004c
    StaccatoCommunicationsInc = 0x004d
    AvagoTechnologies = 0x004e
    APTLicensingLtd = 0x004f
    SiRFTechnology = 0x0050
    TzeroTechnologiesInc = 0x0051
    JMCorporation = 0x0052
    Free2moveAB = 0x0053
    ThreeDiJoyCorporation = 0x0054
    PlantronicsInc = 0x0055
    SonyEricssonMobileCommunications = 0x0056
    HarmanInternationalIndustriesInc = 0x0057
    VizioInc = 0x0058
    NordicSemiconductorASA = 0x0059
    EMMicroelectronicMarinSA = 0x005a
    RalinkTechnologyCorporation = 0x005b
    BelkinInternationalInc = 0x005c
    RealtekSemiconductorCorporation = 0x005d
    StonestreetOneLLC = 0x005e
    WicentricInc = 0x005f
    RivieraWavesSAS = 0x0060
    RDAMicroelectronics = 0x0061
    GibsonGuitars = 0x0062
    MiCommandInc = 0x0063
    BandXIInternationalLLC = 0x0064
    HewlettPackardCompany = 0x0065
    NineSolutionsOy = 0x0066
    GNNetcomAS = 0x0067
    GeneralMotors = 0x0068
    ADEngineeringInc = 0x0069
    MindTreeLtd = 0x006a
    PolarElectroOY = 0x006b
    BeautifulEnterpriseCoLtd = 0x006c
    BriarTekInc = 0x006d
    SummitDataCommunicationsInc = 0x006e
    SoundID = 0x006f
    MonsterLLC = 0x0070
    connectBlueAB = 0x0071
    ShangHaiSuperSmartElectronicsCoLtd = 0x0072
    GroupSenseLtd = 0x0073
    ZommLLC = 0x0074
    SamsungElectronicsCoLtd = 0x0075
    CreativeTechnologyLtd = 0x0076
    LairdTechnologies = 0x0077
    NikeInc = 0x0078
    lesswireAG = 0x0079
    MStarSemiconductorInc = 0x007a
    HanlynnTechnologies = 0x007b
    ARCambridge = 0x007c
    SeersTechnologyCoLtd = 0x007d
    SportsTrackingTechnologiesLtd = 0x007e
    AutonetMobile = 0x007f
    DeLormePublishingCompanyInc = 0x0080
    WuXiVimicro = 0x0081
    SennheiserCommunicationsAS = 0x0082
    TimeKeepingSystemsInc = 0x0083
    LudusHelsinkiLtd = 0x0084
    BlueRadiosInc = 0x0085
    equinoxAG = 0x0086
    GarminInternationalInc = 0x0087
    Ecotest = 0x0088
    GNReSoundAS = 0x0089
    Jawbone = 0x008a
    TopcornPositioningSystemsLLC = 0x008b
    GimbalInc = 0x008c
    ZscanSoftware = 0x008d
    QuinticCorp = 0x008e
    StollmanEVGmbH = 0x008f
    FunaiElectricCoLtd = 0x0090
    AdvancedPANMOBILSystemsGmbHCoKG = 0x0091
    ThinkOpticsInc = 0x0092
    UniversalElectronicsInc = 0x0093
    AirohaTechnologyCorp = 0x0094
    NECLightingLtd = 0x0095
    ODMTechnologyInc = 0x0096
    ConnecteDeviceLtd = 0x0097
    zer01tvGmbH = 0x0098
    iTechDynamicGlobalDistributionLtd = 0x0099
    Alpwise = 0x009a
    JiangsuToppowerAutomotiveElectronicsCoLtd = 0x009b
    ColorfyInc = 0x009c
    GeoforceInc = 0x009d
    BoseCorporation = 0x009e
    SuuntoOy = 0x009f
    KensingtonComputerProductsGroup = 0x00a0
    SRMedizinelektronik = 0x00a1
    VertuCorporationLimited = 0x00a2
    MetaWatchLtd = 0x00a3
    LINAKAS = 0x00a4
    OTLDynamicsLLC = 0x00a5
    PandaOceanInc = 0x00a6
    VisteonCorporation = 0x00a7
    ARPDevicesLimited = 0x00a8
    MagnetiMarelliSpA = 0x00a9
    CAENRFIDsrl = 0x00aa
    IngenieurSystemgruppeZahnGmbH = 0x00ab
    GreenThrottleGames = 0x00ac
    PeterSystemtechnikGmbH = 0x00ad
    OmegawaveOy = 0x00ae
    Cinetix = 0x00af
    PassifSemiconductorCorp = 0x00b0
    SarisCyclingGroupInc = 0x00b1
    BekeyAS = 0x00b2
    ClarinoxTechnologiesPtyLtd = 0x00b3
    BDETechnologyCoLtd = 0x00b4
    SwirlNetworks = 0x00b5
    Mesointernational = 0x00b6
    TreLabLtd = 0x00b7
    QualcommInnovationCenterInc = 0x00b8
    JohnsonControlsInc = 0x00b9
    StarkeyLaboratoriesInc = 0x00ba
    SPowerElectronicsLimited = 0x00bb
    AceSensorInc = 0x00bc
    AplixCorporation = 0x00bd
    AAMPofAmerica = 0x00be
    StalmartTechnologyLimited = 0x00bf
    AMICCOMElectronicsCorporation = 0x00c0
    ShenzhenExcelsecuDataTechnologyCoLtd = 0x00c1
    GeneqInc = 0x00c2
    adidasAG = 0x00c3
    LGElectronics = 0x00c4
    OnsetComputerCorporation = 0x00c5
    SelflyBV = 0x00c6
    QuuppaOy = 0x00c7
    GeLoInc = 0x00c8
    Evluma = 0x00c9
    MC10 = 0x00ca
    BinauricSE = 0x00cb
    BeatsElectronics = 0x00cc
    MicrochipTechnologyInc = 0x00cd
    ElgatoSystemsGmbH = 0x00ce
    ARCHOSSA = 0x00cf
    DexcomInc = 0x00d0
    PolarElectroEuropeBV = 0x00d1
    DialogSemiconductorBV = 0x00d2
    TaixingbangTechnologyCoLTD = 0x00d3
    Kawantech = 0x00d4
    AustcoCommunicationSystems = 0x00d5
    TimexGroupUSAInc = 0x00d6
    QualcommTechnologiesInc = 0x00d7
    QualcommConnectedExperiencesInc = 0x00d8
    VoyetraTurtleBeach = 0x00d9
    txtrGmbH = 0x00da
    Biosentronics = 0x00db
    ProcterGamble = 0x00dc
    HosidenCorporation = 0x00dd
    MuzikLLC = 0x00de
    MisfitWearablesCorp = 0x00df
    Google = 0x00e0
    DanlersLtd = 0x00e1
    SemilinkInc = 0x00e2
    inMusicBrandsInc = 0x00e3
    LSResearchInc = 0x00e4
    EdenSoftwareConsultantsLtd = 0x00e5
    Freshtemp = 0x00e6
    KSTechnologies = 0x00e7
    ACTSTechnologies = 0x00e8
    VtrackSystems = 0x00e9
    NielsenKellermanCompany = 0x00ea
    ServerTechnologyInc = 0x00eb
    BioResearchAssociates = 0x00ec
    JollyLogicLLC = 0x00ed
    AboveAverageOutcomesInc = 0x00ee
    BitsplittersGmbH = 0x00ef
    PayPalInc = 0x00f0
    WitronTechnologyLimited = 0x00f1
    AetherThingsInc = 0x00f2
    KentDisplaysInc = 0x00f3
    NautilusInc = 0x00f4
    SmartifierOy = 0x00f5
    ElcometerLimited = 0x00f6
    VSNTechnologiesInc = 0x00f7
    AceUniCorpLtd = 0x00f8
    StickNFind = 0x00f9
    CrystalCodeAB = 0x00fa
    KOUKAAMas = 0x00fb
    DelphiCorporation = 0x00fc
    ValenceTechLimited = 0x00fd
    Reserved = 0x00fe
    TypoProductsLLC = 0x00ff
    TomTomInternationalBV = 0x0100
    FugooInc = 0x0101
    KeiserCorporation = 0x0102
    BangOlufsenAS = 0x0103
    PLUSLocationsSystemsPtyLtd = 0x0104
    UbiquitousComputingTechnologyCorporation = 0x0105
    InnovativeYachtterSolutions = 0x0106
    WilliamDemantHoldingAS = 0x0107
    ChiconyElectronicsCoLtd = 0x0108
    AtusBV = 0x0109
    CodegateLtd = 0x010a
    ERiInc = 0x010b
    TransducersDirectLLC = 0x010c
    FujitsuTenLimited = 0x010d
    AudiAG = 0x010e
    HiSiliconTechnologiesCoLtd = 0x010f
    NipponSeikiCoLtd = 0x0110
    SteelseriesApS = 0x0111
    VisyblInc = 0x0112
    OpenbrainTechnologiesCoLtd = 0x0113
    Xensr = 0x0114
    esolutions = 0x0115
    OneOAKTechnologies = 0x0116
    WimotoTechnologiesInc = 0x0117
    RadiusNetworksInc = 0x0118
    WizeTechnologyCoLtd = 0x0119
    QualcommLabsInc = 0x011a
    ArubaNetworks = 0x011b
    Baidu = 0x011c
    ArendiAG = 0x011d
    SkodaAutoas = 0x011e
    VolkswagonAG = 0x011f
    PorscheAG = 0x0120
    SinoWealthElectronicLtd = 0x0121
    AirTurnInc = 0x0122
    KinsaInc = 0x0123
    HIDGlobal = 0x0124
    SEATes = 0x0125
    PrometheanLtd = 0x0126
    SaluticaAlliedSolutions = 0x0127
    GPSIGroupPtyLtd = 0x0128
    NimbleDevicesOy = 0x0129
    ChangzhouYongseInfotechCoLtd = 0x012a
    SportIQ = 0x012b
    TEMECInstrumentsBV = 0x012c
    SonyCorporation = 0x012d
    ASSAABLOY = 0x012e
    ClarionCoLtd = 0x012f
    WarehouseInnovations = 0x0130
    CypressSemiconductorCorporation = 0x0131
    MADSInc = 0x0132
    BlueMaestroLimited = 0x0133
    ResolutionProductsInc = 0x0134
    AirewearLLC = 0x0135
    SeedLabsInc = 0x0136
    PrestigioPlazaLtd = 0x0137
    NTEOInc = 0x0138
    FocusSystemsCorporation = 0x0139
    TencentHoldingsLimited = 0x013a
    Allegion = 0x013b
    MurataManufacuringCoLtd = 0x013c
    NodInc = 0x013e
    BBManufacturingCompany = 0x013f
    AlpineElectronicsCoLtd = 0x0140
    FedExServices = 0x0141
    GrapeSystemsInc = 0x0142
    BkonConnect = 0x0143
    LintechGmbH = 0x0144
    NovatelWireless = 0x0145
    Ciright = 0x0146
    MightyCastInc = 0x0147
    AmbimatElectronics = 0x0148
    PerytonsLtd = 0x0149
    TivoliAudioLLC = 0x014a
    MasterLock = 0x014b
    MeshNetLtd = 0x014c
    HuizhouDesaySVAutomotiveCOLTD = 0x014d
    TangerineInc = 0x014e
    BWGroupLtd = 0x014f
    PioneerCorporation = 0x0150
    OnBeep = 0x0151
    VernierSoftwareTechnology = 0x0152
    ROLErgo = 0x0153
    PebbleTechnology = 0x0154
    NETATMO = 0x0155
    AccumulateAB = 0x0156
    AnhuiHuamiInformationTechnologyCoLtd = 0x0157
    Inmitesro = 0x0158
    ChefStepsInc = 0x0159
    micasAG = 0x015a
    BiomedicalResearchLtd = 0x015b
    PitiusTecSL = 0x015c
    EstimoteInc = 0x015d
    UnikeyTechnologiesInc = 0x015e
    TimerCapCo = 0x015f
    AwoX = 0x0160
    yikes = 0x0161
    MADSGlobalNZLtd = 0x0162
    PCHInternational = 0x0163
    QingdaoYeelinkInformationTechnologyCoLtd = 0x0164
    MilwaukeeTool = 0x0165
    MISHIKPteLtd = 0x0166
    BayerHealthCare = 0x0167
    SpiceboxLLC = 0x0168
    emberlight = 0x0169
    CooperAtkinsCorporation = 0x016a
    Qblinks = 0x016b
    MYSPHERA = 0x016c
    LifeScanInc = 0x016d
    VolanticAB = 0x016e
    PodoLabsInc = 0x016f
    FHoffmannLaRocheAG = 0x0170
    AmazonFulfillmentService = 0x0171
    ConnovateTechnologyPrivateLimited = 0x0172
    KocomojoLLC = 0x0173
    EverykeyLLC = 0x0174
    DynamicControls = 0x0175
    SentriLock = 0x0176
    ISYSTinc = 0x0177
    CASIOCOMPUTERCOLTD = 0x0178
    LAPISSemiconductorCoLtd = 0x0179
    TelemonitorInc = 0x017a
    taskitGmbH = 0x017b
    DaimlerAG = 0x017c
    BatAndCat = 0x017d
    BluDotzLtd = 0x017e
    XTelApS = 0x017f
    GigasetCommunicationsGmbH = 0x0180
    GeckoHealthInnovationsInc = 0x0181
    HOPUbiquitous = 0x0182
    ToBeAssigned = 0x0183
    Nectar = 0x0184
    belappsLLC = 0x0185
    CORELightingLtd = 0x0186
    SeraphimSenseLtd = 0x0187
    UnicoRBC = 0x0188
    PhysicalEnterprisesInc = 0x0189
    AbleTrendTechnologyLimited = 0x018a
    KonicaMinoltaInc = 0x018b
    WiloSE = 0x018c
    ExtronDesignServices = 0x018d
    FitbitInc = 0x018e
    FirefliesSystems = 0x018f
    IntellettoTechnologiesInc = 0x0190
    FDKCORPORATION = 0x0191
    CloudleafInc = 0x0192
    MavericAutomationLLC = 0x0193
    AcousticStreamCorporation = 0x0194
    Zuli = 0x0195
    PaxtonAccessLtd = 0x0196
    WiSilicaInc = 0x0197
    VengitLimited = 0x0198
    SALTOSYSTEMSSL = 0x0199
    TRONForum = 0x019a
    CUBETECHsro = 0x019b
    CokiyaIncorporated = 0x019c
    CVSHealth = 0x019d
    Ceruus = 0x019e
    StrainstallLtd = 0x019f
    ChannelEnterprisesLtd = 0x01a0
    FIAMM = 0x01a1
    GIGALANECOLTD = 0x01a2
    EROAD = 0x01a3
    MineSafetyAppliances = 0x01a4
    IconHealthandFitness = 0x01a5
    AsandooGmbH = 0x01a6
    ENERGOUSCORPORATION = 0x01a7
    Taobao = 0x01a8
    CanonInc = 0x01a9
    GeophysicalTechnologyInc = 0x01aa
    FacebookInc = 0x01ab
    NiproDiagnosticsInc = 0x01ac
    FlightSafetyInternational = 0x01ad
    EarlensCorporation = 0x01ae
    SunriseMicroDevicesInc = 0x01af
    StarMicronicsCoLtd = 0x01b0
    NetizensSpzoo = 0x01b1
    NymiInc = 0x01b2
    NytecInc = 0x01b3
    TrineoSpzoo = 0x01b4
    NestLabsInc = 0x01b5
    LMTechnologiesLtd = 0x01b6
    GeneralElectricCompany = 0x01b7
    iD3SL = 0x01b8
    HANAMicron = 0x01b9
    StagesCyclingLLC = 0x01ba
    CochlearBoneAnchoredSolutionsAB = 0x01bb
    SenionLabAB = 0x01bc
    SyszoneCoLtd = 0x01bd
    PulsateMobileLtd = 0x01be
    HongKongHunterSunElectronicLimited = 0x01bf
    pironexGmbH = 0x01c0
    BRADATECHCorp = 0x01c1
    TransenergooilAG = 0x01c2
    Bunch = 0x01c3
    DMEMicroelectronics = 0x01c4
    BitcrazeAB = 0x01c5
    HASWAREInc = 0x01c6
    AbiogenixInc = 0x01c7
    PolyControlApS = 0x01c8
    Avion = 0x01c9
    LaerdalMedicalAS = 0x01ca
    FetchMyPet = 0x01cb
    SamLabsLtd = 0x01cc
    ChengduSynwingTechnologyLtd = 0x01cd
    HOUWASYSTEMDESIGNkk = 0x01ce
    BSH = 0x01cf
    PrimusInterParesLtd = 0x01d0
    August = 0x01d1
    GillElectronics = 0x01d2
    SkyWaveDesign = 0x01d3
    NewlabSrl = 0x01d4
    ELADsrl = 0x01d5
    Gwearablesinc = 0x01d6
    SquadroneSystemsInc = 0x01d7
    CodeCorporation = 0x01d8
    SavantSystemsLLC = 0x01d9
    LogitechInternationalSA = 0x01da
    InnblueConsulting = 0x01db
    iParkingLtd = 0x01dc
    KoninklijkePhilipsElectronicsNV = 0x01dd
    MinelabElectronicsPtyLimited = 0x01de
    BisonGroupLtd = 0x01df
    WidexAS = 0x01e0
    JollaLtd = 0x01e1
    LectronixInc = 0x01e2
    CaterpillarInc = 0x01e3
    FreedomInnovations = 0x01e4
    DynamicDevicesLtd = 0x01e5
    TechnologySolutionsLtd = 0x01e6
    IPSGroupInc = 0x01e7
    STIR = 0x01e8
    SanoInc = 0x01e9
    AdvancedApplicationDesignInc = 0x01ea
    AutoMapLLC = 0x01eb
    SpreadtrumCommunicationsShanghaiLtd = 0x01ec
    CuteCircuitLTD = 0x01ed
    ValeoService = 0x01ee
    FullpowerTechnologiesInc = 0x01ef
    KloudNation = 0x01f0
    ZebraTechnologiesCorporation = 0x01f1
    ItronInc = 0x01f2
    TheUniversityofTokyo = 0x01f3
    UTCFireandSecurity = 0x01f4
    CoolWebthingsLimited = 0x01f5
    DJOGlobal = 0x01f6
    GellinerLimited = 0x01f7
    AnykaMicroelectronicsTechnologyCoLTD = 0x01f8
    MedtronicInc = 0x01f9
    GozioInc = 0x01fa
    FormLiftingLLC = 0x01fb
    WahooFitnessLLC = 0x01fc
    KontaktMicroLocationSpzoo = 0x01fd
    RadioSystemCorporation = 0x01fe
    FreescaleSemiconductorInc = 0x01ff
    VerifoneSystemsPTeLtdTaiwanBranch = 0x0200
    ARTiming = 0x0201
    RigadoLLC = 0x0202
    KemppiOy = 0x0203
    TapcentiveInc = 0x0204
    SmartboticsInc = 0x0205
    OtterProductsLLC = 0x0206
    STEMPInc = 0x0207
    LumiGeekLLC = 0x0208
    InvisionHeartInc = 0x0209
    MacnicaInc = 0x020a
    JaguarLandRoverLimited = 0x020b
    CoroWareTechnologiesInc = 0x020c
    SimploTechnologyCoLTD = 0x020d
    OmronHealthcareCoLTD = 0x020e
    ComoduleGMBH = 0x020f
    ikeGPS = 0x0210
    TelinkSemiconductorCoLtd = 0x0211
    InterplanCoLtd = 0x0212
    WylerAG = 0x0213
    IKMultimediaProductionsrl = 0x0214
    LukotonExperienceOy = 0x0215
    MTILtd = 0x0216
    Tech4homeLda = 0x0217
    HiotechAB = 0x0218
    DOTTLimited = 0x0219
    BlueSpeckLabsLLC = 0x021a
    CiscoSystemsInc = 0x021b
    MobicommInc = 0x021c
    Edamic = 0x021d
    GoodnetLtd = 0x021e
    LusterLeafProductsInc = 0x021f
    ManusMachinaBV = 0x0220
    MobiquityNetworksInc = 0x0221
    PraxisDynamics = 0x0222
    PhilipMorrisProductsSA = 0x0223
    ComarchSA = 0x0224
    NestlNespressoSA = 0x0225
    MerliniaAS = 0x0226
    LifeBEAMTechnologies = 0x0227
    TwocanoesLabsLLC = 0x0228
    MuovertiLimited = 0x0229
    StamerMusikanlagenGMBH = 0x022a
    TeslaMotors = 0x022b
    PharynksCorporation = 0x022c
    Lupine = 0x022d
    SiemensAG = 0x022e
    HuamiCultureCommunicationCOLTD = 0x022f
    FosterElectricCompanyLtd = 0x0230
    ETASA = 0x0231
    xSensoSolutionsKft = 0x0232
    ShenzhenSuLongCommunicationLtd = 0x0233
    FengFanTechnologyCoLtd = 0x0234
    QrioInc = 0x0235
    PitpatpetLtd = 0x0236
    MSHelisrl = 0x0237
    Trakm8Ltd = 0x0238
    JINCOLtd = 0x0239
    AlatechTechnology = 0x023a
    BeijingCarePulseElectronicTechnologyCoLtd = 0x023b
    Awarepoint = 0x023c
    ViCentraBV = 0x023d
    RavenIndustries = 0x023e
    WaveWareTechnologies = 0x023f
    ArgenoxTechnologies = 0x0240
    BragiGmbH = 0x0241
    SixteenLabInc = 0x0242
    MasimoCorp = 0x0243
    IoteraInc = 0x0244
    EndressHauser = 0x0245
    ACKmeNetworksInc = 0x0246
    FiftyThreeInc = 0x0247
    ParkerHannifinCorp = 0x0248
    TranscranialLtd = 0x0249
    UwatecAG = 0x024a
    OrlanLLC = 0x024b
    BlueCloverDevices = 0x024c
    MWaySolutionsGmbH = 0x024d
    MicrotronicsEngineeringGmbH = 0x024e
    SchneiderSchreibgerteGmbH = 0x024f
    SapphireCircuitsLLC = 0x0250
    LumoBodytechInc = 0x0251
    UKCTechnosolution = 0x0252
    XicatoInc = 0x0253
    Playbrush = 0x0254
    DaiNipponPrintingCoLtd = 0x0255
    G24PowerLimited = 0x0256
    AdBabbleLocalCommerceInc = 0x0257
    DevialetSA = 0x0258
    ALTYOR = 0x0259
    UniversityofAppliedSciencesValaisHauteEcoleValaisanne = 0x025a
    FiveInteractiveLLCdbaZendo = 0x025b
    NetEaseNetworkcoLtd = 0x025c
    LexmarkInternationalInc = 0x025d
    FlukeCorporation = 0x025e
    YardarmTechnologies = 0x025f
    SensaRx = 0x0260
    SECVREGmbH = 0x0261
    GlacialRidgeTechnologies = 0x0262
    IdentivInc = 0x0263
    DDSInc = 0x0264
    SMKCorporation = 0x0265
    SchawbelTechnologiesLLC = 0x0266
    XMISystemsSA = 0x0267
    Cerevo = 0x0268
    TorroxGmbHCoKG = 0x0269
    Gemalto = 0x026a
    DEKAResearchDevelopmentCorp = 0x026b
    DomsterTadeuszSzydlowski = 0x026c
    TechnogymSPA = 0x026d
    FLEURBAEYBVBA = 0x026e
    AptcodeSolutions = 0x026f
    LSIADLTechnology = 0x0270
    AnimasCorp = 0x0271
    AlpsElectricCoLtd = 0x0272
    OCEASOFT = 0x0273
    MotsaiResearch = 0x0274
    Geotab = 0x0275
    EGOElektroGertebauGmbH = 0x0276
    bewhereinc = 0x0277
    JohnsonOutdoorsInc = 0x0278
    steuteSchaltgerateGmbHCoKG = 0x0279
    Ekominiinc = 0x027a
    DEFAAS = 0x027b
    AseptikaLtd = 0x027c
    HUAWEITechnologiesCoLtd = 0x027d
    HabitAwareLLC = 0x027e
    ruwidoaustriagmbh = 0x027f
    ITECcorporation = 0x0280
    StoneL = 0x0281
    SonovaAG = 0x0282
    MavenMachinesInc = 0x0283
    SynapseElectronics = 0x0284
    StandardInnovationInc = 0x0285
    RFCodeInc = 0x0286
    WallyVenturesSL = 0x0287
    WillowbankElectronicsLtd = 0x0288
    SKTelecom = 0x0289
    JetroAS = 0x028a
    CodeGearsLTD = 0x028b
    NANOLINKAPS = 0x028c
    IFLLC = 0x028d
    RFDigitalCorp = 0x028e
    ChurchDwightCoInc = 0x028f
    MultibitOy = 0x0290
    CliniCloudInc = 0x0291
    SwiftSensors = 0x0292
    BlueBite = 0x0293
    ELIASGmbH = 0x0294
    SivantosGmbH = 0x0295
    Petzl = 0x0296
    stormpowerltd = 0x0297
    EISSTLtd = 0x0298
    InexessTechnologySimmaKG = 0x0299
    CurrantInc = 0x029a
    C2DevelopmentInc = 0x029b
    BlueSkyScientificLLCA = 0x029c
    ALOTTAZSLABSLLC = 0x029d
    Kupsonspolsro = 0x029e
    AreusEngineeringGmbH = 0x029f
    ImpossibleCameraGmbH = 0x02a0
    InventureTrackSystems = 0x02a1
    LockedUp = 0x02a2
    Itude = 0x02a3
    PacificLockCompany = 0x02a4
    TendyronCorporation = 0x02a5
    RobertBoschGmbH = 0x02a6
    IlluxtroninternationalBV = 0x02a7
    miSportLtd = 0x02a8
    Chargelib = 0x02a9
    DopplerLab = 0x02aa
    BBPOSLimited = 0x02ab
    RTBElektronikGmbHCoKG = 0x02ac
    RxNetworksInc = 0x02ad
    WeatherFlowInc = 0x02ae
    TechnicolorUSAInc = 0x02af
    BestechnicLtd = 0x02b0
    RadenInc = 0x02b1
    JouZenOy = 0x02b2
    CLABERSPA = 0x02b3
    HyginexInc = 0x02b4
    HANSHINELECTRICRAILWAYCOLTD = 0x02b5
    SchneiderElectric = 0x02b6
    OortTechnologiesLLC = 0x02b7
    ChronoTherapeutics = 0x02b8
    RinnaiCorporation = 0x02b9
    SwissprimeTechnologiesAG = 0x02ba
    KohaCoLtd = 0x02bb
    GenevacLtd = 0x02bc
    Chemtronics = 0x02bd
    SeguroTechnologySpzoo = 0x02be
    RedbirdFlightSimulations = 0x02bf
    DashRobotics = 0x02c0
    LINECorporation = 0x02c1
    GuillemotCorporation = 0x02c2
    TechtronicPowerToolsTechnologyLimited = 0x02c3
    WilsonSportingGoods = 0x02c4
    LenovoPteLtd = 0x02c5
    AyatanSensors = 0x02c6
    ElectronicsTomorrowLimited = 0x02c7
    VASCODataSecurityInternationalInc = 0x02c8
    PayRangeInc = 0x02c9
    ABOVSemiconductor = 0x02ca
    AINAWirelessInc = 0x02cb
    EijkelkampSoilWater = 0x02cc
    BMAergonomicsbv = 0x02cd
    TevaBrandedPharmaceuticalProductsRDInc = 0x02ce
    Anima = 0x02cf
    ThreeM = 0x02d0
    EmpaticaSrl = 0x02d1
    AferoInc = 0x02d2
    PowercastCorporation = 0x02d3
    SecuyouApS = 0x02d4
    OMRONCorporation = 0x02d5
    SendSolutions = 0x02d6
    NIPPONSYSTEMWARECOLTD = 0x02d7
    Neosfar = 0x02d8
    FlieglAgrartechnikGmbH = 0x02d9
    Gilvader = 0x02da
    DigiInternationalInc = 0x02db
    DeWalchTechnologiesInc = 0x02dc
    FlintRehabilitationDevicesLLC = 0x02dd
    SamsungSDSCoLtd = 0x02de
    BlurProductDevelopment = 0x02df
    UniversityofMichigan = 0x02e0
    VictronEnergyBV = 0x02e1
    NTTdocomo = 0x02e2
    CarmanahTechnologiesCorp = 0x02e3
    BytestormLtd = 0x02e4
    EspressifIncorporated = 0x02e5
    Unwire = 0x02e6
    ConnectedYardInc = 0x02e7
    AmericanMusicEnvironments = 0x02e8
    SensogramTechnologiesInc = 0x02e9
    FujitsuLimited = 0x02ea
    ArdicTechnology = 0x02eb
    DeltaSystemsInc = 0x02ec
    HTCCorporation = 0x02ed
    CitizenHoldingsCoLtd = 0x02ee
    SMARTINNOVATIONinc = 0x02ef
    BlackratSoftware = 0x02f0
    TheIdeaCaveLLC = 0x02f1
    GoProInc = 0x02f2
    AuthAirInc = 0x02f3
    VensiInc = 0x02f4
    IndagemTechLLC = 0x02f5
    IntemoTechnologies = 0x02f6
    DreamVisionscoLtd = 0x02f7
    RunteqOyLtd = 0x02f8
    IMAGINATIONTECHNOLOGIESLTD = 0x02f9
    CoSTARTechnologies = 0x02fa
    ClariusMobileHealthCorp = 0x02fb
    ShanghaiFrequenMicroelectronicsCoLtd = 0x02fc
    UwannaInc = 0x02fd
    LierdaScienceTechnologyGroupCoLtd = 0x02fe
    SiliconLaboratories = 0x02ff
    WorldMotoInc = 0x0300
    GiatecScientificInc = 0x0301
    LoopDevicesInc = 0x0302
    IACAelectronique = 0x0303
    MartiansInc = 0x0304
    SwippApS = 0x0305
    LifeLaboratoryInc = 0x0306
    FUJIINDUSTRIALCOLTD = 0x0307
    SurefireLLC = 0x0308
    DolbyLabs = 0x0309
    Ellisys = 0x030a
    MagnitudeLightingConverters = 0x030b
    HiltiAG = 0x030c
    DevdataSrl = 0x030d
    Deviceworx = 0x030e
    ShortcutLabs = 0x030f
    SGLItaliaSrl = 0x0310
    PEEQDATA = 0x0311
    DucereTechnologiesPvtLtd = 0x0312
    DiveNavInc = 0x0313
    RIIGAISpzoo = 0x0314
    ThermoFisherScientific = 0x0315
    AGMeasurematicsPvtLtd = 0x0316
    CHUOElectronicsCOLTD = 0x0317
    AspentaInternational = 0x0318
    EugsterFrismagAG = 0x0319
    AmberwirelessGmbH = 0x031a
    HQInc = 0x031b
    LabSensorSolutions = 0x031c
    EnterlabApS = 0x031d
    EyefiInc = 0x031e
    MetaSystemSpA = 0x031f
    SONOELECTRONICSCOLTD = 0x0320
    Jewelbots = 0x0321
    CompumedicsLimited = 0x0322
    RotorBikeComponents = 0x0323
    AstroInc = 0x0324
    AmotusSolutions = 0x0325
    HealthwearTechnologiesLtd = 0x0326
    EssexElectronics = 0x0327
    GrundfosAS = 0x0328
    EargoInc = 0x0329
    ElectronicDesignLab = 0x032a
    ESYLUX = 0x032b
    NIPPONSMTCOLtd = 0x032c
    BMinnovationsGmbH = 0x032d
    indoormap = 0x032e
    OttoQInc = 0x032f
    NorthPoleEngineering = 0x0330
    ThreeFlaresTechnologiesInc = 0x0331
    ElectrocompanietAS = 0x0332
    MulTLock = 0x0333
    CorentiumAS = 0x0334
    EnlightedInc = 0x0335
    GISTIC = 0x0336
    AJP2HoldingsLLC = 0x0337
    COBIGmbH = 0x0338
    BlueSkyScientificLLCB = 0x0339
    AppceptionInc = 0x033a
    CourtneyThorneLimited = 0x033b
    Virtuosys = 0x033c
    TPVTechnologyLimited = 0x033d
    MonitraSA = 0x033e
    AutomationComponentsInc = 0x033f
    Letsensesrl = 0x0340
    EtesianTechnologiesLLC = 0x0341
    GERTECBRASILLTDA = 0x0342
    DrekkerDevelopmentPtyLtd = 0x0343
    WhirlInc = 0x0344
    LocusPositioning = 0x0345
    AcuityBrandsLightingInc = 0x0346
    PreventBiometrics = 0x0347
    Arioneo = 0x0348
    VersaMe = 0x0349
    Vaddio = 0x034a
    LibratoneAS = 0x034b
    HMElectronicsInc = 0x034c
    TASERInternationalInc = 0x034d
    SafeTrustInc = 0x034e
    HeartlandPaymentSystems = 0x034f
    BitstrataSystemsInc = 0x0350
    PiepsGmbH = 0x0351
    iRidingTechnologyCoLtd = 0x0352
    AlphaAudiotronicsInc = 0x0353
    TOPPANFORMSCOLTD = 0x0354
    SigmaDesignsInc = 0x0355
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
