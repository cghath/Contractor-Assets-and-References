# Loadouts catalogue (ported from tools/loadouts_catalog_wip.pl, ids kept; additions marked).
# weapon id -> name, calibre, class, mag id, rounds per mag, exact game item id or '', default optic or ''
# class: rifle carbine br lmg gpmg dmr sniper amr pistol smg

W_ROWS = [
 # 5.56x45 (WIP)
 ('m4a1','M4A1 carbine','5.56x45mm','carbine','mag_556',30,'m4a1'),
 ('m4','M4 carbine','5.56x45mm','carbine','mag_556',30,''),
 ('mk18','Mk18 CQBR','5.56x45mm','carbine','mag_556',30,'mk18'),
 ('m27_iar','M27 IAR','5.56x45mm','rifle','mag_556',30,''),
 ('m16a1','M16A1','5.56x45mm','rifle','mag_556',30,''),
 ('ar_m1','AR-M1 (Georgian AR-15)','5.56x45mm','carbine','mag_556',30,''),
 ('ef88','EF88 Austeyr','5.56x45mm','rifle','mag_556',30,'','prism4'),
 ('scar_l','FN SCAR-L','5.56x45mm','rifle','mag_556',30,''),
 ('hk416','HK416','5.56x45mm','rifle','mag_556',30,''),
 ('hk416f','HK416 F','5.56x45mm','rifle','mag_556',30,''),
 ('hk416f_short','HK416 F short','5.56x45mm','carbine','mag_556',30,''),
 ('g36','HK G36','5.56x45mm','rifle','mag_556',30,'','g36_dual'),
 ('g36k','HK G36K','5.56x45mm','carbine','mag_556',30,'','g36_dual'),
 ('g36e','HK G36E','5.56x45mm','rifle','mag_556',30,'','g36_dual'),
 ('g95a1','G95A1 (HK416 A8)','5.56x45mm','rifle','mag_556',30,''),
 ('arx160','Beretta ARX160','5.56x45mm','rifle','mag_556',30,''),
 ('c7a2','C7A2 rifle','5.56x45mm','rifle','mag_556',30,'','prism4'),
 ('c8a3','C8A3 carbine','5.56x45mm','carbine','mag_556',30,''),
 ('c7nld','C7NLD rifle','5.56x45mm','rifle','mag_556',30,''),
 ('c8nld','C8NLD carbine','5.56x45mm','carbine','mag_556',30,''),
 ('gevaer_m25','Gevaer M/25 (C8 MRR)','5.56x45mm','carbine','mag_556',30,''),
 ('gevaer_m10','Gevaer M/10 (C8 IUR)','5.56x45mm','carbine','mag_556',30,''),
 ('l85a3','L85A3 (SA80)','5.56x45mm','rifle','mag_556',30,'','prism4'),
 ('l403a1','L403A1 KS-1','5.56x45mm','carbine','mag_556',30,''),
 ('mars_l','MARS-L (LMT CQB16)','5.56x45mm','carbine','mag_556',30,''),
 ('r20_rahe','LMT R-20 Rahe','5.56x45mm','rifle','mag_556',30,''),
 ('ak5c','Ak 5C','5.56x45mm','rifle','mag_556',30,''),
 ('ak24','Ak 24 (Sako ARG)','5.56x45mm','rifle','mag_556',30,''),
 ('msbs_grot','MSBS Grot C16 FB-A2','5.56x45mm','rifle','mag_556',30,''),
 ('msbs_grot_carbine','MSBS Grot carbine','5.56x45mm','carbine','mag_556',30,''),
 ('beryl','FB Beryl wz. 96','5.56x45mm','rifle','mag_556',30,''),
 ('k2c1','Daewoo K2C1','5.56x45mm','rifle','mag_556',30,''),
 ('k1a','Daewoo K1A','5.56x45mm','carbine','mag_556',30,''),
 ('type20_howa','Howa Type 20','5.56x45mm','rifle','mag_556',30,''),
 ('t91','T91','5.56x45mm','rifle','mag_556',30,''),
 ('r4a3','Remington R4A3','5.56x45mm','rifle','mag_556',30,''),
 ('sig516','SIG516 G3','5.56x45mm','rifle','mag_556',30,''),
 ('zastava_m19','Zastava M19','5.56x45mm','rifle','mag_556',30,''),
 ('zastava_m21','Zastava M21','5.56x45mm','rifle','mag_556',30,''),
 ('insas','INSAS rifle','5.56x45mm','rifle','mag_556_20',20,''),          # WIP had mag_556 x20; split per Q8
 ('masaf2','Masaf-2 (Iranian AR-pattern)','5.56x45mm','rifle','mag_556',30,''),
 # 5.56x45 (added)
 ('m16a4','M16A4','5.56x45mm','rifle','mag_556',30,''),
 ('m16a2','M16A2','5.56x45mm','rifle','mag_556',30,''),
 ('car816','Caracal CAR 816','5.56x45mm','carbine','mag_556',30,''),
 ('stg77','StG 77 A1 (Steyr AUG)','5.56x45mm','rifle','mag_556',30,'','aug_15x'),
 ('aug_a3','Steyr AUG A3','5.56x45mm','rifle','mag_556',30,'','aug_15x'),
 ('stgw90','Stgw 90 (SIG SG 550)','5.56x45mm','rifle','mag_556',30,''),
 ('fx05','FX-05 Xiuhcoatl','5.56x45mm','rifle','mag_556',30,''),
 ('mpt55','MKE MPT-55','5.56x45mm','carbine','mag_556',30,''),
 ('tavor_x95','IWI Tavor X95','5.56x45mm','rifle','mag_556',30,''),
 ('micro_tavor','IWI Micro Tavor X95 (short)','5.56x45mm','carbine','mag_556',30,''),
 ('ar15_pattern','AR-15 / M4-pattern rifle (commercial or captured)','5.56x45mm','carbine','mag_556',30,''),
 # 7.62x39 Finnish (WIP)
 ('rk62','RK 62','7.62x39mm','rifle','mag_762x39_30',30,''),
 ('rk95','RK 95 TP','7.62x39mm','rifle','mag_762x39_30',30,''),
 # 6.8x51
 ('m7','M7 rifle (NGSW)','6.8x51mm','rifle','mag_68x51_20',20,'','xm157'),
 ('m250','M250 automatic rifle (NGSW)','6.8x51mm','lmg','belt_68x51_100',100,'','xm157'),
 # 7.62x51 battle rifles
 ('g3a3','HK G3A3','7.62x51mm','br','mag_762',20,''),
 ('g3p4','G3P4 (POF licence G3)','7.62x51mm','br','mag_762',20,''),
 ('g3a6','G3A6 (Iranian licence G3)','7.62x51mm','br','mag_762',20,''),
 ('sig716','SIG716','7.62x51mm','br','mag_762',20,''),
 ('mpt76','MKE MPT-76','7.62x51mm','br','mag_762',20,''),   # added
 ('g3a7','HK G3A7 (MKE licence)','7.62x51mm','br','mag_762',20,''),   # added
 # 5.45x39
 ('ak74m','AK-74M','5.45x39mm','rifle','mag_545x39_30',30,''),
 ('ak12','AK-12','5.45x39mm','rifle','mag_545x39_30',30,''),
 ('ak74','AK-74 / AKS-74','5.45x39mm','rifle','mag_545x39_30',30,''),
 ('aks74u','AKS-74U','5.45x39mm','carbine','mag_545x39_30',30,''),
 ('pa_md86','PA md. 86','5.45x39mm','rifle','mag_545x39_30',30,''),
 ('type88_prk','Type 88 (AK-74 pattern)','5.45x39mm','rifle','mag_545x39_30',30,''),
 # 7.62x39
 ('akm','AKM','7.62x39mm','rifle','mag_762x39_30',30,''),
 ('ak47','AK-47 / Type 56 pattern','7.62x39mm','rifle','mag_762x39_30',30,''),
 ('akms','AKMS (folding stock)','7.62x39mm','carbine','mag_762x39_30',30,''),
 ('ak203','AK-203','7.62x39mm','rifle','mag_762x39_30',30,''),
 ('kl762','KL-7.62 (Iranian AKM)','7.62x39mm','rifle','mag_762x39_30',30,''),
 ('type56','Type 56','7.62x39mm','rifle','mag_762x39_30',30,''),
 ('type58_prk','Type 58 / Type 68 (AK pattern)','7.62x39mm','rifle','mag_762x39_30',30,''),
 ('stv380','STV-380','7.62x39mm','rifle','mag_762x39_30',30,''),
 ('stv215','STV-215','7.62x39mm','carbine','mag_762x39_30',30,''),
 ('zastava_m70','Zastava M70','7.62x39mm','rifle','mag_762x39_30',30,''),
 ('pm_md63','PM md. 63/65','7.62x39mm','rifle','mag_762x39_30',30,''),
 ('ak103','AK-103','7.62x39mm','rifle','mag_762x39_30',30,''),   # added
 ('misr','Misr (Egyptian AKM)','7.62x39mm','rifle','mag_762x39_30',30,''),   # added
 # 5.8x42
 ('qbz191','QBZ-191','5.8x42mm','rifle','mag_58x42_30',30,'','chn_optic'),
 ('qbz191_carbine','QBZ-191 carbine','5.8x42mm','carbine','mag_58x42_30',30,'','chn_optic'),
 ('qbz95_1','QBZ-95-1','5.8x42mm','rifle','mag_58x42_30',30,''),
 # LMGs
 ('m249','M249 SAW','5.56x45mm','lmg','belt_556_200',200,''),
 ('minimi','FN Minimi','5.56x45mm','lmg','belt_556_200',200,''),
 ('minimi_para','FN Minimi Para','5.56x45mm','lmg','belt_556_200',200,''),
 ('f89','F89 Minimi','5.56x45mm','lmg','belt_556_200',200,''),
 ('c9a2','C9A2 LMG','5.56x45mm','lmg','belt_556_200',200,''),
 ('mg4','HK MG4','5.56x45mm','lmg','belt_556_200',200,''),
 ('k15','Daewoo K15','5.56x45mm','lmg','belt_556_200',200,''),
 ('k3','Daewoo K3','5.56x45mm','lmg','belt_556_200',200,''),
 ('t75_saw','T75 SAW','5.56x45mm','lmg','belt_556_200',200,''),
 ('negev','IWI Negev','5.56x45mm','lmg','belt_556_200',200,''),
 ('ultimax','Ultimax 100','5.56x45mm','lmg','drum_556_100',100,''),
 ('insas_lmg','INSAS LMG','5.56x45mm','lmg','mag_556',30,''),
 ('ksp90','Ksp 90 (Minimi)','5.56x45mm','lmg','belt_556_200',200,''),
 ('lmg05','LMg 05 (FN Minimi)','5.56x45mm','lmg','belt_556_200',200,''),   # added
 ('negev_ng5','IWI Negev NG5','5.56x45mm','lmg','belt_556_200',200,''),   # added
 ('rpk74','RPK-74','5.45x39mm','lmg','mag_545x39_45',45,''),
 ('rpk16','RPK-16','5.45x39mm','lmg','mag_545x39_45',45,''),
 ('pm_md93','PM md. 93','5.45x39mm','lmg','mag_545x39_45',45,''),
 ('rpk','RPK','7.62x39mm','lmg','mag_762x39_40',40,''),
 ('kvkk62','KvKK 62','7.62x39mm','lmg','belt_762x39_100',100,''),
 ('zastava_m72','Zastava M72','7.62x39mm','lmg','mag_762x39_40',40,''),
 ('type81_lmg','Type 81 / RPK-pattern LMG','7.62x39mm','lmg','drum_762x39_75',75,''),
 ('qjb201','QJB-201 LMG','5.8x42mm','lmg','belt_58x42_100',100,'','chn_optic'),
 # GPMGs 7.62x51
 ('m240b','M240B/L','7.62x51mm','gpmg','belt_762x51_100',100,''),
 ('mag58','FN MAG 58','7.62x51mm','gpmg','belt_762x51_100',100,''),
 ('l7a2','L7A2 GPMG','7.62x51mm','gpmg','belt_762x51_100',100,''),
 ('c6','C6 FLEX GPMG','7.62x51mm','gpmg','belt_762x51_100',100,''),
 ('mg3','MG3','7.62x51mm','gpmg','belt_762x51_100',100,''),
 ('mga3','MGA3 (Iranian licence MG3)','7.62x51mm','gpmg','belt_762x51_100',100,''),
 ('mg5','HK MG5','7.62x51mm','gpmg','belt_762x51_100',100,''),
 ('m60e6','M/60E6','7.62x51mm','gpmg','belt_762x51_100',100,''),
 ('m60','M60','7.62x51mm','gpmg','belt_762x51_100',100,''),
 ('minimi_762','FN Minimi 7.62 Mk3','7.62x51mm','gpmg','belt_762x51_100',100,''),
 ('negev_ng7','Negev NG7','7.62x51mm','gpmg','belt_762x51_100',100,''),
 ('ukm2000p','UKM-2000P','7.62x51mm','gpmg','belt_762x51_100',100,''),
 ('k12','Daewoo K12','7.62x51mm','gpmg','belt_762x51_100',100,''),
 ('t74','T74 GPMG','7.62x51mm','gpmg','belt_762x51_100',100,''),
 ('ksp58','Ksp 58 (FN MAG)','7.62x51mm','gpmg','belt_762x51_100',100,''),
 ('qjy201','QJY-201 GPMG','7.62x51mm','gpmg','belt_762x51_100',100,''),
 ('mk48','Mk 48','7.62x51mm','gpmg','belt_762x51_100',100,''),   # added
 ('mg74','MG 74 (MG3 family)','7.62x51mm','gpmg','belt_762x51_100',100,''),   # added
 ('pmt76','MKE PMT-76','7.62x51mm','gpmg','belt_762x51_100',100,''),   # added
 ('hk21','HK21','7.62x51mm','gpmg','belt_762x51_100',100,''),   # added
 # GPMGs 7.62x54R
 ('pkm','PKM','7.62x54R','gpmg','belt_762x54r_100',100,''),
 ('pkp','PKP Pecheneg','7.62x54R','gpmg','belt_762x54r_100',100,''),
 ('zastava_m84','Zastava M84','7.62x54R','gpmg','belt_762x54r_100',100,''),
 ('type73_prk','Type 73 / PK-pattern GPMG','7.62x54R','gpmg','belt_762x54r_100',100,''),
 ('md66','Mitraliera md. 66 (PKM pattern)','7.62x54R','gpmg','belt_762x54r_100',100,''),
 ('pkm_irn','PKM (Iranian copy)','7.62x54R','gpmg','belt_762x54r_100',100,''),
 # DMRs
 ('m110','M110 SASS','7.62x51mm','dmr','mag_762',20,'m110','dmr_scope'),
 ('m110a1','M110A1 CSASS','7.62x51mm','dmr','mag_762',20,'','lpvo'),
 ('m38_sdmr','M38 SDMR','5.56x45mm','dmr','mag_556',30,'','lpvo'),
 ('sr25','SR-25 / KAC DMR','7.62x51mm','dmr','mag_762',20,'','dmr_scope'),
 ('c20','C20 DMR','7.62x51mm','dmr','mag_762',20,'','dmr_scope'),
 ('g28','HK G28','7.62x51mm','dmr','mag_762',20,'','dmr_scope'),
 ('scar_h_pr','FN SCAR-H PR','7.62x51mm','dmr','mag_762',20,'','dmr_scope'),
 ('hk417','HK417','7.62x51mm','dmr','mag_762',20,'','dmr_scope'),
 ('arx200','Beretta ARX200','7.62x51mm','dmr','mag_762',20,'','dmr_scope'),
 ('m14_ebr','M14 EBR','7.62x51mm','dmr','mag_762',20,'','dmr_scope'),
 ('l129a1','L129A1 Sharpshooter','7.62x51mm','dmr','mag_762',20,'','dmr_scope'),
 ('mars_h','LMT MARS-H DMW','7.62x51mm','dmr','mag_762',20,'','dmr_scope'),
 ('r20l_rahe','LMT R-20L Rahe','7.62x51mm','dmr','mag_762',20,'','dmr_scope'),
 ('msbs_762n','MSBS-7.62N','7.62x51mm','dmr','mag_762',20,'','dmr_scope'),
 ('galatz','IMI Galatz','7.62x51mm','dmr','mag_762',20,'','dmr_scope'),
 ('sig716_dmr','SIG716 DMR','7.62x51mm','dmr','mag_762',20,'','dmr_scope'),
 ('uar10','UAR-10','7.62x51mm','dmr','mag_762',20,'','dmr_scope'),
 ('g3_dmr','G3 with optic (PSR-90 class)','7.62x51mm','dmr','mag_762',20,'','dmr_scope'),
 ('car817','Caracal CAR 817 DMR','7.62x51mm','dmr','mag_762',20,'','dmr_scope'),   # added
 ('knt76','MKE KNT-76','7.62x51mm','dmr','mag_762',20,'','dmr_scope'),   # added
 ('svd','SVD Dragunov','7.62x54R','dmr','mag_762x54r_10',10,'','pso1'),
 ('svdm','SVDM Dragunov','7.62x54R','dmr','mag_762x54r_10',10,'','pso1'),
 ('svch','SVCh Chukavin','7.62x54R','dmr','mag_762x54r_10',10,'','dmr_scope'),
 ('psl','PSL','7.62x54R','dmr','mag_762x54r_10',10,'','pso1'),
 ('tkiv_svd','TKIV Dragunov','7.62x54R','dmr','mag_762x54r_10',10,'','pso1'),
 ('nakhjir','Nakhjir (Iranian SVD)','7.62x54R','dmr','mag_762x54r_10',10,'','pso1'),
 ('zastava_m76','Zastava M76','7.92x57mm','dmr','mag_792x57_10',10,'','pso1'),
 ('zastava_m91','Zastava M91','7.62x54R','dmr','mag_762x54r_10',10,'','pso1'),
 ('qbu191','QBU-191 DMR','5.8x42mm','dmr','mag_58x42_30',30,'','dmr_scope'),
 ('qbu88','QBU-88','5.8x42mm','dmr','mag_58x42_10',10,'','dmr_scope'),
 ('k14','K14 sniper rifle','7.62x51mm','sniper','mag_762x51_5',5,'','sniper_scope'),
 # sniper / anti-materiel
 ('mk22','Mk 22 MRAD','.300 Norma Magnum','sniper','mag_300nm_5',5,'','sniper_scope'),
 ('m107a1','M107A1','12.7x99mm (.50 BMG)','amr','mag_50bmg_10',10,'','sniper_scope'),
 ('m82a1','Barrett M82A1','12.7x99mm (.50 BMG)','amr','mag_50bmg_10',10,'','sniper_scope'),
 ('m95','Barrett M95','12.7x99mm (.50 BMG)','amr','mag_50bmg_5',5,'','sniper_scope'),
 ('blaser_t2','Blaser Tactical 2','.338 Lapua Magnum','sniper','mag_338lm_5',5,'','sniper_scope'),
 ('ax338','Accuracy International AX338','.338 Lapua Magnum','sniper','mag_338lm_5',5,'','sniper_scope'),
 ('axmc','Accuracy International AXMC','.338 Lapua Magnum','sniper','mag_338lm_5',5,'','sniper_scope'),
 ('awm','Accuracy International AWM','.338 Lapua Magnum','sniper','mag_338lm_5',5,'','sniper_scope'),
 ('l115a3','L115A3 AWM','.338 Lapua Magnum','sniper','mag_338lm_5',5,'','sniper_scope'),
 ('ai_aw','Accuracy International AW','7.62x51mm','sniper','mag_762x51_10',10,'','sniper_scope'),
 ('ax308','Accuracy International AX308','7.62x51mm','sniper','mag_762x51_10',10,'','sniper_scope'),
 ('ax50','Accuracy International AX50','12.7x99mm (.50 BMG)','amr','mag_50bmg_5',5,'','sniper_scope'),
 ('c14','C14 Timberwolf','.338 Lapua Magnum','sniper','mag_338lm_5',5,'','sniper_scope'),
 ('g22','G22','.300 Winchester Magnum','sniper','mag_300wm_5',5,'','sniper_scope'),
 ('g29','G29','.338 Lapua Magnum','sniper','mag_338lm_5',5,'','sniper_scope'),
 ('trg42','Sako TRG-42','.338 Lapua Magnum','sniper','mag_338lm_5',5,'','sniper_scope'),
 ('trg22','Sako TRG-22','7.62x51mm','sniper','mag_762x51_10',10,'','sniper_scope'),
 ('trg_m10','Sako TRG M10','.338 Lapua Magnum','sniper','mag_338lm_5',5,'','sniper_scope'),
 ('tkiv2000','TKIV 2000','.338 Lapua Magnum','sniper','mag_338lm_5',5,'','sniper_scope'),
 ('psg90','Psg 90','7.62x51mm','sniper','mag_762x51_10',10,'','sniper_scope'),
 ('hecate2','PGM Hecate II','12.7x99mm (.50 BMG)','amr','mag_50bmg_7',7,'','sniper_scope'),
 ('ultima_ratio','PGM Ultima Ratio','7.62x51mm','sniper','mag_762x51_10',10,'','sniper_scope'),
 ('mrad_338','Barrett MRAD','.338 Lapua Magnum','sniper','mag_338lm_5',5,'','sniper_scope'),
 ('m24','M24 SWS','7.62x51mm','sniper','mag_762x51_5',5,'','sniper_scope'),
 ('t93','T93','7.62x51mm','sniper','mag_762x51_5',5,'','sniper_scope'),
 ('t5000','Orsis T-5000','.338 Lapua Magnum','sniper','mag_338lm_5',5,'','sniper_scope'),
 ('sv98','SV-98','7.62x54R','sniper','mag_762x54r_10',10,'','sniper_scope'),
 ('asvk','ASVK Kord','12.7x108mm','amr','mag_127x108_5',5,'','sniper_scope'),
 ('osv96','OSV-96','12.7x108mm','amr','mag_127x108_5',5,'','sniper_scope'),
 ('vss','VSS Vintorez','9x39mm','sniper','mag_9x39_20',20,'','pso1'),
 ('istiglal','Istiglal','14.5x114mm','amr','mag_145x114_5',5,'','sniper_scope'),
 ('qbu10','QBU-10','12.7x108mm','amr','mag_127x108_5',5,'','sniper_scope'),
 ('cs_lr4','CS/LR4','7.62x51mm','sniper','mag_762x51_5',5,'','sniper_scope'),
 ('bor','Bor','7.62x51mm','sniper','mag_762x51_10',10,'','sniper_scope'),
 ('zastava_m07','Zastava M07','7.62x51mm','sniper','mag_762x51_10',10,'','sniper_scope'),
 ('zastava_m93','Zastava M93 Black Arrow','12.7x108mm','amr','mag_127x108_5',5,'','sniper_scope'),
 ('am50','AM-50 Sayyad','12.7x99mm (.50 BMG)','amr','mag_50bmg_5',5,'','sniper_scope'),
 ('ssg_steyr','Steyr SSG-class','7.62x51mm','sniper','mag_762x51_5',5,'','sniper_scope'),
 ('fort301','Fort-301','7.62x51mm','sniper','mag_762x51_10',10,'','sniper_scope'),
 ('prk_amr','Locally made 12.7 mm anti-materiel rifle','12.7x108mm','amr','mag_127x108_5',5,'','sniper_scope'),
 # sniper / AMR (added)
 ('csr338','Caracal CSR 338','.338 Lapua Magnum','sniper','mag_338lm_5',5,'','sniper_scope'),
 ('steyr_hs50','Steyr HS .50','12.7x99mm (.50 BMG)','amr','mag_50bmg_5',5,'','sniper_scope'),
 ('ssg08','Steyr SSG 08','.338 Lapua Magnum','sniper','mag_338lm_5',5,'','sniper_scope'),
 ('pg04','PG 04 (Sako TRG-42)','.338 Lapua Magnum','sniper','mag_338lm_5',5,'','sniper_scope'),
 ('bora12','MKE Bora-12 (JNG-90)','7.62x51mm','sniper','mag_762x51_10',10,'','sniper_scope'),
 ('c15','C15 LRSW (McMillan TAC-50)','12.7x99mm (.50 BMG)','amr','mag_50bmg_5',5,'','sniper_scope'),
 ('wilk','WKW Wilk','12.7x99mm (.50 BMG)','amr','mag_50bmg_7',7,'','sniper_scope'),
 ('alligator','Snipex Alligator','14.5x114mm','amr','mag_145x114_5',5,'','sniper_scope'),
 ('al_ghoul','Al-Ghoul (locally made 14.5 mm rifle)','14.5x114mm','amr','mag_145x114_5',5,'','sniper_scope'),
 # pistols / SMG
 ('m18','M18 MHS','9x19mm','pistol','mag_9mm',17,''),
 ('m17','M17 MHS','9x19mm','pistol','mag_9mm',17,'m17'),
 ('glock17','Glock 17','9x19mm','pistol','mag_9mm',17,''),
 ('glock19','Glock 19','9x19mm','pistol','mag_9mm',15,''),
 ('p320','SIG Sauer P320','9x19mm','pistol','mag_9mm',17,''),
 ('usp','HK USP','9x19mm','pistol','mag_9mm',15,''),
 ('p8','HK P8','9x19mm','pistol','mag_9mm',15,''),
 ('five_seven','FN Five-seveN Mk2','5.7x28mm','pistol','mag_57x28_20',20,''),
 ('pm_makarov','PM Makarov','9x18mm','pistol','mag_9x18_8',8,''),
 ('grach','MP-443 Grach','9x19mm','pistol','mag_9mm',17,''),
 ('qsz92','QSZ-92','9x19mm','pistol','mag_9mm',15,''),
 ('beretta92','Beretta 92FS','9x19mm','pistol','mag_9mm',15,''),
 ('k5','Daewoo K5','9x19mm','pistol','mag_9mm',13,''),
 ('t75_pistol','T75 pistol','9x19mm','pistol','mag_9mm',15,''),
 ('m1911','M1911','.45 ACP','pistol','mag_45acp_7',7,''),
 ('sfp9','HK SFP9','9x19mm','pistol','mag_9mm',15,''),
 ('vis100','FB VIS 100','9x19mm','pistol','mag_9mm',15,''),
 ('cz75','CZ 75','9x19mm','pistol','mag_9mm',16,''),
 ('cz99','CZ 99','9x19mm','pistol','mag_9mm',15,''),
 ('tt33','TT-33 / Type 68 / K54 (Tokarev pattern)','7.62x25mm','pistol','mag_762x25_8',8,''),
 ('pc9_zoaf','ZOAF PC-9','9x19mm','pistol','mag_9mm',13,''),
 ('pistol_2000','Pistol model 2000','9x19mm','pistol','mag_9mm',15,''),
 ('fort14','Fort-14 / Fort-17','9x18mm','pistol','mag_9x18_12',12,''),
 ('mp7','HK MP7','4.6x30mm','smg','mag_46x30_40',40,''),
 # pistols (added)
 ('caracal_f','Caracal F / Enhanced F','9x19mm','pistol','mag_9mm',18,''),
 ('pist75','Pist 75 (SIG P220)','9x19mm','pistol','mag_9mm',9,''),
 ('helwan','Helwan (Beretta M1951 licence)','9x19mm','pistol','mag_9mm',8,''),
 ('canik_tp9','Canik TP9','9x19mm','pistol','mag_9mm',18,''),
 ('jericho941','IWI Jericho 941','9x19mm','pistol','mag_9mm',16,''),
 ('p226','SIG Sauer P226','9x19mm','pistol','mag_9mm',15,''),
 ('pl15','PL-15','9x19mm','pistol','mag_9mm',16,''),
 ('baekdusan','Baekdusan (CZ 75 copy)','9x19mm','pistol','mag_9mm',15,''),
]
# Dropped from the WIP list: m110_sniper (duplicate of m110; snipers that used it point at m110).

