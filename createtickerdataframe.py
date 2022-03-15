import pickle
import yfinance as yf
import yahoo_fin.stock_info as si
import pandas as pd

filename = 'ticker_shares'

infile = open(filename,'rb')
ticker_shares = pickle.load(infile)
infile.close()

filename = 'tickers'

infile = open(filename,'rb')
tickers = pickle.load(infile)
infile.close()

# ticker_str = ''
#
# for i in tickers[:100]:
#     ticker_str = ticker_str + ' '+ i
#
#data = yf.download(ticker_str, start="2018-01-01", end="2021-01-1", interval='3mo')['Close']

#Some of these tickers from our total list don't have data in earlier years, Russell 1000 is recalculated for every period
#Recalculate Russell 1000 for every period we want to measure,
#if at either the beginning or end date there's a NaN, that ticker is just tossed out and subsituted with the next best






#remove 'None's from both ticker_shares and tickers ||

print(len(ticker_shares.keys()), len(tickers))

for key in list(ticker_shares.keys()):
    if ticker_shares[key] == None:
        del ticker_shares[key]
        tickers.remove(key)

print(len(ticker_shares.keys()), len(tickers))

#trim list to tickers that exist between the period, '16-'18
#calculate market cap for each period

tickers_2018 = tickers

while True:
    remove = ['BSKY', 'DPRO', 'MOLN', 'ASTS', 'SEMR', 'MOHO', 'PEAR', 'FYBR', 'BRLT', 'STEM', 'HIII', 'RCHG', 'ATA', 'VMEO', 'CPAA', 'FACT', 'ADXN', 'VIRI', 'CCV', 'GOEV', 'NRGX', 'GBIO', 'NREF', 'ETTX', 'TRMR', 'APRE', 'OLO', 'INVO', 'PCB', 'GAPA', 'HLLY', 'TKNO', 'AURA', 'ANAC', 'SYTA', 'SLN', 'ADT', 'FTAA', 'AUGX', 'FHS', 'BMBL', 'BRLI', 'AI', 'TRKA', 'MBAC', 'KRON', 'CORS', 'EAC', 'HEPS', 'JXN', 'OXAC', 'WQGA', 'CRON', 'LJAQ', 'ALTG', 'DTRT', 'ABCL', 'INST', 'OPAD', 'MAX', 'BBLN', 'SAMA', 'AIHS', 'ACTD', 'CNVY', 'AUVI', 'LUXA', 'STVN', 'KZR', 'ASLE', 'INAQ', 'CEPU', 'LGVN', 'MCAF', 'AGL', 'NOAC', 'RRBI', 'AHPA', 'ABCM', 'DSP', 'AFYA', 'DRAY', 'DCUE', 'GTBP', 'AKU', 'AMBO', 'CDAY', 'WHD', 'TSPQ', 'PNTM', 'CTAQ', 'LEGN', 'PRVA', 'HAYW', 'FMIV', 'BE', 'ONDS', 'RNXT', 'MIMO', 'UPWK', 'PMGM', 'ZVO', 'RMO', 'PHVS', 'ZY', 'PTRA', 'KAHC', 'SMIH', 'UPST', 'SMAP', 'ETAC', 'ATIP', 'REE', 'XM', 'LEGA', 'AEVA', 'RGC', 'RBLX', 'ASTL', 'DICE', 'BFLY', 'FTRP', 'KRUS', 'VAPO', 'DNAB', 'NVSA', 'CTRM', 'SNSE', 'CNDB', 'ITRM', 'VRT', 'MBINP', 'IREN', 'ACA', 'TXG', 'CNTQ', 'CLAQ', 'TWNI', 'GIIX', 'LOCL', 'ACII', 'EVGO', 'CFB', 'AKRO', 'FINS', 'MAQC', 'IQMD', 'BON', 'PRT', 'XPOA', 'HUT', 'TIGR', 'AFIB', 'EB', 'TWKS', 'GFX', 'EOSE', 'OLMA', 'CRSR', 'TASK', 'EQX', 'LOTZ', 'NRDY', 'MODD', 'SRZN', 'LZ', 'SHPW', 'LGTO', 'MEC', 'BCSF', 'VWE', 'BXRX', 'CING', 'MGTA', 'TUYA', 'CRGY', 'AVAC', 'FST', 'AFAQ', 'DTIL', 'GTX', 'UWMC', 'SPRC', 'CRC', 'AVDX', 'VCNX', 'FUSN', 'GRVI', 'RMM', 'VIEW', 'CBL', 'YALA', 'CND', 'VLYPP', 'MASS', 'CHNG', 'GLBL', 'HTOO', 'GLEE', 'KERN', 'OBNK', 'GATE', 'GHAC', 'AVO', 'NMG', 'APN', 'VTYX', 'SEAT', 'COOL', 'OSCR', 'ARBE', 'GFS', 'ADN', 'HRT', 'TMDX', 'HCTI', 'PUCK', 'BOWL', 'CENQ', 'CFVI', 'GNAC', 'ACT', 'WRAP', 'ADTH', 'AVTE', 'ZWRK', 'VACC', 'RXDX', 'WNW', 'MRVI', 'NSTB', 'TWLV', 'GTEC', 'AKUS', 'DHAC', 'ANEB', 'SI', 'FIXX', 'ARCE', 'BWMX', 'ENVX', 'RNW', 'CCAI', 'MNTV', 'SITM', 'IPVF', 'FOA', 'TERN', 'FWAC', 'DSAC', 'CYXT', 'ELAN', 'ACBA', 'CNM', 'BIGC', 'DNAC', 'SEV', 'JAQC', 'FSEA', 'GAMB', 'BSTZ', 'APLT', 'NN', 'POW', 'NGM', 'RKLY', 'HYRE', 'HIGA', 'VLCN', 'CDAK', 'ALXO', 'FOUN', 'IPVA', 'VSAC', 'OWL', 'NKLA', 'CDRE', 'GSKY', 'TCVA', 'BZ', 'FAMI', 'INCR', 'EGLX', 'HSAQ', 'TGVC', 'LCAP', 'HCNE', 'MNDY', 'FORG', 'PSN', 'AGE', 'ARNC', 'GCMG', 'RNA', 'BIOX', 'SDGR', 'BLTS', 'XYF', 'QTT', 'SDC', 'WALD', 'REZI', 'BTAI', 'VSCO', 'MOVE', 'OSTR', 'IIIV', 'PSTL', 'SMRT', 'BIOT', 'BLZE', 'ASLN', 'THAC', 'TC', 'CLGN', 'GENI', 'LOCC', 'NVST', 'SMFR', 'MKD', 'BLNG', 'AUR', 'BNNR', 'ICCM', 'CISO', 'HUIZ', 'ARBK', 'PROC', 'BQ', 'ADAL', 'SDAC', 'EVOJ', 'NIU', 'NTRB', 'FOUR', 'MSGM', 'LAAA', 'NINE', 'JANX', 'GO', 'LMND', 'SIDU', 'VCTR', 'HCP', 'MPAC', 'PHAR', 'CRWD', 'APP', 'DOYU', 'WEJO', 'VSTA', 'GIPR', 'STNE', 'DOLE', 'AVCO', 'SONM', 'CRTX', 'BASE', 'TSP', 'DNZ', 'AURC', 'KROS', 'IMCR', 'PEPL', 'RPID', 'ACAQ', 'BMEA', 'BGSX', 'OCG', 'MLAI', 'VINE', 'TOST', 'PHIC', 'JUPW', 'EUCR', 'WFRD', 'VRPX', 'ESTC', 'YJ', 'NARI', 'BWMN', 'DNAY', 'RGF', 'XCUR', 'EM', 'BCSA', 'HLTH', 'OMIC', 'EWCZ', 'KVSC', 'BAK', 'STRC', 'NIO', 'GB', 'LUCD', 'INMD', 'NMTC', 'ITRG', 'VNT', 'ARGU', 'MESA', 'SNCE', 'PINS', 'EBET', 'FEMY', 'WBX', 'TEKK', 'WEAV', 'FULC', 'APAC', 'SLGL', 'MYPS', 'ADV', 'NNOX', 'ADOC', 'CNF', 'LTH', 'LSEA', 'ALPA', 'WARR', 'LMAO', 'ATHA', 'CIAN', 'DCRD', 'PACK', 'AGMH', 'BHIL', 'IDBA', 'ACQR', 'YMM', 'ALACW', 'AVIR', 'ANGN', 'BRIV', 'AVHI', 'SJ', 'EQD', 'TRAQ', 'KSI', 'RPTX', 'SBII', 'CMTG', 'STOK', 'COVA', 'TFFP', 'WIMI', 'ROC', 'FREY', 'SBFM', 'VTRU', 'ZEPP', 'WISH', 'CARR', 'CPZ', 'VYGG', 'UPTD', 'BRSP', 'MNTK', 'ENOB', 'ACRO', 'AAN', 'FRHC', 'SPKB', 'LHAA', 'MEG', 'ORCC', 'VLD', 'SLVR', 'SMWB', 'AMR', 'VHAQ', 'RDBX', 'STRO', 'FTVI', 'HYW', 'JRSH', 'PCVX', 'VAXX', 'PYCR', 'CNNB', 'ANPC', 'PATH', 'DT', 'AMPG', 'LNFA', 'SVFC', 'VGII', 'TNYA', 'DH', 'LDHA', 'HCIC', 'SLGG', 'BACA', 'HYPR', 'ALTU', 'RRAC', 'TRIN', 'LPRO', 'TCDA', 'TWST', 'BAFN', 'PNT', 'PSFE', 'WE', 'PPGH', 'WBEV', 'ILPT', 'ZCMD', 'CRKN', 'VFF', 'GRWG', 'NBST', 'TCRR', 'RXRA', 'GRUB', 'ATCX', 'XLO', 'UROY', 'DOMO', 'CANG', 'DPCS', 'TRON', 'MDXH', 'BTTX', 'HUGE', 'XPAX', 'FSBC', 'SOHON', 'RICO', 'ADAG', 'CAAP', 'PRSR', 'JSPR', 'KAII', 'XPEL', 'GSHD', 'CNSP', 'AAC', 'ARYD', 'CVET', 'CFIV', 'NFE', 'TETC', 'IKT', 'LCAA', 'BPTS', 'NEW', 'ADEX', 'THCA', 'IDYA', 'VERY', 'AUUD', 'IS', 'NCAC', 'SGTX', 'IQMDU', 'RADI', 'CVRX', 'VALN']
    for i in tickers_2018[1730:]:
        try:
            print(i, tickers_2018.index(i))
            si.get_data(i,start_date="2018-01-05", end_date="2018-01-06")['close']
        except (AssertionError, KeyError):
            remove.append(i)
    for i in remove:
        tickers_2018.pop(tickers_2018.index(i))
    break


#randomly choose 500 from tickers
#iterate through this list and see if it has a start_date of 2018... with si.get_data
#(if it doesn't) or i

tickers_used = list(set(tickers_2018))

filename = 'tickers_2018'
outfile = open(filename, 'wb')
pickle.dump(tickers, outfile)

outfile.close()

infile = open(filename,'rb')
new_ = pickle.load(infile)
infile.close()



#Russell 1000 function