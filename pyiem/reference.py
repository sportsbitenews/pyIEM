"""Reference values and dictionaries

No functional code found within this module, just a bunch of statics

.. data:: nwsli2state

    A dictionary mapping 2 letter NWSLI codes to their corresponding state
    two letter code.  For locations outside of the US, some of these are
    guesses on my part.

.. data:: nwsli2country

    A dictionary mapping 2 letter NWSLI codes to their correspionding two
    letter country code.  Some of these are sketchy.

"""

IA_WEST = -96.7
IA_EAST = -90.1
IA_NORTH = 43.61
IA_SOUTH = 40.37

MW_WEST = -104.2
MW_EAST = -80.1
MW_NORTH = 49.51
MW_SOUTH = 35.47

CONUS_WEST = -134.2
CONUS_EAST = -60.1
CONUS_NORTH = 49.51
CONUS_SOUTH = 24.47

# National Weather Service Location Identifier (NWSLI) uses two letter codes
# in identifiers to equate to a state, this is a cross reference of that
nwsli2state = {"A2": "AK", "A1": "AL", "A4": "AR", "A3": "AZ", "C1": "CA",
               "C2": "CO", "C3": "CT", "D2": "DC", "D1": "DE", "F1": "FL",
               "G1": "GA", "H1": "HI", "I4": "IA", "I1": "ID",
               "I2": "IL", "I3": "IN", "K1": "KS", "K2": "KY", "L1": "LA",
               "M3": "MA", "M2": "MD", "M1": "ME", "M4": "MI", "M5": "MN",
               "M7": "MO", "M6": "MS", "M8": "MT", "N7": "NC", "N8": "ND",
               "N1": "NE", "N3": "NH", "N4": "NJ", "N5": "NM", "N2": "NV",
               "N6": "NY", "O1": "OH", "O2": "OK", "O3": "OR", "P5": "P1",
               "P6": "P2", "P7": "P3", "P8": "P4", "P1": "PA", "R1": "RI",
               "S1": "SC", "S2": "SD", "T1": "TN", "T2": "TX", "U1": "UT",
               "V2": "VA", "V1": "VT", "W1": "WA", "W3": "WI", "W2": "WV",
               "W4": "WY", "Q1": "AB", "Q2": "BC", "Q3": "MB", "B3": "NB",
               "N9": "NF", "S4": "NS", "Q5": "NW", "Q6": "ON",
               "Q7": "PQ", "Q8": "SK", "Q9": "YK", "B1": "BJ",
               "C6": "CH", "C7": "CL", "C4": "CM", "C5": "CP",
               "D3": "DF", "D4": "DR", "G2": "GJ", "G3": "GR", "H2": "HD",
               "J1": "JL", "C9": "MC", "R2": "MR", "X1": "MX", "L2": "NL",
               "R3": "NR", "O4": "OX", "P9": "PB", "S3": "SL", "S5": "SN",
               "S6": "SO", "T5": "TL", "T4": "TP", "V4": "VC", "C8": "CI",
               "Y1": "YC",
               "P4": "PR",
               "V3": "VI", "QR": "AB", "X4": "QO", "B7": "BR", "Q4": "QR",
               }
nwsli2country = {"A2": "US", "A1": "US", "A4": "US", "A3": "US", "C1": "US",
                 "C2": "US", "C3": "US", "D2": "US", "D1": "US", "F1": "US",
                 "G1": "US", "G5": "GM", "H1": "US", "I4": "US", "I1": "US",
                 "I2": "US", "I3": "US", "K1": "US", "K2": "US", "L1": "US",
                 "M3": "US", "M2": "US", "M1": "US", "M4": "US", "M5": "US",
                 "M7": "US", "M6": "US", "M8": "US", "N7": "US", "N8": "US",
                 "N1": "US", "N3": "US", "N4": "US", "N5": "US", "N2": "US",
                 "N6": "US", "O1": "US", "O2": "US", "O3": "US", "P5": "US",
                 "P6": "US", "P7": "US", "P8": "US", "P1": "US", "R1": "US",
                 "S1": "US", "S2": "US", "T1": "US", "T2": "US", "U1": "US",
                 "V2": "US", "V1": "US", "W1": "US", "W3": "US", "W2": "US",
                 "W4": "US", "Q1": "CA", "Q2": "CA", "Q3": "CA", "B3": "CA",
                 "N9": "CA", "S4": "CA", "Q5": "CA", "Q6": "CA", "E1": "PE",
                 "Q7": "CA", "Q8": "CA", "Q9": "CA", "A5": "AG", "B1": "MX",
                 "C6": "MX", "C8": "MX", "C7": "MX", "C4": "MX", "C5": "MX",
                 "D3": "MX", "D4": "MX", "G2": "MX", "G3": "MX", "H2": "MX",
                 "J1": "MX", "C9": "MX", "R2": "MX", "X1": "MX", "L2": "MX",
                 "R3": "MX", "O4": "MX", "P9": "MX", "S3": "MX", "S5": "MX",
                 "S6": "MX", "T3": "TB", "T5": "MX", "T4": "MX", "V4": "MX",
                 "Y1": "MX", "Z1": "ZC", "E2": "SV", "G4": "GT", "H3": "HN",
                 "R5": "JA", "R6": "NI", "P4": "US", "R4": "RK",
                 "V3": "US", "QR": "CA", "X4": "MX", "B7": "MX", "Q4": "MX",
                 }