WEAPONS = {}
for r in W_ROWS:
    wid, name, cal, cls, mag, rnd, game = r[:7]
    WEAPONS[wid] = dict(name=name, calibre=cal, cls=cls, mag=mag, rounds=rnd, game=game, optic=(r[7] if len(r) > 7 else ''))

# underbarrel / grenade launchers: id -> name, calibre, ammo item  (WIP %GL plus t40, gl40_che)
UGL = {
 'm320': ('M320A1','40x46mm','gl_40x46_he'), 'm203': ('M203','40x46mm','gl_40x46_he'), 'l123': ('L123 UGL','40x46mm','gl_40x46_he'),
 'ag36': ('AG36 / AG40','40x46mm','gl_40x46_he'), 'hk269': ('HK269 F','40x46mm','gl_40x46_he'), 'fn40gl': ('FN40GL','40x46mm','gl_40x46_he'),
 'glx160': ('GLX-160','40x46mm','gl_40x46_he'), 'sl40': ('SL40','40x46mm','gl_40x46_he'), 'gg18': ('Gg 18','40x46mm','gl_40x46_he'),
 'grk_m13': ('GRK M/13','40x46mm','gl_40x46_he'), 'k201': ('K201','40x46mm','gl_40x46_he'), 't85': ('T85','40x46mm','gl_40x46_he'),
 'gsbo40': ('GSBO-40','40x46mm','gl_40x46_he'), 'ugl40': ('40 mm underbarrel launcher','40x46mm','gl_40x46_he'),
 't40': ('MKE T-40','40x46mm','gl_40x46_he'), 'gl40_che': ('GL 40 (Gw 97)','40x46mm','gl_40x46_he'),
 'gp25': ('GP-25 / GP-30','40mm VOG-25 (caseless)','gl_vog25'), 'gp34': ('GP-34','40mm VOG-25 (caseless)','gl_vog25'),
 'ag40_rou': ('AG-40','40mm VOG-25 (caseless)','gl_vog25'), 'gp25_irn': ('GP-25-type (Iranian)','40mm VOG-25 (caseless)','gl_vog25'),
 'qlg10': ('35 mm underbarrel launcher (QLG-10 class)','35x32mm','gl_35mm_he'),
 'type06': ('Type 06 rifle grenade','rifle grenade (22mm muzzle)','rifle_grenade_type06'),
}
UGL_AMMO = {
 'gl_40x46_he': ('40x46mm HEDP grenade (M433 class)', '40x46mm'),
 'gl_40x46_smoke': ('40x46mm white smoke grenade (M714 class)', '40x46mm'),
 'gl_vog25': ('VOG-25 40mm caseless HE grenade', '40mm VOG-25'),
 'gl_35mm_he': ('35x32mm HE grenade (QLG-10)', '35x32mm'),
 'rifle_grenade_type06': ('Type 06 rifle grenade (HEDP)', 'rifle grenade'),
}

