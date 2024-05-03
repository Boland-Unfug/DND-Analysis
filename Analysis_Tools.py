import pandas as pd

def get_data(name):
    data = pd.read_csv(name, sep=',')
    return data

def drop_sources(data):
#These are the ones that are not official
#'UA2020SubclassesPt2' 'UA2020SubclassesPt5' 'UA2020SpellsAndMagicTattoos', 'UA2021DraconicOptions' 'UA2021MagesOfStrixhaven' 'UA2022GiantOptions', 'UAArtificerRevisited' 'UAClassFeatureVariants' 'UAClericDruidWizard', 'AitFR-ISF' 'AitFR-THP' 'AitFR-DN' 'AitFR-FCD', DoD, HftT, HoL, , IMR, KKW, LLK, MaBJoV, MCV1SC, NRH-TCMC, NRH-AVitW, NRH-ASS, NRH-CoI, NRH-AWoL, NRH-AT, OoW, PSA, PSD, PSI, PSK, PSX, PSZ, RMBRE, RtG, SADS


#These are the ones that are official. Make sure they match these.
# PHB, DMG, MM, VGM, XGE, MTF, TCE, FTD, AI, MPMM, AAG, BAM, BGG, MPP, SatO, BMT, SCAG, GGR, ERLW, EGW, MOT, VRGR, SCC
# BGDIA, CM, CoS, CRCotN, DC, DIP, ESK, GoS, HotDQ, IDRotF, WDMM, WDH, LMoP, LR, MFF, MGELFT
# ootA, PotA, RoT, ToA, SDW, SKT, SLW, TTP, TftYP,WBtW

    data = data[data['source'].isin(['PHB', 'DMG', 'MM', 'VGM', 'XGE', 'MTF', 'TCE', 'FTD', 'AI', 'MPMM', 'AAG', 'BAM', 'BGG', 'MPP', 'SatO', 'BMT', 'SCAG', 'GGR', 'ERLW', 'EGW', 'MOT', 'VRGR', 'SCC', 'BGDIA', 'CM', 'CoS', 'CRCotN', 'DC', 'DIP', 'ESK', 'GoS', 'HotDQ', 'IDRotF', 'WDMM', 'WDH', 'LMoP', 'LR', 'MFF', 'MGELFT', 'ootA', 'PotA', 'RoT', 'ToA', 'SDW', 'SKT', 'SLW', 'TTP', 'TftYP', 'WBtW'])]
    return data