txt2drct = {
 'N': 360,
 'North': 360,
 'NNE': 25,
 'NE': 45,
 'ENE': 70,
 'E': 90,
 'East': 90,
 'ESE': 115,
 'SE': 135,
 'SSE': 155,
 'S': 180,
 'South': 180,
 'SSW':  205,
 'SW':   225,
 'WSW':  250,
 'W':    270,
 'West': 270,
 'WNW': 295,
 'NW': 315,
 'NNW': 335
}


hailsize = {
 '0.25': "pea",
 '0.50': "marble",
 '0.75': "penny",
 '0.88': "nickel",
 '1.00': "quarter",
 '1.25': "half dollar",
 '1.50': "ping pong ball",
 '1.75': "golf ball",
 '2.00': "egg",
 '2.50': "tennis ball",
 '2.75': "baseball",
 '3.00': "teacup",
 '4.00': "grapefruit",
 '4.50': "softball"
}

lsr_events = {
 'BLOWING SNOW': 'a',
 'DRIFTING SNOW': 'a',
 'HIGH SUST WINDS': 'A',
 'DOWNBURST': 'B',
 'FUNNEL CLOUD': 'C',
 'FUNNEL': 'C',
 'TSTM WND DMG': 'D',
 'TREES DOWN': 'D',
 'TSTM WIND DMG': 'D',
 'FLOOD': 'E',
 'FLOODING': 'E',
 'FLASH FLOOD': 'F',
 'MAJ FLASH FLD': 'F',
 'TSTM WND GST': 'G',
 'TSTM WIND': 'G',
 'TSTM WIND GST': 'G',
 'HAIL': 'H',
 'MARINE HAIL': 'H',
 'EXCESSIVE HEAT': 'I',
 'DENSE FOG': 'J',
 'FOG': 'J',
 'LIGHTNING STRIKE': 'K',
 'LIGHTNING': 'L',
 'MARINE TSTM WND': 'M',
 'MARINE TSTM WIND': 'M',
 'NON-TSTM WND GST': 'N',
 'NON TSTM WND GST': 'N',
 'NON-TSTM WND DMG': 'O',
 'NON TSTM WND DMG': 'O',
 'NON-TSTM DMG GST': 'O',
 'NON TSTM DMG GST': 'O',
 'NON-TSTM DMG': 'O',
 'NON-TSTM WND': 'O',
 'HIGH WINDS': 'O',
 'WND DAMAGE': 'O',
 'RIP CURRENTS': 'P',
 'RIP CURRENT': 'P',
 'HIGH SURF': 'P',
 'TROPICAL STORM': 'Q',
 'HEAVY RAIN': 'R',
 'RAIN': 'R',
 'SNOW': 'S',
 'STORM TOTAL SNOW': 'S',
 'SLEET': 's',
 'MODERATE SLEET': 's',
 'HEAVY SLEET': 's',
 'HEAVY SNOW': 'S',
 'TORNADO': 'T',
 'WILDFIRE': 'U',
 'FIRE': 'U',
 'AVALANCHE': 'V',
 'WALL CLOUD': 'X',
 'WATER SPOUT': 'W',
 'WATERSPOUT': 'W',
 'BLIZZARD': 'Z',
 'HURRICANE': '0',
 'STORM SURGE': '1',
 'DUST STORM': '2',
 'SPRINKLES - FEW': '3',
 'HIGH ASTR TIDES': '4',
 'LOW ASTR TIDES': '4',
 'FREEZING RAIN': '5',
 'FREEZING DRIZZLE': '5',
 'ICE STORM': '5',
 'ICING ON ROADS': '5',
 'EXTREME COLD': '6',
 'FREEZE': '6',
 'EXTR WIND CHILL': '7',
 'SEICHE': '9',
 'VOLCANIC ASHFALL': 'z',
 'TSUNAMI': 'y',
 'DEBRIS FLOW': 'x',
 'COASTAL FLOOD': 'v',
 'LAKESHORE FLOOD': 'u',
 'SNEAKER WAVE': 't'
}