# optics: id -> name (WIP %O plus g36_dual, aug_15x, xm157)
OPTICS = {
 'iron': 'Iron sights', 'red_dot': 'Red dot (Aimpoint CompM4/CompM5 class)', 'red_dot_magnifier': 'Red dot + 3x magnifier',
 'holo': 'Holographic sight (EOTech class)', 'prism4': '4x prism (ACOG / ELCAN SpecterDR / SUSAT class)', 'lpvo': '1-6x / 1-8x LPVO',
 'dmr_scope': '3-18x DMR scope', 'sniper_scope': '5-25x sniper scope', 'collimator': 'Collimator (Kobra / 1P87 / EKP-8 class)',
 'pso1': 'PSO-1 4x scope', 'chn_optic': 'Chinese 3x prism / red dot (QMK-class)',
 'g36_dual': 'G36 integrated 3x scope with reflex sight', 'aug_15x': 'AUG integrated 1.5x scope',
 'xm157': 'XM157 fire control (NGSW, 1-8x with laser rangefinder)',
}

# launchers: id -> real name, game launcher name or '', rounds list [(round name, type, count)], substitute, kind
RPG_R = [('PG-7V','HEAT',2), ('OG-7V','frag',1)]
DISP = lambda n: [(n, 'HEAT', 1)]
LAUNCHERS = {
 'at4': ('M136 AT4 (84mm)','AT4',DISP('M136 HEAT'),'','disposable'),
 'at4cs': ('AT4 CS (84mm)','AT4',DISP('AT4 CS HEAT'),'','disposable'),
 'ilaw': ('L2A1 ILAW (AT4 CS)','AT4',DISP('AT4 CS HEAT'),'','disposable'),
 'pskott86': ('Pskott 86 (AT4)','AT4',DISP('AT4 HEAT'),'','disposable'),
 'maaws': ('M3E1 MAAWS (84mm)','MAAWS',[('FFV551 HEAT','HEAT',1),('FFV441D HE','HE',1)],'','recoilless'),
 'cg_m2': ('Carl Gustaf M2 (84mm)','MAAWS',[('FFV551 HEAT','HEAT',1),('FFV441D HE','HE',1)],'','recoilless'),
 'cg_m3': ('Carl Gustaf M3 (84mm)','MAAWS',[('FFV551 HEAT','HEAT',1),('FFV441D HE','HE',1)],'','recoilless'),
 'cg_m4': ('Carl Gustaf M4 (84mm)','MAAWS',[('FFV551 HEAT','HEAT',1),('FFV441D HE','HE',1)],'','recoilless'),
 'grg86': ('Grg m/86 (Carl Gustaf M3)','MAAWS',[('FFV551 HEAT','HEAT',1),('FFV441D HE','HE',1)],'','recoilless'),
 'par6679': ('PAR 66/79 (Carl Gustaf family, 84mm)','MAAWS',[('FFV551 HEAT','HEAT',1),('FFV441D HE','HE',1)],'','recoilless'),
 'smaw': ('Mk 153 SMAW (83mm)','SMAW',[('Mk 6 HEAA','HEAT',1),('Mk 3 HEDP','HEDP',1)],'','rocket'),
 'nlaw': ('NLAW','NLAW',DISP('NLAW HEAT (overfly top attack)'),'','disposable'),
 'rb57': ('Rb 57 (NLAW)','NLAW',DISP('NLAW HEAT (overfly top attack)'),'','disposable'),
 'javelin': ('FGM-148 Javelin','Javelin',[('FGM-148 missile (tandem HEAT, top attack)','tandem HEAT',1)],'','atgm'),
 'rpg7': ('RPG-7','RPG-7',RPG_R,'','rocket'), 'rpg7v2': ('RPG-7V2','RPG-7',RPG_R,'','rocket'),
 'rpg7_irn': ('RPG-7 (Iranian copy)','RPG-7',RPG_R,'','rocket'), 'ag7': ('AG-7 (Romanian RPG-7)','RPG-7',RPG_R,'','rocket'),
 'b41': ('B41 (Vietnamese RPG-7)','RPG-7',RPG_R,'','rocket'), 'rpg7_prk': ('RPG-7 copy (DPRK)','RPG-7',RPG_R,'','rocket'),
 'rpg7_copy': ('RPG-7 copy','RPG-7',RPG_R,'','rocket'),
 'm72': ('M72 LAW (66mm)','',DISP('66mm HEAT'),'AT4','disposable'),
 'rpg26': ('RPG-26 Aglen (72.5mm)','',DISP('72.5mm HEAT'),'AT4','disposable'),
 'rpg22': ('RPG-22 Netto (72.5mm)','',DISP('72.5mm HEAT'),'AT4','disposable'),
 'rpg18': ('RPG-18 (64mm)','',DISP('64mm HEAT'),'AT4','disposable'),
 'zolja': ('M80 Zolja (64mm)','',DISP('64mm HEAT'),'AT4','disposable'),
 'osa': ('M79 Osa (90mm)','',[('90mm HEAT','HEAT',2)],'MAAWS','rocket'),
 'pzf3': ('Panzerfaust 3 (110mm)','',[('PzF 3-IT600 tandem HEAT','tandem HEAT',1)],'MAAWS','rocket'),
 'rgw90': ('RGW 90 (90mm)','',[('RGW 90 HH (HEAT/HE)','HEDP',1)],'AT4','disposable'),
 'c90': ('Instalaza C90 (90mm)','',DISP('C90-CR-AM HEAT'),'AT4','disposable'),
 'c100': ('Instalaza C100 Alcotan (100mm)','',[('100mm HEAT','HEAT',1)],'MAAWS','rocket'),
 'pf98': ('PF-98 (120mm)','',[('120mm HEAT','HEAT',1),('120mm HE','HE',1)],'MAAWS','rocket'),
 'pf89': ('PF-89 (80mm)','',DISP('80mm HEAT'),'AT4','disposable'),
 'apilas': ('APILAS (112mm)','',DISP('112mm HEAT'),'AT4','disposable'),
 'kestrel': ('Kestrel (66mm)','',DISP('66mm HEAT'),'AT4','disposable'),
 'm67rr': ('M67 recoilless rifle (90mm)','',[('90mm HEAT','HEAT',2)],'MAAWS','recoilless'),
 'rpg29': ('RPG-29 Vampir (105mm)','',[('PG-29V tandem HEAT','tandem HEAT',2)],'RPG-7','rocket'),
 'rpo_a': ('RPO-A Shmel (93mm thermobaric)','',[('93mm thermobaric','thermobaric',1)],'AT4','thermobaric'),
 'rpg32': ('RPG-32 Hashim (105mm)','',[('105mm tandem HEAT','tandem HEAT',2)],'RPG-7','rocket'),
 'rpg30': ('RPG-30 Kryuk (105mm)','',DISP('105mm tandem HEAT (with decoy)'),'AT4','disposable'),
 'spg9': ('SPG-9 recoilless (73mm)','',[('PG-9 HEAT','HEAT',4)],'MAAWS','recoilless'),
 # added
 'rshg2': ('RShG-2 (72.5mm thermobaric)','',[('72.5mm thermobaric','thermobaric',1)],'AT4','thermobaric'),
 'matador': ('MATADOR (RGW 90 family, 90mm)','',[('90mm HEAT/HESH dual mode','HEDP',1)],'AT4','disposable'),
 'har66': ('HAR-66 (66mm, M72 type)','',DISP('66mm HEAT'),'AT4','disposable'),
 # team ATGM / MANPADS (team_weapons only)
 'spike_lr': ('Spike LR / LR2 ATGM','',[('missile','tandem HEAT',1)],'Javelin','atgm'), 'spike_sr': ('Spike SR','',[('missile','tandem HEAT',1)],'NLAW','atgm'),
 'spike_mr': ('Spike MR ATGM','',[('missile','tandem HEAT',1)],'Javelin','atgm'), 'kornet': ('9M133 Kornet ATGM','',[('missile','tandem HEAT',1)],'Javelin','atgm'),
 'konkurs': ('9M113 Konkurs ATGM','',[('missile','tandem HEAT',1)],'Javelin','atgm'), 'fagot': ('9K111 Fagot ATGM','',[('missile','HEAT',1)],'Javelin','atgm'),
 'metis': ('9K115-2 Metis-M ATGM','',[('missile','tandem HEAT',1)],'Javelin','atgm'), 'hj12': ('HJ-12 ATGM','',[('missile','tandem HEAT',1)],'Javelin','atgm'),
 'hj8': ('Baktar-Shikan (HJ-8) ATGM','',[('missile','HEAT',1)],'Javelin','atgm'), 'lmat': ('Type 01 LMAT','',[('missile','HEAT',1)],'Javelin','atgm'),
 'raybolt': ('Hyungung (Raybolt) ATGM','',[('missile','tandem HEAT',1)],'Javelin','atgm'), 'akeron': ('Akeron MP ATGM','',[('missile','tandem HEAT',1)],'Javelin','atgm'),
 'mells': ('MELLS (Spike LR) ATGM','',[('missile','tandem HEAT',1)],'Javelin','atgm'), 'stugna': ('Stugna-P ATGM','',[('missile','tandem HEAT',1)],'Javelin','atgm'),
 'toophan': ('Toophan (TOW copy) ATGM','',[('missile','HEAT',1)],'Javelin','atgm'), 'dehlavieh': ('Dehlavieh (Kornet copy) ATGM','',[('missile','tandem HEAT',1)],'Javelin','atgm'),
 'skif': ('Skif ATGM','',[('missile','tandem HEAT',1)],'Javelin','atgm'), 'bulsae': ('Bulsae-2/3 ATGM','',[('missile','HEAT',1)],'Javelin','atgm'),
 'mpatgm': ('MPATGM','',[('missile','tandem HEAT',1)],'Javelin','atgm'), 'tow': ('BGM-71 TOW','',[('missile','tandem HEAT',1)],'Javelin','atgm'),
 'shershen': ('Shershen ATGM','',[('missile','tandem HEAT',1)],'Javelin','atgm'),
 'milan': ('MILAN ATGM','',[('missile','tandem HEAT',1)],'Javelin','atgm'), 'bill2': ('PAL 2000 BB (BILL 2) ATGM','',[('missile','top attack',1)],'Javelin','atgm'),
 'saeghe': ('Saeghe (Dragon copy) ATGM','',[('missile','HEAT',1)],'Javelin','atgm'), 'almas': ('Almas (Iranian Spike-type) ATGM','',[('missile','tandem HEAT',1)],'Javelin','atgm'),
 'karaok': ('Roketsan KARAOK ATGM','',[('missile','tandem HEAT',1)],'NLAW','atgm'), 'omtas': ('Roketsan OMTAS ATGM','',[('missile','tandem HEAT',1)],'Javelin','atgm'),
 'eryx': ('Eryx ATGM','',[('missile','tandem HEAT',1)],'NLAW','atgm'), 'nag': ('Nag-family ATGM','',[('missile','tandem HEAT',1)],'Javelin','atgm'),
 'igla': ('9K38 Igla MANPADS','',[('missile','SAM',1)],'','manpads'), 'verba': ('9K333 Verba MANPADS','',[('missile','SAM',1)],'','manpads'),
 'stinger': ('FIM-92 Stinger MANPADS','',[('missile','SAM',1)],'','manpads'), 'piorun': ('Piorun MANPADS','',[('missile','SAM',1)],'','manpads'),
 'misagh': ('Misagh-2/3 MANPADS','',[('missile','SAM',1)],'','manpads'), 'mistral': ('Mistral MANPADS','',[('missile','SAM',1)],'','manpads'),
 'rbs70': ('RBS 70 MANPADS','',[('missile','SAM',1)],'','manpads'), 'strela': ('9K32 Strela-2 / 9K34 Strela-3 MANPADS','',[('missile','SAM',1)],'','manpads'),
 'm40rr': ('M40 106mm recoilless rifle (vehicle)','',[('106mm HEAT','HEAT',1)],'','recoilless'),
}
GAME_LAUNCHERS = ['AT4', 'RPG-7', 'Javelin', 'MAAWS', 'NLAW', 'SMAW']
# proposed items.json ids for the six design-doc launchers (none exist in items.json yet)
GAME_LAUNCHER_IDS = {'AT4': 'at4', 'RPG-7': 'rpg7', 'Javelin': 'javelin', 'MAAWS': 'maaws', 'NLAW': 'nlaw', 'SMAW': 'smaw'}

