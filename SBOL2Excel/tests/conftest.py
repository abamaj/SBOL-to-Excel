import pytest
import sbol2
import os
import math
import pandas as pd


@pytest.fixture()
def sbol_doc():
    file_dir = os.path.dirname(__file__)
    test_file_path = os.path.join(file_dir, 'test_files', 'test_sbol.xml')
    doc = sbol2.Document()
    doc.read(test_file_path)
    return doc


@pytest.fixture()
def test_df():
    d = {'col1': [1, 2], 'col2': [3, 4], 'Role': [5, 6], 'Design Notes': [7, 8]}
    df = pd.DataFrame(data=d)
    return df


@pytest.fixture()
def org_onto_v001_expected():
    onto_dict = {'1': 'Root',
                 '2': 'Bacteria',
                 '6': 'Azorhizobium',
                 '7': 'Azorhizobium caulinodans',
                 '9': 'Buchnera aphidicola',
                 '10': 'Cellvibrio',
                 '11': 'Cellulomonas gilvus',
                 '12': 'Photobacterium profundum',
                 '13': 'Dictyoglomus',
                 '14': 'Dictyoglomus thermophilum',
                 '16': 'Methylophilus',
                 '17': 'Methylophilus methylotrophus',
                 '18': 'Pelobacter',
                 '19': 'Pelobacter carbinolicus',
                 '20': 'Phenylobacterium',
                 '21': 'Phenylobacterium immobile',
                 '22': 'Shewanella',
                 '23': 'Shewanella colwelliana',
                 '24': 'Shewanella putrefaciens',
                 '25': 'Shewanella hanedai',
                 '27': 'halophilic eubacterium NRCC 41227',
                 '28': 'halophilic eubacterium',
                 '29': 'Myxococcales',
                 '4932': 'Saccharomyces cerevisiae',
                 '562': 'Escherichia coli',
                 '1034331': 'Ashbya gossypii',
                 '1718': 'Corynebacterium\xa0glutamicum',
                 '6100': 'Aequorea victoria',
                 '4922': 'Pichia pastoris',
                 '86600': 'Discosoma\xa0sp.'
                 }
    return onto_dict