name2pytz = {
    'GMT': 'UTC',
    'CHDT': 'Etc/GMT-8', 'CHST': 'Etc/GMT-9', 'LST': 'Etc/GMT-10',
    'ADT': 'Etc/GMT-3',
    'VDT': 'Etc/GMT-3', 'VST': 'Etc/GMT-4',
    'EDT': 'US/Eastern', 'AST': 'Etc/GMT-4',
    'CDT': 'US/Central', 'EST': 'US/Eastern',
    'MDT': 'US/Mountain', 'CST': 'US/Central',
    'PDT': 'US/Pacific', 'MST': 'US/Mountain',
    'AKDT': 'US/Alaska', 'PST': 'US/Pacific',
    'HDT': 'US/Hawaii', 'AKST': 'US/Alaska',
           'HST': 'US/Hawaii',
    'SST': 'Etc/GMT+11',
    'PLT': 'Etc/GMT-5',
    'GSST': 'Etc/GMT-4'
}

offsets = {
 'GMT': 0, 'UTC': 0,
 'CHDT': -8, 'CHST': -9, 'LST': -10,
 'ADT': 3,
 'VDT': 3, 'VST': 4,
 'EDT': 4, 'AST': 4,
 'CDT': 5, 'EST': 5,
 'MDT': 6, 'CST': 6,
 'PDT': 7, 'MST': 7,
 'AKDT': 8, 'PST': 8,
 'HDT': 9, 'AKST': 9,
           'HST': 10,
 'SST': 11,
 'PLT': -5,
 'GSST': -4
}