# magazines and belts: id -> (name, calibre, kind, rounds)
MAGS = {
 'mag_556': ('5.56x45mm 30-round magazine (STANAG / AUG / national)', '5.56x45mm', 'mag', 30),
 'mag_556_20': ('5.56x45mm 20-round magazine (INSAS)', '5.56x45mm', 'mag', 20),
 'belt_556_200': ('5.56x45mm 200-round belt (box or soft pouch)', '5.56x45mm', 'belt', 200),
 'drum_556_100': ('5.56x45mm 100-round drum (Ultimax)', '5.56x45mm', 'drum', 100),
 'mag_68x51_20': ('6.8x51mm 20-round magazine', '6.8x51mm', 'mag', 20),
 'belt_68x51_100': ('6.8x51mm 100-round belt', '6.8x51mm', 'belt', 100),
 'mag_762': ('7.62x51mm 20-round magazine', '7.62x51mm', 'mag', 20),
 'mag_762x51_5': ('7.62x51mm 5-round magazine', '7.62x51mm', 'mag', 5),
 'mag_762x51_10': ('7.62x51mm 10-round magazine', '7.62x51mm', 'mag', 10),
 'belt_762x51_100': ('7.62x51mm 100-round belt', '7.62x51mm', 'belt', 100),
 'mag_545x39_30': ('5.45x39mm 30-round magazine', '5.45x39mm', 'mag', 30),
 'mag_545x39_45': ('5.45x39mm 45-round magazine (RPK-74)', '5.45x39mm', 'mag', 45),
 'mag_762x39_30': ('7.62x39mm 30-round magazine', '7.62x39mm', 'mag', 30),
 'mag_762x39_40': ('7.62x39mm 40-round magazine (RPK)', '7.62x39mm', 'mag', 40),
 'drum_762x39_75': ('7.62x39mm 75-round drum', '7.62x39mm', 'drum', 75),
 'belt_762x39_100': ('7.62x39mm 100-round belt (KvKK 62)', '7.62x39mm', 'belt', 100),
 'belt_762x54r_100': ('7.62x54R 100-round belt (box)', '7.62x54R', 'belt', 100),
 'mag_762x54r_10': ('7.62x54R 10-round magazine', '7.62x54R', 'mag', 10),
 'mag_58x42_30': ('5.8x42mm 30-round magazine', '5.8x42mm', 'mag', 30),
 'mag_58x42_10': ('5.8x42mm 10-round magazine', '5.8x42mm', 'mag', 10),
 'belt_58x42_100': ('5.8x42mm 100-round belt', '5.8x42mm', 'belt', 100),
 'mag_792x57_10': ('7.92x57mm 10-round magazine', '7.92x57mm', 'mag', 10),
 'mag_300nm_5': ('.300 Norma Magnum 5-round magazine', '.300 Norma Magnum', 'mag', 5),
 'mag_300wm_5': ('.300 Winchester Magnum 5-round magazine', '.300 Winchester Magnum', 'mag', 5),
 'mag_338lm_5': ('.338 Lapua Magnum 5-round magazine', '.338 Lapua Magnum', 'mag', 5),
 'mag_50bmg_5': ('12.7x99mm 5-round magazine', '12.7x99mm (.50 BMG)', 'mag', 5),
 'mag_50bmg_7': ('12.7x99mm 7-round magazine', '12.7x99mm (.50 BMG)', 'mag', 7),
 'mag_50bmg_10': ('12.7x99mm 10-round magazine', '12.7x99mm (.50 BMG)', 'mag', 10),
 'mag_127x108_5': ('12.7x108mm 5-round magazine', '12.7x108mm', 'mag', 5),
 'mag_145x114_5': ('14.5x114mm 5-round magazine', '14.5x114mm', 'mag', 5),
 'mag_9x39_20': ('9x39mm 20-round magazine', '9x39mm', 'mag', 20),
 'mag_9mm': ('9x19mm pistol magazine', '9x19mm', 'mag', 17),
 'mag_57x28_20': ('5.7x28mm 20-round magazine', '5.7x28mm', 'mag', 20),
 'mag_9x18_8': ('9x18mm 8-round magazine (PM)', '9x18mm', 'mag', 8),
 'mag_9x18_12': ('9x18mm 12-round magazine (Fort)', '9x18mm', 'mag', 12),
 'mag_45acp_7': ('.45 ACP 7-round magazine', '.45 ACP', 'mag', 7),
 'mag_762x25_8': ('7.62x25mm 8-round magazine', '7.62x25mm', 'mag', 8),
 'mag_46x30_40': ('4.6x30mm 40-round magazine', '4.6x30mm', 'mag', 40),
}