@pytest.fixture()
def sbol_to_df_expected():
    df_dict = {
                'Identity': ['http://examples.org/aMF_u916__no_Kex/1',
                             'http://examples.org/Glucoamylase_u45_aMF_u916_/1',
                             'http://examples.org/RFP_Sec/1',
                             'http://examples.org/Killer_u45_aMF_u916_/1',
                             'http://examples.org/aMF_no_EAEA/1',
                             'http://examples.org/aAmylase_u45_aMF_u916_/1',
                             'http://examples.org/Inulinase_u45_aMF_u916_/1',
                             'http://examples.org/attB/1', 'http://examples.org/aMF_u916_/1', 'http://examples.org/yEGFP/1', 'http://examples.org/pGAP/1', 'http://examples.org/pAOX1/1', 'http://examples.org/SA_u45_aMF_u916_/1', 'http://examples.org/tAOX1/1', 'http://examples.org/aMF/1', 'http://examples.org/pENO1/1', 'http://examples.org/Invertase_u45_aMF_u916_/1', 'http://examples.org/RFP/1', 'http://examples.org/yEGFP_Sec/1', 'http://examples.org/PARS/1', 'http://examples.org/pTPI1/1'],
                'Persistentidentity': ['http://examples.org/aMF_u916__no_Kex', 'http://examples.org/Glucoamylase_u45_aMF_u916_', 'http://examples.org/RFP_Sec', 'http://examples.org/Killer_u45_aMF_u916_', 'http://examples.org/aMF_no_EAEA', 'http://examples.org/aAmylase_u45_aMF_u916_', 'http://examples.org/Inulinase_u45_aMF_u916_', 'http://examples.org/attB', 'http://examples.org/aMF_u916_', 'http://examples.org/yEGFP', 'http://examples.org/pGAP', 'http://examples.org/pAOX1', 'http://examples.org/SA_u45_aMF_u916_', 'http://examples.org/tAOX1', 'http://examples.org/aMF', 'http://examples.org/pENO1', 'http://examples.org/Invertase_u45_aMF_u916_', 'http://examples.org/RFP', 'http://examples.org/yEGFP_Sec', 'http://examples.org/PARS', 'http://examples.org/pTPI1'],
                'Displayid': ['aMF_u916__no_Kex', 'Glucoamylase_u45_aMF_u916_', 'RFP_Sec', 'Killer_u45_aMF_u916_', 'aMF_no_EAEA', 'aAmylase_u45_aMF_u916_', 'Inulinase_u45_aMF_u916_', 'attB', 'aMF_u916_', 'yEGFP', 'pGAP', 'pAOX1', 'SA_u45_aMF_u916_', 'tAOX1', 'aMF', 'pENO1', 'Invertase_u45_aMF_u916_', 'RFP', 'yEGFP_Sec', 'PARS', 'pTPI1'],
                'Version': ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                'Part Name': ['aMFΔ_no_Kex', 'Glucoamylase-aMFΔ', 'RFP_Sec', 'Killer-aMFΔ', 'aMF_no_EAEA', 'aAmylase-aMFΔ', 'Inulinase-aMFΔ', 'attB', 'aMFΔ', 'yEGFP', 'pGAP', 'pAOX1', 'SA-aMFΔ', 'tAOX1', 'aMF', 'pENO1', 'Invertase-aMFΔ', 'RFP', 'yEGFP_Sec', 'PARS', 'pTPI1'],
                'Part Description': ['α-mating factor no Kex recognition site', 'Glucoamylase followed by aMFΔ', 'Red fluorescent protein, BsaI removed', 'Killer followed by aMFΔ', 'α-mating factor no EAEA', 'α-Amylase followed by aMFΔ', 'Inulinase followed by aMFΔ', 'BxbI recognition site, BsaI site removed', 'α-mating factor, pre-sequence shortened', 'Green fluorescent protein', 'Glyceraldehyde-3-phosphate dehydrogenase', 'Alcohol oxidase 1', 'Serum albumin followed by aMFΔ', 'Alcohol oxidase 1', 'α-mating factor', 'Enolase 1', 'Invertase followed by aMFΔ', 'Red fluorescent protein, BsaI removed', 'Green fluorescent protein', 'Pichia autonomously replicating sequence', 'Triose phosphate isomerase 1'],
                'Wasderivedfrom': ['https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957', 'https://pubmed.ncbi.nlm.nih.gov/28252957'],
                'Wasgeneratedby': ['https://synbiohub.org/public/Excel2SBOL/Truncated/1', '', 'https://synbiohub.org/public/Excel2SBOL/mutations/1', '', 'https://synbiohub.org/public/Excel2SBOL/Truncated/1', 'https://synbiohub.org/public/Excel2SBOL/Composite/1', '', 'https://synbiohub.org/public/Excel2SBOL/mutations/1', 'https://synbiohub.org/public/Excel2SBOL/Truncated/1', 'https://synbiohub.org/public/Excel2SBOL/codon_optimisation/1', 'https://synbiohub.org/public/Excel2SBOL/mutations/1', 'https://synbiohub.org/public/Excel2SBOL/direct/1', '', 'https://synbiohub.org/public/Excel2SBOL/direct/1', 'https://synbiohub.org/public/Excel2SBOL/mutations/1', 'https://synbiohub.org/public/Excel2SBOL/mutations/1', '', 'https://synbiohub.org/public/Excel2SBOL/mutations/1', 'https://synbiohub.org/public/Excel2SBOL/codon_optimisation/1', 'https://synbiohub.org/public/Excel2SBOL/mutations/1', 'https://synbiohub.org/public/Excel2SBOL/mutations/1'],
                'Attachment': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                'Types': ['DnaRegion', 'DnaRegion', 'DnaRegion', 'DnaRegion', 'DnaRegion', 'DnaRegion', 'DnaRegion', 'DnaRegion', 'DnaRegion', 'DnaRegion', 'DnaRegion', 'DnaRegion', 'DnaRegion', 'DnaRegion', 'DnaRegion', 'DnaRegion', 'DnaRegion', 'DnaRegion', 'DnaRegion', 'DnaRegion', 'DnaRegion'],
                'Role': ['signal_peptide_region_of_CDS', 'signal_peptide_region_of_CDS', 'CDS', 'signal_peptide_region_of_CDS', 'signal_peptide_region_of_CDS', 'signal_peptide_region_of_CDS', 'signal_peptide_region_of_CDS', 'site_specific_recombination_target_region', 'signal_peptide_region_of_CDS', 'CDS', 'promoter', 'promoter', 'signal_peptide_region_of_CDS', 'terminator', 'signal_peptide_region_of_CDS', 'promoter', 'signal_peptide_region_of_CDS', 'CDS', 'CDS', 'origin_of_replication', 'promoter'],
                'Sequence': ['atgagattcccatcaatttttactgctgttctgttcgccgcttctagtgcacttgccatgagatttcctagtattttcactgctgtgctatttgccgctagttccgctctagctgctccagttaatactactactgaagatgaattggagggtgacttcgatgttgctgttctgcctttttccgcttctatcacagccaaggaagaaggtgtatctctagagaagcgt', 'atgtctttcagatccctattggcattgtcagggttggtctgttctggattggctatgagatttcctagtattttcactgctgtgctatttgccgctagttccgctctagctgctccagttaatactactactgaagatgaattggagggtgacttcgatgttgctgttctgcctttttccgcttctatcgcagccaaggaagaaggtgtatctctagagaagcgt', 'gcaacttccggtatggtgtcaaagggagaggaaaataatatggctattattaaggagtttatgcgttttaaggtacatatggaaggttctgtcaacggtcacgaattcgaaattgaaggtgagggggaggggaggccatacgagggaactcagactgctaagttaaaggtcactaaaggtggtcctttacctttcgcctgggatatcctgtctccacagtttatgtacggttcaaaggcttatgtgaaacatcctgccgatatcccagattatcttaaactttctttccctgagggttttaagtgggagagggtaatgaactttgaagacggtggtgtggtcactgttactcaggactcaagtctgcaggacggtgagttcatctacaaggtgaagctgagaggtaccaattttccatcagatggtcccgtgatgcaaaaaaagacaatgggttgggaagcttctagtgaacgtatgtatcccgaagatggagctttgaaaggtgaaattaagcaaagactaaaacttaaggatggtggacattacgatgctgaagttaagacgacctacaaggccaaaaagccagtccagttgcctggagcatacaatgttaacatcaaattggatataacttcccataatgaagactataccatcgtcgagcaatacgaacgagccgaagggagacacagtactggtggtatggatgaactttataaaggatccggaaccgca', 'atgaccaaaccaacgcaagtcttagttcgttcagtctctattttattcttcatcacactgttgcacttggttgttgcaatgagatttcctagtattttcactgctgtgctatttgccgctagttccgctctagctgctccagttaatactactactgaagatgaattggagggtgacttcgatgttgctgttctgcctttttccgcttctatcgcagccaaggaagaaggtgtatctctagagaagcgt', 'atgagatttccttcaatttttactgctgttttattcgcagcatcctccgcattagctgctccagtcaacactacaacagaagatgaaacggcacaaattccggctgaagctgtcatcggttactcagatttagaaggggatttcgatgttgctgttttgccattttccaacagcacaaataacgggttattgtttataaatactactattgccagcattgctgctaaagaagaaggggtatctctcgagaaaagag', 'atggtggcatggtggtccttattcttatatggtcttcaagttgctgctcctgcccttgctatgagatttcctagtattttcactgctgtgctatttgccgctagttccgctctagctgctccagttaatactactactgaagatgaattggagggtgacttcgatgttgctgttctgcctttttccgcttctatcgcagccaaggaagaaggtgtatctctagagaagcgt', 'atgaaactggcttactccctgttgctacctctggctggagtttccgctatgagatttcctagtattttcactgctgtgctatttgccgctagttccgctctagctgctccagttaatactactactgaagatgaattggagggtgacttcgatgttgctgttctgcctttttccgcttctatcgcagccaaggaagaaggtgtatctctagagaagcgt', 'tggccgtggccgtgctcgtcctcgtcggccggcttgtcgacgacggcggtcaccgtcgtcaggatcatccgggccacaagcttgctgacagaagcctcaagaaaaaaaaaattcttcttcgactatgctggaggcagagatgatcgagccggtagttaactatatatagctaaattggttccatcac', 'atgagatttcctagtattttcactgctgtgctatttgccgctagttcc', 'atggtgagcaagggcgaggagctgttcaccggggtggtgcccatcctggtcgagctggacggcgacgtaaacggccacaagttcagcgtgtccggcgagggcgagggcgatgccacctacggcaagctgaccctgaagttcatctgcaccaccggcaagctgcccgtgccctggcccaccctcgtgaccaccctgacctacggcgtgcagtgcttcagccgctaccccgaccacatgaagcagcacgacttcttcaagtccgccatgcccgaaggctacgtccaggagcgcaccatcttcttcaaggacgacggcaactacaagacccgcgccgaggtgaagttcgagggcgacaccctggtgaaccgcatcgagctgaagggcatcgacttcaaggaggacggcaacatcctggggcacaagctggagtacaactacaacagccacaacgtctatatcatggccgacaagcagaagaacggcatcaaggtgaacttcaagatccgccacaacatcgaggacggcagcgtgcagctcgccgaccactaccagcagaacacccccatcggcgacggccccgtgctgctgcccgacaaccactacctgagcacccagagcgccctgagcaaagaccccaacgagaagcgcgatcacatggtcctgctggagttcgtgaccgccgccgggatcactctcggcatggacgagctgtacaag', 'tttttgtagaaatgtcttggtgtcctcgtccaatcaggtagccatctctgaaatatctggctccgttgcaactccgaacgacctgctggcaacgtaaaattctccggggtaaaacttaaatgtggagtaatggaaccagaaacgtgtcttcccttctctctccttccaccgcccgttaccgtccctaggaaattttactctgctggagagcttcttctacggcccccttgcagcaatgctcttcccagcattacgttgcgggtaaaacggaggtcgtgtacccgacctagcagcccagggatggaaaagtcccggccgtcgctggcaataatagcgggcggacgcatgtcatgagattattggaaaccaccagaatcgaatataaaaggcgaacacctttcccaattttggtttctcctgacccaaagactttaaatttaatttatttgtccctatttcaatcaattgaacaactat', 'gatctaacatccaaagacgaaaggttgaatgaaacctttttgccatccgacatccacaggtccattctcacacataagtgccaaacgcaacaggaggggatacactagcagcagaccgttgcaaacgcaggacctccactcctcttctcctcaacacccacttttgccatcgaaaaaccagcccagttattgggcttgattggagctcgctcattccaattccttctattaggctactaacaccatgactttattagcctgtctatcctggcccccctggcgaggttcatgtttgtttatttccgaatgcaacaagctccgcattacacccgaacatcactccagatgagggctttctgagtgtggggtcaaatagtttcatgttccccaaatggcccaaaactgacagtttaaacgctgtcttggaacctaatatgacaaaagcgtgatctcatccaagatgaactaagtttggttcgttgaaatgctaacggccagttggtcaaaaagaaacttccaaaagtcggcataccgtttgtcttgtttggtattgattgacgaatgctcaaaaataatctcattaatgcttagcgcagtctctctatcgcttctgaaccccggtgcacctgtgccgaaacgcaaatggggaaacacccgctttttggatgattatgcattgtctccacattgtatgcttccaagattctggtgggaatactgctgatagcctaacgttcatgatcaaaatttaactgttctaacccctacttgacagcaatatataaacagaaggaagctgccctgtcttaaacctttttttttatcatcattattagcttactttcataattgcgactggttccaattgacaagcttttgattttaacgacttttaacgacaacttgagaagatcaaaaaacaactaattattcgaaacg',
                             'atgaagtgggtaactttcatctcattgttattcttgttctcctctgcttactctatgagatttcctagtattttcactgctgtgctatttgcctctagttccgctctagctgctccagttaatactactactgaagatgaattggagggtgacttcgatgttgctgttctgcctttttccgcttctatcgcagccaaggaagaaggtgtatctctagagaagcgt', 'tcaagaggatgtcagaatgccatttgcctgagagatgcaggcttcatttttgatacttttttatttgtaacctatatagtataggattttttttgtcattttgtttcttctcgtacgagcttgctcctgatcagcctatctcgcagctgatgaatatcttgtggtaggggtttgggaaaatcattcgagtttgatgtttttcttggtatttcccactcctcttcagagtacagaagattaagtgaga', 'atgagatttccttcaatttttactgctgttttattcgcagcatcctccgcattagctgctccagtcaacactacaacagaagatgaaacggcacaaattccggctgaagctgtcatcggttactcagatttagaaggggatttcgatgttgctgttttgccattttccaacagcacaaataacgggttattgtttataaatactactattgccagcattgctgctaaagaagaaggggtatctctcgagaaaagagaggctgaagct', 'agaaagcatactatactattcgacattcctttcaatcctggaattaacagtcacttttaaaaaagacatctaccgtgaaggtgccgtagagtatcgcgttaccatatcgccaaaaactgatatacgccgcggaaaccaggcaaacaattgaaaagaaaaattttgaggaactctctgcatcgaagccgtctagagttaccactagtcagatgccgcgggcacttgagcacctcatgcacagcaataacacaacacaatggttagtagcaacctgaattcggtcattgatgcatgcatgtgccgtgaagcgggacaaccagaaaagtcgtctataaatgccggcacgtgcgatcatcgtggcggggttttaagagtgcatatcacaaattgtcgcattaccgcggaaccgccagatattcattacttgacgcaaaagcgtttgaaataatgacgaaaaagaaggaagaaaaaaaaagaaaaataccgcttctaggcgggttatctactgatccgagcttccactaggatagcacccaaacacctgcatatttggacgacctttacttacaccaccaaaaaccactttcgcctctcccgcccctgataacgtccactaattgagcgattacctgagcggtcctcttttgtttgcagcatgagacttgcatactgcaaatcgtaagtagcaacctctcaaggtcaaaactgtatggaaaccttgtcacctcacttaattctagctagcctaccctgcaagtcaagagctctccgtgattcctagccacctcaaggtatgcctctccccggaaactgtggccttttctggcacacatgatctccacgatttcaacatataaatagcttttgataatggcaatattaatcaaatttattttacttctttcttgtaacatctctcttgtaatcccttattccttctagctatttttcataaaaaaccaagcaactgcttatcaacacacaaacactaaatcaaa', 'atgttattgcaagcttttttatttctgctggcaggttttgcagcaaagatttctgccatgagatttcctagtattttcactgctgtgctatttgccgctagttccgctctagctgctccagttaatactactactgaagatgaattggagggtgacttcgatgttgctgttctgcctttttccgcttctatcgcagccaaggaagaaggtgtatctctagagaagcgt', 'atcgcaacttccggtatggtgtcaaagggagaggaaaataatatggctattattaaggagtttatgcgttttaaggtacatatggaaggttctgtcaacggtcacgaattcgaaattgaaggtgagggggaggggaggccatacgagggaactcagactgctaagttaaaggtcactaaaggtggtcctttacctttcgcctgggatatcctgtctccacagtttatgtacggttcaaaggcttatgtgaaacatcctgccgatatcccagattatcttaaactttctttccctgagggttttaagtgggagagggtaatgaactttgaagacggtggtgtggtcactgttactcaggactcaagtctgcaggacggtgagttcatctacaaggtgaagctgagaggtaccaattttccatcagatggtcccgtgatgcaaaaaaagacaatgggttgggaagcttctagtgaacgtatgtatcccgaagatggagctttgaaaggtgaaattaagcaaagactaaaacttaaggatggtggacattacgatgctgaagttaagacgacctacaaggccaaaaagccagtccagttgcctggagcatacaatgttaacatcaaattggatataacttcccataatgaagactataccatcgtcgagcaatacgaacgagccgaagggagacacagtactggtggtatggatgaactttataaaggatccggaaccgca', 'gtgagcaagggcgaggagctgttcaccggggtggtgcccatcctggtcgagctggacggcgacgtaaacggccacaagttcagcgtgtccggcgagggcgagggcgatgccacctacggcaagctgaccctgaagttcatctgcaccaccggcaagctgcccgtgccctggcccaccctcgtgaccaccctgacctacggcgtgcagtgcttcagccgctaccccgaccacatgaagcagcacgacttcttcaagtccgccatgcccgaaggctacgtccaggagcgcaccatcttcttcaaggacgacggcaactacaagacccgcgccgaggtgaagttcgagggcgacaccctggtgaaccgcatcgagctgaagggcatcgacttcaaggaggacggcaacatcctggggcacaagctggagtacaactacaacagccacaacgtctatatcatggccgacaagcagaagaacggcatcaaggtgaacttcaagatccgccacaacatcgaggacggcagcgtgcagctcgccgaccactaccagcagaacacccccatcggcgacggccccgtgctgctgcccgacaaccactacctgagcacccagagcgccctgagcaaagaccccaacgagaagcgcgatcacatggtcctgctggagttcgtgaccgccgccgggatcactctcggcatggacgagctgtacaag', 'ccttcgtttgtgcggatccaattaatatttacttattttggtcaaccccaaataggttgatttcatacttggttcattcaaaaataagtagtcttttgagatctttcaatattataataaatatactataacagccgacttgtttcattttcgcgaatgttcccccagcttatcg', 'gtgtttaaagattacggatatttaacttacttagaataatgccatttttttgagttataataatcctacgttagtgtgagcgggatttaaactgtgaggaccttaatacattcagacacttctgcggtatcaccctacttattcccttcgagattatatctaggaacccatcaggttggtggaagattacccgttctaagacttttcagcttcctctattgatgttacacctggacaccccttttctggcatccagtttttaatcttcagtggcatgtgagattctccgaaattaactaaagcaatcacacaattctctcggataccacctcggttgaaactgacaggtggtttgttacgcatgctaatgcaaaggagcctatatacctttggctcggctgctgtaacagggaatataaagggcagcataatttaggagtttagtgaacttgcaacatttactattttcccttcttacgtaaatatttttctttttaattctaaatcaatctttttcaattttttgtttgtattcttttcttgcttaaatctataactacaaaaaacacatacataaactaaaa'],
                'Target Organism': ['Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris', 'Pichia pastoris'],
                'OBI_0001617': ['28252957', '28252957', '28252957', '28252957', '28252957', '28252957', '28252957', '28252957', '28252957', '28252957', '28252957', '28252957', '28252957', '28252957', '28252957', '28252957', '28252957', '28252957', '28252957', '28252957', '28252957'],
                'Design Notes': ['No Kex recognition site', math.nan, 'No start or stop codon, for use with N-terminal secretion tag', math.nan, 'No EAEA', math.nan, math.nan, 'BsaI site removed', 'Pre-sequence shortened', 'No stop codon', 'BsaI site removed', math.nan, math.nan, math.nan, math.nan, 'BsaI and BsmBI site removed', math.nan, 'No stop codon', 'No start or stop codon, for use with N-terminal secretion tag', math.nan, math.nan],
                'Source Organism': ['Saccharomyces cerevisiae', math.nan, 'Discosoma\xa0sp.', math.nan, 'Saccharomyces cerevisiae', math.nan, math.nan, math.nan, 'Saccharomyces cerevisiae', 'Aequorea victoria', 'Pichia pastoris', 'Pichia pastoris', math.nan, 'Pichia pastoris', 'Saccharomyces cerevisiae', 'Saccharomyces cerevisiae', math.nan, 'Discosoma\xa0sp.', 'Aequorea victoria', 'Pichia pastoris', 'Saccharomyces cerevisiae']
              }
    return df_dict


@pytest.fixture()
def role_onto_v001_expected():
    onto_dict = {
                    'http://identifiers.org/so/SO:0000316': 'CDS',
                    'http://identifiers.org/so/SO:0000167': 'promoter',
                    'http://identifiers.org/so/SO:0000139': 'ribosome_entry_site',
                    'http://identifiers.org/so/SO:0000141': 'terminator',
                    'http://identifiers.org/so/SO:0000296': 'origin_of_replication',
                    'http://identifiers.org/so/SO:0000724': 'oriT',
                    'http://identifiers.org/so/SO:0000952': 'oriV',
                    'http://identifiers.org/so/SO:0000342': 'site_specific_recombination_target_region',
                    'http://identifiers.org/so/SO:0002251': 'signal_peptide_region_of_CDS'
                }
    return onto_dict