wfo_dict = {
 "ABQ": {"name": "ALBUQUERQUE", "region": "SR"},
 "ABR": {"name": "ABERDEEN", "region": "CR"},
 "AFC": {"name": "ANCHORAGE", "region": "PR"},
 "AFG": {"name": "FAIRBANKS", "region": "PR"},
 "AJK": {"name": "JUNEAU", "region": "PR"},
 "AKQ": {"name": "WAKEFIELD", "region": "ER"},
 "ALY": {"name": "ALBANY", "region": "ER"},
 "AMA": {"name": "AMARILLO", "region": "SR"},
 "APX": {"name": "GAYLORD", "region": "CR"},
 "ARX": {"name": "LA_CROSSE", "region": "CR"},
 "BGM": {"name": "BINGHAMTON", "region": "ER"},
 "BIS": {"name": "BISMARCK", "region": "CR"},
 "BMX": {"name": "BIRMINGHAM", "region": "SR"},
 "BOI": {"name": "BOISE", "region": "WR"},
 "BOU": {"name": "DENVER", "region": "CR"},
 "BOX": {"name": "TAUNTON", "region": "ER"},
 "BRO": {"name": "BROWNSVILLE", "region": "SR"},
 "BTV": {"name": "BURLINGTON", "region": "ER"},
 "BUF": {"name": "BUFFALO", "region": "ER"},
 "BYZ": {"name": "BILLINGS", "region": "WR"},
 "CAE": {"name": "COLUMBIA", "region": "SR"},
 "CAR": {"name": "CARIBOU", "region": "ER"},
 "CHS": {"name": "CHARLESTON", "region": "SR"},
 "CLE": {"name": "CLEVELAND", "region": "ER"},
 "CRP": {"name": "CORPUS_CHRISTI", "region": "SR"},
 "CTP": {"name": "STATE_COLLEGE", "region": "ER"},
 "CYS": {"name": "CHEYENNE", "region": "CR"},
 "DDC": {"name": "DODGE_CITY", "region": "CR"},
 "DLH": {"name": "DULUTH", "region": "CR"},
 "DMX": {"name": "DES_MOINES", "region": "CR"},
 "DTX": {"name": "DETROIT", "region": "CR"},
 "DVN": {"name": "QUAD_CITIES_IA", "region": "CR"},
 "EAX": {"name": "KANSAS_CITY/PLEASANT_HILL", "region": "CR"},
 "EKA": {"name": "EUREKA", "region": "WR"},
 "EPZ": {"name": "EL_PASO_TX/SANTA_TERESA", "region": "SR"},
 "EWX": {"name": "AUSTIN/SAN_ANTONIO", "region": "SR"},
 "EYW": {"name": "KEY_WEST", "region": "SR"},
 "FFC": {"name": "PEACHTREE_CITY", "region": "SR"},
 "FGF": {"name": "EASTERN_NORTH_DAKOTA", "region": "CR"},
 "FGZ": {"name": "FLAGSTAFF", "region": "WR"},
 "FSD": {"name": "SIOUX_FALLS", "region": "CR"},
 "FWD": {"name": "DALLAS/FORT_WORTH", "region": "SR"},
 "GGW": {"name": "GLASGOW", "region": "WR"},
 "GID": {"name": "HASTINGS", "region": "CR"},
 "GJT": {"name": "GRAND_JUNCTION", "region": "CR"},
 "GLD": {"name": "GOODLAND", "region": "CR"},
 "GRB": {"name": "GREEN_BAY", "region": "CR"},
 "GRR": {"name": "GRAND_RAPIDS", "region": "CR"},
 "GSP": {"name": "GREENVILLE/SPARTANBURG", "region": "ER"},
 "GUM": {"name": "Guam", "region": "SR"},
 "GYX": {"name": "GRAY", "region": "ER"},
 "HFO": {"name": "HONOLULU", "region": "PR"},
 "HGX": {"name": "HOUSTON/GALVESTON", "region": "SR"},
 "HNX": {"name": "SAN_JOAQUIN_VALLEY/HANFORD", "region": "WR"},
 "HUN": {"name": "Huntsville", "region": "SR"},
 "ICT": {"name": "WICHITA", "region": "CR"},
 "ILM": {"name": "WILMINGTON", "region": "ER"},
 "ILN": {"name": "WILMINGTON", "region": "ER"},
 "ILX": {"name": "LINCOLN", "region": "CR"},
 "IND": {"name": "INDIANAPOLIS", "region": "CR"},
 "IWX": {"name": "NORTHERN_INDIANA", "region": "CR"},
 "JAN": {"name": "JACKSON", "region": "SR"},
 "JAX": {"name": "JACKSONVILLE", "region": "SR"},
 "JKL": {"name": "JACKSON", "region": "ER"},
 "JSJ": {"name": "San Juan", "region": "SR"},
 "LBF": {"name": "NORTH_PLATTE", "region": "CR"},
 "LCH": {"name": "LAKE_CHARLES", "region": "SR"},
 "LIX": {"name": "NEW_ORLEANS", "region": "SR"},
 "LKN": {"name": "ELKO", "region": "WR"},
 "LMK": {"name": "LOUISVILLE", "region": "CR"},
 "LOT": {"name": "CHICAGO", "region": "CR"},
 "LOX": {"name": "LOS_ANGELES/OXNARD", "region": "WR"},
 "LSX": {"name": "ST_LOUIS", "region": "CR"},
 "LUB": {"name": "LUBBOCK", "region": "SR"},
 "LWX": {"name": "BALTIMORE_MD/_WASHINGTON_DC", "region": "ER"},
 "LZK": {"name": "LITTLE_ROCK", "region": "SR"},
 "MAF": {"name": "MIDLAND/ODESSA", "region": "SR"},
 "MEG": {"name": "MEMPHIS", "region": "SR"},
 "MFL": {"name": "MIAMI", "region": "SR"},
 "MFR": {"name": "MEDFORD", "region": "WR"},
 "MHX": {"name": "NEWPORT/MOREHEAD_CITY", "region": "ER"},
 "MKX": {"name": "MILWAUKEE/SULLIVAN", "region": "CR"},
 "MLB": {"name": "MELBOURNE", "region": "SR"},
 "MOB": {"name": "MOBILE", "region": "SR"},
 "MPX": {"name": "TWIN_CITIES/CHANHASSEN", "region": "CR"},
 "MQT": {"name": "MARQUETTE", "region": "CR"},
 "MRX": {"name": "MORRISTOWN", "region": "SR"},
 "MSO": {"name": "MISSOULA", "region": "WR"},
 "MTR": {"name": "SAN_FRANCISCO", "region": "WR"},
 "OAX": {"name": "OMAHA/VALLEY", "region": "CR"},
 "OHX": {"name": "NASHVILLE", "region": "SR"},
 "OKX": {"name": "NEW_YORK", "region": "ER"},
 "OTX": {"name": "SPOKANE", "region": "WR"},
 "OUN": {"name": "NORMAN", "region": "SR"},
 "PAH": {"name": "PADUCAH", "region": "CR"},
 "PBZ": {"name": "PITTSBURGH", "region": "ER"},
 "PDT": {"name": "PENDLETON", "region": "WR"},
 "PHI": {"name": "MOUNT_HOLLY", "region": "ER"},
 "PIH": {"name": "POCATELLO/IDAHO_FALLS", "region": "WR"},
 "PQR": {"name": "PORTLAND", "region": "WR"},
 "PSR": {"name": "PHOENIX", "region": "WR"},
 "PUB": {"name": "PUEBLO", "region": "CR"},
 "RAH": {"name": "RALEIGH", "region": "ER"},
 "REV": {"name": "RENO", "region": "WR"},
 "RIW": {"name": "RIVERTON", "region": "WR"},
 "RLX": {"name": "CHARLESTON", "region": "ER"},
 "RNK": {"name": "BLACKSBURG", "region": "ER"},
 "SEW": {"name": "SEATTLE", "region": "WR"},
 "SGF": {"name": "SPRINGFIELD", "region": "CR"},
 "SGX": {"name": "SAN_DIEGO", "region": "WR"},
 "SHV": {"name": "SHREVEPORT", "region": "SR"},
 "SJT": {"name": "SAN_ANGELO", "region": "SR"},
 "SJU": {"name": "SAN_JUAN", "region": "SR"},
 "SLC": {"name": "SALT_LAKE_CITY", "region": "WR"},
 "STO": {"name": "SACRAMENTO", "region": "WR"},
 "TAE": {"name": "TALLAHASSEE", "region": "SR"},
 "TBW": {"name": "TAMPA_BAY_AREA/RUSKIN", "region": "SR"},
 "TFX": {"name": "GREAT_FALLS", "region": "WR"},
 "TOP": {"name": "TOPEKA", "region": "CR"},
 "TSA": {"name": "TULSA", "region": "WR"},
 "TWC": {"name": "TUCSON", "region": "WR"},
 "UNR": {"name": "RAPID_CITY", "region": "CR"},
 "VEF": {"name": "LAS_VEGAS", "region": "WR"},
}