# Round designations by ammo family and calibre: (designation, game round id or None, match 'exact'|'generic'|None)
ROUNDS = {
 'default': {
  '5.56x45mm': ('5.56x45mm SS109 / M855 (NATO ball)', '556_m855', 'generic'),
  '6.8x51mm': ('6.8x51mm Common Cartridge, XM1186 general purpose', None, None),
  '7.62x51mm': ('7.62x51mm M80 / NATO ball', '762x51_m80', 'exact'),
  '5.45x39mm': ('5.45x39mm 7N6M (steel core)', None, None),
  '7.62x39mm': ('7.62x39mm 57-N-231 PS (mild steel core)', '762x39_msc', 'exact'),
  '7.62x54R': ('7.62x54R 57-N-323S LPS (steel core)', '762x54r_lps', 'exact'),
  '5.8x42mm': ('5.8x42mm DBP10', None, None),
  '7.92x57mm': ('7.92x57mm M49 ball', None, None),
  '.300 Norma Magnum': ('.300 Norma Magnum match', None, None),
  '.300 Winchester Magnum': ('.300 Winchester Magnum match (Mk 248 class)', None, None),
  '.338 Lapua Magnum': ('.338 Lapua Magnum ball / match', None, None),
  '12.7x99mm (.50 BMG)': ('12.7x99mm M33 ball', '50bmg_m33', 'exact'),
  '12.7x108mm': ('12.7x108mm B-32 API', None, None),
  '14.5x114mm': ('14.5x114mm B-32 API', None, None),
  '9x39mm': ('9x39mm SP-5 / SP-6', None, None),
  '9x19mm': ('9x19mm FMJ (NATO ball)', '9x19_fmj', 'exact'),
  '5.7x28mm': ('5.7x28mm SS190', None, None),
  '9x18mm': ('9x18mm 57-N-181S', None, None),
  '.45 ACP': ('.45 ACP M1911 ball', '45acp_fmj', 'exact'),
  '7.62x25mm': ('7.62x25mm 57-N-134S', None, None),
  '4.6x30mm': ('4.6x30mm DM11', None, None),
 },
 'us': {
  '5.56x45mm': ('5.56x45mm M855A1 EPR', '556_m855', 'generic'),
  '7.62x51mm': ('7.62x51mm M80A1 EPR', '762x51_m80', 'generic'),
  '9x19mm': ('9x19mm M1152 ball', '9x19_fmj', 'exact'),
  '.300 Norma Magnum': ('.300 Norma Magnum Mk 22 match', None, None),
 },
 'rus': {
  '5.45x39mm': ('5.45x39mm 7N10 (enhanced penetration)', None, None),
  '7.62x54R': ('7.62x54R 7N13 (steel core), 7N1 for the SVD', '762x54r_lps', 'generic'),
 },
 'chn': {
  '7.62x51mm': ('7.62x51mm (Chinese DVC12-class ball)', '762x51_m80', 'generic'),
  '12.7x108mm': ('12.7x108mm Chinese API (Type 54-class)', None, None),
  '9x19mm': ('9x19mm DAP92-9 (Chinese)', '9x19_fmj', 'generic'),
 },
}

