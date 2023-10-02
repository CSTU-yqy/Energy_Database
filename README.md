EIA ENERGY DATA / EIA ENERGY DATA2 Folder Structure


A snapshot of each key folder's function is provided to help users find the data they want:

* `/data/data/`: This folder stores the air quality data from the EPA as well as all the energy-related data.
    * `12_aqs/`: Air quality data from EPA.
        * `data/`: This folder contains state-level air quality data and a full set of parameters involved in all query functions.
            * `map/`: The full set of the parameters involved in all query function.
            * `state/`: State-level air quality data.
    * `energy_data/`: Energy data from the [project data item sheet](https://www.dropbox.com/s/t9qu97yoliq3mb0/energy%20data%20sources.xlsx?dl=0).
        * `11_eiv/`: [Data item 11: EIA us energy atlas](https://atlas.eia.gov/search) and [Data item 5: EIA-solar energy infrastructure and resources](https://atlas.eia.gov/apps/solar/explore)
            * `README.txt/`: A brief introduction to data item 11, along with all the file types associated with it.
            * `data/`: All the data associated with data item 11, as well as the data from data item 5, is included in the '/Power Plants' directory.
        * `3_wind_turbine/`: [Data item 3: USGS - wind turbine database](https://eerscmap.usgs.gov/uswtdb/)
            * `data/`: A database of wind turbines queried from the official API.
        * `6_electricity/`: [Data item 6: EIA - electrciity data browser](https://www.eia.gov/electricity/data/browser/#/plant/63344)
            * `data/`: There are two methods to download the datasets: 'Change data set' and 'View a pre-generated report'. Currently, the datasets have been sourced from all the options within 'View a pre-generated report' and the 'Change data set' option.
                * `annual/`: Annual data from the options available under 'View a pre-generated report' and 'Change data set' option.
                * `monthly/`: Monthly data from the options available under 'View a pre-generated report' and 'Change data set' option.
                * `quarterly/`: Quarterly data from the options available under 'View a pre-generated report' and 'Change data set' option.
        * `6_electricity_beta/`: [Data item 6: EIA - electrciity data browser Beta](https://www.eia.gov/beta/electricity/data/browser/#/topic/1?agg=2,0,1&fuel=vtvv&sec=g&geo=g&freq=M&datecode=202001&tab=generation&pin=&rse=0&maptype=0&ltype=pin&ctype=linechart&end=201710&start=200101)
            * `data/`: An updated version of electricity data browser in data item 6 with addtional information about generation, consumption, water, and annual emissions.
                * `annual/`: Annual data from the options available under 'View a pre-generated report' and 'Change data set' option.
                * `monthly/`: Monthly data from the options available under 'View a pre-generated report' and 'Change data set' option.
                * `quarterly/`: Quarterly data from the options available under 'View a pre-generated report' and 'Change data set' option.
        * `9_energy_dept/`: [Data item 9: Energy dept - wind](https://www.energy.gov/eere/wind/wind-resource-assessment-and-characterization) and [Data item 8: Energy department - environmental impact - wind projects](https://www.energy.gov/eere/wind/environmental-impacts-and-siting-wind-projects)
            * `data/`: The Wind Energy Technologies Office Projects Map includes information on the 'Project Title', 'Awardee Program Area', 'DOE Funding Amount', 'Recipient Type', 'Award Type', and 'State(s)'. The project map in data item 8 is identical to the project map in data item 9.
        * `2_renewable_alternative_fuels/`: [Data item 2: EIA - renewable & alternative fuels](https://www.eia.gov/renewable/monthly/solar_photo/)
            * `data/`: Data tables in Monthly Solar Photovoltaic Module Shipments Report from 2017/10 to 2023/05 including:
                * Table 1. U.S. photovoltaic industry status, Table 2. Value and average value of photovoltaic module shipments
                * Table 2. Value and average value of photovoltaic module shipments
                * Table 3. Monthly photovoltaic module shipments
                * Table 4. Average value of photovoltaic modules
                * Table 5. Source and disposition of photovoltaic cell shipments
                * Table 6. Source and disposition of photovoltaic module shipments
                * Table 7. Photovoltaic module import shipments by country
                * Table 8. Destination of photovoltaic module export shipments
                * Table 9. U.S. photovoltaic module shipments by state or territory
    * `energy_price/`: LMP (Locational Marginal Price) data from various regions, or Price data exclusively for ERCOT.
        * `data/`: LMP (Locational Marginal Price) data from various ISOs, or Price data specifically for ERCOT.
            * `CAISO.zip/`: [CAISO - California ISO](http://oasis.caiso.com/mrioasis/logon.do)
            * `ERCOT.zip/`: [Electric Reliability Council of Texas (ERCOT); also a Regional Reliability Council](https://www.ercot.com/mktinfo/prices)
            * `MISO.zip/`: [Midcontinent Independent System Operator - Midcontinent ISO](https://www.misoenergy.org/markets-and-operations/real-time--market-data/market-reports/market-report-archives/#nt=)
            * `NewEnglandISO.zip/`: [ISO-NE - ISO New England](https://www.iso-ne.com/isoexpress/web/reports/pricing/-/tree/lmps-da-hourly)
            * `NYISO.zip/`: [NYISO - New York ISO](https://www.nyiso.com/energy-market-operational-data)
            * `SPPISO/`: [SPP - Southwest Power Pool](https://marketplace.spp.org/pages/rtbm-lmp-by-location)
                * `DAM/`: Day-Ahead Market
                * `RTM/`: Real-Time Market
    * `tool/`: 
        * `folder_tree.py/`: A self-built tool to assist in creating customized folder trees.
        * `unzip.py/`: A self-built tool to assist in extracting ZIP files.

Additional Information: Only the key folders are outlined here, with the aim of highlighting the primary sources users should focus on.

The folder structure is organized as follows:
```
/data/data/
    12_aqs/
        code/
        ├── AQS_api_state.py
        ├── email_signup.py
        ├── run_state.py
        data/
            map/
            ├── cbsa.json
            ├── county.json
            ├── mas.json
            ├── param.json
            ├── pclass.json
            ├── pqao.json
            ├── site.json
            ├── state.json
            raw_request/
            state/
                01/
                02/
                04/
                05/
                06/
                08/
                09/
                10/
                11/
                12/
                13/
                15/
                16/
                17/
                18/
                20/
                22/
                23/
                24/
                26/
                28/
                29/
                30/
                32/
                34/
                38/
                40/
                45/
                47/
                54/
    energy_data/
        11_eiv/
        ├── README.txt
            code/
            ├── 11.py
            ├── energy_structure.ipynb
            ├── fields_description.py
            ├── table_description_and_tag_list.py
            ├── test.ipynb
            data/
                0_database_summary/
                ├── data_description.csv
                ├── fields_explanation.csv
                ├── tag_list.csv
                2020 USA Population Density/
                ├── description.json
                ├── summary.txt
                ├── update.txt
                Accumulation by Time/
                ├── description.json
                ├── National_Weather_Service_Precipitation_Forecast.csv
                ├── National_Weather_Service_Precipitation_Forecast.geojson
                ├── National_Weather_Service_Precipitation_Forecast.kml
                ├── National_Weather_Service_Precipitation_Forecast.zip
                ├── summary.txt
                Active Hurricanes, Cyclones and Typhoons/
                Amount by Time/
                ├── description.json
                ├── National_Weather_Service_Precipitation_Forecast.csv
                ├── National_Weather_Service_Precipitation_Forecast.geojson
                ├── National_Weather_Service_Precipitation_Forecast.kml
                ├── National_Weather_Service_Precipitation_Forecast.zip
                ├── summary.txt
                Biodiesel Plants/
                ├── Biodiesel_Plants.csv
                ├── Biodiesel_Plants.gdb.zip
                ├── Biodiesel_Plants.geojson
                ├── Biodiesel_Plants.kml
                ├── Biodiesel_Plants.zip
                ├── description.json
                ├── summary.txt
                Border Crossings - Electricity/
                ├── Border_Crossings_-_Electricity.csv
                ├── Border_Crossings_-_Electricity.gdb.zip
                ├── Border_Crossings_-_Electricity.geojson
                ├── Border_Crossings_-_Electricity.kml
                ├── Border_Crossings_-_Electricity.zip
                ├── description.json
                ├── summary.txt
                Border Crossings - Liquids/
                ├── Border_Crossings_-_Liquids.csv
                ├── Border_Crossings_-_Liquids.gdb.zip
                ├── Border_Crossings_-_Liquids.geojson
                ├── Border_Crossings_-_Liquids.kml
                ├── Border_Crossings_-_Liquids.zip
                ├── description.json
                ├── summary.txt
                Border Crossings - Natural Gas/
                ├── Border_Crossings_-_Natural_Gas.csv
                ├── Border_Crossings_-_Natural_Gas.gdb.zip
                ├── Border_Crossings_-_Natural_Gas.geojson
                ├── Border_Crossings_-_Natural_Gas.kml
                ├── Border_Crossings_-_Natural_Gas.zip
                ├── description.json
                ├── summary.txt
                Buoys/
                ├── Current_Weather_and_Wind_Station_Data.csv
                ├── Current_Weather_and_Wind_Station_Data.geojson
                ├── Current_Weather_and_Wind_Station_Data.kml
                ├── Current_Weather_and_Wind_Station_Data.zip
                ├── description.json
                ├── summary.txt
                Climate Zones - DOE Building America Program/
                ├── Climate_Zones_-_DOE_Building_America_Program.csv
                ├── Climate_Zones_-_DOE_Building_America_Program.geojson
                ├── Climate_Zones_-_DOE_Building_America_Program.kml
                ├── Climate_Zones_-_DOE_Building_America_Program.zip
                ├── description.json
                ├── summary.txt
                Coal Mines/
                ├── Coal_Mines.csv
                ├── Coal_Mines.geojson
                ├── Coal_Mines.kml
                ├── Coal_Mines.zip
                ├── description.json
                ├── summary.txt
                Coastal and Offshore Marine Zones/
                ├── description.json
                ├── summary.txt
                ├── USA_Weather_Watches_and_Warnings.csv
                ├── USA_Weather_Watches_and_Warnings.geojson
                ├── USA_Weather_Watches_and_Warnings.kml
                ├── USA_Weather_Watches_and_Warnings.zip
                Crude Oil Pipelines/
                ├── Crude_Oil_Pipelines.csv
                ├── Crude_Oil_Pipelines.gdb.zip
                ├── Crude_Oil_Pipelines.geojson
                ├── Crude_Oil_Pipelines.kml
                ├── Crude_Oil_Pipelines.zip
                ├── description.json
                ├── summary.txt
                Crude Oil Rail Terminals/
                ├── Crude_Oil_Rail_Terminals.csv
                ├── Crude_Oil_Rail_Terminals.gdb.zip
                ├── Crude_Oil_Rail_Terminals.geojson
                ├── Crude_Oil_Rail_Terminals.kml
                ├── Crude_Oil_Rail_Terminals.zip
                ├── description.json
                ├── summary.txt
                Cumulative Total/
                ├── description.json
                ├── National_Weather_Service_Precipitation_Forecast.csv
                ├── National_Weather_Service_Precipitation_Forecast.geojson
                ├── National_Weather_Service_Precipitation_Forecast.kml
                ├── National_Weather_Service_Precipitation_Forecast.zip
                ├── summary.txt
                Current Incidents/
                ├── description.json
                ├── summary.txt
                ├── USA_Current_Wildfires.csv
                ├── USA_Current_Wildfires.geojson
                ├── USA_Current_Wildfires.kml
                ├── USA_Current_Wildfires.zip
                Current Perimeters/
                ├── description.json
                ├── summary.txt
                ├── USA_Current_Wildfires.csv
                ├── USA_Current_Wildfires.geojson
                ├── USA_Current_Wildfires.kml
                ├── USA_Current_Wildfires.zip
                Current Weather and Wind Station Data/
                ├── Current_Weather_and_Wind_Station_Data.csv
                ├── Current_Weather_and_Wind_Station_Data.geojson
                ├── Current_Weather_and_Wind_Station_Data.kml
                ├── Current_Weather_and_Wind_Station_Data.zip
                ├── description.json
                ├── summary.txt
                Electric Retail Service Territories/
                ├── description.json
                ├── Electric_Retail_Service_Territories.csv
                ├── Electric_Retail_Service_Territories.geojson
                ├── Electric_Retail_Service_Territories.kml
                ├── Electric_Retail_Service_Territories.zip
                ├── summary.txt
                Ethanol Plants/
                ├── description.json
                ├── Ethanol_Plants.csv
                ├── Ethanol_Plants.gdb.zip
                ├── Ethanol_Plants.geojson
                ├── Ethanol_Plants.kml
                ├── Ethanol_Plants.zip
                ├── summary.txt
                Ethylene Crackers/
                ├── description.json
                ├── Ethylene_Crackers.csv
                ├── Ethylene_Crackers.gdb.zip
                ├── Ethylene_Crackers.geojson
                ├── Ethylene_Crackers.kml
                ├── Ethylene_Crackers.zip
                ├── summary.txt
                Events Ordered by Size and Severity/
                ├── description.json
                ├── summary.txt
                ├── USA_Weather_Watches_and_Warnings.csv
                ├── USA_Weather_Watches_and_Warnings.geojson
                ├── USA_Weather_Watches_and_Warnings.kml
                ├── USA_Weather_Watches_and_Warnings.zip
                Extreme Events/
                ├── description.json
                ├── summary.txt
                ├── USA_Weather_Watches_and_Warnings.csv
                ├── USA_Weather_Watches_and_Warnings.geojson
                ├── USA_Weather_Watches_and_Warnings.kml
                ├── USA_Weather_Watches_and_Warnings.zip
                Fire Forecast Zones/
                ├── description.json
                ├── summary.txt
                ├── USA_Weather_Watches_and_Warnings.csv
                ├── USA_Weather_Watches_and_Warnings.geojson
                ├── USA_Weather_Watches_and_Warnings.kml
                ├── USA_Weather_Watches_and_Warnings.zip
                Forecast Error Cone/
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.csv
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.geojson
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.kml
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.zip
                ├── description.json
                ├── summary.txt
                Forecast Position/
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.csv
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.geojson
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.kml
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.zip
                ├── description.json
                ├── summary.txt
                Forecast Track/
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.csv
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.geojson
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.kml
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.zip
                ├── description.json
                ├── summary.txt
                Geothermal Potential/
                ├── description.json
                ├── Geothermal_Potential.csv
                ├── Geothermal_Potential.geojson
                ├── Geothermal_Potential.kml
                ├── Geothermal_Potential.zip
                ├── summary.txt
                Hurricane Force (64kts+)/
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.csv
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.geojson
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.kml
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.zip
                ├── description.json
                ├── summary.txt
                Hydrocarbon Gas Liquids (HGL) Market Hubs/
                ├── description.json
                ├── Hydrocarbon_Gas_Liquids_(HGL)_Market_Hubs.csv
                ├── Hydrocarbon_Gas_Liquids_(HGL)_Market_Hubs.geojson
                ├── Hydrocarbon_Gas_Liquids_(HGL)_Market_Hubs.kml
                ├── Hydrocarbon_Gas_Liquids_(HGL)_Market_Hubs.zip
                ├── summary.txt
                Hydrocarbon Gas Liquids (HGL) Pipelines/
                ├── description.json
                ├── Hydrocarbon_Gas_Liquids_(HGL)_Pipelines.csv
                ├── Hydrocarbon_Gas_Liquids_(HGL)_Pipelines.gdb.zip
                ├── Hydrocarbon_Gas_Liquids_(HGL)_Pipelines.geojson
                ├── Hydrocarbon_Gas_Liquids_(HGL)_Pipelines.kml
                ├── Hydrocarbon_Gas_Liquids_(HGL)_Pipelines.zip
                ├── summary.txt
                Liquid Natural Gas (LNG) Import and Export Terminals/
                ├── description.json
                ├── Liquid_Natural_Gas_(LNG)_Import_and_Export_Terminals.csv
                ├── Liquid_Natural_Gas_(LNG)_Import_and_Export_Terminals.gdb.zip
                ├── Liquid_Natural_Gas_(LNG)_Import_and_Export_Terminals.geojson
                ├── Liquid_Natural_Gas_(LNG)_Import_and_Export_Terminals.kml
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Abo-Yeso Play Extent/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Abo-Yeso_Play_Extent.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Abo-Yeso_Play_Extent.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Abo-Yeso_Play_Extent.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Abo-Yeso_Play_Extent.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Abo-Yeso_Play_Extent.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Bakken Elevation of Top in Feet/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Elevation_of_Top_in_Feet.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Elevation_of_Top_in_Feet.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Elevation_of_Top_in_Feet.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Elevation_of_Top_in_Feet.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Elevation_of_Top_in_Feet.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Bakken Isopach (Thickness) in Feet/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Isopach_(Thickness)_in_Feet.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Isopach_(Thickness)_in_Feet.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Isopach_(Thickness)_in_Feet.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Isopach_(Thickness)_in_Feet.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Isopach_(Thickness)_in_Feet.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Bakken Play Extent/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Play_Extent.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Play_Extent.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Play_Extent.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Play_Extent.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Play_Extent.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Bone Spring Play Extent/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Isopach_(Thickness)_in_Feet.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Isopach_(Thickness)_in_Feet.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Isopach_(Thickness)_in_Feet.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Isopach_(Thickness)_in_Feet.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bakken_Isopach_(Thickness)_in_Feet.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Delaware Play Extent/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bone_Spring_Play_Extent.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bone_Spring_Play_Extent.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bone_Spring_Play_Extent.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bone_Spring_Play_Extent.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Bone_Spring_Play_Extent.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Eagle Ford Elevation of Top in Feet/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Eagle_Ford_Elevation_of_Top_in_Feet.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Eagle_Ford_Elevation_of_Top_in_Feet.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Eagle_Ford_Elevation_of_Top_in_Feet.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Eagle_Ford_Elevation_of_Top_in_Feet.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Eagle_Ford_Elevation_of_Top_in_Feet.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Eagle Ford Isopach (Thickness) in Feet/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Eagle_Ford_Elevation_of_Top_in_Feet.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Eagle_Ford_Elevation_of_Top_in_Feet.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Eagle_Ford_Elevation_of_Top_in_Feet.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Eagle_Ford_Elevation_of_Top_in_Feet.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Eagle_Ford_Elevation_of_Top_in_Feet.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Eagle Ford Play Extent/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Eagle_Ford_Play_Extent.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Eagle_Ford_Play_Extent.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Eagle_Ford_Play_Extent.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Eagle_Ford_Play_Extent.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Eagle_Ford_Play_Extent.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Glorieta-Yeso Play Extent/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Glorieta-Yeso_Play_Extent.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Glorieta-Yeso_Play_Extent.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Glorieta-Yeso_Play_Extent.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Glorieta-Yeso_Play_Extent.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Marcellus Elevation of Top in Feet/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Elevation_of_Top_in_Feet.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Elevation_of_Top_in_Feet.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Elevation_of_Top_in_Feet.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Elevation_of_Top_in_Feet.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Elevation_of_Top_in_Feet.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Marcellus Formation Extent/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Formation_Extent.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Formation_Extent.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Formation_Extent.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Formation_Extent.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Marcellus Isopach (Thickness) in Feet/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Formation_Extent.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Formation_Extent.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Formation_Extent.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Formation_Extent.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Formation_Extent.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Marcellus Play Extent/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Play_Extent.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Play_Extent.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Play_Extent.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Play_Extent.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Marcellus_Play_Extent.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Niobrara Elevation of Top in Feet/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Elevation_of_Top_in_Feet.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Elevation_of_Top_in_Feet.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Elevation_of_Top_in_Feet.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Elevation_of_Top_in_Feet.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Elevation_of_Top_in_Feet.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Niobrara Isopach (Thickness) in Feet/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Isopach_(Thickness)_in_Feet.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Isopach_(Thickness)_in_Feet.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Isopach_(Thickness)_in_Feet.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Isopach_(Thickness)_in_Feet.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Isopach_(Thickness)_in_Feet.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Niobrara Play Extent/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Play_Extent.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Play_Extent.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Play_Extent.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Play_Extent.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Play_Extent.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Point Pleasant Elevation of Top in Feet/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Point_Pleasant_Elevation_of_Top_in_Feet.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Point_Pleasant_Elevation_of_Top_in_Feet.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Point_Pleasant_Elevation_of_Top_in_Feet.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Point_Pleasant_Elevation_of_Top_in_Feet.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Point_Pleasant_Elevation_of_Top_in_Feet.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Point Pleasant Isopach (Thickness) in Feet/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Point_Pleasant_Isopach_(Thickness)_in_Feet.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Point_Pleasant_Isopach_(Thickness)_in_Feet.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Point_Pleasant_Isopach_(Thickness)_in_Feet.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Point_Pleasant_Isopach_(Thickness)_in_Feet.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Point_Pleasant_Isopach_(Thickness)_in_Feet.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Spraberry Play Extent/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Isopach_(Thickness)_in_Feet.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Isopach_(Thickness)_in_Feet.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Isopach_(Thickness)_in_Feet.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Isopach_(Thickness)_in_Feet.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Niobrara_Isopach_(Thickness)_in_Feet.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Three Forks Elevation of Top in Feet/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Three_Forks_Elevation_of_Top_in_Feet.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Three_Forks_Elevation_of_Top_in_Feet.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Three_Forks_Elevation_of_Top_in_Feet.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Three_Forks_Elevation_of_Top_in_Feet.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Three_Forks_Elevation_of_Top_in_Feet.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Three Forks Play Extent/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Three_Forks_Play_Extent.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Three_Forks_Play_Extent.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Three_Forks_Play_Extent.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Three_Forks_Play_Extent.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Three_Forks_Play_Extent.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Utica Elevation of Top in Feet/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Elevation_of_Top_in_Feet.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Elevation_of_Top_in_Feet.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Elevation_of_Top_in_Feet.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Elevation_of_Top_in_Feet.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Elevation_of_Top_in_Feet.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Utica Isopach (Thickness) in Feet/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Isopach_(Thickness)_in_Feet.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Isopach_(Thickness)_in_Feet.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Isopach_(Thickness)_in_Feet.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Isopach_(Thickness)_in_Feet.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Isopach_(Thickness)_in_Feet.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Utica Play Extent/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Play_Extent.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Play_Extent.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Play_Extent.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Play_Extent.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Play_Extent.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Wolfcamp Elevation of Top in Feet/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Elevation_of_Top_in_Feet.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Elevation_of_Top_in_Feet.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Elevation_of_Top_in_Feet.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Elevation_of_Top_in_Feet.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Utica_Elevation_of_Top_in_Feet.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Wolfcamp Isopach, 200-Foot Interval/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Wolfcamp_Isopach%2C_200-Foot_Interval.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Wolfcamp_Isopach%2C_200-Foot_Interval.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Wolfcamp_Isopach%2C_200-Foot_Interval.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Wolfcamp_Isopach%2C_200-Foot_Interval.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Wolfcamp_Isopach%2C_200-Foot_Interval.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Wolfcamp Isopach, 400-Foot Interval/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Wolfcamp_Isopach%2C_400-Foot_Interval.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Wolfcamp_Isopach%2C_400-Foot_Interval.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Wolfcamp_Isopach%2C_400-Foot_Interval.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Wolfcamp_Isopach%2C_400-Foot_Interval.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Wolfcamp_Isopach%2C_400-Foot_Interval.zip
                ├── summary.txt
                Major Tight Oil and Shale Gas Play - Wolfcamp Play Delaware Extent/
                ├── description.json
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Wolfcamp_Play_Delaware_Extent.csv
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Wolfcamp_Play_Delaware_Extent.gdb.zip
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Wolfcamp_Play_Delaware_Extent.geojson
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Wolfcamp_Play_Delaware_Extent.kml
                ├── Major_Tight_Oil_and_Shale_Gas_Play_-_Wolfcamp_Play_Delaware_Extent.zip
                ├── summary.txt
                Minor Events/
                ├── description.json
                ├── summary.txt
                ├── USA_Weather_Watches_and_Warnings.csv
                ├── USA_Weather_Watches_and_Warnings.geojson
                ├── USA_Weather_Watches_and_Warnings.kml
                ├── USA_Weather_Watches_and_Warnings.zip
                Moderate Events/
                ├── description.json
                ├── summary.txt
                ├── USA_Weather_Watches_and_Warnings.csv
                ├── USA_Weather_Watches_and_Warnings.geojson
                ├── USA_Weather_Watches_and_Warnings.kml
                ├── USA_Weather_Watches_and_Warnings.zip
                MODIS Thermal (Last 48 hours)/
                ├── description.json
                ├── Satellite_(MODIS)_Thermal_Hotspots_and_Fire_Activity.csv
                ├── Satellite_(MODIS)_Thermal_Hotspots_and_Fire_Activity.geojson
                ├── Satellite_(MODIS)_Thermal_Hotspots_and_Fire_Activity.kml
                ├── Satellite_(MODIS)_Thermal_Hotspots_and_Fire_Activity.zip
                ├── summary.txt
                MODIS Thermal (Last 7 days)/
                ├── description.json
                ├── Satellite_(MODIS)_Thermal_Hotspots_and_Fire_Activity.csv
                ├── Satellite_(MODIS)_Thermal_Hotspots_and_Fire_Activity.geojson
                ├── Satellite_(MODIS)_Thermal_Hotspots_and_Fire_Activity.kml
                ├── Satellite_(MODIS)_Thermal_Hotspots_and_Fire_Activity.zip
                ├── summary.txt
                National Weather Service Precipitation Forecast/
                ├── description.json
                ├── summary.txt
                ├── USA_Weather_Watches_and_Warnings.csv
                ├── USA_Weather_Watches_and_Warnings.geojson
                ├── USA_Weather_Watches_and_Warnings.kml
                ├── USA_Weather_Watches_and_Warnings.zip
                National Weather Service Smoke Forecast/
                ├── description.json
                ├── National_Weather_Service_Smoke_Forecast.csv
                ├── National_Weather_Service_Smoke_Forecast.geojson
                ├── National_Weather_Service_Smoke_Forecast.kml
                ├── National_Weather_Service_Smoke_Forecast.zip
                ├── summary.txt
                National Weather Service Wind Speed Forecast/
                ├── description.json
                ├── National_Weather_Service_Wind_Speed_Forecast.csv
                ├── National_Weather_Service_Wind_Speed_Forecast.geojson
                ├── National_Weather_Service_Wind_Speed_Forecast.kml
                ├── National_Weather_Service_Wind_Speed_Forecast.zip
                ├── summary.txt
                Natural Gas Interstate and Intrastate Pipelines/
                ├── description.json
                ├── Natural_Gas_Interstate_and_Intrastate_Pipelines.csv
                ├── Natural_Gas_Interstate_and_Intrastate_Pipelines.geojson
                ├── Natural_Gas_Interstate_and_Intrastate_Pipelines.kml
                ├── Natural_Gas_Interstate_and_Intrastate_Pipelines.zip
                ├── summary.txt
                Natural Gas Processing Plants/
                ├── description.json
                ├── Natural_Gas_Processing_Plants.csv
                ├── Natural_Gas_Processing_Plants.gdb.zip
                ├── Natural_Gas_Processing_Plants.geojson
                ├── Natural_Gas_Processing_Plants.kml
                ├── Natural_Gas_Processing_Plants.zip
                ├── summary.txt
                Natural Gas Storage Regions/
                ├── description.json
                ├── Natural_Gas_Storage_Regions.csv
                ├── Natural_Gas_Storage_Regions.gdb.zip
                ├── Natural_Gas_Storage_Regions.geojson
                ├── Natural_Gas_Storage_Regions.kml
                ├── Natural_Gas_Storage_Regions.zip
                ├── summary.txt
                Natural Gas Trading Hubs/
                ├── description.json
                ├── Natural_Gas_Trading_Hubs.csv
                ├── Natural_Gas_Trading_Hubs.gdb.zip
                ├── Natural_Gas_Trading_Hubs.geojson
                ├── Natural_Gas_Trading_Hubs.kml
                ├── Natural_Gas_Trading_Hubs.zip
                ├── summary.txt
                Natural Gas Underground Storage/
                ├── description.json
                ├── Natural_Gas_Underground_Storage.csv
                ├── Natural_Gas_Underground_Storage.gdb.zip
                ├── Natural_Gas_Underground_Storage.geojson
                ├── Natural_Gas_Underground_Storage.kml
                ├── Natural_Gas_Underground_Storage.zip
                ├── summary.txt
                Natural Gas Wells/
                ├── description.json
                ├── Natural_Gas_Wells.csv
                ├── Natural_Gas_Wells.geojson
                ├── Natural_Gas_Wells.kml
                ├── Natural_Gas_Wells.zip
                ├── summary.txt
                NERC Regions/
                ├── description.json
                ├── NERC_Regions.csv
                ├── NERC_Regions.gdb.zip
                ├── NERC_Regions.geojson
                ├── NERC_Regions.kml
                ├── NERC_Regions.zip
                ├── summary.txt
                NOAA Flash Flood Warnings/
                ├── description.json
                ├── summary.txt
                ├── USA_Short-Term_Weather_Warnings.csv
                ├── USA_Short-Term_Weather_Warnings.geojson
                ├── USA_Short-Term_Weather_Warnings.kml
                ├── USA_Short-Term_Weather_Warnings.zip
                NOAA Severe Thunderstorm Warnings/
                ├── description.json
                ├── summary.txt
                ├── USA_Short-Term_Weather_Warnings.csv
                ├── USA_Short-Term_Weather_Warnings.geojson
                ├── USA_Short-Term_Weather_Warnings.kml
                ├── USA_Short-Term_Weather_Warnings.zip
                NOAA Special Marine Warnings/
                ├── description.json
                ├── summary.txt
                ├── update.txt
                NOAA Tornado Warnings/
                ├── description.json
                ├── summary.txt
                ├── USA_Short-Term_Weather_Warnings.csv
                ├── USA_Short-Term_Weather_Warnings.geojson
                ├── USA_Short-Term_Weather_Warnings.kml
                ├── USA_Short-Term_Weather_Warnings.zip
                Northeast Petroleum Reserves/
                ├── description.json
                ├── Northeast_Petroleum_Reserves.csv
                ├── Northeast_Petroleum_Reserves.gdb.zip
                ├── Northeast_Petroleum_Reserves.geojson
                ├── Northeast_Petroleum_Reserves.kml
                ├── Northeast_Petroleum_Reserves.zip
                ├── summary.txt
                Observed Position/
                ├── description.json
                ├── summary.txt
                ├── update.txt
                Observed Position*/
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.csv
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.geojson
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.kml
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.zip
                ├── description.json
                ├── summary.txt
                Observed Track/
                ├── description.json
                ├── Recent_Hurricanes%2C_Cyclones_and_Typhoons.csv
                ├── Recent_Hurricanes%2C_Cyclones_and_Typhoons.geojson
                ├── Recent_Hurricanes%2C_Cyclones_and_Typhoons.kml
                ├── Recent_Hurricanes%2C_Cyclones_and_Typhoons.zip
                ├── summary.txt
                Observed Track*/
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.csv
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.geojson
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.kml
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.zip
                ├── description.json
                ├── summary.txt
                Observed Wind Swath/
                ├── description.json
                ├── Recent_Hurricanes%2C_Cyclones_and_Typhoons.csv
                ├── Recent_Hurricanes%2C_Cyclones_and_Typhoons.geojson
                ├── Recent_Hurricanes%2C_Cyclones_and_Typhoons.kml
                ├── Recent_Hurricanes%2C_Cyclones_and_Typhoons.zip
                ├── summary.txt
                Observed Wind Swath*/
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.csv
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.geojson
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.kml
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.zip
                ├── description.json
                ├── summary.txt
                Off Shore Wind Speed 90m (NREL)/
                ├── description.json
                ├── Off_Shore_Wind_Speed_90m_(NREL).csv
                ├── Off_Shore_Wind_Speed_90m_(NREL).geojson
                ├── Off_Shore_Wind_Speed_90m_(NREL).kml
                ├── Off_Shore_Wind_Speed_90m_(NREL).zip
                ├── summary.txt
                Oil and Natural Gas Platforms/
                ├── description.json
                ├── Oil_and_Natural_Gas_Platforms.csv
                ├── Oil_and_Natural_Gas_Platforms.gdb.zip
                ├── Oil_and_Natural_Gas_Platforms.geojson
                ├── Oil_and_Natural_Gas_Platforms.kml
                ├── Oil_and_Natural_Gas_Platforms.zip
                ├── summary.txt
                Oil Wells/
                ├── description.json
                ├── summary.txt
                ├── Wells_Oil_Generalized.csv
                ├── Wells_Oil_Generalized.geojson
                ├── Wells_Oil_Generalized.kml
                ├── Wells_Oil_Generalized.zip
                On Shore Wind Speed/
                ├── description.json
                ├── On_Shore_Wind_Speed.csv
                ├── On_Shore_Wind_Speed.geojson
                ├── On_Shore_Wind_Speed.kml
                ├── On_Shore_Wind_Speed.zip
                ├── summary.txt
                Other Events/
                ├── description.json
                ├── summary.txt
                ├── USA_Weather_Watches_and_Warnings.csv
                ├── USA_Weather_Watches_and_Warnings.geojson
                ├── USA_Weather_Watches_and_Warnings.kml
                ├── USA_Weather_Watches_and_Warnings.zip
                Petroleum Administration for Defense Districts (PADD)/
                ├── description.json
                ├── Petroleum_Administration_for_Defense_Districts_(PADD).csv
                ├── Petroleum_Administration_for_Defense_Districts_(PADD).gdb.zip
                ├── Petroleum_Administration_for_Defense_Districts_(PADD).geojson
                ├── Petroleum_Administration_for_Defense_Districts_(PADD).kml
                ├── Petroleum_Administration_for_Defense_Districts_(PADD).zip
                ├── summary.txt
                Petroleum Ports/
                ├── description.json
                ├── Petroleum_Ports.csv
                ├── Petroleum_Ports.geojson
                ├── Petroleum_Ports.kml
                ├── Petroleum_Ports.zip
                ├── summary.txt
                Petroleum Product Pipelines/
                ├── description.json
                ├── Petroleum_Product_Pipelines.csv
                ├── Petroleum_Product_Pipelines.gdb.zip
                ├── Petroleum_Product_Pipelines.geojson
                ├── Petroleum_Product_Pipelines.kml
                ├── Petroleum_Product_Pipelines.zip
                ├── summary.txt
                Petroleum Product Terminals/
                ├── description.json
                ├── Petroleum_Product_Terminals.csv
                ├── Petroleum_Product_Terminals.gdb.zip
                ├── Petroleum_Product_Terminals.geojson
                ├── Petroleum_Product_Terminals.kml
                ├── Petroleum_Product_Terminals.zip
                ├── summary.txt
                Petroleum Refineries/
                ├── description.json
                ├── Petroleum_Refineries.csv
                ├── Petroleum_Refineries.gdb.zip
                ├── Petroleum_Refineries.geojson
                ├── Petroleum_Refineries.kml
                ├── Petroleum_Refineries.zip
                ├── summary.txt
                Petroleum Waterways/
                ├── description.json
                ├── Petroleum_Waterways.csv
                ├── Petroleum_Waterways.geojson
                ├── Petroleum_Waterways.kml
                ├── Petroleum_Waterways.zip
                ├── summary.txt
                Population By County US Census 2010/
                ├── description.json
                ├── Population_By_County_US_Census_2010.csv
                ├── Population_By_County_US_Census_2010.geojson
                ├── Population_By_County_US_Census_2010.kml
                ├── Population_By_County_US_Census_2010.zip
                ├── summary.txt
                Power Plants/
                ├── description.json
                ├── Power_Plants.csv
                ├── Power_Plants.geojson
                ├── Power_Plants.kml
                ├── Power_Plants.zip
                ├── summary.txt
                Public Forecast Zones/
                ├── description.json
                ├── summary.txt
                ├── USA_Weather_Watches_and_Warnings.csv
                ├── USA_Weather_Watches_and_Warnings.geojson
                ├── USA_Weather_Watches_and_Warnings.kml
                ├── USA_Weather_Watches_and_Warnings.zip
                Raw 1_10th Degree Data (All)/
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.csv
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.geojson
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.kml
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.zip
                ├── description.json
                ├── summary.txt
                Recent Hurricanes, Cyclones and Typhoons/
                Renewable Diesel and Other Biofuels/
                ├── description.json
                ├── Renewable_Diesel_and_Other_Biofuels.csv
                ├── Renewable_Diesel_and_Other_Biofuels.geojson
                ├── Renewable_Diesel_and_Other_Biofuels.kml
                ├── Renewable_Diesel_and_Other_Biofuels.zip
                ├── summary.txt
                Satellite (MODIS) Thermal Hotspots and Fire Activity/
                ├── description.json
                ├── Recent_Hurricanes%2C_Cyclones_and_Typhoons.csv
                ├── Recent_Hurricanes%2C_Cyclones_and_Typhoons.geojson
                ├── Recent_Hurricanes%2C_Cyclones_and_Typhoons.kml
                ├── Recent_Hurricanes%2C_Cyclones_and_Typhoons.zip
                ├── summary.txt
                Satellite (VIIRS) Thermal Hotspots and Fire Activity/
                ├── description.json
                ├── Satellite_(VIIRS)_Thermal_Hotspots_and_Fire_Activity.csv
                ├── Satellite_(VIIRS)_Thermal_Hotspots_and_Fire_Activity.geojson
                ├── Satellite_(VIIRS)_Thermal_Hotspots_and_Fire_Activity.kml
                ├── Satellite_(VIIRS)_Thermal_Hotspots_and_Fire_Activity.zip
                ├── summary.txt
                Sedimentary Basins/
                ├── description.json
                ├── Sedimentary_Basins.csv
                ├── Sedimentary_Basins.gdb.zip
                ├── Sedimentary_Basins.geojson
                ├── Sedimentary_Basins.kml
                ├── Sedimentary_Basins.zip
                ├── summary.txt
                Severe Events/
                ├── description.json
                ├── summary.txt
                ├── USA_Weather_Watches_and_Warnings.csv
                ├── USA_Weather_Watches_and_Warnings.geojson
                ├── USA_Weather_Watches_and_Warnings.kml
                ├── USA_Weather_Watches_and_Warnings.zip
                ShalePlay Midland Spraberry Lower Elevation EIA 202111/
                ├── description.json
                ├── ShalePlay_Midland_Spraberry_Lower_Elevation_EIA_202111.csv
                ├── ShalePlay_Midland_Spraberry_Lower_Elevation_EIA_202111.geojson
                ├── ShalePlay_Midland_Spraberry_Lower_Elevation_EIA_202111.kml
                ├── ShalePlay_Midland_Spraberry_Lower_Elevation_EIA_202111.zip
                ├── summary.txt
                ShalePlay Midland Spraberry Lower Isopach EIA 202111/
                ├── description.json
                ├── ShalePlay_Midland_Spraberry_Lower_Isopach_EIA_202111.csv
                ├── ShalePlay_Midland_Spraberry_Lower_Isopach_EIA_202111.geojson
                ├── ShalePlay_Midland_Spraberry_Lower_Isopach_EIA_202111.kml
                ├── ShalePlay_Midland_Spraberry_Lower_Isopach_EIA_202111.zip
                ├── summary.txt
                ShalePlay Midland Spraberry Middle Elevation EIA 202111/
                ├── description.json
                ├── ShalePlay_Midland_Spraberry_Middle_Elevation_EIA_202111.csv
                ├── ShalePlay_Midland_Spraberry_Middle_Elevation_EIA_202111.geojson
                ├── ShalePlay_Midland_Spraberry_Middle_Elevation_EIA_202111.kml
                ├── ShalePlay_Midland_Spraberry_Middle_Elevation_EIA_202111.zip
                ├── summary.txt
                ShalePlay Midland Spraberry Middle Isopach EIA 202111/
                ├── description.json
                ├── ShalePlay_Midland_Spraberry_Middle_Isopach_EIA_202111.csv
                ├── ShalePlay_Midland_Spraberry_Middle_Isopach_EIA_202111.geojson
                ├── ShalePlay_Midland_Spraberry_Middle_Isopach_EIA_202111.kml
                ├── ShalePlay_Midland_Spraberry_Middle_Isopach_EIA_202111.zip
                ├── summary.txt
                ShalePlay Midland Spraberry Upper Elevation EIA 202111/
                ├── description.json
                ├── ShalePlay_Midland_Spraberry_Middle_Isopach_EIA_202111.csv
                ├── ShalePlay_Midland_Spraberry_Middle_Isopach_EIA_202111.geojson
                ├── ShalePlay_Midland_Spraberry_Middle_Isopach_EIA_202111.kml
                ├── ShalePlay_Midland_Spraberry_Middle_Isopach_EIA_202111.zip
                ├── summary.txt
                ShalePlay Midland Spraberry Upper Isopach EIA 202111/
                ├── description.json
                ├── ShalePlay_Midland_Spraberry_Upper_Isopach_EIA_202111.csv
                ├── ShalePlay_Midland_Spraberry_Upper_Isopach_EIA_202111.geojson
                ├── ShalePlay_Midland_Spraberry_Upper_Isopach_EIA_202111.kml
                ├── ShalePlay_Midland_Spraberry_Upper_Isopach_EIA_202111.zip
                ├── summary.txt
                ShalePlay Midland SpraberryLower Boundary EIA 202111/
                ├── description.json
                ├── ShalePlay_Midland_SpraberryLower_Boundary_EIA_202111.csv
                ├── ShalePlay_Midland_SpraberryLower_Boundary_EIA_202111.geojson
                ├── ShalePlay_Midland_SpraberryLower_Boundary_EIA_202111.kml
                ├── ShalePlay_Midland_SpraberryLower_Boundary_EIA_202111.zip
                ├── summary.txt
                ShalePlay Midland SpraberryMiddle Boundary EIA 202111/
                ├── description.json
                ├── ShalePlay_Midland_SpraberryMiddle_Boundary_EIA_202111.csv
                ├── ShalePlay_Midland_SpraberryMiddle_Boundary_EIA_202111.geojson
                ├── ShalePlay_Midland_SpraberryMiddle_Boundary_EIA_202111.kml
                ├── ShalePlay_Midland_SpraberryMiddle_Boundary_EIA_202111.zip
                ├── summary.txt
                ShalePlay Midland SpraberryUpper Boundary EIA 202111/
                ├── description.json
                ├── ShalePlay_Midland_SpraberryUpper_Boundary_EIA_202111.csv
                ├── ShalePlay_Midland_SpraberryUpper_Boundary_EIA_202111.geojson
                ├── ShalePlay_Midland_SpraberryUpper_Boundary_EIA_202111.kml
                ├── ShalePlay_Midland_SpraberryUpper_Boundary_EIA_202111.zip
                ├── summary.txt
                Solar Resources/
                ├── description.json
                ├── Solar_Resources.csv
                ├── Solar_Resources.geojson
                ├── Solar_Resources.kml
                ├── Solar_Resources.zip
                ├── summary.txt
                Solid Biomass Resources/
                ├── description.json
                ├── Solid_Biomass_Resources.csv
                ├── Solid_Biomass_Resources.geojson
                ├── Solid_Biomass_Resources.kml
                ├── Solid_Biomass_Resources.zip
                ├── summary.txt
                Stations/
                ├── Current_Weather_and_Wind_Station_Data.csv
                ├── Current_Weather_and_Wind_Station_Data.geojson
                ├── Current_Weather_and_Wind_Station_Data.kml
                ├── Current_Weather_and_Wind_Station_Data.zip
                ├── description.json
                ├── summary.txt
                Strategic Petroleum Reserves/
                ├── description.json
                ├── Strategic_Petroleum_Reserves.csv
                ├── Strategic_Petroleum_Reserves.geojson
                ├── Strategic_Petroleum_Reserves.kml
                ├── Strategic_Petroleum_Reserves.zip
                ├── summary.txt
                Strong Tropical Storm (50kts)/
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.csv
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.geojson
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.kml
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.zip
                ├── description.json
                ├── summary.txt
                Tight Oil and Shale Gas Plays/
                ├── description.json
                ├── summary.txt
                ├── Tight_Oil_and_Shale_Gas_Plays.csv
                ├── Tight_Oil_and_Shale_Gas_Plays.gdb.zip
                ├── Tight_Oil_and_Shale_Gas_Plays.geojson
                ├── Tight_Oil_and_Shale_Gas_Plays.kml
                ├── Tight_Oil_and_Shale_Gas_Plays.zip
                Tropical Storm Force (34kts)/
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.csv
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.geojson
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.kml
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.zip
                ├── description.json
                ├── summary.txt
                United States Wind Turbine Database (USWTDB)/
                ├── description.json
                ├── summary.txt
                ├── United_States_Wind_Turbine_Database_(USWTDB) (1).geojson
                ├── United_States_Wind_Turbine_Database_(USWTDB).csv
                ├── United_States_Wind_Turbine_Database_(USWTDB).gdb.zip
                ├── United_States_Wind_Turbine_Database_(USWTDB).kml
                ├── United_States_Wind_Turbine_Database_(USWTDB).zip
                Uranium - Associated with Phosphate/
                ├── description.json
                ├── summary.txt
                ├── Uranium_-_Associated_with_Phosphate.csv
                ├── Uranium_-_Associated_with_Phosphate.geojson
                ├── Uranium_-_Associated_with_Phosphate.kml
                ├── Uranium_-_Associated_with_Phosphate.zip
                Uranium - Identified Resource Areas/
                ├── description.json
                ├── summary.txt
                ├── Uranium_-_Identified_Resource_Areas.csv
                ├── Uranium_-_Identified_Resource_Areas.gdb.zip
                ├── Uranium_-_Identified_Resource_Areas.geojson
                ├── Uranium_-_Identified_Resource_Areas.kml
                ├── Uranium_-_Identified_Resource_Areas.zip
                Uranium - NURE Favorable Areas/
                ├── description.json
                ├── summary.txt
                ├── Uranium_-_NURE_Favorable_Areas.csv
                ├── Uranium_-_NURE_Favorable_Areas.gdb.zip
                ├── Uranium_-_NURE_Favorable_Areas.geojson
                ├── Uranium_-_NURE_Favorable_Areas.kml
                ├── Uranium_-_NURE_Favorable_Areas.zip
                Uranium In-Situ Leach Plants/
                ├── description.json
                ├── summary.txt
                ├── Uranium_In-Situ_Leach_Plants.csv
                ├── Uranium_In-Situ_Leach_Plants.gdb.zip
                ├── Uranium_In-Situ_Leach_Plants.geojson
                ├── Uranium_In-Situ_Leach_Plants.kml
                ├── Uranium_In-Situ_Leach_Plants.zip
                Uranium Mills and Heap Leach Facilities/
                ├── description.json
                ├── summary.txt
                ├── Uranium_Mills_and_Heap_Leach_Facilities.csv
                ├── Uranium_Mills_and_Heap_Leach_Facilities.gdb.zip
                ├── Uranium_Mills_and_Heap_Leach_Facilities.geojson
                ├── Uranium_Mills_and_Heap_Leach_Facilities.kml
                ├── Uranium_Mills_and_Heap_Leach_Facilities.zip
                US Counties/
                ├── description.json
                ├── summary.txt
                ├── USA_Weather_Watches_and_Warnings.csv
                ├── USA_Weather_Watches_and_Warnings.geojson
                ├── USA_Weather_Watches_and_Warnings.kml
                ├── USA_Weather_Watches_and_Warnings.zip
                US States and Territories/
                ├── description.json
                ├── summary.txt
                ├── USA_Weather_Watches_and_Warnings.csv
                ├── USA_Weather_Watches_and_Warnings.geojson
                ├── USA_Weather_Watches_and_Warnings.kml
                ├── USA_Weather_Watches_and_Warnings.zip
                USA 116th Congressional Districts/
                ├── description.json
                ├── summary.txt
                ├── United_States_Wind_Turbine_Database_(USWTDB).csv
                ├── United_States_Wind_Turbine_Database_(USWTDB).gdb.zip
                ├── United_States_Wind_Turbine_Database_(USWTDB).kml
                ├── United_States_Wind_Turbine_Database_(USWTDB).zip
                USA 117th Congressional Districts/
                ├── description.json
                ├── summary.txt
                ├── USA_117th_Congressional_Districts.csv
                ├── USA_117th_Congressional_Districts.geojson
                ├── USA_117th_Congressional_Districts.kml
                ├── USA_117th_Congressional_Districts.zip
                USA Census Populated Place Areas/
                ├── description.json
                ├── summary.txt
                ├── USA_Census_Populated_Place_Areas.csv
                ├── USA_Census_Populated_Place_Areas.gdb.zip
                ├── USA_Census_Populated_Place_Areas.geojson
                ├── USA_Census_Populated_Place_Areas.kml
                ├── USA_Census_Populated_Place_Areas.zip
                USA Coal Fields/
                ├── description.json
                ├── summary.txt
                ├── USA_Coal_Fields.csv
                ├── USA_Coal_Fields.geojson
                ├── USA_Coal_Fields.kml
                ├── USA_Coal_Fields.zip
                USA Counties (Generalized)/
                ├── description.json
                ├── summary.txt
                ├── USA_Counties_(Generalized).csv
                ├── USA_Counties_(Generalized).geojson
                ├── USA_Counties_(Generalized).kml
                ├── USA_Counties_(Generalized).zip
                USA Current Wildfires/
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.csv
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.geojson
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.kml
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.zip
                ├── description.json
                ├── summary.txt
                USA Federal Lands/
                ├── description.json
                ├── summary.txt
                ├── USA_Federal_Lands.csv
                ├── USA_Federal_Lands.gdb.zip
                ├── USA_Federal_Lands.geojson
                ├── USA_Federal_Lands.kml
                ├── USA_Federal_Lands.zip
                USA Railroads/
                ├── description.json
                ├── summary.txt
                ├── USA_Railroads.csv
                ├── USA_Railroads.geojson
                ├── USA_Railroads.kml
                ├── USA_Railroads.zip
                USA Short-Term Weather Warnings/
                USA States (Generalized)/
                ├── description.json
                ├── summary.txt
                ├── USA_States_(Generalized).csv
                ├── USA_States_(Generalized).gdb.zip
                ├── USA_States_(Generalized).geojson
                ├── USA_States_(Generalized).kml
                ├── USA_States_(Generalized).zip
                USA Urban Areas/
                USA Urban Areas (1:500k-1.5M)/
                ├── description.json
                ├── summary.txt
                ├── USA_Urban_Areas.csv
                ├── USA_Urban_Areas.geojson
                ├── USA_Urban_Areas.kml
                ├── USA_Urban_Areas.zip
                USA Urban Areas (below 1:500k)/
                ├── description.json
                ├── summary.txt
                ├── USA_Urban_Areas.csv
                ├── USA_Urban_Areas.geojson
                ├── USA_Urban_Areas.kml
                ├── USA_Urban_Areas.zip
                USA Urban Areas (over 1:1.5M)/
                ├── description.json
                ├── summary.txt
                ├── USA_Urban_Areas.csv
                ├── USA_Urban_Areas.geojson
                ├── USA_Urban_Areas.kml
                ├── USA_Urban_Areas.zip
                USA Weather Watches and Warnings/
                Watches and Warnings/
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.csv
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.geojson
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.kml
                ├── Active_Hurricanes%2C_Cyclones_and_Typhoons.zip
                ├── description.json
                ├── summary.txt
                Wells Gas Generalized/
                ├── description.json
                ├── Population_By_County_US_Census_2010.csv
                ├── Population_By_County_US_Census_2010.geojson
                ├── Population_By_County_US_Census_2010.kml
                ├── Population_By_County_US_Census_2010.zip
                ├── summary.txt
                Wells Oil Generalized/
                ├── description.json
                ├── summary.txt
                ├── Wells_Gas_Generalized.csv
                ├── Wells_Gas_Generalized.geojson
                ├── Wells_Gas_Generalized.kml
                ├── Wells_Gas_Generalized.zip
        2_renewable_alternative_fuels/
            code/
            ├── test.ipynb
            data/
                2017/
                    december/
                    november/
                    october/
                2018/
                    april/
                    august/
                    december/
                    february/
                    january/
                    july/
                    june/
                    march/
                    may/
                    november/
                    october/
                    september/
                2019/
                    april/
                    august/
                    december/
                    february/
                    january/
                    july/
                    june/
                    march/
                    may/
                    november/
                    october/
                    september/
                2020/
                    april/
                    august/
                    december/
                    february/
                    january/
                    july/
                    june/
                    march/
                    may/
                    november/
                    october/
                    september/
                2021/
                    april/
                    august/
                    december/
                    february/
                    january/
                    july/
                    june/
                    march/
                    may/
                    november/
                    october/
                    september/
                2022/
                    april/
                    august/
                    december/
                    february/
                    january/
                    july/
                    june/
                    march/
                    may/
                    november/
                    october/
                    september/
                2023/
                    april/
                    february/
                    january/
                    march/
                    may/
        3_wind_turbine/
            code/
            ├── test.ipynb
            data/
        6_electricity/
            code/
            data/
                annual/
                    1.1 Net generation by energy source: total - all sectors/
                    ├── Net_generation_for_all_sectors.csv
                    1.1.a Net generation by renewable sources: total - all sectors/
                    ├── Net_generation_for_all_sectors.csv
                    1.10 Net generation from hydroelectric (conventional) power by state by sector/
                    ├── Net_generation_for_conventional_hydroelectric.csv
                    1.11 Net generation from renewable sources excluding hydroelectric by state by sector/
                    ├── Net_generation_for_other_renewables.csv
                    1.12 Net generation from hydroelectric (pumped storage) power by state by sector/
                    ├── Net_generation_for_hydro-electric_pumped_storage.csv
                    1.13 Net generation from other energy sources by state by sector/
                    ├── Net_generation_for_other.csv
                    1.14 Net generation from wind by state by sector/
                    ├── Net_generation_for_wind.csv
                    1.15 Net generation from biomass by state by sector/
                    ├── Net_generation_for_biomass.csv
                    1.16 Net generation from geothermal by census division by sector/
                    ├── Net_generation_for_geothermal.csv
                    1.2.a Net generation by energy source: electric utilities/
                    ├── Net_generation_for_electric_utility.csv
                    1.2.b Net generation by energy source: independent power producers/
                    ├── Net_generation_for_independent_power_producers.csv
                    1.2.c Net generation by energy source: commercial sector/
                    ├── Net_generation_for_all_commercial.csv
                    1.2.d Net generation by energy source: industrial sector/
                    ├── Net_generation_for_all_industrial.csv
                    1.20 Net generation from solar by state by sector/
                    ├── Net_generation_for_all_utility-scale_solar.csv
                    1.3 Net generation by state by sector/
                    ├── Net_generation_for_all_fuels_(utility-scale).csv
                    1.4 Net generation from coal by state by sector/
                    ├── Net_generation_for_coal.csv
                    1.5 Net generation from petroleum liquids by state by sector/
                    ├── Net_generation_for_petroleum_liquids.csv
                    1.6 Net generation from petroleum coke by state by sector/
                    ├── Net_generation_for_petroleum_coke.csv
                    1.7 Net generation from natural gas by state by sector/
                    ├── Net_generation_for_natural_gas.csv
                    1.8 Net generation from other gases by state by sector/
                    ├── Net_generation_for_other_gases.csv
                    1.9 Net generation from nuclear energy by state by sector/
                    ├── Net_generation_for_nuclear.csv
                    2.1.a Consumption of coal for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_coal.csv
                    2.1.b Consumption of coal for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_coal.csv
                    2.1.c Consumption of coal for electricity generation and useful thermal output by sector/
                    ├── Total_consumption_for_coal.csv
                    2.2.a Consumption of petroleum liquids for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_liquids.csv
                    2.2.b Consumption of petroleum liquids for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_petroleum_liquids.csv
                    2.2.c Total consumption of petroleum liquids by sector/
                    ├── Total_consumption_for_petroleum_liquids.csv
                    2.3.a Consumption of petroleum coke for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_coke.csv
                    2.3.b Consumption of petroleum coke for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_petroleum_coke.csv
                    2.3.c Total consumption of petroleum coke by sector/
                    ├── Total_consumption_for_petroleum_coke.csv
                    2.4.a Consumption of natural gas for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_natural_gas.csv
                    2.4.b Consumption of natural gas for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_natural_gas.csv
                    2.4.c Total consumption of natural gas by sector/
                    ├── Total_consumption_for_natural_gas.csv
                    2.5 Consumption of coal for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_coal.csv
                    2.6 Consumption of petroleum liquids for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_liquids.csv
                    2.7 Consumption of petroleum coke for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_coke.csv
                    2.8 Consumption of natural gas for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_natural_gas.csv
                    3.1 Stocks of coal, petroleum liquids, and petroleum coke: electric power sector/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_United_States.csv
                    3.2 Stocks of coal, petroleum liquids, and petroleum coke: electric power sector by state/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_electric_power.csv
                    3.3 Stocks of coal: electric power sector by census division/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_coal.csv
                    3.3 Stocks of petroleum coke: electric power sector by census division/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_petroleum_coke.csv
                    3.3 Stocks of petroleum liquids: electric power sector by census division/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_petroleum_liquids.csv
                    3.4 Stocks of coal by coal rank/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_electric_utility.csv
                    4.10.a Average cost of coal delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_coal.csv
                    4.11.a Average cost of petroleum liquids delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_petroleum_liquids.csv
                    4.12.a Average cost of petroleum coke delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_petroleum_coke.csv
                    4.13.a Average cost of natural gas delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_natural_gas.csv
                    4.6.a Receipts of coal delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_coal.csv
                    4.7.a Receipts of petroleum liquids delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_petroleum_liquids.csv
                    4.8.a Receipts of petroleum coke delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_petroleum_coke.csv
                    4.9.a Receipts of natural gas delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_natural_gas.csv
                    5.1 Retail sales of electricity to ultimate customers: total by end-use sector/
                    ├── Retail_sales_of_electricity.csv
                    5.2 Revenue from retail sales of electricity to ultimate customers total by end-use sector/
                    ├── Revenue_from_retail_sales_of_electricity.csv
                    5.3 Average retail price of electricity to ultimate customers: total by end-use sector/
                    ├── Average_retail_price_of_electricity.csv
                    5.4 Retail sales of electricity to ultimate customers by end-use sector, by state/
                    ├── Retail_sales_of_electricity.csv
                    5.5 Revenue from retail sales of electricity to ultimate customers by end-use sector, by state/
                    ├── Revenue_from_retail_sales_of_electricity.csv
                    5.6 Average retail price of electricity to ultimate customers by end-use sector, by state/
                    ├── Average_retail_price_of_electricity.csv
                    Average cost of fossil fuels for electricity generation/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_for_coal.csv
                    Average cost of fossil fuels for electricity generation (per Btu)/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_petroleum_liquids.csv
                    Average retail price of electricity/
                    ├── Average_retail_price_of_electricity.csv
                    Consumption for electricity generation/
                    ├── Consumption_for_electricity_generation_for_coal.csv
                    Consumption for electricity generation (Btu)/
                    ├── Consumption_for_electricity_generation_(Btu)_for_coal.csv
                    Consumption for useful thermal output/
                    ├── Consumption_for_useful_thermal_output_for_petroleum_coke.csv
                    Consumption for useful thermal output (Btu)/
                    ├── Consumption_for_useful_thermal_output_(Btu)_for_coal.csv
                    Fossil-fuel stocks for electricity generation/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_petroleum_coke.csv
                    Net generation/
                    ├── Net_generation_for_natural_gas.csv
                    Number of customer accounts/
                    ├── Number_of_customer_accounts.csv
                    Plant level data/
                    ├── Plants_for_all_sectorsUnited_Statesmultiple_fuel_types.csv
                    Quality of fossil fuels in electricity generation : ash content/
                    ├── Quality_of_fossil_fuels_in_electricity_generation___ash_content_for_coal.csv
                    Quality of fossil fuels in electricity generation : sulfur content/
                    ├── Quality_of_fossil_fuels_in_electricity_generation___sulfur_content_for_United_States.csv
                    Receipts of fossil fuels by electricity plants/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_all_sectors.csv
                    Receipts of fossil fuels by electricity plants (Btu)/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_(Btu)_for_petroleum_liquids.csv
                    Retail sales of electricity/
                    ├── Retail_sales_of_electricity.csv
                    Revenue from retail sales of electricity/
                    ├── Revenue_from_retail_sales_of_electricity.csv
                    Total consumption/
                    ├── Total_consumption_for_coal.csv
                    Total consumption (Btu)/
                    ├── Total_consumption_(Btu)_for_all_sectors.csv
                monthly/
                    1.1 Net generation by energy source: total - all sectors/
                    ├── Net_generation_for_all_sectors.csv
                    1.1.a Net generation by renewable sources: total - all sectors/
                    ├── Net_generation_for_all_sectors.csv
                    1.10 Net generation from hydroelectric (conventional) power by state by sector/
                    ├── Net_generation_for_conventional_hydroelectric.csv
                    1.11 Net generation from renewable sources excluding hydroelectric by state by sector/
                    ├── Net_generation_for_other_renewables.csv
                    1.12 Net generation from hydroelectric (pumped storage) power by state by sector/
                    ├── Net_generation_for_hydro-electric_pumped_storage.csv
                    1.13 Net generation from other energy sources by state by sector/
                    ├── Net_generation_for_other.csv
                    1.14 Net generation from wind by state by sector/
                    ├── Net_generation_for_wind.csv
                    1.15 Net generation from biomass by state by sector/
                    ├── Net_generation_for_biomass.csv
                    1.16 Net generation from geothermal by census division by sector/
                    ├── Net_generation_for_geothermal.csv
                    1.2.a Net generation by energy source: electric utilities/
                    ├── Net_generation_for_electric_utility.csv
                    1.2.b Net generation by energy source: independent power producers/
                    ├── Net_generation_for_independent_power_producers.csv
                    1.2.c Net generation by energy source: commercial sector/
                    ├── Net_generation_for_all_commercial.csv
                    1.2.d Net generation by energy source: industrial sector/
                    ├── Net_generation_for_all_industrial.csv
                    1.20 Net generation from solar by state by sector/
                    ├── Net_generation_for_all_utility-scale_solar.csv
                    1.3 Net generation by state by sector/
                    ├── Net_generation_for_all_fuels_(utility-scale).csv
                    1.4 Net generation from coal by state by sector/
                    ├── Net_generation_for_all_fuels_(utility-scale).csv
                    1.5 Net generation from petroleum liquids by state by sector/
                    ├── Net_generation_for_petroleum_liquids.csv
                    1.6 Net generation from petroleum coke by state by sector/
                    ├── Net_generation_for_petroleum_coke.csv
                    1.7 Net generation from natural gas by state by sector/
                    ├── Net_generation_for_natural_gas.csv
                    1.8 Net generation from other gases by state by sector/
                    ├── Net_generation_for_other_gases.csv
                    1.9 Net generation from nuclear energy by state by sector/
                    ├── Net_generation_for_nuclear.csv
                    2.1.a Consumption of coal for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_coal.csv
                    2.1.b Consumption of coal for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_coal.csv
                    2.1.c Consumption of coal for electricity generation and useful thermal output by sector/
                    ├── Total_consumption_for_coal.csv
                    2.2.a Consumption of petroleum liquids for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_liquids.csv
                    2.2.b Consumption of petroleum liquids for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_petroleum_liquids.csv
                    2.2.c Total consumption of petroleum liquids by sector/
                    ├── Total_consumption_for_petroleum_liquids.csv
                    2.3.a Consumption of petroleum coke for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_coke.csv
                    2.3.b Consumption of petroleum coke for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_petroleum_coke.csv
                    2.3.c Total consumption of petroleum coke by sector/
                    ├── Total_consumption_for_petroleum_coke.csv
                    2.4.a Consumption of natural gas for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_natural_gas.csv
                    2.4.b Consumption of natural gas for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_natural_gas.csv
                    2.4.c Total consumption of natural gas by sector/
                    ├── Total_consumption_for_natural_gas.csv
                    2.5 Consumption of coal for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_coal.csv
                    2.6 Consumption of petroleum liquids for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_liquids.csv
                    2.7 Consumption of petroleum coke for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_coke.csv
                    2.8 Consumption of natural gas for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_natural_gas.csv
                    3.1 Stocks of coal, petroleum liquids, and petroleum coke: electric power sector/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_United_States.csv
                    3.2 Stocks of coal, petroleum liquids, and petroleum coke: electric power sector by state/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_electric_power.csv
                    3.3 Stocks of coal: electric power sector by census division/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_coal.csv
                    3.3 Stocks of petroleum coke: electric power sector by census division/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_petroleum_coke.csv
                    3.3 Stocks of petroleum liquids: electric power sector by census division/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_petroleum_liquids.csv
                    3.4 Stocks of coal by coal rank/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_electric_utility.csv
                    4.10.a Average cost of coal delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_coal.csv
                    4.11.a Average cost of petroleum liquids delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_petroleum_liquids.csv
                    4.12.a Average cost of petroleum coke delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_petroleum_coke.csv
                    4.13.a Average cost of natural gas delivered for electricity generation by state/
                    ├── Consumption_for_electricity_generation_for_petroleum_liquids.csv
                    4.6.a Receipts of coal delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_coal.csv
                    4.7.a Receipts of petroleum liquids delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_petroleum_liquids.csv
                    4.8.a Receipts of petroleum coke delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_petroleum_coke.csv
                    4.9.a Receipts of natural gas delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_natural_gas.csv
                    5.1 Retail sales of electricity to ultimate customers: total by end-use sector/
                    ├── Retail_sales_of_electricity.csv
                    5.2 Revenue from retail sales of electricity to ultimate customers total by end-use sector/
                    ├── Revenue_from_retail_sales_of_electricity.csv
                    5.3 Average retail price of electricity to ultimate customers: total by end-use sector/
                    ├── Average_retail_price_of_electricity.csv
                    5.4 Retail sales of electricity to ultimate customers by end-use sector, by state/
                    ├── Retail_sales_of_electricity.csv
                    5.5 Revenue from retail sales of electricity to ultimate customers by end-use sector, by state/
                    ├── Revenue_from_retail_sales_of_electricity.csv
                    5.6 Average retail price of electricity to ultimate customers by end-use sector, by state/
                    ├── Average_retail_price_of_electricity.csv
                    Average cost of fossil fuels for electricity generation/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_for_natural_gas.csv
                    Average cost of fossil fuels for electricity generation (per Btu)/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_petroleum_coke.csv
                    Average retail price of electricity/
                    ├── Average_retail_price_of_electricity.csv
                    Consumption for electricity generation/
                    ├── Consumption_for_electricity_generation_for_coal.csv
                    Consumption for electricity generation (Btu)/
                    ├── Consumption_for_electricity_generation_(Btu)_for_petroleum_liquids.csv
                    Consumption for useful thermal output/
                    ├── Consumption_for_useful_thermal_output_for_petroleum_liquids.csv
                    Consumption for useful thermal output (Btu)/
                    ├── Consumption_for_useful_thermal_output_(Btu)_for_coal.csv
                    Fossil-fuel stocks for electricity generation/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_electric_power.csv
                    Net generation/
                    ├── Net_generation_for_biomass.csv
                    Number of customer accounts/
                    ├── Number_of_customer_accounts.csv
                    Plant level data/
                    ├── Plants_for_all_sectorsUnited_Statesmultiple_fuel_types.csv
                    Quality of fossil fuels in electricity generation : ash content/
                    ├── Quality_of_fossil_fuels_in_electricity_generation___ash_content_for_petroleum_liquids.csv
                    Quality of fossil fuels in electricity generation : sulfur content/
                    ├── Quality_of_fossil_fuels_in_electricity_generation___sulfur_content_for_petroleum_coke.csv
                    Receipts of fossil fuels by electricity plants/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_all_sectors.csv
                    Receipts of fossil fuels by electricity plants (Btu)/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_(Btu)_for_coal.csv
                    Retail sales of electricity/
                    ├── Retail_sales_of_electricity.csv
                    Revenue from retail sales of electricity/
                    ├── Revenue_from_retail_sales_of_electricity.csv
                    Total consumption/
                    ├── Total_consumption_for_all_sectors.csv
                    Total consumption (Btu)/
                    ├── Total_consumption_(Btu)_for_all_sectors.csv
                quarterly/
                    1.1 Net generation by energy source: total - all sectors/
                    ├── Net_generation_for_all_sectors.csv
                    1.1.a Net generation by renewable sources: total - all sectors/
                    ├── Net_generation_for_all_sectors.csv
                    1.10 Net generation from hydroelectric (conventional) power by state by sector/
                    ├── Net_generation_for_conventional_hydroelectric.csv
                    1.11 Net generation from renewable sources excluding hydroelectric by state by sector/
                    ├── Net_generation_for_other_renewables.csv
                    1.12 Net generation from hydroelectric (pumped storage) power by state by sector/
                    ├── Net_generation_for_hydro-electric_pumped_storage.csv
                    1.13 Net generation from other energy sources by state by sector/
                    ├── Net_generation_for_other.csv
                    1.14 Net generation from wind by state by sector/
                    ├── Net_generation_for_wind.csv
                    1.15 Net generation from biomass by state by sector/
                    ├── Net_generation_for_biomass.csv
                    1.16 Net generation from geothermal by census division by sector/
                    ├── Net_generation_for_geothermal.csv
                    1.2.a Net generation by energy source: electric utilities/
                    ├── Net_generation_for_electric_utility.csv
                    1.2.b Net generation by energy source: independent power producers/
                    ├── Net_generation_for_independent_power_producers.csv
                    1.2.c Net generation by energy source: commercial sector/
                    ├── Net_generation_for_all_commercial.csv
                    1.2.d Net generation by energy source: industrial sector/
                    ├── Net_generation_for_all_industrial.csv
                    1.20 Net generation from solar by state by sector/
                    ├── Net_generation_for_all_utility-scale_solar.csv
                    1.3 Net generation by state by sector/
                    ├── Net_generation_for_all_fuels_(utility-scale).csv
                    1.4 Net generation from coal by state by sector/
                    ├── Net_generation_for_coal.csv
                    1.5 Net generation from petroleum liquids by state by sector/
                    ├── Net_generation_for_petroleum_liquids.csv
                    1.6 Net generation from petroleum coke by state by sector/
                    ├── Net_generation_for_petroleum_coke.csv
                    1.7 Net generation from natural gas by state by sector/
                    ├── Net_generation_for_natural_gas.csv
                    1.8 Net generation from other gases by state by sector/
                    ├── Net_generation_for_other_gases.csv
                    1.9 Net generation from nuclear energy by state by sector/
                    ├── Net_generation_for_nuclear.csv
                    2.1.a Consumption of coal for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_coal.csv
                    2.1.b Consumption of coal for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_coal.csv
                    2.1.c Consumption of coal for electricity generation and useful thermal output by sector/
                    ├── Total_consumption_for_coal.csv
                    2.2.a Consumption of petroleum liquids for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_liquids.csv
                    2.2.b Consumption of petroleum liquids for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_petroleum_liquids.csv
                    2.2.c Total consumption of petroleum liquids by sector/
                    ├── Total_consumption_for_petroleum_liquids.csv
                    2.3.a Consumption of petroleum coke for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_coke.csv
                    2.3.b Consumption of petroleum coke for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_petroleum_coke.csv
                    2.3.c Total consumption of petroleum coke by sector/
                    ├── Total_consumption_for_petroleum_coke.csv
                    2.4.a Consumption of natural gas for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_natural_gas.csv
                    2.4.b Consumption of natural gas for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_natural_gas.csv
                    2.4.c Total consumption of natural gas by sector/
                    ├── Total_consumption_for_natural_gas.csv
                    2.5 Consumption of coal for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_coal.csv
                    2.6 Consumption of petroleum liquids for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_liquids.csv
                    2.7 Consumption of petroleum coke for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_coke.csv
                    2.8 Consumption of natural gas for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_natural_gas.csv
                    3.1 Stocks of coal, petroleum liquids, and petroleum coke: electric power sector/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_United_States.csv
                    3.2 Stocks of coal, petroleum liquids, and petroleum coke: electric power sector by state/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_electric_power.csv
                    3.3 Stocks of coal: electric power sector by census division/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_coal.csv
                    3.3 Stocks of petroleum coke: electric power sector by census division/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_petroleum_coke.csv
                    3.3 Stocks of petroleum liquids: electric power sector by census division/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_petroleum_liquids.csv
                    3.4 Stocks of coal by coal rank/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_electric_utility.csv
                    4.10.a Average cost of coal delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_coal.csv
                    4.11.a Average cost of petroleum liquids delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_petroleum_liquids.csv
                    4.12.a Average cost of petroleum coke delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_petroleum_coke.csv
                    4.13.a Average cost of natural gas delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_natural_gas.csv
                    4.6.a Receipts of coal delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_coal.csv
                    4.7.a Receipts of petroleum liquids delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_natural_gas.csv
                    4.8.a Receipts of petroleum coke delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_petroleum_coke.csv
                    4.9.a Receipts of natural gas delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_natural_gas.csv
                    5.1 Retail sales of electricity to ultimate customers: total by end-use sector/
                    ├── Retail_sales_of_electricity.csv
                    5.2 Revenue from retail sales of electricity to ultimate customers total by end-use sector/
                    ├── Revenue_from_retail_sales_of_electricity.csv
                    5.3 Average retail price of electricity to ultimate customers: total by end-use sector/
                    ├── Average_retail_price_of_electricity.csv
                    5.4 Retail sales of electricity to ultimate customers by end-use sector, by state/
                    ├── Retail_sales_of_electricity.csv
                    5.5 Revenue from retail sales of electricity to ultimate customers by end-use sector, by state/
                    ├── Revenue_from_retail_sales_of_electricity.csv
                    5.6 Average retail price of electricity to ultimate customers by end-use sector, by state/
                    ├── Average_retail_price_of_electricity.csv
                    Average cost of fossil fuels for electricity generation/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_for_all_sectors.csv
                    Average cost of fossil fuels for electricity generation (per Btu)/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_coal.csv
                    Average retail price of electricity/
                    ├── Average_retail_price_of_electricity.csv
                    Consumption for electricity generation/
                    ├── Consumption_for_electricity_generation_for_coal.csv
                    Consumption for electricity generation (Btu)/
                    ├── Consumption_for_electricity_generation_(Btu)_for_petroleum_liquids.csv
                    Consumption for useful thermal output/
                    ├── Consumption_for_useful_thermal_output_for_coal.csv
                    Consumption for useful thermal output (Btu)/
                    ├── Consumption_for_useful_thermal_output_(Btu)_for_all_sectors.csv
                    Fossil-fuel stocks for electricity generation/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_coal.csv
                    Net generation/
                    ├── Net_generation_for_geothermal.csv
                    Number of customer accounts/
                    ├── Number_of_customer_accounts.csv
                    Plant level data/
                    ├── Plants_for_all_sectorsUnited_Statesmultiple_fuel_types.csv
                    Quality of fossil fuels in electricity generation : ash content/
                    ├── Quality_of_fossil_fuels_in_electricity_generation___ash_content_for_coal.csv
                    Quality of fossil fuels in electricity generation : sulfur content/
                    ├── Quality_of_fossil_fuels_in_electricity_generation___sulfur_content_for_coal.csv
                    Receipts of fossil fuels by electricity plants/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_all_sectors.csv
                    Receipts of fossil fuels by electricity plants (Btu)/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_(Btu)_for_coal.csv
                    Retail sales of electricity/
                    ├── Retail_sales_of_electricity.csv
                    Revenue from retail sales of electricity/
                    ├── Revenue_from_retail_sales_of_electricity.csv
                    Total consumption/
                    ├── Total_consumption_for_all_sectors.csv
                    Total consumption (Btu)/
                    ├── Total_consumption_(Btu)_for_coal.csv
        6_electricity_beta/
            code/
            ├── 6.py
            ├── test.ipynb
            data/
                annual/
                    1.10 Net generation from hydroelectric (conventional) power by state by sector/
                    ├── Net_generation_for_conventional_hydroelectric.csv
                    1.11 Net generation from renewable sources excluding hydroelectric by state by sector/
                    ├── Net_generation_for_other_renewables.csv
                    1.12 Net generation from hydroelectric (pumped storage) power by state by sector/
                    ├── Net_generation_for_hydro-electric_pumped_storage.csv
                    1.13 Net generation from other energy sources by state by sector/
                    ├── Net_generation_for_other.csv
                    1.14 Net generation from wind by state by sector/
                    ├── Net_generation_for_wind.csv
                    1.15 Net generation from biomass by state by sector/
                    ├── Net_generation_for_all_sectors.csv
                    1.16 Net generation from geothermal by census division by sector/
                    ├── Net_generation_for_geothermal.csv
                    1.20 Net generation from solar by state by sector/
                    ├── Net_generation_for_all_utility-scale_solar.csv
                    1.3 Net generation by state by sector/
                    ├── Net_generation_for_all_fuels_(utility-scale).csv
                    1.4 Net generation from coal by state by sector/
                    ├── Net_generation_for_coal.csv
                    1.5 Net generation from petroleum liquids by state by sector/
                    ├── Net_generation_for_petroleum_liquids.csv
                    1.6 Net generation from petroleum coke by state by sector/
                    ├── Net_generation_for_petroleum_coke.csv
                    1.7 Net generation from natural gas by state by sector/
                    ├── Net_generation_for_natural_gas.csv
                    1.8 Net generation from other gases by state by sector/
                    ├── Net_generation_for_other_gases.csv
                    1.9 Net generation from nuclear energy by state by sector/
                    ├── Net_generation_for_nuclear.csv
                    2.1.a Consumption of coal for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_coal.csv
                    2.1.b Consumption of coal for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_coal.csv
                    2.1.c Consumption of coal for electricity generation and useful thermal output by sector/
                    ├── Total_consumption_for_coal.csv
                    2.2.a Consumption of petroleum liquids for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_liquids.csv
                    2.2.b Consumption of petroleum liquids for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_petroleum_liquids.csv
                    2.2.c Total consumption of petroleum liquids by sector/
                    ├── Total_consumption_for_petroleum_liquids.csv
                    2.3.a Consumption of petroleum coke for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_coke.csv
                    2.3.b Consumption of petroleum coke for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_petroleum_coke.csv
                    2.3.c Total consumption of petroleum coke by sector/
                    ├── Total_consumption_for_petroleum_coke.csv
                    2.4.a Consumption of natural gas for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_natural_gas.csv
                    2.4.b Consumption of natural gas for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_natural_gas.csv
                    2.4.c Total consumption of natural gas by sector/
                    ├── Total_consumption_for_natural_gas.csv
                    2.5 Consumption of coal for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_coal.csv
                    2.6 Consumption of petroleum liquids for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_liquids.csv
                    2.7 Consumption of petroleum coke for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_coke.csv
                    2.8 Consumption of natural gas for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_natural_gas.csv
                    3.4 Stocks of coal by coal rank/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_electric_utility.csv
                    4.10.a Average cost of coal delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_coal.csv
                    4.11.a Average cost of petroleum liquids delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_petroleum_liquids.csv
                    4.12.a Average cost of petroleum coke delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_petroleum_coke.csv
                    4.13.a Average cost of natural gas delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_natural_gas.csv
                    4.6.a Receipts of coal delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_coal.csv
                    4.7.a Receipts of petroleum liquids delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_petroleum_liquids.csv
                    4.8.a Receipts of petroleum coke delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_petroleum_coke.csv
                    4.9.a Receipts of natural gas delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_natural_gas.csv
                    5.2 Revenue from retail sales of electricity to ultimate customers total by end-use sector/
                    ├── Revenue_from_retail_sales_of_electricity.csv
                    5.4 Retail sales of electricity to ultimate customers by end-use sector, by state/
                    ├── Retail_sales_of_electricity.csv
                    5.5 Revenue from retail sales of electricity to ultimate customers by end-use sector, by state/
                    ├── Revenue_from_retail_sales_of_electricity.csv
                    5.6 Average retail price of electricity to ultimate customers by end-use sector, by state/
                    ├── Average_retail_price_of_electricity.csv
                    Average cost of fossil fuels for electricity generation/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_for_petroleum_liquids.csv
                    Average cost of fossil fuels for electricity generation (per Btu)/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_all_sectors.csv
                    Average retail price of electricity/
                    ├── Average_retail_price_of_electricity.csv
                    Consumption for electricity generation/
                    ├── Consumption_for_electricity_generation_for_natural_gas.csv
                    Consumption for electricity generation (Btu)/
                    ├── Consumption_for_electricity_generation_(Btu)_for_independent_power_producers.csv
                    Consumption for useful thermal output/
                    ├── Consumption_for_useful_thermal_output_for_electric_utility.csv
                    Consumption for useful thermal output (Btu)/
                    ├── Consumption_for_useful_thermal_output_(Btu)_for_independent_power_producers.csv
                    Fossil-fuel stocks for electricity generation/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_petroleum_liquids.csv
                    Net generation/
                    ├── Net_generation_for_all_sectors.csv
                    Number of customer accounts/
                    ├── Number_of_customer_accounts.csv
                    Plant level data/
                        annual_emissions/
                        ├── 2014.csv
                        ......
                        ├── 2021.csv
                        consumption-mmbtu/
                        ├── 2001.csv
                        ......
                        ├── 2022.csv
                        consumption-mmbtu_unit/
                        ├── 2001.csv
                        ......
                        ├── 2022.csv
                        consumption-quantity/
                        ├── 2001.csv
                        ......
                        ├── 2022.csv
                        generation/
                        ├── 2001.csv
                        ......
                        ├── 2022.csv
                        overview/
                        ├── 2001.csv
                        ......
                        ├── 2022.csv
                        water-intensity/
                        ├── 2014.csv
                        ......
                        ├── 2021.csv
                        water-rate/
                        ├── 2014.csv
                        ......
                        ├── 2021.csv
                        water-source/
                        ├── 2014.csv
                        ......
                        ├── 2021.csv
                        water-volume/
                        ├── 2014.csv
                        ......
                        ├── 2021.csv
                    Receipts of fossil fuels by electricity plants/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_petroleum_coke.csv
                    Receipts of fossil fuels by electricity plants (Btu)/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_(Btu)_for_coal.csv
                    Retail sales of electricity/
                    ├── Retail_sales_of_electricity.csv
                    Revenue from retail sales of electricity/
                    ├── Revenue_from_retail_sales_of_electricity.csv
                    Total consumption/
                    ├── Total_consumption_for_coal.csv
                    Total consumption (Btu)/
                    ├── Total_consumption_(Btu)_for_coal.csv
                monthly/
                    1.10 Net generation from hydroelectric (conventional) power by state by sector/
                    ├── Net_generation_for_conventional_hydroelectric.csv
                    1.11 Net generation from renewable sources excluding hydroelectric by state by sector/
                    ├── Net_generation_for_other_renewables.csv
                    1.12 Net generation from hydroelectric (pumped storage) power by state by sector/
                    ├── Net_generation_for_hydro-electric_pumped_storage.csv
                    1.13 Net generation from other energy sources by state by sector/
                    ├── Net_generation_for_other.csv
                    1.14 Net generation from wind by state by sector/
                    ├── Net_generation_for_wind.csv
                    1.15 Net generation from biomass by state by sector/
                    ├── Net_generation_for_biomass.csv
                    1.16 Net generation from geothermal by census division by sector/
                    ├── Net_generation_for_geothermal.csv
                    1.20 Net generation from solar by state by sector/
                    ├── Net_generation_for_all_utility-scale_solar.csv
                    1.3 Net generation by state by sector/
                    ├── Net_generation_for_all_fuels_(utility-scale).csv
                    1.4 Net generation from coal by state by sector/
                    ├── Net_generation_for_coal.csv
                    1.5 Net generation from petroleum liquids by state by sector/
                    ├── Net_generation_for_petroleum_liquids.csv
                    1.6 Net generation from petroleum coke by state by sector/
                    ├── Net_generation_for_petroleum_coke.csv
                    1.7 Net generation from natural gas by state by sector/
                    ├── Net_generation_for_natural_gas.csv
                    1.8 Net generation from other gases by state by sector/
                    ├── Net_generation_for_other_gases.csv
                    1.9 Net generation from nuclear energy by state by sector/
                    ├── Net_generation_for_nuclear.csv
                    2.1.a Consumption of coal for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_coal.csv
                    2.1.b Consumption of coal for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_coal.csv
                    2.1.c Consumption of coal for electricity generation and useful thermal output by sector/
                    ├── Total_consumption_for_coal.csv
                    2.2.a Consumption of petroleum liquids for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_liquids.csv
                    2.2.b Consumption of petroleum liquids for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_petroleum_liquids.csv
                    2.2.c Total consumption of petroleum liquids by sector/
                    ├── Total_consumption_for_petroleum_liquids.csv
                    2.3.a Consumption of petroleum coke for electricity generation by sector/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_coal.csv
                    2.3.b Consumption of petroleum coke for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_petroleum_coke.csv
                    2.3.c Total consumption of petroleum coke by sector/
                    ├── Total_consumption_for_petroleum_coke.csv
                    2.4.a Consumption of natural gas for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_natural_gas.csv
                    2.4.b Consumption of natural gas for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_natural_gas.csv
                    2.4.c Total consumption of natural gas by sector/
                    ├── Total_consumption_for_natural_gas.csv
                    2.5 Consumption of coal for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_coal.csv
                    2.6 Consumption of petroleum liquids for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_liquids.csv
                    2.7 Consumption of petroleum coke for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_coke.csv
                    2.8 Consumption of natural gas for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_natural_gas.csv
                    3.4 Stocks of coal by coal rank/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_electric_utility.csv
                    4.10.a Average cost of coal delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_coal.csv
                    4.11.a Average cost of petroleum liquids delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_petroleum_liquids.csv
                    4.12.a Average cost of petroleum coke delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_petroleum_coke.csv
                    4.13.a Average cost of natural gas delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_natural_gas.csv
                    4.6.a Receipts of coal delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_coal.csv
                    4.7.a Receipts of petroleum liquids delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_petroleum_liquids.csv
                    4.8.a Receipts of petroleum coke delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_petroleum_coke.csv
                    4.9.a Receipts of natural gas delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_natural_gas.csv
                    5.2 Revenue from retail sales of electricity to ultimate customers total by end-use sector/
                    ├── Revenue_from_retail_sales_of_electricity.csv
                    5.4 Retail sales of electricity to ultimate customers by end-use sector, by state/
                    ├── Retail_sales_of_electricity.csv
                    5.5 Revenue from retail sales of electricity to ultimate customers by end-use sector, by state/
                    ├── Revenue_from_retail_sales_of_electricity.csv
                    5.6 Average retail price of electricity to ultimate customers by end-use sector, by state/
                    ├── Average_retail_price_of_electricity.csv
                    Average cost of fossil fuels for electricity generation/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_for_petroleum_liquids.csv
                    Average cost of fossil fuels for electricity generation (per Btu)/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_all_sectors.csv
                    Average retail price of electricity/
                    ├── Average_retail_price_of_electricity.csv
                    Consumption for electricity generation/
                    ├── Consumption_for_electricity_generation_for_natural_gas.csv
                    Consumption for electricity generation (Btu)/
                    ├── Consumption_for_electricity_generation_(Btu)_for_independent_power_producers.csv
                    Consumption for useful thermal output/
                    ├── Consumption_for_useful_thermal_output_for_electric_utility.csv
                    Consumption for useful thermal output (Btu)/
                    ├── Consumption_for_useful_thermal_output_(Btu)_for_independent_power_producers.csv
                    Fossil-fuel stocks for electricity generation/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_petroleum_liquids.csv
                    Net generation/
                    ├── Net_generation_for_all_sectors.csv
                    Number of customer accounts/
                    ├── Number_of_customer_accounts.csv
                    Plant level data/
                        consumption-mmbtu/
                        ├── 200101.csv
                        ......
                        ├── 202305.csv
                        consumption-mmbtu_unit/
                        ├── 200101.csv
                        ......
                        ├── 202305.csv
                        consumption-quantity/
                        ├── 200101.csv
                        ......
                        ├── 202305.csv
                        generation/
                        ├── 200101.csv
                        ......
                        ├── 202305.csv
                        overview/
                        ├── 200101.csv
                        ......
                        ├── 202305.csv
                        water-intensity/
                        ├── 201401.csv
                        ......
                        ├── 202112.csv
                        water-rate/
                        ├── 201401.csv
                        ......
                        ├── 202112.csv
                        water-source/
                        ├── 201401.csv
                        ......
                        ├── 202112.csv
                        water-volume/
                        ├── 201401.csv
                        ......
                        ├── 202112.csv
                    Receipts of fossil fuels by electricity plants/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_petroleum_coke.csv
                    Receipts of fossil fuels by electricity plants (Btu)/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_(Btu)_for_coal.csv
                    Retail sales of electricity/
                    ├── Retail_sales_of_electricity.csv
                    Revenue from retail sales of electricity/
                    ├── Revenue_from_retail_sales_of_electricity.csv
                    Total consumption/
                    ├── Total_consumption_for_coal.csv
                    Total consumption (Btu)/
                    ├── Total_consumption_(Btu)_for_coal.csv
                quarterly/
                    1.10 Net generation from hydroelectric (conventional) power by state by sector/
                    ├── Net_generation_for_conventional_hydroelectric.csv
                    1.11 Net generation from renewable sources excluding hydroelectric by state by sector/
                    ├── Net_generation_for_other_renewables.csv
                    1.12 Net generation from hydroelectric (pumped storage) power by state by sector/
                    ├── Net_generation_for_hydro-electric_pumped_storage.csv
                    1.13 Net generation from other energy sources by state by sector/
                    ├── Net_generation_for_other.csv
                    1.14 Net generation from wind by state by sector/
                    ├── Net_generation_for_wind.csv
                    1.15 Net generation from biomass by state by sector/
                    ├── Net_generation_for_biomass.csv
                    1.16 Net generation from geothermal by census division by sector/
                    ├── Net_generation_for_geothermal.csv
                    1.20 Net generation from solar by state by sector/
                    ├── Net_generation_for_all_utility-scale_solar.csv
                    1.3 Net generation by state by sector/
                    ├── Net_generation_for_all_fuels_(utility-scale).csv
                    1.4 Net generation from coal by state by sector/
                    ├── Net_generation_for_coal.csv
                    1.5 Net generation from petroleum liquids by state by sector/
                    ├── Net_generation_for_petroleum_liquids.csv
                    1.6 Net generation from petroleum coke by state by sector/
                    ├── Net_generation_for_petroleum_coke.csv
                    1.7 Net generation from natural gas by state by sector/
                    ├── Net_generation_for_natural_gas.csv
                    1.8 Net generation from other gases by state by sector/
                    ├── Net_generation_for_other_gases.csv
                    1.9 Net generation from nuclear energy by state by sector/
                    ├── Net_generation_for_nuclear.csv
                    2.1.a Consumption of coal for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_coal.csv
                    2.1.b Consumption of coal for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_coal.csv
                    2.1.c Consumption of coal for electricity generation and useful thermal output by sector/
                    ├── Total_consumption_for_coal.csv
                    2.2.a Consumption of petroleum liquids for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_liquids.csv
                    2.2.b Consumption of petroleum liquids for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_petroleum_liquids.csv
                    2.2.c Total consumption of petroleum liquids by sector/
                    ├── Total_consumption_for_petroleum_liquids.csv
                    2.3.a Consumption of petroleum coke for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_coke.csv
                    2.3.b Consumption of petroleum coke for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_petroleum_coke.csv
                    2.3.c Total consumption of petroleum coke by sector/
                    ├── Total_consumption_for_petroleum_coke.csv
                    2.4.a Consumption of natural gas for electricity generation by sector/
                    ├── Consumption_for_electricity_generation_for_natural_gas.csv
                    2.4.b Consumption of natural gas for useful thermal output by sector/
                    ├── Consumption_for_useful_thermal_output_for_natural_gas.csv
                    2.4.c Total consumption of natural gas by sector/
                    ├── Total_consumption_for_natural_gas.csv
                    2.5 Consumption of coal for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_coal.csv
                    2.6 Consumption of petroleum liquids for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_liquids.csv
                    2.7 Consumption of petroleum coke for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_petroleum_coke.csv
                    2.8 Consumption of natural gas for electricity generation by state by sector/
                    ├── Consumption_for_electricity_generation_for_natural_gas.csv
                    3.4 Stocks of coal by coal rank/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_electric_utility.csv
                    4.10.a Average cost of coal delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_coal.csv
                    4.11.a Average cost of petroleum liquids delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_petroleum_liquids.csv
                    4.12.a Average cost of petroleum coke delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_petroleum_coke.csv
                    4.13.a Average cost of natural gas delivered for electricity generation by state/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_natural_gas.csv
                    4.6.a Receipts of coal delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_coal.csv
                    4.7.a Receipts of petroleum liquids delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_petroleum_liquids.csv
                    4.8.a Receipts of petroleum coke delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_petroleum_coke.csv
                    4.9.a Receipts of natural gas delivered for electricity generation by state/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_natural_gas.csv
                    5.2 Revenue from retail sales of electricity to ultimate customers total by end-use sector/
                    ├── Revenue_from_retail_sales_of_electricity.csv
                    5.4 Retail sales of electricity to ultimate customers by end-use sector, by state/
                    ├── Retail_sales_of_electricity.csv
                    5.5 Revenue from retail sales of electricity to ultimate customers by end-use sector, by state/
                    ├── Revenue_from_retail_sales_of_electricity.csv
                    5.6 Average retail price of electricity to ultimate customers by end-use sector, by state/
                    ├── Average_retail_price_of_electricity.csv
                    Average cost of fossil fuels for electricity generation/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_for_petroleum_liquids.csv
                    Average cost of fossil fuels for electricity generation (per Btu)/
                    ├── Average_cost_of_fossil_fuels_for_electricity_generation_(per_Btu)_for_all_sectors.csv
                    Average retail price of electricity/
                    ├── Average_retail_price_of_electricity.csv
                    Consumption for electricity generation/
                    ├── Consumption_for_electricity_generation_for_natural_gas.csv
                    Consumption for electricity generation (Btu)/
                    ├── Consumption_for_electricity_generation_(Btu)_for_independent_power_producers.csv
                    Consumption for useful thermal output/
                    ├── Consumption_for_useful_thermal_output_for_electric_utility.csv
                    Consumption for useful thermal output (Btu)/
                    ├── Consumption_for_useful_thermal_output_(Btu)_for_independent_power_producers.csv
                    Fossil-fuel stocks for electricity generation/
                    ├── Fossil-fuel_stocks_for_electricity_generation_for_petroleum_liquids.csv
                    Net generation/
                    ├── Net_generation_for_all_sectors.csv
                    Number of customer accounts/
                    ├── Number_of_customer_accounts.csv
                    Plant level data/
                        consumption-mmbtu/
                        ├── 200101.csv
                        ......
                        ├── 202301.csv
                        consumption-mmbtu_unit/
                        ├── 200101.csv
                        ......
                        ├── 202301.csv
                        consumption-quantity/
                        ├── 200101.csv
                        ......
                        ├── 202301.csv
                        generation/
                        ├── 200101.csv
                        ......
                        ├── 202301.csv
                        overview/
                        ├── 200101.csv
                        ......
                        ├── 202301.csv
                        water-intensity/
                        ├── 201401.csv
                        ......
                        ├── 202104.csv
                        water-rate/
                        ├── 201401.csv
                        ......
                        ├── 202104.csv
                        water-source/
                        ├── 201401.csv
                        ......
                        ├── 202104.csv
                        water-volume/
                        ├── 201401.csv
                        ......
                        ├── 202104.csv
                    Receipts of fossil fuels by electricity plants/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_for_petroleum_coke.csv
                    Receipts of fossil fuels by electricity plants (Btu)/
                    ├── Receipts_of_fossil_fuels_by_electricity_plants_(Btu)_for_coal.csv
                    Retail sales of electricity/
                    ├── Retail_sales_of_electricity.csv
                    Revenue from retail sales of electricity/
                    ├── Revenue_from_retail_sales_of_electricity.csv
                    Total consumption/
                    ├── Total_consumption_for_coal.csv
                    Total consumption (Btu)/
                    ├── Total_consumption_(Btu)_for_coal.csv
        9_energy_dept/
            code/
            ├── test.ipynb
            data/
            ├── 9.csv
            ├── data.pkl
    energy_price/
        code/
        data/
        ├── CAISO.zip
        ├── ERCOT.zip
        ├── MISO.zip
        ├── NewEnglandISO.zip
        ├── NYISO.zip
            SPPISO/
                DAM/
                ├── 2013.zip
                ├── 2014.zip
                ├── 2015.zip
                ├── 2016.zip
                ├── 2017.zip
                ├── 2018.zip
                ├── 2019.zip
                ├── 2020.zip
                ├── 2021.zip
                ├── DA-LMP-MONTHLY-SL-202201.csv
                ├── DA-LMP-MONTHLY-SL-202202.csv
                ├── DA-LMP-MONTHLY-SL-202203.csv
                ├── DA-LMP-MONTHLY-SL-202204.csv
                ├── DA-LMP-MONTHLY-SL-202205.csv
                ├── DA-LMP-MONTHLY-SL-202206.csv
                ├── DA-LMP-MONTHLY-SL-202207.csv
                ├── DA-LMP-MONTHLY-SL-202208.csv
                ├── DA-LMP-MONTHLY-SL-202209.csv
                ├── DA-LMP-MONTHLY-SL-202210.csv
                ├── DA-LMP-MONTHLY-SL-202211.csv
                ├── DA-LMP-MONTHLY-SL-202212.csv
                ├── DA-LMP-MONTHLY-SL-202301.csv
                ├── DA-LMP-MONTHLY-SL-202302.csv
                ├── DA-LMP-MONTHLY-SL-202303.csv
                ├── DA-LMP-MONTHLY-SL-202304.csv
                ├── DA-LMP-MONTHLY-SL-202305.csv
                ├── DA-LMP-MONTHLY-SL-202306.csv
                RTM/
                ├── rtbm-lmp-by-location?path=%2F2013%2F2013.zip
                ├── rtbm-lmp-by-location?path=%2F2014%2F2014.zip
                ├── rtbm-lmp-by-location?path=%2F2015%2F2015.zip
                ├── rtbm-lmp-by-location?path=%2F2016%2F2016.zip
                ├── rtbm-lmp-by-location?path=%2F2017%2F2017.zip
                ├── rtbm-lmp-by-location?path=%2F2018%2F2018.zip
                ├── rtbm-lmp-by-location?path=%2F2019%2F2019.zip
                ├── rtbm-lmp-by-location?path=%2F2020%2F2020.zip
                ├── rtbm-lmp-by-location?path=%2F2021%2F2021.zip
                ├── rtbm-lmp-by-location?path=%2F2022%2F2022-RTBM-LMP-SL-ANNUAL-ROLLUP.zip
                ├── rtbm-lmp-by-location?path=%2F2023%2F01%2FRTBM-LMP-MONTHLY-SL-202301.csv
                ├── rtbm-lmp-by-location?path=%2F2023%2F02%2FRTBM-LMP-MONTHLY-SL-202302.csv
                ├── rtbm-lmp-by-location?path=%2F2023%2F03%2FRTBM-LMP-MONTHLY-SL-202303.csv
                ├── rtbm-lmp-by-location?path=%2F2023%2F04%2FRTBM-LMP-MONTHLY-SL-202304.csv
                ├── rtbm-lmp-by-location?path=%2F2023%2F05%2FRTBM-LMP-MONTHLY-SL-202305.csv
                ├── rtbm-lmp-by-location?path=%2F2023%2F06%2FRTBM-LMP-MONTHLY-SL-202306.csv
                ├── rtm.log
    tool/
    ├── folder_tree.py
    ├── unzip.py
```