centertext = {
    "SPC": "Storm Prediction Center",
    "WNS": "Storm Prediction Center",
    "NHC": "National Hurricane Center",
    "WNH": "Hydrometeorological Prediction Center",
    "WNO": "NCEP Central Operations",
}

# http://forecast.weather.gov/product_types.php?site=NWS
prodDefinitions = {
    'FFA': 'Areal Flood Watch (FFA)',
    'MWW': 'Marine Weather Warning (MWW)',
    'EWW': 'Extreme Wind Warning (EWW)',
    'CFW': 'Coastal Hazzard Message (CFW)',
    'TOR': 'Tornado Warning (TOR)',
    'SVR': 'Severe Thunderstorm Warning (SVR)',
    'SVS': 'Severe Weather Statement (SVS)',
    'RFD': 'Grassland Fire Danger (RFD)',
    'TWO': 'Tropical Weather Outlook (TWO)',
    'PWO': 'Public Severe Weather Outlook (PWO)',
    'TCM': 'Tropical Storm Forecast (TCM)',
    'TCU': 'Tropical Cyclone Update (TCU)',
    'HLS': 'Hurricane Local Statement (HLS)',
    'NOW': 'Short-term Forecast (NOW)',
    'HWO': 'Hazardous Weather Outlook (HWO)',
    'AFD': 'Area Forecast Discussion (AFD)',
    'AWU': 'Area Weather Update (AWU)',
    'PNS': 'Public Information Statement (PNS)',
    'FFW': 'Flash Flood Warning (FFW)',
    'FLS': 'Flood Advisory (FLS)',
    'FFS': 'Flash Flood Statement (FFS)',
    'FLW': 'Flood Warning (FLW)',
    'ESF': 'Hydrologic Outlook (ESF)',
    'PSH': 'Post Tropical Event Report (PSH)',
    'RER': 'Record Event Report (RER)',
    'FTM': 'Free Text Message (FTM)',
    'ADM': 'Administrative Message (ADM)',
    'CAE': 'Child Abduction Emergency (CAE)',
    'ADR': 'Administrative Message (ADR)',
    'TOE': 'Telephone Outage Emergency (TOE)',
    'LAE': 'Local Area Emergency (LAE)',
    'AVA': 'Avalanche Watch (AVA)',
    'AVW': 'Avalanche Warning (AVW)',
    'CDW': 'Civil Danger Warning (CDW)',
    'CEM': 'Civil Emergency Message (CEM)',
    'EQW': 'Earthquake Warning (EQW)',
    'EVI': 'Evacuation Immediate (EVI)',
    'FRW': 'Fire Warning (FRW)',
    'HMW': 'Hazardous Materials Warning (HMW)',
    'LEW': 'Law Enforcement Warning (LEW)',
    'NMN': 'Network Message Notification (NMN)',
    'NUW': 'Nuclear Power Plant Warning (NUW)',
    'RHW': 'Radiological Hazard Warning (RHW)',
    'SPW': 'Shelter In Place Warning (SPW)',
    'VOW': 'Volcano Warning (VOW)',
    'ZFP': 'Zone Forecast Package (ZFP)',
    'PFM': 'Point Forecast Matrices (PFM)',
    'SFT': 'State Forecast Tabular Product (SFT)',
    'SRF': 'Surf Zone Forecast (SRF)',
    'CWF': 'Coastal Waters Forecast (CWF)',
    'RVS': 'Hydrologic Statement (RVS)',
    'HPA': 'High Pollution Advisory (HPA)',
    'RTP': 'Regional Temperature and Precipitation (RTP)',
    'FWF': 'Fire Weather Planning Forecast (FWF)',
    'DGT': 'Drought Information (DGT)',
    'MWS': 'Marine Weather Statement (MWS)',
    'AQA': 'Air Quality Alert (AQA)',
    'DSA': 'Tropical Disturbance Statement (DSA)',
    'TCE': 'Tropical Cyclone Position Estimate (TCE)',
    'RVF': 'River Forecast (RVF)',
    'RVA': 'Hydrologic Summary (RVA)',
    'EQR': 'Earthquake Report (EQR)',
    'OEP': 'TAF Collaboration Product (OEP)',
    'SIG': 'Convective Sigment (SIG)',
    'VAA': 'Volcanic Ash Advisory (VAA)',
}