# grenades: id -> (name, kind)  kind: frag smoke_white smoke_green smoke_red smoke_violet flash
GRENADES = {
 'm67': ('M67 fragmentation grenade', 'frag'), 'c13': ('C13 fragmentation grenade (M67 pattern)', 'frag'),
 'l109a2': ('L109A2 fragmentation grenade', 'frag'), 'dm51a2': ('DM51A2 hand grenade', 'frag'),
 'hg85': ('HG 85 (Handgranate 85)', 'frag'), 'rgd5': ('RGD-5 fragmentation grenade', 'frag'), 'f1': ('F-1 fragmentation grenade', 'frag'),
 'rgn': ('RGN fragmentation grenade', 'frag'), 'type82_2': ('Type 82-2 fragmentation grenade', 'frag'),
 'm75_srb': ('M75 hand grenade', 'frag'), 'k400': ('K400 fragmentation grenade', 'frag'),
 'frag_nato': ('Fragmentation grenade, national issue (M67 / DM51 / HG 85 class)', 'frag'),
 'frag_copy': ('Locally made or copied fragmentation grenade (RGD-5 / M67 pattern)', 'frag'),
 'an_m8': ('AN-M8 HC white smoke', 'smoke_white'), 'm18_green': ('M18 green signal smoke', 'smoke_green'),
 'm18_red': ('M18 red signal smoke', 'smoke_red'), 'm18_violet': ('M18 violet signal smoke', 'smoke_violet'),
 'rdg2b': ('RDG-2B white smoke', 'smoke_white'),
 'smoke_white_nato': ('White screening smoke, national issue (L83 / DM25 class)', 'smoke_white'),
 'signal_green': ('Green signal smoke, national issue', 'smoke_green'), 'signal_red': ('Red signal smoke, national issue', 'smoke_red'),
 'signal_violet': ('Violet signal smoke, national issue', 'smoke_violet'),
 'm84': ('M84 stun grenade', 'flash'), 'stun_nato': ('Stun grenade, national issue (M84 class)', 'flash'),
}
GRENADE_GAME = {'frag': 'frag_grenade', 'smoke_white': 'smoke_grenade', 'flash': 'flashbang',
                'smoke_green': 'smoke_green', 'smoke_violet': 'smoke_purple'}
