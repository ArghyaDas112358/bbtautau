"""HLTs for bbtautau analysis."""

from __future__ import annotations

from typing import ClassVar, Dict, List, Union
import fnmatch
import copy
from dataclasses import dataclass

from boostedhh.utils import HLT

years_2022 = ["2022", "2022EE"]
years_2023 = ["2023", "2023BPix"]
years = years_2022 + years_2023

HLT_WILD_SYMB = "*"

@dataclass
class HLTs_Pattern:
    """A dataclass to define HLT patterns and their properties."""
    pattern: str
    dataset: str
    years: list[str] = None
    mc_years: list[str] = None
    data_years: list[str] = None

class HLTs:
    HLTs_precursor: ClassVar[dict[str, list[HLT]]] = {
        "pnet": [
            # 2022 + 6fb-1 of 2023
            HLT(
                name="HLT_AK8PFJet250_SoftDropMass40_PFAK8ParticleNetBB0p35",
                mc_years=years_2022,
                data_years=years_2022 + ["2023"],
                dataset="JetMET",
            ),
            HLT(
                name="HLT_AK8PFJet230_SoftDropMass40_PFAK8ParticleNetTauTau0p30",
                mc_years=years_2022,
                data_years=years_2022 + ["2023"],
                dataset="JetMET",
            ),
            # 2023 after 6fb-1, that is from Run2023C_0v2 to Run2023C_0v3
            HLT(
                name="HLT_AK8PFJet230_SoftDropMass40_PNetBB0p06",
                years=years_2023,
                dataset="JetMET",
            ),
            HLT(
                name="HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p03",
                years=years_2023,
                dataset="JetMET",
            ),
        ],
        "pfjet": [
            HLT(
                name="HLT_AK8PFJet420_MassSD30",
                years=years,  # years_2023  makes it work in 25Mar7 data samples
                dataset="JetMET",
            ),
            HLT(
                name="HLT_AK8PFJet425_SoftDropMass40",
                years=years,
                dataset="JetMET",
            ),
        ],
        "quadjet": [
            # 2022 + 6fb-1 of 2023 (moves to Parking after this)
            HLT(
                name="HLT_QuadPFJet70_50_40_35_PFBTagParticleNet_2BTagSum0p65",
                mc_years=years_2022,
                data_years=years_2022,
                dataset="JetMET",
            ),
            # HLT( #This should be there but is not in 25Apr16 samples. For now just ignore
            #     name="HLT_QuadPFJet70_50_40_35_PNet2BTagMean0p65",
            #     mc_years=[],
            #     data_years=["2023"],
            #     dataset="JetMET",
            # ),
            # 2022 + 2023
            HLT(
                name="HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2",
                years=years,
                dataset="JetMET",
            ),
            HLT(
                name="HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1",
                years=years,
                dataset="JetMET",
            ),
        ],
        "singletau": [
            HLT(
                name="HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                years=years,
                dataset="Tau",
            ),
        ],
        "ditau": [
            HLT(
                name="HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1",
                years=years,
                dataset="Tau",
            ),
        ],
        "ditaujet": [
            HLT(
                name="HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60",
                years=years,
                dataset="Tau",
            ),
            HLT(
                name="HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75",
                years=years,
                dataset="Tau",
            ),
        ],
        "muon": [
            HLT(
                name="HLT_IsoMu24",
                years=years,
                dataset="Muon",
            ),
            # TODO: check sensitivity without below triggers
            HLT(
                name="HLT_Mu50",
                years=years,
                dataset="Muon",
            ),
        ],
        "muontau": [
            HLT(
                name="HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1",
                years=years,
                dataset="Muon",
            ),
        ],
        "egamma": [
            HLT(
                name="HLT_Ele30_WPTight_Gsf",
                years=years,
                dataset="EGamma",
            ),
            HLT(
                name="HLT_Ele115_CaloIdVT_GsfTrkIdT",
                years=years,
                dataset="EGamma",
            ),
            HLT(
                name="HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165",
                years=years,
                dataset="EGamma",
            ),
            HLT(
                name="HLT_Photon200",
                years=years,
                dataset="EGamma",
            ),
        ],
        "etau": [
            HLT(
                name="HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1",
                years=years,
                dataset="EGamma",
            ),
        ],
        "met": [
            HLT(
                name="HLT_PFMET120_PFMHT120_IDTight",
                years=years,
                dataset="JetMET",
            ),
        ],
        "parking": [
            # Moved to Parking in 2023 after 6fb-1
            HLT(
                name="HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p55",
                years=["2023BPix"],
                dataset="ParkingHH",
            ),
            HLT(
                name="HLT_PFHT340_QuadPFJet70_50_40_40_PNet2BTagMean0p70",
                years=years_2023,
                dataset="ParkingHH",
            ),
        ],
    }
    
    HLTs_pattern: ClassVar[dict[str, list[HLTs_Pattern]]] = { 
        "parkingHH_2023": [
            HLTs_Pattern(
                pattern = "HLT_PFHT*",
                years = years_2023,
                dataset = "ParkingHH",
            )
        ] 
    }
    
    HLTs: ClassVar[Dict[str, List[HLT]]] = None
    
    @classmethod
    def prime(cls, events):
        available_hlts = events.HLT.fields
        final_hlt_dict = copy.deepcopy(cls.HLTs_precursor)
        
        for hlt_type, patterns in cls.HLTs_pattern.items():
            if hlt_type not in final_hlt_dict:
                final_hlt_dict[hlt_type] = []
            
            for hlt_pattern_obj in patterns:
                for hlt_name in available_hlts:
                    if fnmatch.fnmatch(hlt_name, hlt_pattern_obj.pattern):
                        print(f"[DEBUG] Pattern '{hlt_pattern_obj.pattern}' matched trigger '{hlt_name}'. Creating new HLT object.")

                        new_hlt = HLT(
                            name = hlt_name,
                            years = hlt_pattern_obj.years,
                            dataset = hlt_pattern_obj.dataset,
                        )
                        if new_hlt not in final_hlt_dict[hlt_type]:
                            final_hlt_dict[hlt_type].append(new_hlt)
                        
        cls.HLTs = final_hlt_dict
    
    @classmethod
    def hlt_dict(
        cls,
        year: str,
        as_str: bool = True,
        hlt_prefix: bool = True,
        data_only: bool = False,
        mc_only: bool = False,
    ) -> dict[str, list[HLT | str]]:
        """
        Convert into a dictionary of HLTs per year, optionally filtered by data or MC.

        Args:
            year (str): year to filter by.
            as_str (bool): if True, return HLT names only. If False, return HLT objects. Defaults to True.
            data_only (bool): filter by HLTs in data for that year. Defaults to False.
            mc_only (bool): filter by HLTs in MC for that year. Defaults to False.

        Returns:
            dict[str, list[HLT | str]]: format is ``{hlt_type: [hlt, ...]}``
        """
        if cls.HLTs is None:
            raise RuntimeError("HLTs class has not been primed. Call HLTs.prime(events) first.")

        if data_only and mc_only:
            raise ValueError("Cannot filter by both data and MC")

        return {
            hlt_type: [
                (hlt.get_name(hlt_prefix) if as_str else hlt)
                for hlt in hlt_list
                if hlt.check_year(year, data_only, mc_only)
            ]
            for hlt_type, hlt_list in cls.HLTs.items()
        }


    @classmethod
    def hlt_list(
        cls, year: str, as_str: bool = True, hlt_prefix: bool = True, **kwargs
    ) -> List[Union[HLT, str]]:
        """
        Gets a single list of all HLTs for a given year.
        This is now simple because it reads from the already-built HLTs dictionary.
        """
        if cls.HLTs is None:
            raise RuntimeError("HLTs class has not been primed. Call HLTs.prime(events) first.")
        
        full_list = []
        for hlt_list_for_type in cls.HLTs.values():
            for hlt in hlt_list_for_type:
                if hlt.check_year(year, **kwargs):
                    full_list.append(hlt.get_name(hlt_prefix) if as_str else hlt)

        return list(dict.fromkeys(full_list))

    @classmethod
    def hlts_by_type(
        cls,
        year: str,
        hlt_type: str | list[str],
        **hlt_kwargs,
    ) -> list[HLT | str]:
        """
        HLTs per year and type(s), with optional filters.

        Args:
            year (str): year to filter by.
            hlt_type (str | list[str]): filter by HLT type(s) out of ["PNet", "PFJet", "QuadJet", "DiTau", "SingleTau", "Muon", "EGamma", "MET", "Parking"].
            **hlt_kwargs: additional kwargs to pass to the hlt_dict function.

        Returns:
            list[HLT | str]: list of HLTs. Returns strings if as_str=True is passed in hlt_kwargs, otherwise returns HLT objects.
        """
        if cls.HLTs is None:
            raise RuntimeError("HLTs class has not been primed. Call HLTs.prime(events) first.")

        hlts = cls.hlt_dict(year, **hlt_kwargs)

        if isinstance(hlt_type, str):
            return hlts[hlt_type.lower()]
        else:
            return [hlt for ht in hlt_type for hlt in hlts[ht.lower()]]

    @classmethod
    def hlts_by_dataset(
        cls,
        year: str,
        dataset: str,
        as_str: bool = True,
        hlt_prefix: bool = True,
        **hlt_kwargs,
    ) -> list[HLT | str]:
        """
        HLTs per year and dataset, with optional filters.

        Args:
            year (str): year to filter by.
            dataset (str): filter by dataset out of ["JetMET", "Tau", "Muon", "EGamma", "ParkingHH"].
            as_str (bool): if True, return HLT names only. If False, return HLT objects. Defaults to True.
            hlt_prefix (bool): if True, return HLT names with "HLT_" prefix. If False, return HLT names without "HLT_" prefix. Defaults to True.
            **hlt_kwargs: additional kwargs to pass to the hlt_list function.

        Returns:
            list[HLT | str]: list of HLTs
        """
        hlts = cls.hlt_list(False, **hlt_kwargs)[year]
        ret_hlts = [
            (hlt.get_name(hlt_prefix) if as_str else hlt)
            for hlt in hlts
            if hlt.dataset.lower() == dataset.lower()
        ]

        if len(ret_hlts) == 0:
            raise ValueError(f"Dataset {dataset} not found in HLTs")

        return ret_hlts

    @classmethod
    def hlts_list_by_dtype(
        cls,
        year: str,
        as_str: bool = True,
        hlt_prefix: bool = True,
        **hlt_kwargs,
    ) -> list[HLT | str]:
        """
        HLTs per year, with optional filters.

        Args:
            year (str): year to filter by.
            as_str (bool): if True, return HLT names only. If False, return HLT objects. Defaults to True.
            hlt_prefix (bool): if True, return HLT names with "HLT_" prefix. If False, return HLT names without "HLT_" prefix. Defaults to True.
            **hlt_kwargs: additional kwargs to pass to the hlt_list function.

        Returns:
            dict[str, list[HLT | str]]: format is ``{data: [hlt, ...], signal: [...]}``
        """
        return {
            "signal": [
                (hlt.get_name(hlt_prefix) if as_str else hlt)
                for sublist in cls.hlt_dict(year, as_str=False, mc_only=True, **hlt_kwargs).values()
                for hlt in sublist
            ],
            "data": [
                (hlt.get_name(hlt_prefix) if as_str else hlt)
                for sublist in cls.hlt_dict(
                    year, as_str=False, data_only=True, **hlt_kwargs
                ).values()
                for hlt in sublist
            ],
        }

    @classmethod
    def get_hlt(cls, name: str) -> HLT:
        for cat in cls.HLTs.values():
            for hlt in cat:
                if hlt.get_name() == name:
                    return hlt
        raise ValueError(f"HLT {name} not found in HLTs")