# State bounds (buffered by 0.2 degrees)
#
# ! BE CAREFUL WITH ALASKA
#
# with data as (
#    select state_abbr, st_extent(the_geom) as ext from states
#    GROUP by state_abbr)
#
# SELECT '"'||state_abbr||'": ['||
# round((ST_xmin(ext) - 0.2)::numeric, 2) ||', '||
# round((ST_ymin(ext) - 0.2)::numeric, 2) ||', '||
# round((ST_xmax(ext) + 0.2)::numeric, 2) ||', '||
# round((ST_ymax(ext) + 0.2)::numeric, 2) ||'],'
# from data ORDER by state_abbr ASC
#
state_bounds = {
 "AK": [-178.43, 51.39, -129.81, 71.58],
 "AL": [-88.67, 30.02, -84.69, 35.21],
 "AR": [-94.82, 32.80, -89.44, 36.70],
 "AZ": [-115.02, 31.13, -108.85, 37.20],
 "CA": [-124.61, 32.33, -113.93, 42.21],
 "CO": [-109.26, 36.79, -101.84, 41.20],
 "CT": [-73.93, 40.79, -71.59, 42.25],
 "DC": [-77.32, 38.59, -76.71, 39.20],
 "DE": [-75.99, 38.25, -74.85, 40.04],
 "FL": [-87.83, 24.34, -79.83, 31.20],
 "GA": [-85.81, 30.16, -80.64, 35.20],
 "HI": [-160.45, 18.71, -154.61, 22.44],
 "IA": [-96.84, 40.18, -89.94, 43.70],
 "ID": [-117.44, 41.79, -110.84, 49.20],
 "IL": [-91.71, 36.77, -87.30, 42.71],
 "IN": [-88.30, 37.57, -84.58, 41.96],
 "KS": [-102.25, 36.79, -94.39, 40.20],
 "KY": [-89.77, 36.30, -81.76, 39.35],
 "LA": [-94.24, 28.73, -88.62, 33.22],
 "MA": [-73.71, 41.04, -69.73, 43.09],
 "MD": [-79.69, 37.72, -74.85, 39.92],
 "ME": [-71.28, 42.86, -66.75, 47.66],
 "MI": [-90.62, 41.50, -82.22, 48.39],
 "MN": [-97.44, 43.30, -89.28, 49.58],
 "MO": [-95.97, 35.80, -88.90, 40.81],
 "MS": [-91.86, 29.97, -87.90, 35.20],
 "MT": [-116.25, 44.16, -103.84, 49.20],
 "NC": [-84.52, 33.64, -75.26, 36.79],
 "ND": [-104.25, 45.74, -96.35, 49.20],
 "NE": [-104.25, 39.80, -95.11, 43.20],
 "NH": [-72.76, 42.50, -70.51, 45.51],
 "NJ": [-75.76, 38.73, -73.69, 41.56],
 "NM": [-109.25, 31.13, -102.80, 37.20],
 "NV": [-120.21, 34.80, -113.84, 42.20],
 "NY": [-79.96, 40.30, -71.66, 45.22],
 "OH": [-85.02, 38.20, -80.32, 42.18],
 "OK": [-103.20, 33.42, -94.23, 37.20],
 "OR": [-124.77, 41.79, -116.26, 46.44],
 "PA": [-80.72, 39.52, -74.49, 42.47],
 "RI": [-72.09, 40.95, -70.92, 42.22],
 "SC": [-83.55, 31.85, -78.35, 35.42],
 "SD": [-104.26, 42.28, -96.24, 46.15],
 "TN": [-90.51, 34.78, -81.45, 36.88],
 "TX": [-106.85, 25.64, -93.31, 36.70],
 "UT": [-114.25, 36.80, -108.84, 42.20],
 "VA": [-83.88, 36.34, -75.04, 39.67],
 "VT": [-73.64, 42.53, -71.26, 45.22],
 "WA": [-124.93, 45.34, -116.72, 49.20],
 "WI": [-93.09, 42.29, -86.61, 47.20],
 "WV": [-82.84, 37.00, -77.52, 40.84],
 "WY": [-111.26, 40.79, -103.85, 45.21],
}