# proposed new game ids for signal smoke (Q7); game_substitute smoke_grenade
# green and violet signal smoke exist in the game (smoke_green, smoke_purple); red doesn't yet
GRENADE_NEW = {'smoke_red': 'smoke_red'}

# ARMOR -------------------------------------------------------------------
# helmets: id -> (name, default tier, designation 'specific'|'class', real rating text)
HELMETS = {
 'ihps': ('IHPS (Integrated Head Protection System)', 'medium', 'specific', 'fragment and 9mm protection, limited rifle (NIJ IIIA class)'),
 'ech': ('Enhanced Combat Helmet (ECH)', 'medium', 'specific', 'fragment and pistol, limited rifle (UHMWPE shell)'),
 'ach': ('ACH / MICH 2000-pattern aramid helmet', 'medium', 'specific', 'NIJ IIIA class'),
 'fast_sf': ('Ops-Core FAST SF high-cut helmet', 'medium', 'specific', 'NIJ IIIA class'),
 'caiman': ('Galvion Batlskin Caiman high-cut helmet', 'medium', 'specific', 'NIJ IIIA class'),
 'cg634': ('CG634 combat helmet', 'medium', 'specific', 'fragment and pistol (aramid)'),
 'virtus_helmet': ('Virtus helmet', 'medium', 'specific', 'fragment and pistol (aramid/composite)'),
 'f3_helmet': ('Casque F3', 'medium', 'specific', 'fragment and pistol (aramid)'),
 'gefechtshelm': ('Gefechtshelm Streitkraefte (Galvion Caiman-based)', 'medium', 'specific', 'NIJ IIIA class'),
 '6b47': ('6B47 Ratnik helmet', 'medium', 'specific', 'GOST Br1 class (fragment and pistol)'),
 '6b7': ('6B7-1M aramid helmet', 'medium', 'specific', 'fragment and pistol'),
 'ssh68': ('SSh-68 steel helmet', 'light', 'specific', 'fragment only (steel)'),
 'qgf11': ('QGF-11 (Type 11) aramid helmet', 'medium', 'specific', 'fragment and pistol'),
 'hp05': ('HP-05 (wz. 2005) aramid helmet', 'medium', 'specific', 'fragment and pistol'),
 'or201': ('Orlite OR-201-type aramid helmet (Mitznefet cover)', 'medium', 'specific', 'fragment and pistol'),
 'delta_dh': ('Delta DH MK-II aramid helmet', 'medium', 'specific', 'fragment and pistol'),
 'st4_hc22': ('Stimpex ST-4 / STI-HC22 helmet', 'medium', 'specific', 'fragment and pistol'),
 'irn_ach': ('Iranian ACH-pattern aramid helmet', 'medium', 'specific', 'fragment and pistol'),
 'type88kai': ('Type 88 Kai / Type 18 combat helmet', 'medium', 'specific', 'fragment and pistol'),
 'pasgt': ('PASGT-type aramid helmet', 'light', 'class', 'fragment and pistol (older aramid); game light per faction file'),
 'steel_helmet': ('Steel helmet (M1 / SSh-40 / SSh-68 pattern)', 'light', 'class', 'fragment only'),
 'kpa_steel_helmet': ('KPA steel helmet (SSh-40 pattern)', 'light', 'class', 'fragment only'),
 'aramid_helmet': ('Aramid combat helmet, national issue (PASGT / MICH class)', 'medium', 'class', 'NIJ IIIA class'),
 'captured_helmet': ('Captured military helmet (ACH / PASGT / SSh-68, mixed)', 'light', 'class', 'mixed'),
 'commercial_helmet': ('Commercial ballistic helmet (FAST / MICH copy)', 'medium', 'class', 'NIJ IIIA claimed'),
 'cvc_helmet': ('Armoured vehicle crew helmet (DH-132 CVC class)', 'light', 'class', 'fragment'),
 'tsh_tanker': ('TSh-series padded tanker helmet (non-ballistic)', 'none', 'specific', 'none'),
 'flight_helmet': ('Aircrew flight helmet (HGU-56/P / ZSh-7 class, non-ballistic)', 'none', 'class', 'none'),
}
HELMET_GAME = {'light': 'helmet_bump', 'medium': 'helmet', 'heavy': 'helmet_heavy'}

# vests: id -> (name, designation, notes)
VESTS = {
 'msv': ('Modular Scalable Vest (MSV, Soldier Protection System)', 'specific'),
 'pc_gen3': ('USMC Plate Carrier Gen III', 'specific'),
 'iotv': ('IOTV (Improved Outer Tactical Vest)', 'specific'),
 'virtus_stv': ('Virtus Scalable Tactical Vest', 'specific'),
 'tbas': ('TBAS (Tiered Body Armour System) plate carrier', 'specific'),
 'caf_pc': ('CAF fragmentation vest / plate carrier with ceramic plates', 'class'),
 'smb': ('SMB (Structure Modulaire Balistique)', 'specific'),
 'mobast': ('MOBAST modular ballistic protection system', 'specific'),
 '6b45': ('6B45 Ratnik body armour', 'specific'),
 '6b43': ('6B43 Ratnik assault body armour (with side and groin protection)', 'specific'),
 '6b23': ('6B23 body armour (steel plates)', 'specific'),
 'type19_pc': ('Type 19 plate carrier', 'specific'),
 'ruyin': ('Ruyin-series vest', 'specific'),
 'kasda': ("IDF 'Kasda' / 'Ephod'-style plate carrier", 'specific'),
 'mk7_geo': ('Delta MK-VII plate carrier', 'specific'),
 'vst_pc22': ('VST-PC22 plate carrier', 'specific'),
 'ba_type3': ('Body Armour Type 3 (Kai)', 'specific'),
 'crye_avs': ('Crye AVS-pattern plate carrier with side plates', 'specific'),
 'crye_jpc': ('Crye JPC / commercial plate carrier', 'specific'),
 'plate_carrier_nat': ('Modular plate carrier, national issue', 'class'),
 'commercial_pc': ('Commercial plate carrier (Condor / Crye-pattern copy)', 'class'),
 'soft_vest': ('Soft armour vest (aramid, NIJ IIIA class)', 'class'),
 'old_vest': ('Older fragmentation / soft vest (national issue)', 'class'),
 'aircrew_vest': ('Aircrew survival armour vest (AIRSAVE class)', 'class'),
}
VEST_GAME = {'light': 'plate_carrier_light', 'medium': 'plate_carrier', 'heavy': 'plate_carrier_heavy'}

# plates: id -> (name, material, designation, real rating text)
PLATES = {
 'esapi': ('ESAPI (Enhanced Small Arms Protective Insert)', 'ceramic', 'specific', 'US ESAPI spec (7.62x54R B32 API); NIJ IV class'),
 'esbi': ('ESBI side plates', 'ceramic', 'specific', 'ESAPI-class side inserts'),
 'virtus_plates': ('Virtus hard armour plates (ceramic)', 'ceramic', 'specific', 'NIJ IV class'),
 'sapi_class': ('SAPI-class ceramic plates, national issue', 'ceramic', 'class', 'NIJ III+ to IV class'),
 'smb_plates': ('SMB ceramic plates', 'ceramic', 'specific', 'NIJ IV class'),
 'mobast_plates': ('MOBAST ceramic plates', 'ceramic', 'specific', 'NIJ IV class (VPAM 9 class)'),
 '6b45_plates': ('6B45 ceramic plates (GOST Br5)', 'ceramic', 'specific', 'GOST Br5 (7.62x54R B32 API)'),
 '6b23_steel': ('6B23 steel plates', 'steel', 'specific', 'GOST Br3/Br4 class'),
 'type19_plates': ('Type 19 ceramic plates', 'ceramic', 'class', 'NIJ III+ to IV class'),
 'steel_commercial': ('Commercial steel plates (AR500-class, level III)', 'steel', 'class', 'NIJ III (spall risk without coating)'),
 'steel_light': ('Light steel plate, front only (improvised, captured or commercial)', 'steel', 'class', 'NIJ III or below'),
 'pe_light': ('UHMWPE plate, level III (front only)', 'polyethylene', 'class', 'NIJ III'),
 'side_plates': ('Side plates, national issue (6x8 in class)', 'ceramic', 'class', 'NIJ III to IV class'),
}
# game plate items: (material, fits) -> item
#   ceramic medium/heavy -> plate_ceramic_l4 (IV); steel medium/heavy -> plate_steel_l3 (III++); pe light -> plate_pe_l3 (III)
#   steel light -> plate_steel_light (NEW, to build; substitute plate_pe_l3); side -> plate_side

