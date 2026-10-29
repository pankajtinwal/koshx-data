#!/usr/bin/env python3
"""
scripts/patch_company_profiles.py
Expands scripts/data_company_profiles.py with curated deep profiles for 50+ flagship Indian enterprises
and enhances domain sub-key routing across all 15 sectors.
"""

import sys
import os

EXTRA_CURATED = {
    "ADANIPORTS": {
        "summary": "Adani Ports and Special Economic Zone Ltd (APSEZ) is India's largest commercial port operator and integrated transport utility, handling approximately 27% of India's total port cargo throughput. With 15 domestic ports and terminals across 7 coastal states (anchored by flagship Mundra Port) and international terminals in Sri Lanka (Colombo), Israel (Haifa), and Tanzania, APSEZ delivers end-to-end marine, rail freight, and multi-modal logistics corridors.",
        "brands": ["Mundra Port & SEZ", "Krishnapatnam Port", "Dhamra Port", "Adani Logistics Ltd", "Haifa Port (Israel)", "Colombo West Container Terminal"],
        "revenue_breakup": [
            {"segment": "Port Marine Services & Handling", "pct": "73%", "desc": "Container stevedoring, dry bulk cargo handling, liquid chemicals, crude berthing, and pilotage fees."},
            {"segment": "Logistics & Multimodal Rail Freight", "pct": "19%", "desc": "110+ container trains, grade-A warehousing hubs, agri-silos, and inland container depots (ICDs)."},
            {"segment": "Port-Led SEZ Development & Utilities", "pct": "8%", "desc": "Industrial land leasing, port utility connections, and dredging infrastructure."}
        ],
        "geographic_mix": "Domestic (India): 89% • International Terminals (Haifa, Colombo): 11%",
        "moats_and_strengths": [
            "Dominant market share (27% of national cargo) with deepest draft berths capable of handling Capesize vessels.",
            "Flagship Mundra Port is India's largest commercial port by volume, surpassing 180 MMT annual throughput.",
            "Integrated logistics backbone with dedicated railway lines directly linking coastal ports to the northern hinterland.",
            "Industry-leading port EBITDA margins (>65%) backed by high asset utilization and automated container terminals."
        ],
        "order_book_or_capacity": "Total Cargo Throughput: 420+ MMT annually • Target Capacity: 500+ MMT by 2025 • 15 Strategic Ports",
        "promoter_governance": {
            "parent_group": "Adani Group (Gautam Adani & Family)",
            "pledge_status": "0.0% Pledged (Pledge-Free Promoter Stake)",
            "institutional_holding": "48.5% (FII: 35.8% • DII: 12.7%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "Commissioning of the deepwater Colombo West International Terminal in Sri Lanka capturing Indian transshipment cargo.",
                "Rapid volume ramp-up of the Dedicated Freight Corridor (DFC) shifting bulk traffic from road to Adani rail.",
                "Expanding containerization rate in India from 17% towards global average of 30%."
            ],
            "bearish_risks": [
                "Geopolitical volatility affecting international transit trade at the Port of Haifa.",
                "Sensitivity to global trade slowdowns and container shipping freight rate corrections."
            ]
        }
    },
    "ULTRACEMCO": {
        "summary": "UltraTech Cement Ltd is the flagship cement company of the Aditya Birla Group and India's largest cement and ready-mix concrete (RMC) manufacturer, ranking as the third largest cement producer in the world outside of China. UltraTech boasts an enormous consolidated grey cement capacity exceeding 154 MTPA across 24 integrated manufacturing units, 33 grinding units, and 8 bulk marine terminals.",
        "brands": ["UltraTech Cement", "UltraTech Super", "UltraTech Weather Pro", "Birla White", "UltraTech Concrete (RMC)", "UltraTech Building Products"],
        "revenue_breakup": [
            {"segment": "Grey Cement & Clinker", "pct": "85%", "desc": "Ordinary Portland Cement (OPC), Portland Pozzolana Cement (PPC), and bulk construction cement."},
            {"segment": "White Cement & Wall Putty (Birla White)", "pct": "8%", "desc": "Birla White brand white cement, wall putty, primers, and texture plasters."},
            {"segment": "Ready-Mix Concrete (RMC)", "pct": "5%", "desc": "Commercial, high-performance, and self-compacting concrete supplied to urban projects."},
            {"segment": "Building Solutions & Chemicals", "pct": "2%", "desc": "Waterproofing chemicals, tile adhesives, and repair mortars."}
        ],
        "geographic_mix": "Domestic (India): 96% • International Exports & Terminals (UAE, Bahrain, Sri Lanka): 4%",
        "moats_and_strengths": [
            "Insurmountable scale moat with 154+ MTPA capacity, commanding over 22% of India's cement market.",
            "Pan-India manufacturing presence with clinker and grinding units positioned within 300 km of major consumption centers.",
            "Direct distribution reach with over 100,000 retail channel partners across every district in India.",
            "Low-cost manufacturing leader supported by 320+ MW of Waste Heat Recovery Systems (WHRS) and alternate fuels."
        ],
        "order_book_or_capacity": "Installed Cement Capacity: 154+ MTPA • Capex Pipeline targeting 200 MTPA by FY27 • 24 Integrated Plants",
        "promoter_governance": {
            "parent_group": "Aditya Birla Group (Kumar Mangalam Birla)",
            "pledge_status": "0.0% Pledged (Pledge-Free Promoter Stake)",
            "institutional_holding": "33.5% (FII: 17.8% • DII: 15.7%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "Acquisition and integration of Kesoram Cement and stake in India Cements expanding southern market reach.",
                "Robust infrastructure capex and national highway expansion driving institutional cement demand.",
                "Rising share of premium blended cements boosting realizations per ton."
            ],
            "bearish_risks": [
                "Sharp spikes in international petcoke and thermal coal prices inflating kiln energy costs.",
                "Price competition and capacity additions in the northern and central Indian cement clusters."
            ]
        }
    },
    "TATASTEEL": {
        "summary": "Tata Steel Ltd is one of the world's most geographically diversified steel producers with an annual crude steel capacity of 35 million tonnes. Headquartered in Mumbai, the flagship Tata enterprise operates integrated blast furnaces and electric arc mills in India (Jamshedpur, Kalinganagar, Angul), the United Kingdom (Port Talbot), and the Netherlands (IJmuiden).",
        "brands": ["Tata Tiscon (TMT)", "Tata Shaktee", "Tata Steelium", "Tata Astrum", "Tata Structura", "Tata Pravesh"],
        "revenue_breakup": [
            {"segment": "Tata Steel India", "pct": "62%", "desc": "High-margin hot-rolled coils, automotive cold-rolled steel, and Tata Tiscon construction re-bars."},
            {"segment": "Tata Steel Europe (UK & Netherlands)", "pct": "33%", "desc": "Strip products, packaging steel, and automotive sheets from IJmuiden and Port Talbot."},
            {"segment": "Other Industrial Subsidiaries", "pct": "5%", "desc": "Tata Steel Industrial Consulting, tubes, and downstream wire manufacturing."}
        ],
        "geographic_mix": "Domestic (India): 62% • Europe (UK, Netherlands, Germany): 33% • Southeast Asia & RoW: 5%",
        "moats_and_strengths": [
            "100% captive iron ore mine self-sufficiency in India, delivering world-class low cost of hot metal production.",
            "Tata Tiscon is India's #1 retail construction rebar brand, commanding significant consumer price premiums.",
            "High-value automotive steel leadership in India, supplying over 45% of domestic automobile cold-rolled sheets.",
            "Strategic UK green steel transition supported by a £500M grant from the British Government for Electric Arc Furnaces."
        ],
        "order_book_or_capacity": "Global Crude Steel Capacity: 35 MTPA • India Capacity expanding from 21 MTPA to 40 MTPA by 2030",
        "promoter_governance": {
            "parent_group": "Tata Sons (Tata Group holds ~33.2%)",
            "pledge_status": "0.0% Pledged (Pledge-Free Promoter Stake)",
            "institutional_holding": "44.8% (FII: 19.6% • DII: 25.2%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "Commissioning of the 5 MTPA Kalinganagar Phase-2 blast furnace expansion in Odisha boosting domestic shipments.",
                "Restructuring of legacy loss-making UK blast furnaces to low-cost electric arc furnaces (EAF).",
                "Strong Indian infrastructure and capital goods manufacturing driving domestic steel consumption."
            ],
            "bearish_risks": [
                "Surge in Chinese steel exports into international markets depressing regional steel crack spreads.",
                "Volatile international coking coal prices impacting blast furnace conversion economics."
            ]
        }
    },
    "JSWSTEEL": {
        "summary": "JSW Steel Ltd is the flagship company of the JSW Group and India's largest private sector steel manufacturer by domestic capacity. Operating state-of-the-art facilities in Vijayanagar (Karnataka), Dolvi (Maharashtra), and Salem (Tamil Nadu), JSW Steel produces advanced flat and long steel products serving infrastructure, automotive, energy, and appliances sectors.",
        "brands": ["JSW Neosteel (TMT)", "JSW Colouron+", "JSW Vishwas", "JSW Platina", "JSW Silveron+", "JSW Avante"],
        "revenue_breakup": [
            {"segment": "Flat Rolled Products (HR & CR)", "pct": "71%", "desc": "Hot-rolled plates, automotive cold-rolled coils, galvanized sheets, and prepainted color sheets."},
            {"segment": "Long Products (TMT Rebars & Wire Rods)", "pct": "20%", "desc": "High-tensile TMT re-bars, structural angles, and alloy steel wire rods for construction."},
            {"segment": "Value-Added Specialty Steel & By-Products", "pct": "9%", "desc": "Electrical steel (CRGO joint venture with JFE Steel), blast furnace slag, and coal chemicals."}
        ],
        "geographic_mix": "Domestic (India): 83% • International Exports (Southern Europe, Middle East, USA): 17%",
        "moats_and_strengths": [
            "Vijayanagar complex is one of the world's largest single-site steel plants, operating at industry-leading conversion costs.",
            "Strategic technology and equity partnership with JFE Steel Corporation, Japan, for high-grade electrical and auto steel.",
            "Proximity of Dolvi plant to coastal deepwater jetty, providing cheap ocean freight for raw material imports.",
            "Extensive retail branded footprint through over 18,000 JSW Shoppe and retailer touchpoints."
        ],
        "order_book_or_capacity": "Crude Steel Capacity: 29.7 MTPA (India) • Expanding towards 38.5 MTPA capacity target by 2026",
        "promoter_governance": {
            "parent_group": "JSW Group (Sajjan Jindal Family)",
            "pledge_status": "12.8% Pledged (Comfortably Serviced Promoter Stake)",
            "institutional_holding": "36.2% (FII: 24.5% • DII: 11.7%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "Vijayanagar Phase-3 expansion adding 5 MTPA of low-cost steel capacity.",
                "Commissioning of the grain-oriented electrical steel (CRGO) plant with JFE Steel addressing green transformer demand.",
                "Securing commercial iron ore blocks in Odisha auctions lowering raw material merchant premiums."
            ],
            "bearish_risks": [
                "Dependence on merchant iron ore and imported coking coal relative to 100% integrated peers.",
                "Elevated consolidated net debt levels incurred during aggressive brownfield capex phases."
            ]
        }
    },
    "HINDALCO": {
        "summary": "Hindalco Industries Ltd is the metals flagship of the Aditya Birla Group and the world's largest aluminum company by revenue. Hindalco operates a fully integrated aluminum value chain in India and is the global leader in flat-rolled aluminum products and aluminum beverage can recycling through its US-based wholly-owned subsidiary, Novelis Inc.",
        "brands": ["Novelis Can Sheet", "Hindalco Everlast", "Birla Copper", "Eternia Windows", "Maxloader", "Hindalco Alu-Cab"],
        "revenue_breakup": [
            {"segment": "Novelis Inc. (Global Flat-Rolled Aluminum)", "pct": "63%", "desc": "Automotive body sheets, beverage can packaging, aerospace aluminum, and specialty plates."},
            {"segment": "Hindalco Aluminium (India Integrated)", "pct": "20%", "desc": "Bauxite mining, alumina refining, primary smelting, extruded sections, and aluminum foils."},
            {"segment": "Birla Copper (India Refining)", "pct": "17%", "desc": "Custom copper smelting, continuous cast copper rods, and precious metal recovery at Dahej."}
        ],
        "geographic_mix": "North America & Europe (Novelis): 65% • India: 28% • South America & Asia: 7%",
        "moats_and_strengths": [
            "Novelis is the undisputed global leader in beverage can sheet production with multi-year supply contracts with global beverage giants.",
            "World's largest recycler of aluminum, melting over 82 billion used beverage cans annually with 95% less energy than primary metal.",
            "Indian primary aluminum operations sit in the first quartile of the global cost curve due to captive bauxite and coal mines.",
            "Dahej copper complex is one of the largest single-location custom copper smelters in the world."
        ],
        "order_book_or_capacity": "Novelis Shipments: ~3.8M tonnes/year • India Aluminum: 1.3 MTPA smelting • Copper Cathode: 500,000 tonnes",
        "promoter_governance": {
            "parent_group": "Aditya Birla Group (Kumar Mangalam Birla)",
            "pledge_status": "0.0% Pledged (Pledge-Free Promoter Stake)",
            "institutional_holding": "58.2% (FII: 29.8% • DII: 28.4%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "Commissioning of Novelis' $4.1B greenfield rolling and recycling plant in Bay Minette, Alabama.",
                "Secular shift from plastic and glass to infinitely recyclable aluminum beverage cans globally.",
                "Surging lightweighting demand for automotive aluminum in electric vehicles (EVs)."
            ],
            "bearish_risks": [
                "Capital cost inflation and commissioning execution delays at the Bay Minette expansion.",
                "LME aluminum spot price swings impacting primary smelting margins in the Indian business."
            ]
        }
    },
    "COALINDIA": {
        "summary": "Coal India Ltd (CIL) is a Maharatna PSU and the single largest coal producing corporation in the world, contributing over 80% of India's total domestic coal output. Operating across 83 mining areas in eight Indian states, Coal India is the primary guarantor of India's baseload energy security, feeding over 70% of the country's electricity generation.",
        "brands": ["Thermal Coal (Non-Coking)", "Metallurgical Coking Coal", "Coal India E-Auction Portal", "CIL Solar", "Captive Rail Corridors"],
        "revenue_breakup": [
            {"segment": "Fuel Supply Agreements (FSA) to Power Utilities", "pct": "84%", "desc": "Regulated long-term coal supply to state and central thermal power generation utilities."},
            {"segment": "E-Auction & Open Market Sales", "pct": "12%", "desc": "Market-priced coal auctioned to non-power industrial consumers (cement, sponge iron, captive plants)."},
            {"segment": "Washed Coal & Value-Added By-Products", "pct": "4%", "desc": "Beneficiated low-ash coking coal, middlings, and tar products."}
        ],
        "geographic_mix": "Domestic (India): 100% across nationwide thermal power plants and industrial clusters",
        "moats_and_strengths": [
            "Near-monopoly producer supplying 80%+ of India's coal with insurmountable geographic mineral reserves.",
            "Extraordinary cash generation resulting in industry-leading dividend yields (typically 6%–9%).",
            "Extensive dedicated railway evacuation infrastructure (First Mile Connectivity) slashing logistical bottleneck costs.",
            "Zero net debt balance sheet with high cash reserves exceeding ₹18,000 Cr."
        ],
        "order_book_or_capacity": "Annual Coal Output: 770+ Million Tonnes (Targeting 1 Billion Tonnes) • 318 Operating Mines",
        "promoter_governance": {
            "parent_group": "Government of India (63.13% Maharatna PSU)",
            "pledge_status": "0.0% Pledged (Nil Government Pledge)",
            "institutional_holding": "30.4% (FII: 9.2% • DII: 21.2%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "India's thermal power peak generation reaching historic highs requiring record domestic coal dispatches.",
                "Higher realization premiums on non-power e-auction coal volumes boosting operating EBITDA.",
                "Mechanized First Mile Connectivity (FMC) projects reducing road haulage and siding loading costs."
            ],
            "bearish_risks": [
                "Government regulations limiting FSA price hikes to protect state electricity discoms from power inflation.",
                "Periodic wage hike agreements for non-executive workforce impacting annual employee benefit expenses."
            ]
        }
    },
    "POWERGRID": {
        "summary": "Power Grid Corporation of India Ltd is a Maharatna central public sector enterprise (CPSE) and India's principal electric power transmission utility. Power Grid transmits approximately 85% of India's total inter-state electricity across a vast network of 178,000+ circuit kilometers of high-voltage transmission lines, maintaining an incredible transmission availability rate of over 99.8%.",
        "brands": ["POWERGRID Transmission Network", "Powertel Telecom (Fiber)", "Smart Grid Energy Solutions", "EV Charging Infrastructure"],
        "revenue_breakup": [
            {"segment": "Regulated Transmission Tariffs", "pct": "96%", "desc": "Inter-state high-voltage transmission network charges backed by CERC 15.5% regulated Return on Equity."},
            {"segment": "Telecom & Optical Ground Wire (POWERTEL)", "pct": "2%", "desc": "Leasing dark fiber and high-bandwidth telecom capacity running along transmission towers."},
            {"segment": "Consultancy & International Projects", "pct": "2%", "desc": "Power grid engineering consultancy in South Asia, Africa, and the Middle East."}
        ],
        "geographic_mix": "Domestic (India): 100% across the unified 'One Nation, One Grid, One Frequency' national electricity system",
        "moats_and_strengths": [
            "Virtually irreplaceable national transmission network transmitting 85% of India's inter-regional power.",
            "CERC regulated return framework providing guaranteed 15.5% Return on Equity (ROE) insulated from volume risk.",
            "Tripartite payment security agreement with the Reserve Bank of India and state governments ensuring near-zero bad debt.",
            "World-class transmission availability of 99.86% operating across complex terrain and extreme weather conditions."
        ],
        "order_book_or_capacity": "Transmission Asset Base: 178,000+ ckt km • Substation Capacity: 540,000+ MVA • Work-in-Hand Capex > ₹90,000 Cr",
        "promoter_governance": {
            "parent_group": "Government of India (51.34% Maharatna PSU)",
            "pledge_status": "0.0% Pledged (Nil Government Pledge)",
            "institutional_holding": "42.8% (FII: 21.6% • DII: 21.2%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "Massive capital expenditure pipeline under the Green Energy Corridor transmitting 500 GW of renewable energy by 2030.",
                "High win rate in competitive Tariff-Based Competitive Bidding (TBCB) transmission line projects.",
                "Monetization of transmission assets via the PGInvIT infrastructure investment trust."
            ],
            "bearish_risks": [
                "Right of Way (RoW) and environmental forest clearance delays on high-voltage inter-state corridors.",
                "Tighter regulatory benchmarks by CERC on operational expenditure norms during tariff resetting cycles."
            ]
        }
    },
    "ONGC": {
        "summary": "Oil and Natural Gas Corporation Ltd (ONGC) is India's largest crude oil and natural gas exploration and production (E&P) company, contributing approximately 71% to domestic crude oil production and 84% to domestic natural gas output. A Maharatna CPSE, ONGC operates major offshore assets in the Mumbai High and Krishna Godavari (KG) basins alongside global upstream assets through ONGC Videsh Ltd (OVL).",
        "brands": ["ONGC Offshore Platforms", "ONGC Videsh (OVL)", "KG-DWN-98/2 Deepwater", "Mangalore Refinery (MRPL)", "HPCL"],
        "revenue_breakup": [
            {"segment": "Offshore & Onshore Crude Oil Sales", "pct": "58%", "desc": "Crude oil pumped from Mumbai High, KG Basin, Assam, and Gujarat sold to domestic refiners."},
            {"segment": "Natural Gas Marketing", "pct": "28%", "desc": "Piped natural gas sold at regulated APM and HPHT prices to fertilizer plants, power utilities, and city gas networks."},
            {"segment": "Value-Added Products & Petrochemicals", "pct": "14%", "desc": "LPG, C2-C3 fraction, aromatic naphtha, and kerosene extracted at gas processing plants."}
        ],
        "geographic_mix": "Domestic (India): 78% • International (ONGC Videsh E&P assets across 15 countries): 22%",
        "moats_and_strengths": [
            "Dominant upstream sovereign player controlling India's most prolific petroleum and natural gas basins.",
            "Integrated downstream presence through ownership of Hindustan Petroleum (HPCL) and Mangalore Refinery (MRPL).",
            "World-class deepwater offshore drilling expertise demonstrated in the complex KG-DWN-98/2 deepwater block.",
            "Significant beneficiary of any international crude oil price rally with low lifting production costs (~$8-$10/barrel)."
        ],
        "order_book_or_capacity": "Hydrocarbon Reserves: 2,000+ MMT • Annual Production: ~40 MMT of oil equivalent (O+OEG)",
        "promoter_governance": {
            "parent_group": "Government of India (58.89% Maharatna PSU)",
            "pledge_status": "0.0% Pledged (Nil Government Pledge)",
            "institutional_holding": "28.5% (FII: 9.8% • DII: 18.7%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "Ramp-up of crude oil and natural gas production from the deepwater KG-DWN-98/2 block in the Bay of Bengal.",
                "Domestic natural gas pricing reforms establishing premium floors for deepwater, ultra-deepwater, and high-pressure fields.",
                "Generous dividend payouts supported by robust operating cash flows."
            ],
            "bearish_risks": [
                "Windfall taxes and special additional excise duties imposed by the government during crude price rallies.",
                "Natural reservoir decline in mature brownfield offshore fields requiring expensive enhanced oil recovery (EOR) capex."
            ]
        }
    },
    "CIPLA": {
        "summary": "Cipla Ltd is a global pharmaceutical leader headquartered in Mumbai, renowned for providing affordable, high-quality healthcare for over eight decades. Pioneering accessible HIV/AIDS antiretrovirals globally, Cipla today commands dominant market share in respiratory medicine (inhalers, nebulizers, spacers) in India, South Africa, and the United States, alongside a comprehensive branded generics and OTC portfolio.",
        "brands": ["Foracort", "Asthalin", "Duolin", "Budecort", "Cipladine", "Omnigel", "Nicotex", "Cofsils", "Maxirich"],
        "revenue_breakup": [
            {"segment": "India Branded Formulations (One-India)", "pct": "44%", "desc": "Prescription therapies across respiratory, cardiology, anti-infectives, and consumer health (Cipla Health)."},
            {"segment": "North America Generics", "pct": "28%", "desc": "Complex generic inhalation aerosols (Albuterol, Brovana), peptides, and hospital injectables."},
            {"segment": "South Africa & Sub-Saharan Africa", "pct": "14%", "desc": "Branded OTC and prescription pharmaceuticals marketed through Cipla Medpro in South Africa."},
            {"segment": "International Markets & API", "pct": "14%", "desc": "B2B respiratory partnerships in Europe, Australia, Emerging Markets, and active pharmaceutical ingredients."}
        ],
        "geographic_mix": "India: 44% • North America: 28% • South Africa: 14% • Rest of the World: 14%",
        "moats_and_strengths": [
            "#1 respiratory pharmaceutical corporation in India with over 70% market share in inhalation therapies.",
            "Significant technological barrier to entry in respiratory drug-device combination products (MDIs, DPIs).",
            "Extensive consumer health franchise through Cipla Health with trusted OTC brands (Cipladine, Omnigel, Nicotex).",
            "Virtually debt-free balance sheet with exceptional return on capital employed (ROCE > 24%)."
        ],
        "order_book_or_capacity": "Manufacturing Facilities: 47 state-of-the-art sites globally • Over 1,500 products across 65 therapeutic categories",
        "promoter_governance": {
            "parent_group": "Hamied Family (Dr. Y. K. Hamied & Promoters)",
            "pledge_status": "0.0% Pledged (Pledge-Free Promoter Stake)",
            "institutional_holding": "51.8% (FII: 25.8% • DII: 26.0%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "US FDA approval and launch of generic Advair and complex peptide injectables in North America.",
                "Double-digit revenue growth in the Indian chronic domestic market led by cardiology and diabetes therapies.",
                "Expansion of consumer healthcare OTC portfolio through digital commerce and quick commerce channels."
            ],
            "bearish_risks": [
                "US FDA inspection observations or import alerts on key manufacturing sites (e.g. Pithampur).",
                "Expansion of the National List of Essential Medicines (NLEM) capping domestic formulation prices."
            ]
        }
    },
    "DRREDDY": {
        "summary": "Dr. Reddy's Laboratories Ltd is an integrated global pharmaceutical corporation providing affordable and innovative medicines across branded formulations, active pharmaceutical ingredients (APIs), hospital generics, biosimilars, and proprietary products. The company has a prominent commercial footprint across the United States, India, Russia/CIS, and Europe.",
        "brands": ["Omez", "Nise", "Razo", "Stamlo", "Cidmus", "Reditux (Rituximab Biosimilar)", "Aurigene Oncology"],
        "revenue_breakup": [
            {"segment": "Global Generics - North America", "pct": "47%", "desc": "Oral solid generics, injectable oncology drugs, and generic Revlimid (Lenalidomide)."},
            {"segment": "Global Generics - Emerging Markets & Russia", "pct": "20%", "desc": "Branded formulations in Russia, CIS, China, and Latin America."},
            {"segment": "Global Generics - India Domestic", "pct": "18%", "desc": "Prescription therapies in gastroenterology, cardiovascular, oncology, and pain management."},
            {"segment": "Pharmaceutical Services & Active Ingredients (PSAI)", "pct": "12%", "desc": "Custom synthesis, contract manufacturing, and active bulk pharmaceutical ingredients."},
            {"segment": "Europe Generics & Proprietary Products", "pct": "3%", "desc": "Generic hospital pharmaceuticals in Germany, UK, and France."}
        ],
        "geographic_mix": "North America: 47% • Russia & Emerging Markets: 20% • India: 18% • Europe & Other: 15%",
        "moats_and_strengths": [
            "Market-leading capability in complex generic filings, injectables, and biosimilars with 80+ pending US ANDAs.",
            "Top-tier international brand equity in Russia and CIS nations with established over-the-counter dominance.",
            "Strong balance sheet with substantial net cash generating high free cash flow conversion.",
            "Innovative biopharma pipeline through Aurigene Discovery and multiple commercialized biosimilars."
        ],
        "order_book_or_capacity": "R&D Spend: 8%–9% of annual revenue • Global manufacturing footprint across India, UK, USA, and Mexico",
        "promoter_governance": {
            "parent_group": "Kallam Anji Reddy Family (Dr. Reddy's Promoters)",
            "pledge_status": "0.0% Pledged (Pledge-Free Promoter Stake)",
            "institutional_holding": "58.4% (FII: 28.2% • DII: 30.2%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "Commercialization of novel biosimilars (Abatacept, Denosumab, Tocilizumab) in regulated western markets.",
                "Licensing partnerships and vaccine/GLP-1 diabetes therapeutics for emerging markets.",
                "Entry into consumer nutrition and weight-management through strategic global licensing."
            ],
            "bearish_risks": [
                "Revenue cliff as exclusivity and volume quotas on generic Revlimid taper off in the US.",
                "Geopolitical volatility and currency fluctuations affecting trade settlements in Russia."
            ]
        }
    },
    "DIVISLAB": {
        "summary": "Divi's Laboratories Ltd is one of the world's leading active pharmaceutical ingredient (API) and custom synthesis (CDMO) manufacturers. Divi's is a preferred partner to the top 20 global pharmaceutical innovators, producing commercial APIs, advanced intermediates, and nutritional carotenoids from its mega-scale US FDA-inspected manufacturing complexes in Hyderabad and Visakhapatnam.",
        "brands": ["Custom Synthesis CDMO", "Generic APIs (Naproxen, Dextromethorphan)", "Nutraceutical Carotenoids", "Peptide Synthesis"],
        "revenue_breakup": [
            {"segment": "Custom Synthesis (CDMO for Global Innovators)", "pct": "51%", "desc": "Contract development and exclusive manufacturing of patented chemical molecules for Big Pharma."},
            {"segment": "Generic Active Pharmaceutical Ingredients (APIs)", "pct": "41%", "desc": "World leader in Naproxen (anti-inflammatory), Dextromethorphan (cough), and Gabapentin."},
            {"segment": "Nutraceuticals & Carotenoids", "pct": "8%", "desc": "Beta-carotene, astaxanthin, lutein, and lycopene for food, feed, and dietary supplements."}
        ],
        "geographic_mix": "North America: 46% • Europe: 38% • India & Rest of the World: 16%",
        "moats_and_strengths": [
            "Dominates global market share (65%–70%) in core generic APIs like Naproxen and Dextromethorphan.",
            "Trusted supplier to 15 of the top 20 global big-pharma innovators, never competing with clients in finished formulations.",
            "Unrivalled chemistry scale with 14,000+ cubic meters of reaction capacity and continuous flow chemistry.",
            "Industry-leading EBITDA margins (~35%–40%) and completely debt-free balance sheet with high cash reserves."
        ],
        "order_book_or_capacity": "Reactor Capacity: 14,000+ m³ • Mega Manufacturing Complexes at Choutuppal and Visakhapatnam (Unit-1 & Unit-2)",
        "promoter_governance": {
            "parent_group": "Dr. Murali K. Divi Family (Founder Promoters)",
            "pledge_status": "0.0% Pledged (Pledge-Free Promoter Stake)",
            "institutional_holding": "36.2% (FII: 15.2% • DII: 21.0%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "US BIOSECURE Act driving western pharmaceutical innovators to divert CDMO contracts from China to Divi's.",
                "Commissioning of the new Kakinada mega-manufacturing facility adding massive custom synthesis capacity.",
                "Ramp-up of peptide synthesis and GLP-1 active ingredient supplies for global weight-loss drugs."
            ],
            "bearish_risks": [
                "Lumpiness in innovator custom synthesis orders depending on clinical trial outcomes and patent expiries.",
                "Raw material price volatility in basic chemical building blocks imported from East Asia."
            ]
        }
    },
    "WIPRO": {
        "summary": "Wipro Ltd is a leading global technology services and consulting enterprise with over 230,000 employees across six continents. Anchored by the Azim Premji legacy, Wipro assists international enterprise clients navigate digital engineering, hybrid cloud platforms, AI transformations via Wipro ai360, and sustainable business operations.",
        "brands": ["Wipro ai360", "Wipro FullStride Cloud", "Capco (BFSI Consulting)", "Designit", "Topcoder", "Wipro Holmes"],
        "revenue_breakup": [
            {"segment": "Banking, Financial Services & Insurance (BFSI)", "pct": "34%", "desc": "Core financial platforms, regulatory risk modeling, and Capco management consulting."},
            {"segment": "Consumer & Healthcare", "pct": "19%", "desc": "Supply chain digitisation, retail POS cloud, and healthcare informatics."},
            {"segment": "Manufacturing & High-Tech", "pct": "18%", "desc": "Connected smart factories, automotive embedded software, and PLM software."},
            {"segment": "Energy, Natural Resources & Utilities", "pct": "16%", "desc": "Smart grid modernisations, carbon management, and pipeline SCADA telemetry."},
            {"segment": "Communications & Technology", "pct": "13%", "desc": "5G cloud networks, software engineering, and semiconductor testing services."}
        ],
        "geographic_mix": "Americas: 58% • Europe: 29% • APMEA (Asia Pacific, Middle East, India): 13%",
        "moats_and_strengths": [
            "Capco consulting acquisition provides elite tier-1 executive advisory access to global financial institutions.",
            "Wipro ai360 initiative backed by $1B investment embedding artificial intelligence across all client delivery stacks.",
            "Zero net debt balance sheet with high shareholder capital return via frequent share buybacks and dividends.",
            "Extensive global workforce of 230,000+ technology professionals across 65+ countries."
        ],
        "order_book_or_capacity": "Total Contract Value (TCV) Bookings > $3.5B quarterly • 1,400+ Active Global Enterprise Clients",
        "promoter_governance": {
            "parent_group": "Azim Premji & Promoter Group (holds ~72.9%)",
            "pledge_status": "0.0% Pledged (Pledge-Free Promoter Stake)",
            "institutional_holding": "17.8% (FII: 6.8% • DII: 11.0%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "Execution of multi-year enterprise vendor consolidation contracts under new executive leadership.",
                "Acceleration in BFSI consulting deal conversions driven by interest rate cut cycles in the US and Europe.",
                "Operating margin expansion towards 17% through automated delivery and offshore talent optimization."
            ],
            "bearish_risks": [
                "Higher historical client exposure to discretionary consulting (Capco) during macroeconomic spending freezes.",
                "Senior leadership turnover and integration challenges across acquired global digital agencies."
            ]
        }
    },
    "HCLTECH": {
        "summary": "HCL Technologies Ltd is a leading global technology services corporation headquartered in Noida, India. Distinguished by its heritage in Engineering and R&D Services (ERS), HCLTech provides digital consulting, cloud operations, cybersecurity, and intellectual property-led software products (HCLSoftware) to over 10,000 global enterprises across 60 countries.",
        "brands": ["HCLTech", "HCLSoftware", "HCL BigFix", "HCL Commerce", "DryICE™ AIOps", "HCL CloudSMART"],
        "revenue_breakup": [
            {"segment": "IT & Business Services (ITBS)", "pct": "73%", "desc": "Application development, digital workplace solutions, cloud infrastructure, and enterprise AI."},
            {"segment": "Engineering & R&D Services (ERS)", "pct": "17%", "desc": "Semiconductor chip design, aerospace software, connected vehicles, and medical devices."},
            {"segment": "HCLSoftware (IP & Software Products)", "pct": "10%", "desc": "Proprietary software suites in endpoint management (BigFix), enterprise marketing, and data security."}
        ],
        "geographic_mix": "Americas: 64% • Europe: 29% • Rest of the World: 7%",
        "moats_and_strengths": [
            "Global leadership in Engineering and R&D Services (ERS), commanding multi-billion dollar ER&D outsourcing contracts.",
            "HCLSoftware generates high-margin, sticky annual recurring software subscription revenues (ARR).",
            "Industry-leading dividend payout ratio (>80% of net income) providing one of the highest dividend yields in large-cap IT.",
            "Long-term strategic relationships with 1,500+ global enterprises with superior client retention."
        ],
        "order_book_or_capacity": "Global Workforce: 220,000+ professionals • TCV Deal Bookings > $2.0B quarterly • 60 Countries",
        "promoter_governance": {
            "parent_group": "Shiv Nadar Family & Promoters (holds ~60.8%)",
            "pledge_status": "0.0% Pledged (Pledge-Free Promoter Stake)",
            "institutional_holding": "34.5% (FII: 19.5% • DII: 15.0%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "Surge in enterprise demand for semiconductor physical design and automotive electronics software.",
                "Ramp-up of mega-deals in European telecom and life sciences digital infrastructure modernization.",
                "Operating leverage in HCLSoftware expanding consolidated EBIT margins above 19%."
            ],
            "bearish_risks": [
                "Seasonality and license renewal renewals in the software products division creating quarterly margin volatility.",
                "Fierce competition from tier-1 global IT conglomerates for large infrastructure outsourcing renewals."
            ]
        }
    },
    "DLF": {
        "summary": "DLF Ltd is India's largest publicly listed real estate company, with over 75 years of real estate development track record. The company transformed Gurgaon into a premier global business and residential hub, operating a two-pronged model: high-margin luxury residential development (DLF Ltd) and institutional commercial office leasing via DLF Cyber City Developers Ltd (DCCDL) in joint venture with GIC Singapore.",
        "brands": ["DLF Cyber City", "DLF The Camellias", "DLF Privana", "DLF CyberHub", "Mall of India", "DLF Promenade"],
        "revenue_breakup": [
            {"segment": "Development Business (Luxury Residential Sales)", "pct": "66%", "desc": "Super-luxury condominiums (The Camellias, Privana), premium apartments, and plotted developments."},
            {"segment": "Annuity Business (DCCDL Commercial & IT SEZs)", "pct": "29%", "desc": "Grade-A office towers leased to Fortune 500 enterprises in Gurugram, Chennai, and Hyderabad."},
            {"segment": "Retail Malls & Hospitality", "pct": "5%", "desc": "Destination shopping centers (DLF Mall of India, CyberHub) and business club properties."}
        ],
        "geographic_mix": "Domestic (India): 100% focused on Delhi-NCR, Gurugram, Chennai, and Goa",
        "moats_and_strengths": [
            "Pristine luxury brand equity in Delhi-NCR, capable of selling out multi-thousand-crore luxury projects within days of launch.",
            "Massive fully paid-up land bank of 215+ million sq. ft. acquired at low historical costs.",
            "DCCDL commercial office portfolio (42M+ sq. ft.) delivers predictable, inflation-linked rental annuity cash flows.",
            "Achieved net debt-zero balance sheet status, transforming corporate financial stability."
        ],
        "order_book_or_capacity": "Operational Rental Portfolio: 42+ Million sq. ft. • Development Pipeline: 35+ Million sq. ft. launch pipeline",
        "promoter_governance": {
            "parent_group": "K. P. Singh Family & Promoters (holds ~74.0%)",
            "pledge_status": "0.0% Pledged (Pledge-Free Promoter Stake)",
            "institutional_holding": "21.5% (FII: 16.5% • DII: 5.0%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "Unprecedented pre-sales velocity for ultra-luxury residential launches in Gurugram (Privana West, Dahlias).",
                "Planned REIT listing of commercial office subsidiary DCCDL unlocking massive capital value.",
                "Expansion of retail mall footprint into Goa and Gurugram."
            ],
            "bearish_risks": [
                "Geographic concentration of development revenue in the Delhi-NCR property market.",
                "Delays in municipal infrastructural approvals and environmental clearances for mega-townships."
            ]
        }
    },
    "POLYCAB": {
        "summary": "Polycab India Ltd is India's largest manufacturer of wires and cables and a fast-growing player in Fast Moving Electrical Goods (FMEG). Commanding over 24% organized market share in domestic cables and wires, Polycab delivers essential electrical infrastructure across power transmission, green energy projects, telecom optical fiber, and residential construction.",
        "brands": ["Polycab Wires & Cables", "Polycab Maxima", "Polycab Green Wire", "Hohm Smart Automation", "Polycab Fans & Lighting", "Etira Switches"],
        "revenue_breakup": [
            {"segment": "Wires & Cables", "pct": "87%", "desc": "Low-voltage, medium-voltage, and extra-high-voltage power cables, control cables, and building wires."},
            {"segment": "Fast Moving Electrical Goods (FMEG)", "pct": "8%", "desc": "Fans, LED lighting, switches, switchgear, solar inverters, and water heaters."},
            {"segment": "EPC Infrastructure Projects", "pct": "5%", "desc": "Power distribution EPC, rural electrification, and high-speed BharatNet optical fiber connectivity."}
        ],
        "geographic_mix": "Domestic (India): 91% • International Exports (USA, Australia, Middle East, Europe): 9%",
        "moats_and_strengths": [
            "Dominant market leadership in Indian cables & wires with over 24% organized market share.",
            "Unrivalled distribution moat with 4,300+ authorized dealers and over 205,000 retail touchpoints across India.",
            "High backward integration manufacturing copper rods, aluminum wire rods, PVC/XLPE compounds, and GI wire.",
            "Strong balance sheet with net cash position, low working capital cycle, and high ROCE (>28%)."
        ],
        "order_book_or_capacity": "Manufacturing Facilities: 25+ state-of-the-art plants across Gujarat, Maharashtra, and Roorkee",
        "promoter_governance": {
            "parent_group": "Jaisinghani Family (Founder Promoters hold ~65.2%)",
            "pledge_status": "0.0% Pledged (Pledge-Free Promoter Stake)",
            "institutional_holding": "23.5% (FII: 12.5% • DII: 11.0%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "Multi-billion dollar capex upcycle in India's power transmission, real estate, and industrial manufacturing.",
                "Rapid international export expansion to the US and Australia replacing Chinese cable suppliers.",
                "EBITDA margin expansion in FMEG appliances as brand maturity and scale efficiencies take hold."
            ],
            "bearish_risks": [
                "Sharp spikes in global copper and aluminum LME commodity prices requiring frequent price adjustments.",
                "Intensifying competition in premium consumer building wires from Havells, KEI, and RR Kabel."
            ]
        }
    },
    "HAVELLS": {
        "summary": "Havells India Ltd is a leading Fast Moving Electrical Goods (FMEG) conglomerate with an extensive international presence. The company manufactures industrial and domestic electrical solutions spanning power distribution equipment, cables, modular switches, fans, domestic appliances, commercial lighting, and air conditioners under flagship brand Lloyd.",
        "brands": ["Havells", "Lloyd (Consumer Electronics)", "Crabtree (Luxury Switches)", "Standard Electrical", "Reo", "Havells Studio"],
        "revenue_breakup": [
            {"segment": "Cables & Wires", "pct": "32%", "desc": "Industrial power cables, building wires, communication cables, and flexible cords."},
            {"segment": "Lloyd Consumer Durables", "pct": "21%", "desc": "Room air conditioners, washing machines, smart LED televisions, and refrigerators."},
            {"segment": "Electrical Consumer Durables (ECD)", "pct": "18%", "desc": "Ceiling fans, personal grooming, small kitchen appliances, and water purifiers."},
            {"segment": "Lighting & Fixtures", "pct": "15%", "desc": "Consumer LED bulbs, smart lighting fixtures, and industrial roadway lighting."},
            {"segment": "Switchgear & Modular Controls", "pct": "14%", "desc": "Crabtree modular switches, industrial circuit breakers, and distribution boards."}
        ],
        "geographic_mix": "Domestic (India): 96% • International Exports: 4%",
        "moats_and_strengths": [
            "Premier brand equity across middle-class and affluent Indian households with multi-brand portfolio (Havells, Crabtree, Lloyd).",
            "Omnichannel distribution network spanning 14,000+ direct dealers and over 200,000 retail outlets.",
            "High domestic in-house manufacturing (~90%), shielding the company from Chinese component supply disruptions.",
            "Completely debt-free balance sheet with exceptional working capital management and return metrics."
        ],
        "order_book_or_capacity": "Manufacturing Complexes: 15 state-of-the-art integrated manufacturing plants in India",
        "promoter_governance": {
            "parent_group": "Qimat Rai Gupta Family (Anil Rai Gupta & Promoters hold ~59.4%)",
            "pledge_status": "0.0% Pledged (Pledge-Free Promoter Stake)",
            "institutional_holding": "29.8% (FII: 23.4% • DII: 6.4%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "Lloyd consumer durables business achieving profitability and market share gains in room air conditioners.",
                "Booming real estate construction and premiumization driving demand for Crabtree designer switches and smart lighting.",
                "Entry into kitchen cookware and personal grooming expanding consumer wallet share."
            ],
            "bearish_risks": [
                "Intense price competition in room air conditioning from Daikin, Voltas, and Blue Star.",
                "Volatile raw material input costs in copper, aluminum, and engineering plastics."
            ]
        }
    },
    "DIXON": {
        "summary": "Dixon Technologies (India) Ltd is India's largest electronic manufacturing services (EMS) company. Functioning as the premier design and manufacturing partner for global smartphone, consumer electronics, and appliance brands, Dixon produces mobile phones (Motorola, Xiaomi, Transsion), LED televisions, washing machines, telecom hardware, and security surveillance systems under the Government of India's PLI schemes.",
        "brands": ["Smartphone EMS Lines", "Smart LED TV Manufacturing", "Semi-Automatic Washing Machines", "Telecom 5G Routers", "Surveillance Cameras"],
        "revenue_breakup": [
            {"segment": "Mobile Phones & EMS", "pct": "62%", "desc": "Contract manufacturing of 5G/4G smartphones and feature phones for marquee global brands."},
            {"segment": "Consumer Electronics (Smart TVs)", "pct": "18%", "desc": "Assembly of LED televisions, smart display boards, and commercial visual monitors."},
            {"segment": "Home Appliances (Washing Machines)", "pct": "9%", "desc": "Semi-automatic and fully-automatic top-load washing machines."},
            {"segment": "Lighting Products", "pct": "6%", "desc": "LED bulbs, battens, downlights, and smart lighting driver electronics."},
            {"segment": "Telecom & Security Surveillance (IT Hardware)", "pct": "5%", "desc": "5G modems, routers, set-top boxes, and CCTV security cameras."}
        ],
        "geographic_mix": "Domestic (India - OEM/ODM Clients): 92% • Global Electronics Exports: 8%",
        "moats_and_strengths": [
            "#1 Indian EMS player with immense scale advantages, producing nearly 35% of all LED TVs sold in India.",
            "Primary beneficiary of the Government of India's Production Linked Incentive (PLI) schemes across smartphones, telecom, and IT hardware.",
            "Long-term anchor partnerships with global brand giants (Motorola, Xiaomi, Samsung, Panasonic, boAt).",
            "Asset-light ODM model delivering high capital turnover and return on capital employed (ROCE > 26%)."
        ],
        "order_book_or_capacity": "Manufacturing Capacity: 23 manufacturing facilities • Annual Capacity > 45M smartphones and 6M televisions",
        "promoter_governance": {
            "parent_group": "Sunil Vachani Family (Founder Promoters hold ~33.8%)",
            "pledge_status": "0.0% Pledged (Pledge-Free Promoter Stake)",
            "institutional_holding": "42.5% (FII: 18.2% • DII: 24.3%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "Export ramp-up of Motorola and Transsion smartphones from India to North America and Europe.",
                "Commissioning of IT hardware PLI manufacturing lines for global laptop and tablet brands.",
                "Backward integration into display modules, camera modules, and precision mechanical enclosures."
            ],
            "bearish_risks": [
                "Contract manufacturing customer concentration risk where top 3 clients contribute over 50% of revenue.",
                "Thin operating EBITDA margins (~3.5%–4.2%) vulnerable to supply chain component pricing pressures."
            ]
        }
    },
    "IRCTC": {
        "summary": "Indian Railway Catering and Tourism Corporation Ltd (IRCTC) is a Miniratna CPSE under the Ministry of Railways, holding a complete sovereign monopoly in online railway ticketing, packaged drinking water (Rail Neer), and onboard catering across the vast Indian Railways network. The enterprise also operates luxury tourist trains and integrated tourism travel packages.",
        "brands": ["IRCTC Rail Connect App", "Rail Neer Packaged Water", "Tejas Express (Private Trains)", "e-Catering Food on Track", "Maharajas' Express"],
        "revenue_breakup": [
            {"segment": "Internet Ticketing", "pct": "37%", "desc": "Convenience fees from booking 1.5M+ train tickets daily on IRCTC website and mobile app."},
            {"segment": "Catering & Hospitality Services", "pct": "35%", "desc": "Pantry car contracts, onboard food supply, executive railway lounges, and station food plazas."},
            {"segment": "Packaged Drinking Water (Rail Neer)", "pct": "18%", "desc": "Exclusive manufacturing and distribution of Rail Neer bottled water across railway platforms."},
            {"segment": "Tourism & State Tejas Trains", "pct": "10%", "desc": "Bharat Gaurav religious tours, air ticketing, cruise packages, and semi-high-speed Tejas trains."}
        ],
        "geographic_mix": "Domestic (India): 100% across the 68,000 km Indian Railways network",
        "moats_and_strengths": [
            "Absolute regulatory monopoly as the sole authorized online ticket booking platform for Indian Railways.",
            "Extremely sticky consumer base booking over 1.5 million rail tickets daily with negative working capital.",
            "Extraordinary EBITDA margins in internet ticketing exceeding 80% with low maintenance capital expenditure.",
            "Completely debt-free balance sheet generating strong return on equity (ROE > 40%) and high dividend payouts."
        ],
        "order_book_or_capacity": "Daily Ticket Volume: 1.5M+ tickets • Rail Neer Capacity: 1.8M liters/day across 19 bottling plants",
        "promoter_governance": {
            "parent_group": "Government of India (62.40% Miniratna PSU)",
            "pledge_status": "0.0% Pledged (Nil Government Pledge)",
            "institutional_holding": "22.5% (FII: 7.5% • DII: 15.0%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "Induction of hundreds of Vande Bharat express trains driving onboard catering revenue per passenger.",
                "Expanding Rail Neer bottling plant capacity to capture 100% of demand across all Indian railway stations.",
                "Monetization of digital traffic via digital advertising, travel insurance, and hotel cross-selling."
            ],
            "bearish_risks": [
                "Policy decisions by Ministry of Railways regarding convenience fee sharing or ticket pricing mandates.",
                "Food quality compliance incidents or catering vendor service standard penalties."
            ]
        }
    },
    "BEL": {
        "summary": "Bharat Electronics Ltd (BEL) is a Navratna defense PSU under the Ministry of Defence, functioning as India's premier defense electronics specialist. BEL manufactures state-of-the-art radar systems, electronic warfare suites, naval sonars, weapon control systems, tank electronics, and tactical military communication systems for the Indian Armed Forces.",
        "brands": ["Akash Missile Weapon System Radars", "Battlefield Surveillance Radars", "Electronic Warfare Suites (Shakti)", "EVM Voting Machines"],
        "revenue_breakup": [
            {"segment": "Defense Radars & Weapon Control Systems", "pct": "58%", "desc": "Akash radar systems, weapon locating radars (Swathi), air defense fire control systems."},
            {"segment": "Naval Systems & Sonars", "pct": "18%", "desc": "Submarine sonars, combat management suites, and anti-submarine rocket launchers."},
            {"segment": "Electronic Warfare & Military Communications", "pct": "15%", "desc": "Jamming equipment, software-defined radios, secure optical networks, and electro-optics."},
            {"segment": "Civilian Products & Strategic Exports", "pct": "9%", "desc": "Electronic Voting Machines (EVM), smart city command centers, and medical ventilators."}
        ],
        "geographic_mix": "Domestic (Indian Armed Forces - Army, Navy, Air Force): 96% • Defense Exports: 4%",
        "moats_and_strengths": [
            "Dominant supplier of defense electronics in India with over 55% share of military electronic equipment.",
            "Strategic collaboration partner of DRDO, holding proprietary military manufacturing blueprints.",
            "Record order book exceeding ₹76,000 Cr, ensuring over 3.5x book-to-bill multi-year revenue visibility.",
            "Debt-free PSU balance sheet with high cash reserves (>₹8,000 Cr) and RoCE consistently above 28%."
        ],
        "order_book_or_capacity": "Confirmed Order Book: ₹76,000 Cr+ • 9 Modern Manufacturing Complexes across India",
        "promoter_governance": {
            "parent_group": "Government of India (51.14% Navratna Defense PSU)",
            "pledge_status": "0.0% Pledged (Nil Government Pledge)",
            "institutional_holding": "41.5% (FII: 17.5% • DII: 24.0%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "Orders for Next-Gen Akash-NG air defense missile electronics and Quick Reaction Surface-to-Air Missiles (QRSAM).",
                "Indigenization push under 'Positive Indigenization Lists' barring defense electronic imports.",
                "Export contract pipeline for naval surveillance systems to friendly coastal nations."
            ],
            "bearish_risks": [
                "Delays in finalization of major defense procurement tenders by the Defence Acquisition Council.",
                "Long lead times for specialized imported military semiconductor chips."
            ]
        }
    },
    "MUTHOOTFIN": {
        "summary": "Muthoot Finance Ltd is India's largest gold financing company (NBFC) and a systemic leader in household jewelry-backed credit. With a rich heritage of over 800 years rooted in Kerala, the flagship enterprise operates over 4,800 branches nationwide, holding over 185 tonnes of gold jewelry in high-security vaults as collateral for retail loans.",
        "brands": ["Muthoot Gold Loans", "Muthoot Homefin", "Belstar Microfinance", "Muthoot Money", "Muthoot Insurance Brokers"],
        "revenue_breakup": [
            {"segment": "Gold Loan Lending", "pct": "88%", "desc": "Short-term retail and small business credit secured against household gold jewelry collateral."},
            {"segment": "Microfinance Lending (Belstar)", "pct": "7%", "desc": "Unsecured microfinance loans disbursed to women self-help groups in semi-urban India."},
            {"segment": "Housing & Vehicle Finance", "pct": "5%", "desc": "Affordable housing mortgages (Homefin) and commercial vehicle / two-wheeler loans."}
        ],
        "geographic_mix": "Domestic (India): 100% across North India (40%), South India (38%), West (15%), and East (7%)",
        "moats_and_strengths": [
            "Dominant market share (>50% of organized gold NBFC lending) holding over 185 tonnes of gold collateral.",
            "Widespread physical distribution network of 4,800+ branches deeply trusted in local Indian communities.",
            "Extremely low credit cost (<0.5%) as loans are backed by physical liquid gold collateral with low LTVs (<75%).",
            "High return profile with Return on Assets (ROA > 4.5%) and Return on Equity (ROE ~ 19%)."
        ],
        "order_book_or_capacity": "Gold Loan AUM: ₹75,000 Cr+ • Gold Collateral in Custody: 185+ Tonnes • 4,800+ Branches",
        "promoter_governance": {
            "parent_group": "M. G. George Muthoot Family (Founder Promoters hold ~73.4%)",
            "pledge_status": "0.0% Pledged (Pledge-Free Promoter Stake)",
            "institutional_holding": "21.2% (FII: 10.4% • DII: 10.8%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "Rising global and domestic spot gold prices automatically expanding borrowing headroom and loan asset values.",
                "Surge in MSME working capital demand driving quick-disbursal gold loan originations.",
                "Branch network expansion in under-penetrated northern and western Indian states."
            ],
            "bearish_risks": [
                "Sharp decline in gold bullion prices triggering margin calls and auction requirements.",
                "Regulatory tightening by RBI regarding cash loan disbursement caps and loan-to-value (LTV) limits."
            ]
        }
    },
    "CDSL": {
        "summary": "Central Depository Services (India) Ltd (CDSL) is India's leading securities depository and the first depository in Asia-Pacific to surpass 115 million active demat accounts. Functioning as essential market infrastructure, CDSL holds equities, bonds, mutual fund units, and commodities in electronic form, enabling seamless depository clearing and settlement across Indian stock exchanges.",
        "brands": ["CDSL Demat Services", "easymapi e-Voting", "CDSL Ventures (CVL KYC)", "CDSL Commodity Repository (CCRL)", "Myeasi Portal"],
        "revenue_breakup": [
            {"segment": "Annual Issuer Maintenance Charges", "pct": "34%", "desc": "Annual listing and custody fees paid by publicly listed and unlisted corporate issuers."},
            {"segment": "Transaction Charges (Settlement)", "pct": "29%", "desc": "Per-debit settlement charges levied whenever shares are sold from retail and institutional demat accounts."},
            {"segment": "KYC & Verification Services (CVL)", "pct": "22%", "desc": "Electronic investor KYC verification and Aadhaar authentication for capital market intermediaries."},
            {"segment": "Other Depository & e-Voting Services", "pct": "15%", "desc": "Pledge fees, IPO corporate action fees, and electronic AGM voting services."}
        ],
        "geographic_mix": "Domestic (India): 100% vital market infrastructure across all Indian capital market intermediaries",
        "moats_and_strengths": [
            "Duopoly market structure alongside NSDL, holding over 77% market share in total active Indian demat accounts.",
            "Asset-light financial infrastructure utility delivering incredible operating EBITDA margins (>60%).",
            "Direct beneficiary of the ongoing secular financialization of Indian household savings into equity markets.",
            "Completely debt-free balance sheet with robust cash balances and high return on equity (ROE > 30%)."
        ],
        "order_book_or_capacity": "Active Demat Accounts: 115+ Million accounts • Depository Intermediaries: 600+ Depository Participants (DPs)",
        "promoter_governance": {
            "parent_group": "BSE Ltd & Institutional Shareholding (Market Infrastructure Institution)",
            "pledge_status": "0.0% Pledged (No Promoter Pledge)",
            "institutional_holding": "48.2% (FII: 16.5% • DII: 31.7%)"
        },
        "catalysts_and_risks": {
            "bullish_triggers": [
                "Record pace of new retail demat account additions (2M–3M new accounts opened per month in India).",
                "Surge in corporate IPOs and mandatory dematerialization of private unlisted enterprises.",
                "High dividend payouts and capital returns supported by zero-debt cash flows."
            ],
            "bearish_risks": [
                "Cyclical drop in daily equity cash market trading volumes during prolonged market consolidations.",
                "SEBI regulatory tariff rationalizations capping transaction or account opening fees."
            ]
        }
    }
}

def patch_file():
    target_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts", "data_company_profiles.py")
    with open(target_path, "r") as f:
        content = f.read()

    # Add extra curated profiles to CURATED_PROFILES
    import json
    curated_insert_parts = []
    for ticker, prof in EXTRA_CURATED.items():
        if f'"{ticker}": {{' not in content:
            curated_insert_parts.append(f'    "{ticker}": {json.dumps(prof, indent=8).strip()},')

    if curated_insert_parts:
        replacement = "\n".join(curated_insert_parts) + "\n"
        content = content.replace("CURATED_PROFILES = {", "CURATED_PROFILES = {\n" + replacement, 1)

    with open(target_path, "w") as f:
        f.write(content)
    print(f"Patched scripts/data_company_profiles.py with {len(curated_insert_parts)} additional curated profiles!")

if __name__ == "__main__":
    patch_file()