# WFO bounds
#
# ! BE CAREFUL WITH AFC, CHECK THE BOUNDS!
#
# with data as (
#    select wfo, st_extent(geom) as ext from ugcs
#    GROUP by wfo)
# SELECT '"'||wfo||'": ['||
# round((ST_xmin(ext) - 0.2)::numeric, 2) ||', '||
# round((ST_ymin(ext) - 0.2)::numeric, 2) ||', '||
# round((ST_xmax(ext) + 0.2)::numeric, 2) ||', '||
# round((ST_ymax(ext) + 0.2)::numeric, 2) ||'],'
# from data WHERE length(wfo) = 3 ORDER by wfo ASC;
wfo_bounds = {
 "ABQ": [-109.25, 32.32, -102.80, 37.20],
 "ABR": [-102.20, 43.30, -95.90, 46.22],
 "AFC": [-179.35, 51.02, -139.81, 63.75],
 "AFG": [-172.05, 61.02, -140.80, 71.59],
 "AJK": [-144.10, 54.47, -129.78, 60.87],
 "AKQ": [-78.94, 35.61, -74.85, 38.90],
 "ALY": [-75.42, 41.24, -72.23, 44.32],
 "AMA": [-103.24, 34.55, -99.80, 37.20],
 "APX": [-86.59, 43.61, -82.99, 46.97],
 "ARX": [-93.25, 42.31, -89.40, 45.58],
 "BGM": [-77.95, 40.70, -74.16, 43.81],
 "BIS": [-104.25, 45.74, -97.81, 49.20],
 "BMX": [-88.62, 31.42, -84.69, 34.73],
 "BOI": [-120.14, 41.79, -113.73, 45.47],
 "BOU": [-107.07, 38.32, -101.85, 41.20],
 "BOX": [-73.27, 40.95, -69.73, 43.09],
 "BRO": [-99.65, 25.64, -96.93, 27.56],
 "BTV": [-76.04, 43.02, -71.27, 45.22],
 "BUF": [-79.96, 41.80, -74.91, 44.60],
 "BYZ": [-111.25, 44.36, -103.84, 47.06],
 "CAE": [-82.85, 32.60, -79.58, 35.27],
 "CAR": [-70.52, 43.88, -66.75, 47.66],
 "CHS": [-82.45, 31.09, -79.07, 33.71],
 "CLE": [-84.08, 40.04, -79.41, 42.47],
 "CRP": [-100.41, 27.01, -96.12, 29.30],
 "CTP": [-79.81, 39.52, -75.56, 42.20],
 "CYS": [-108.13, 40.80, -102.41, 43.70],
 "DDC": [-102.24, 36.79, -98.15, 39.33],
 "DLH": [-94.99, 45.18, -89.28, 48.91],
 "DMX": [-95.87, 40.37, -91.86, 43.70],
 "DTX": [-84.81, 41.51, -82.21, 44.27],
 "DVN": [-92.61, 39.99, -88.96, 42.88],
 "EAX": [-95.97, 37.83, -92.09, 40.80],
 "EKA": [-124.62, 38.56, -122.25, 42.20],
 "EPZ": [-109.25, 30.43, -104.65, 33.68],
 "EWX": [-101.96, 28.00, -96.36, 31.23],
 "FFC": [-85.80, 31.58, -81.80, 35.19],
 "FGF": [-100.05, 45.56, -94.21, 49.59],
 "FGZ": [-113.55, 33.28, -108.85, 37.20],
 "FSD": [-99.73, 42.01, -94.65, 44.83],
 "FWD": [-99.32, 30.26, -95.06, 34.19],
 "GGW": [-109.09, 46.34, -103.84, 49.20],
 "GID": [-100.42, 38.93, -97.17, 41.94],
 "GJT": [-111.11, 36.79, -105.98, 41.20],
 "GLD": [-103.37, 38.06, -99.40, 40.64],
 "GRB": [-90.52, 43.59, -86.61, 46.50],
 "GRR": [-86.74, 41.87, -83.93, 44.38],
 "GSP": [-84.24, 33.75, -79.98, 36.49],
 "GUM": [133.92, 5.06, 172.36, 20.75],
 "GYX": [-72.76, 42.50, -68.34, 46.18],
 "HFO": [-160.45, 18.71, -154.61, 22.44],
 "HGX": [-97.16, 28.18, -94.15, 31.79],
 "HNX": [-121.45, 34.59, -117.42, 38.38],
 "HUN": [-88.40, 33.66, -85.31, 35.61],
 "ICT": [-99.24, 36.80, -94.87, 39.42],
 "ILM": [-80.49, 32.92, -77.32, 35.15],
 "ILN": [-85.64, 38.12, -81.96, 41.02],
 "ILX": [-91.11, 38.37, -87.30, 41.43],
 "IND": [-87.96, 38.21, -84.60, 40.94],
 "IWX": [-87.30, 40.11, -83.68, 42.44],
 "JAN": [-92.34, 30.71, -88.05, 34.32],
 "JAX": [-83.51, 28.76, -80.90, 32.17],
 "JKL": [-85.26, 36.38, -81.77, 38.72],
 "KEY": [-83.13, 24.32, -80.06, 25.55],
 "LBF": [-102.99, 40.15, -98.10, 43.20],
 "LCH": [-94.93, 29.13, -90.87, 31.72],
 "LIX": [-92.02, 28.72, -88.19, 31.57],
 "LKN": [-119.53, 37.84, -113.84, 42.20],
 "LMK": [-87.34, 36.41, -83.63, 39.12],
 "LOT": [-89.89, 40.20, -86.73, 42.70],
 "LOX": [-121.55, 32.60, -117.45, 36.00],
 "LSX": [-93.04, 36.85, -88.49, 40.50],
 "LUB": [-103.26, 32.76, -99.79, 34.95],
 "LWX": [-80.01, 37.34, -75.86, 39.92],
 "LZK": [-94.67, 32.96, -90.67, 36.70],
 "MAF": [-105.18, 28.77, -100.46, 33.77],
 "MEG": [-91.61, 33.45, -87.72, 36.83],
 "MFL": [-82.05, 24.92, -79.83, 27.41],
 "MFR": [-124.81, 40.79, -119.16, 44.15],
 "MHX": [-78.40, 34.24, -75.26, 36.43],
 "MKX": [-90.63, 42.29, -87.50, 44.18],
 "MLB": [-82.16, 26.76, -79.88, 29.63],
 "MOB": [-89.54, 30.02, -85.94, 32.51],
 "MPX": [-96.65, 43.30, -90.48, 46.57],
 "MQT": [-90.62, 44.89, -85.04, 48.39],
 "MRX": [-86.07, 34.78, -81.41, 37.40],
 "MSO": [-116.99, 44.03, -111.99, 49.20],
 "MTR": [-123.73, 35.59, -120.01, 39.06],
 "OAX": [-98.51, 39.80, -94.71, 43.08],
 "OHX": [-88.27, 34.79, -84.46, 36.88],
 "OKX": [-74.96, 40.30, -71.59, 41.91],
 "OTX": [-121.38, 45.66, -114.76, 49.20],
 "OUN": [-100.25, 33.20, -95.47, 37.20],
 "PAH": [-91.42, 36.14, -86.57, 38.81],
 "PBZ": [-82.43, 38.76, -78.51, 41.83],
 "PDT": [-122.20, 43.41, -116.26, 47.80],
 "PHI": [-76.64, 38.25, -73.77, 41.56],
 "PIH": [-115.51, 41.79, -110.84, 45.08],
 "PPG": [-171.25, -14.57, -169.22, -10.88],
 "PQR": [-124.36, 43.24, -121.24, 46.99],
 "PSR": [-116.67, 31.84, -109.80, 34.52],
 "PUB": [-107.35, 36.79, -101.84, 39.58],
 "RAH": [-80.72, 34.35, -77.03, 36.74],
 "REV": [-121.53, 37.26, -117.10, 42.20],
 "RIW": [-111.35, 40.80, -105.81, 45.31],
 "RLX": [-83.54, 36.76, -79.15, 40.13],
 "RNK": [-82.12, 35.80, -78.04, 38.47],
 "SEW": [-124.96, 46.18, -120.45, 49.20],
 "SGF": [-95.29, 36.30, -90.82, 38.89],
 "SGX": [-118.31, 32.34, -115.75, 35.02],
 "SHV": [-95.87, 30.83, -91.67, 34.71],
 "SJT": [-102.58, 30.09, -98.21, 33.60],
 "SJU": [-68.15, 17.47, -64.37, 18.72],
 "SLC": [-114.25, 36.80, -109.67, 42.20],
 "STO": [-123.29, 36.93, -119.40, 41.38],
 "TAE": [-86.59, 29.09, -82.68, 32.19],
 "TBW": [-83.37, 26.12, -80.74, 29.79],
 "TFX": [-114.27, 44.16, -108.04, 49.20],
 "TOP": [-98.13, 37.84, -94.86, 40.20],
 "TSA": [-97.26, 33.67, -93.10, 37.20],
 "TWC": [-113.53, 31.13, -108.85, 33.98],
 "UNR": [-106.22, 42.80, -99.33, 46.15],
 "VEF": [-118.99, 33.83, -112.33, 38.88],
}