# additions found while writing faction specs
for r in [
 ('l121a1','L121A1 AW50','12.7x99mm (.50 BMG)','amr','mag_50bmg_5',5,'','sniper_scope'),
]:
    WEAPONS[r[0]] = dict(name=r[1], calibre=r[2], cls=r[3], mag=r[4], rounds=r[5], game=r[6], optic=(r[7] if len(r) > 7 else ''))
PLATES['steel_nat'] = ('Steel plates, national manufacture (NIJ III / III+ class)', 'steel', 'class', 'NIJ III to III+ class')
GRENADES['mmhg'] = ('Multi-mode hand grenade (MMHG)', 'frag')
for r in [
 ('mg51','MG 51','7.62x51mm','gpmg','belt_762x51_100',100,''),
 ('ssg69','Steyr SSG 69','7.62x51mm','sniper','mag_762x51_5',5,'','sniper_scope'),
 ('ar10_pattern','AR-10-pattern DMR (commercial)','7.62x51mm','dmr','mag_762',20,'','dmr_scope'),
]:
    WEAPONS[r[0]] = dict(name=r[1], calibre=r[2], cls=r[3], mag=r[4], rounds=r[5], game=r[6], optic=(r[7] if len(r) > 7 else ''))
HELMETS['cheap_helmet'] = ('Low-cost commercial ballistic helmet (PASGT copy)', 'light', 'class', 'NIJ IIIA claimed, often lower')

# ---- Captain's decisions (2026-10-10) -------------------------------------------------
# Q2: proposed items.json ids for the rounds of the reloadable in-game launchers (AT4 and NLAW are
# single-shot: the launcher item is the round; the Javelin missile is its own item).
LAUNCHER_ROUND_IDS = {'PG-7V': 'pg7v', 'OG-7V': 'og7v', 'FFV551 HEAT': 'ffv551', 'FFV441D HE': 'ffv441d',
                      'Mk 6 HEAA': 'mk6_heaa', 'Mk 3 HEDP': 'mk3_hedp',
                      'FGM-148 missile (tandem HEAT, top attack)': 'javelin_missile'}
# Q4: non-ballistic crew helmets are cosmetic items to build.
HELMET_NEW = {'tsh_tanker': 'helmet_tanker', 'flight_helmet': 'helmet_flight'}
# Q5: heavy (III++) helmets for elite / SOF variants only. Real ratings are below NIJ III++; heavy is the game tier.
HELMETS['k63_altyn'] = ('K6-3 / Altyn-type titanium assault helmet with visor', 'heavy', 'specific',
                        'titanium shell with visor, pistol and fragment rated in reality; game heavy tier (Captain, 2026-10-10)')
HELMETS['assault_helmet_visor'] = ('Assault helmet with ballistic visor and mandible (Caiman / FAST class)', 'heavy', 'class',
                                   'high-cut helmet with rifle applique and visor; game heavy tier (Captain, 2026-10-10)')

# Q7: round specs for every round name with no exact match in the game's data/rounds.json.
# designation -> (id, calibre, projectile, approx. muzzle velocity m/s, approx. bullet mass g, game ladder level, class)
# Level is the round's place on the game's NIJ-named ladder (design doc); values are proposed starting points.
_R = [
 ('5.45x39mm 7N6M (steel core)', '545x39_7n6m', '5.45x39mm', 'FMJ, hardened steel core', 880, 3.4, 'III+', 'intermediate'),
 ('5.45x39mm 7N10 (enhanced penetration)', '545x39_7n10', '5.45x39mm', 'FMJ, enhanced-penetration steel core', 880, 3.6, 'III++', 'intermediate'),
 ('5.56x45mm M855A1 EPR', '556_m855a1', '5.56x45mm', 'EPR: exposed steel penetrator over a copper slug', 910, 4.0, 'III++', 'intermediate'),
 ('5.56x45mm SS109 / M855 (NATO ball)', '556_ss109', '5.56x45mm', 'FMJ with steel penetrator (M855 equivalent)', 915, 4.0, 'III++', 'intermediate'),
 ('5.8x42mm DBP10', '58x42_dbp10', '5.8x42mm', 'FMJ, hardened steel core', 930, 4.15, 'III++', 'intermediate'),
 ('6.8x51mm Common Cartridge, XM1186 general purpose', '68x51_xm1186', '6.8x51mm', 'general purpose, steel-tipped (EPR style)', 915, 8.75, 'IV', 'full_power'),
 ('7.62x51mm M80A1 EPR', '762x51_m80a1', '7.62x51mm', 'EPR: exposed steel penetrator over a copper slug', 860, 8.4, 'III++', 'full_power'),
 ('7.62x51mm (Chinese DVC12-class ball)', '762x51_chn_ball', '7.62x51mm', 'FMJ ball, mild steel core', 830, 9.5, 'III+', 'full_power'),
 ('7.62x54R 7N13 (steel core), 7N1 for the SVD', '762x54r_7n13', '7.62x54R', 'FMJ, heat-treated steel core', 830, 9.4, 'III++', 'full_power'),
 ('7.92x57mm M49 ball', '792x57_m49', '7.92x57mm', 'FMJ ball, lead core', 760, 12.8, 'III+', 'full_power'),
 ('.300 Norma Magnum match', '300nm_match', '.300 Norma Magnum', 'match, open tip', 870, 14.3, 'III++', 'full_power'),
 ('.300 Norma Magnum Mk 22 match', '300nm_match', '.300 Norma Magnum', 'match, open tip', 870, 14.3, 'III++', 'full_power'),
 ('.300 Winchester Magnum match (Mk 248 class)', '300wm_mk248', '.300 Winchester Magnum', 'match, open tip (Mk 248 Mod 1)', 869, 14.3, 'III++', 'full_power'),
 ('.338 Lapua Magnum ball / match', '338lm_ball', '.338 Lapua Magnum', 'ball / match, 250 gr', 905, 16.2, 'IV', 'full_power'),
 ('12.7x108mm B-32 API', '127x108_b32', '12.7x108mm', 'armour-piercing incendiary, steel core', 820, 48.3, 'ABOVE_IV', 'full_power'),
 ('12.7x108mm Chinese API (Type 54-class)', '127x108_chn_api', '12.7x108mm', 'armour-piercing incendiary, steel core', 820, 48.0, 'ABOVE_IV', 'full_power'),
 ('14.5x114mm B-32 API', '145x114_b32', '14.5x114mm', 'armour-piercing incendiary, steel core', 990, 64.4, 'ABOVE_IV', 'full_power'),
 ('9x39mm SP-5 / SP-6', '9x39_sp5_sp6', '9x39mm', 'subsonic; SP-5 ball, SP-6 steel-core AP', 290, 16.2, 'III', 'intermediate'),
 ('5.7x28mm SS190', '57x28_ss190', '5.7x28mm', 'FMJ with steel penetrator (pistol barrel)', 650, 2.0, 'IIIA', 'pistol'),
 ('9x18mm 57-N-181S', '9x18_57n181s', '9x18mm', 'FMJ, mild steel core', 315, 6.1, 'IIA', 'pistol'),
 ('7.62x25mm 57-N-134S', '762x25_57n134s', '7.62x25mm', 'FMJ, mild steel core', 420, 5.5, 'II', 'pistol'),
 ('9x19mm DAP92-9 (Chinese)', '9x19_dap92', '9x19mm', 'FMJ, steel core', 350, 7.5, 'II', 'pistol'),
 ('4.6x30mm DM11', '46x30_dm11', '4.6x30mm', 'FMJ, steel core', 720, 2.0, 'IIIA', 'pistol'),
]
ROUND_SPECS = {r[0]: r[1:] for r in _R}
LADDER = ['IIA', 'II', 'IIIA', 'III', 'III+', 'III++', 'IV', 'ABOVE_IV']
# game armor ratings (design doc / data/items.json)
GAME_ARMOR_RATINGS = [('light vest soft armour (front)', 'IIA'), ('medium/heavy vest soft armour', 'IIIA'),
                      ('light helmet', 'IIA'), ('medium helmet', 'IIIA'), ('heavy helmet', 'III++'),
                      ('light plate (PE / proposed light steel)', 'III'), ('steel plate', 'III++'), ('ceramic plate', 'IV')]
