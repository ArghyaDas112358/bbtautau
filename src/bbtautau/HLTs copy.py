"""HLTs for bbtautau analysis."""

from __future__ import annotations

from typing import ClassVar, Dict, List, Union
import fnmatch
import copy

from boostedhh.utils import HLT

years_2022 = ["2022", "2022EE"]
years_2023 = ["2023", "2023BPix"]
years = years_2022 + years_2023


# years_2024 = ["2024"]
# years = years_2022 + years_2023 + years_2024

HLT_WILD_SYMB = "*"


class HLTs:
    HLTs: ClassVar[dict[str, list[HLT]]] = {
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
        "parkingHH_2023": [
            HLT(
                name="HLT_PFHT*",
                years=years_2023,
                dataset="ParkingHH",
            ),
        ],
    }          
    
    _available_hlts_cache: ClassVar[List[str]] = None
    
    @classmethod
    def prime(cls, events):
        cls._available_hlts_cache = events.HLT.fields
        
    @classmethod
    def _get_available_hlts(cls) -> List[str]:
        if cls._available_hlts_cache is None:
            raise RuntimeError(
                "HLTs class has not been primed. Call HLTs.prime(events) before using any other HLTs method."
            )
        return cls._available_hlts_cache
    
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
        available_hlts = cls._get_available_hlts()
        
        if data_only and mc_only:
            raise ValueError("Cannot filter by both data and MC")

        expanded_dict= {}

        for hlt_type, hlt_patterns in cls.HLTs.items():
            expanded_dict[hlt_type] = []
            for hlt_pattern_obj in hlt_patterns:
                # Check if this rule applies to the given year
                if not hlt_pattern_obj.check_year(year, data_only, mc_only):
                    continue

                pattern = hlt_pattern_obj.get_name()

                # Find all available HLTs that match this pattern
                for hlt_name in available_hlts:
                    if fnmatch.fnmatch(hlt_name, pattern):
                        # Create a new, concrete HLT object with the real name
                        # and properties from the pattern object.
                        new_hlt = copy.copy(hlt_pattern_obj)
                        new_hlt.name = hlt_name # Set the real, expanded name

                        # Add the real HLT to our list
                        expanded_dict[hlt_type].append(
                            new_hlt.get_name(hlt_prefix) if as_str else new_hlt
                        )
        # Remove Duplicates
        for hlt_type in expanded_dict:
            expanded_dict[hlt_type] = list(dict.fromkeys(expanded_dict[hlt_type]))

        return expanded_dict

    @classmethod
    def hlt_list(
        cls, 
        year: str,
        as_str: bool = True, 
        hlt_prefix: bool = True, 
        **hlt_kwargs
    ) -> List[Union[HLT, str]]:

        hlt_dictionary = cls.hlt_dict(year, as_str, hlt_prefix, **hlt_kwargs)
        full_list = [hlt for sublist in hlt_dictionary.values() for hlt in sublist]
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
        hlts = cls.hlt_list(year, as_str=False, **hlt_kwargs)
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
                hlt for sublist in cls.hlt_dict(year, as_str, mc_only=True, **hlt_kwargs).values()
                for hlt in sublist
            ],
            "data": [
                hlt for sublist in cls.hlt_dict(year, as_str, data_only=True, **hlt_kwargs).values()
                for hlt in sublist
            ],
        }


    @classmethod
    def get_hlt(cls, name_pattern: str) -> List[HLT]:
        """
        Finds all HLT objects whose names match the given pattern from the list
        of available HLTs at runtime. Always returns a list.
        """
        available_hlts = cls._get_available_hlts()
        matched_hlts = []
        for hlt_name in available_hlts:
            if fnmatch.fnmatch(hlt_name, name_pattern):
                # Find the corresponding rule to get the dataset info etc.
                for hlt_pattern_obj in (p for sublist in cls.HLTs.values() for p in sublist):
                    if fnmatch.fnmatch(hlt_name, hlt_pattern_obj.get_name()):
                        new_hlt = copy.copy(hlt_pattern_obj)
                        new_hlt.name = hlt_name
                        if new_hlt not in matched_hlts:
                           matched_hlts.append(new_hlt)
                        break # Found the rule, move to next hlt_name
        return matched_hlts