# state names
# select '"'||state_abbr||'": "'||state_name||'",' from states
# ORDER by state_abbr ASC
state_names = {
 "AK": "Alaska",
 "AL": "Alabama",
 "AR": "Arkansas",
 "AZ": "Arizona",
 "CA": "California",
 "CO": "Colorado",
 "CT": "Connecticut",
 "DC": "District of Columbia",
 "DE": "Delaware",
 "FL": "Florida",
 "GA": "Georgia",
 "HI": "Hawaii",
 "IA": "Iowa",
 "ID": "Idaho",
 "IL": "Illinois",
 "IN": "Indiana",
 "KS": "Kansas",
 "KY": "Kentucky",
 "LA": "Louisiana",
 "MA": "Massachusetts",
 "MD": "Maryland",
 "ME": "Maine",
 "MI": "Michigan",
 "MN": "Minnesota",
 "MO": "Missouri",
 "MS": "Mississippi",
 "MT": "Montana",
 "NC": "North Carolina",
 "ND": "North Dakota",
 "NE": "Nebraska",
 "NH": "New Hampshire",
 "NJ": "New Jersey",
 "NM": "New Mexico",
 "NV": "Nevada",
 "NY": "New York",
 "OH": "Ohio",
 "OK": "Oklahoma",
 "OR": "Oregon",
 "PA": "Pennsylvania",
 "RI": "Rhode Island",
 "SC": "South Carolina",
 "SD": "South Dakota",
 "TN": "Tennessee",
 "TX": "Texas",
 "UT": "Utah",
 "VA": "Virginia",
 "VT": "Vermont",
 "WA": "Washington",
 "WI": "Wisconsin",
 "WV": "West Virginia",
 "WY": "Wyoming",
}
