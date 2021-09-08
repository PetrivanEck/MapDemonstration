
############################### Libraries:

import pandas as pd
import folium
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from folium import plugins
import os
from folium.plugins import MiniMap
from folium import plugins
from folium.plugins import HeatMap
import pandas as pd
import geopandas as gpd
import flask
from flask import Flask
import matplotlib.pyplot as plt
from folium.plugins import Draw
from shapely.ops import nearest_points
from shapely.geometry import LineString
warnings.filterwarnings('ignore')

######## Emerging Farmers:
emerging_Farmers = pd.read_excel('comprehensive.xls',sheet_name=4)
emerging_Farmers.columns = ['Emerging_Farmers', 'Seller_Area_Cluster', 'Co_ordinates']
emerging_Farmers[['Latitude','Longitude']] = emerging_Farmers['Co_ordinates'].str.split(',', expand=True)
emerging_Farmers['Latitude'] = emerging_Farmers['Latitude'].str.replace(r'S', '')
emerging_Farmers['Latitude'] = emerging_Farmers['Latitude'].str.replace(r'°', '')
emerging_Farmers['Longitude'] = emerging_Farmers['Longitude'].str.replace(r'E', '')
emerging_Farmers['Longitude'] = emerging_Farmers['Longitude'].str.replace(r'°', '')
emerging_Farmers = emerging_Farmers.drop(['Co_ordinates'], axis=1)
emerging_Farmers['Latitude'] = ('-' + emerging_Farmers['Latitude'])
print(emerging_Farmers.head())
####### Hotspot Towns:

unrest = pd.read_excel('comprehensive.xls',sheet_name=0)
unrest[['Latitude','Longitude']] = unrest['Co-Ords'].str.split(',', expand=True)
unrest['Latitude'] = unrest['Latitude'].str.replace(r'S', '')
unrest['Latitude'] = unrest['Latitude'].str.replace(r'°', '')
unrest['Longitude'] = unrest['Longitude'].str.replace(r'E', '')
unrest['Longitude'] = unrest['Longitude'].str.replace(r'°', '')
unrest = unrest.drop(['Co-Ords'], axis=1)
unrest['Latitude'] = ('-' + unrest['Latitude'])
print(unrest.head())

###### OFS Sellers:
ofs = pd.read_excel('comprehensive.xls',sheet_name=6)
ofs[['Latitude','Longitude']] = ofs['Co ordinates'].str.split(',', expand=True)
ofs['Latitude'] = ofs['Latitude'].str.replace(r'S', '')
ofs['Latitude'] = ofs['Latitude'].str.replace(r'°', '')
ofs['Longitude'] = ofs['Longitude'].str.replace(r'E', '')
ofs['Longitude'] = ofs['Longitude'].str.replace(r'°', '')
ofs = ofs.drop(['Co ordinates'], axis=1)
ofs['Latitude'] = ('-' + ofs['Latitude'])
ofs.columns = ['Account_Name', 'Seller_Area_Cluster', 'Latitude', 'Longitude']
print(ofs.head())

######## DARD:
dard = pd.read_excel('comprehensive.xls',sheet_name=5)
dard[['Latitude','Longitude']] = dard['Co ordinates'].str.split(',', expand=True)
dard['Latitude'] = dard['Latitude'].str.replace(r'S', '')
dard['Latitude'] = dard['Latitude'].str.replace(r'°', '')
dard['Longitude'] = dard['Longitude'].str.replace(r'E', '')
dard['Longitude'] = dard['Longitude'].str.replace(r'°', '')
dard = dard.drop(['Co ordinates'], axis=1)
dard['Latitude'] = ('-' + dard['Latitude'])
print(dard.head())


###### FOOD FORWARD SA:
ffsa = pd.read_excel('SAHandFassa.xlsx',sheet_name=2)
ffsa.columns = ['Locations', 'Co']
ffsa[['Latitude','Longitude']] = ffsa['Co'].str.split('S', expand=True)
ffsa['Latitude'] = ffsa['Latitude'].str.replace(r'°', '')
ffsa['Latitude'] = ffsa['Latitude'].str.replace(r'"', '')
ffsa['Longitude'] = ffsa['Longitude'].str.replace(r'°', '')
ffsa['Longitude'] = ffsa['Longitude'].str.replace(r'"', '')
ffsa['Latitude'] = ffsa['Latitude'].str.replace(r'’', '')
ffsa['Longitude'] = ffsa['Longitude'].str.replace(r'’', '')
ffsa['Longitude'] = ffsa['Longitude'].str.replace(r'E', '')
ffsa['Latitude'] = ('-' + ffsa['Latitude'])
ffsa = ffsa.drop(['Co'],axis=1)
img = os.path.abspath("fooddrive2.png")
print(ffsa.head())

######## Pick n Pay DC:

DC = pd.read_excel('picknpay.xlsx',sheet_name=2)
pickimg = os.path.abspath("pick.png")
DC[['Latitude','Longitude']] = DC['Co-Ordinates'].str.split('S', expand=True)
DC['Latitude'] = DC['Latitude'].str.replace(r'°', '')
DC['Latitude'] = DC['Latitude'].str.replace(r'"', '')
DC['Longitude'] = DC['Longitude'].str.replace(r'°', '')
DC['Longitude'] = DC['Longitude'].str.replace(r'"', '')
DC['Longitude'] = DC['Longitude'].str.replace(r'E', '')
DC['Latitude'] = DC['Latitude'].str.replace(r'’', '')
DC['Longitude'] = DC['Longitude'].str.replace(r'’', '')
DC['Latitude'] = ('-' + DC['Latitude'])
DC.columns = ['Destribution_Centre','Co','Latitude','Longitude']
print(DC.head())

######## Pick n Pay Staging Hubs:

staging_hubs = pd.read_excel('picknpay.xlsx',sheet_name=3,header=1 )
staging_hubs = staging_hubs.drop(['Unnamed: 0'],axis=1)
staging_hubs.columns = ['staging_hubs', 'Town','Co']
staging_hubs[['Latitude','Longitude']] = staging_hubs['Co'].str.split(',', expand=True)
staging_hubs['Latitude'] = staging_hubs['Latitude'].str.replace(r'S', '')
staging_hubs['Latitude'] = staging_hubs['Latitude'].str.replace(r'°', '')
staging_hubs['Longitude'] = staging_hubs['Longitude'].str.replace(r'E', '')
staging_hubs['Longitude'] = staging_hubs['Longitude'].str.replace(r'°', '')
staging_hubs['Latitude'] = ('-' + staging_hubs['Latitude'])
print(staging_hubs.head())

######### SA HARVEST:

sa_harvest = pd.read_excel('SAHandFassa.xlsx',sheet_name=1)
sa_harvest.columns = ['Locations', 'Co']
sa_harvest[['Latitude','Longitude']] = sa_harvest['Co'].str.split('S', expand=True)
sa_harvest = sa_harvest.drop(['Co'],axis=1)
sa_harvest['Latitude'] = sa_harvest['Latitude'].str.replace(r'°', '')
sa_harvest['Latitude'] = sa_harvest['Latitude'].str.replace(r'"', '')
sa_harvest['Longitude'] = sa_harvest['Longitude'].str.replace(r'°', '')
sa_harvest['Longitude'] = sa_harvest['Longitude'].str.replace(r'"', '')
sa_harvest['Latitude'] = ('-' + sa_harvest['Latitude'])
sa_harvest['Latitude'] = sa_harvest['Latitude'].str.replace(r'’', '')
sa_harvest['Longitude'] = sa_harvest['Longitude'].str.replace(r'’', '')
sa_harvest['Longitude'] = sa_harvest['Longitude'].str.replace(r'E', '')
simg = os.path.abspath("Unknown.png")
print(sa_harvest.head())

############ Municipalities:

Municipalities = gpd.read_file('Municipalities.json')
Municipalities = Municipalities[Municipalities['PROVINCE'] == 'KZN']
Municipalities = Municipalities[['MUNICNAME','geometry']]
Municipalities = Municipalities.reset_index()
Municipalities = Municipalities.drop('index', axis=1)
Municipalities.columns = ['Municipality', 'geometry']
Municipalities = Municipalities.to_json()
Municipality_style = {'color':'black'}

######### Hello choice Buyers:
buyer = pd.read_excel('comprehensive.xls',sheet_name=1)
buyer[['Latitude','Longitude']] = buyer['Co ordinates'].str.split(',', expand=True)
buyer['Latitude'] = buyer['Latitude'].str.replace(r'S', '')
buyer['Latitude'] = buyer['Latitude'].str.replace(r'°', '')
buyer['Longitude'] = buyer['Longitude'].str.replace(r'E', '')
buyer['Longitude'] = buyer['Longitude'].str.replace(r'°', '')
buyer_heat_map = buyer
buyer['Latitude'] = ('-' + buyer['Latitude'])
buyer = buyer.drop(['Co ordinates','Co ordinates.1'], axis=1)
buyer = buyer[['Account Name','Account Owner','Buyer Area Cluster','Area', 'Province.', 'Shipping Street',
        'Buyer Products', 'Size of Buyer','Latitude', 'Longitude']]
buyer = buyer.dropna(subset=['Latitude'])
buyer_heat_map = buyer_heat_map.drop(['Co ordinates','Co ordinates.1'], axis=1)
buyer_heat_map = buyer_heat_map[['Account Name','Account Owner','Buyer Area Cluster','Area', 'Province.', 'Shipping Street',
        'Buyer Products', 'Size of Buyer','Latitude', 'Longitude']]
buyer_heat_map = buyer_heat_map.dropna(subset=['Latitude'])
buyer_heat_map['density'] = 1
print(buyer.head())
print(buyer_heat_map.head())


########## Hello Choice Sellers:

cleaned_sellers = pd.read_excel('comprehensive.xls',sheet_name=3)
cleaned_sellers[['Latitude','Longitude']] = cleaned_sellers['Co ordinates'].str.split(',', expand=True)
cleaned_sellers['Latitude'] = cleaned_sellers['Latitude'].str.replace(r'S', '')
cleaned_sellers['Latitude'] = cleaned_sellers['Latitude'].str.replace(r'°', '')
cleaned_sellers['Longitude'] = cleaned_sellers['Longitude'].str.replace(r'E', '')
cleaned_sellers['Longitude'] = cleaned_sellers['Longitude'].str.replace(r'°', '')
cleaned_sellers = cleaned_sellers.drop(['Co ordinates'], axis=1)
cleaned_sellers['Latitude'] = ('-' + cleaned_sellers['Latitude'])
seller_heat_map = cleaned_sellers
seller_heat_map['Density'] = 1
print(seller_heat_map.head())
######### NEXT STEP - COMBINE SELLER INFORMATION:


Sellers_locations = pd.read_excel('comprehensive.xls',sheet_name=3)
Sellers_locations[['Latitude','Longitude']] = Sellers_locations['Co ordinates'].str.split(',', expand=True)
Sellers_locations['Latitude'] = Sellers_locations['Latitude'].str.replace(r'S', '')
Sellers_locations['Latitude'] = Sellers_locations['Latitude'].str.replace(r'°', '')
Sellers_locations['Longitude'] = Sellers_locations['Longitude'].str.replace(r'E', '')
Sellers_locations['Longitude'] = Sellers_locations['Longitude'].str.replace(r'°', '')
Sellers_locations = Sellers_locations.drop(['Co ordinates'], axis=1)
Sellers_locations['Latitude'] = ('-' + Sellers_locations['Latitude'])
Sellers_data = pd.read_excel('comprehensive.xls',sheet_name=8)
Sellers_data = Sellers_data [['Account Name', 'Seller Products','Season 1']]
Sellers_data.columns = ['Account_Name', 'Seller_Products','Seller_seasons']
Sellers_locations.columns = ['Account_Name', 'Seller_Area_Clusters', 'Latitude','Longitude']
Consolidated_Sellers = Sellers_locations.merge(Sellers_data, on=['Account_Name'], how='left')
print(Consolidated_Sellers.head())


################### MAP:


app = Flask(__name__)

@app.route('/')
def index():

    KZN = folium.Map(location=[-28.503833,
                            30.8875009],
                            zoom_start=7,
                            control_scale=True)

### Municipalities:

    Municipality = folium.GeoJson(Municipalities,
                              style_function=lambda x: Municipality_style,
                              name="KZN Municipality Demaracation",
                              tooltip=folium.GeoJsonTooltip(
                              fields=['Municipality'],
                              aliases=['Municipality: '],
                              sticky=True,
                              opacity=2.3,
                              direction='right')
                             ).add_to(KZN)

### Pick n Pay Staging Hubs:

    PickNPaystaging_fg = folium.FeatureGroup(name='Pick n Pay Staging Hub', show=False)

    KZN.add_child(PickNPaystaging_fg)

    for lat, lon, locations, hubs in zip(staging_hubs.Latitude, staging_hubs.Longitude, staging_hubs.Town,
                                     staging_hubs.staging_hubs):
        folium.Marker(
        location=[lat, lon],
        popup=folium.Popup('Town: ' + locations + "<br>" + "staging hub: " + str(hubs)
                           , min_width=300, max_width=300, height=300),
        icon=folium.features.CustomIcon(pickimg, icon_size=(50, 50), icon_anchor=(15, 15),
                                        popup_anchor=(-3, -76))
        ).add_to(PickNPaystaging_fg)
#
#
## Hotspot Radius:

    Radius = folium.FeatureGroup(name='50km Radius Around Hotspots', show=False)

    KZN.add_child(Radius)



    for lat, lon in zip(unrest["Latitude"].values.tolist(),
                    unrest["Longitude"].values.tolist()):
        folium.Circle([lat, lon],
                    radius=50000,
                   ).add_to(Radius)
#
#
    Sellers_marker_cluster = plugins.marker_cluster.MarkerCluster(name='HelloChoice Sellers', show=False).add_to(KZN)

    for lat, lon, seller, products, seasons in zip(Consolidated_Sellers["Latitude"].values.tolist(),
                                               Consolidated_Sellers["Longitude"].values.tolist(),
                                               Consolidated_Sellers["Account_Name"].values.tolist(),
                                               Consolidated_Sellers["Seller_Products"].values.tolist(),
                                               Consolidated_Sellers["Seller_seasons"].values.tolist()):
        folium.Marker( location=[lat, lon],
        popup= folium.Popup('Seller Name: ' + seller + "<br>" + "Seller Product Offering: " + str(products)
                         + "<br>" + "Seasons Offered: " + str(seasons)
                        ,min_width=300, max_width=300, height=300),
        icon=folium.Icon(color="black", icon="users",prefix="fa"),
    ).add_to(Sellers_marker_cluster)
#
# # ### Hello Choice Marketing Buyers:

    Buyers_heatmap = folium.FeatureGroup(name='Marketing Campaign: HelloChoice Buyer Clusters', show=False)

    KZN.add_child(Buyers_heatmap)

    buyer_heatmap = HeatMap(list(zip(buyer_heat_map.Latitude.tolist(),
                 buyer_heat_map.Longitude.tolist()))).add_to(Buyers_heatmap)
#
#
# # ### Hello Choice Marketing Sellers:


    Seller_heatmap = folium.FeatureGroup(name='Marketing Campaign: HelloChoice Seller Clusters', show=False)

    KZN.add_child(Seller_heatmap)

    seller_heatmap = HeatMap(list(zip(seller_heat_map.Latitude.to_list(),
                  seller_heat_map.Longitude.to_list()))).add_to(Seller_heatmap)
#
# ## Emerging Farmers:
#
    Emerging_marker_cluster = plugins.marker_cluster.MarkerCluster(name='HelloChoice Emerging Farmers', show=False).add_to(KZN)

    for lat, lon, Emerging_farmer, Area in zip(emerging_Farmers["Latitude"].values.tolist(),
                                      emerging_Farmers["Longitude"].values.tolist(),
                                      emerging_Farmers["Emerging_Farmers"].values.tolist(),
                                      emerging_Farmers["Seller_Area_Cluster"].values.tolist()):
        folium.Marker( location=[lat, lon],
        popup= folium.Popup('Emerging Farmer: ' + Emerging_farmer + "<br>" + " Seller Area Cluster: " + str(Area)
                        ,min_width=300, max_width=300, height=300),
        icon=folium.Icon(color="green", icon="users",prefix="fa"),
        ).add_to(Emerging_marker_cluster)
#
### Hello Choice Buyers:

        Buyer_marker_cluster = plugins.marker_cluster.MarkerCluster(name='HelloChoice Buyers', show=False).add_to(KZN)

    for lat, lon, account_name,products in zip(buyer["Latitude"].values.tolist(),
                                      buyer["Longitude"].values.tolist(),
                                      buyer["Account Name"].values.tolist(),
                                      buyer["Buyer Products"].values.tolist() ):
        folium.Marker( location=[lat, lon],
        popup= folium.Popup('Buyer Name: ' + account_name + "<br>" + " Buyer Products: " + str(products)
                        ,min_width=300, max_width=300, height=300),
        icon=folium.Icon(color="purple", icon="users",prefix="fa"),
        ).add_to(Buyer_marker_cluster)
#
### Unrest Towns:

        Unrest_marker_cluster = plugins.marker_cluster.MarkerCluster(name='Hotspot Towns', show=False).add_to(KZN)

    for lat, lon, Town in zip(unrest["Latitude"].values.tolist(),
                          unrest["Longitude"].values.tolist(),
                          unrest["Town"].values.tolist()):
        folium.Marker(location=[lat, lon],
                  popup=folium.Popup('Hotspot Town: ' + Town
                                     , min_width=300, max_width=300, height=300),
                  icon=folium.Icon(color="red", icon="fire", prefix="fa"),
                  ).add_to(Unrest_marker_cluster)

## OFS SELLERS:

    Ofs_marker_cluster = plugins.marker_cluster.MarkerCluster(name='OFS Sellers', show=False).add_to(KZN)

    for lat, lon, name in zip(ofs["Latitude"].values.tolist(),
                          ofs["Longitude"].values.tolist(),
                          ofs["Account_Name"].values.tolist()):
        folium.Marker(location=[lat, lon],
                  popup=folium.Popup('OFS Seller Name: ' + name
                                     , min_width=300, max_width=300, height=300),
                  icon=folium.Icon(color="yellow", icon="money", prefix="fa"),
                  ).add_to(Ofs_marker_cluster)
#
### DARD:

    Dard_marker_cluster = plugins.marker_cluster.MarkerCluster(name='DARD', show=False).add_to(KZN)

    for lat, lon, name, area in zip(dard["Latitude"].values.tolist(),
                                dard["Longitude"].values.tolist(),
                                dard["Account Name"].values.tolist(),
                                dard["Seller Area Cluster"].values.tolist()):
        folium.Marker(location=[lat, lon],
                  popup=folium.Popup('DARD: ' + name + "<br>" + " Seller Area Cluster: " + str(area)
                                     , min_width=300, max_width=300, height=300),
                  icon=folium.Icon(color="black", icon="building", prefix="fa"),
                  ).add_to(Dard_marker_cluster)
#
### Food Forward SA:

    Food_Forward_sa_fg = folium.FeatureGroup(name='Food Forward SA Warehouses', show=False)

    KZN.add_child(Food_Forward_sa_fg)

    for lat, lon, locations in zip(ffsa.Latitude, ffsa.Longitude, ffsa.Locations):
        folium.Marker(
        location=[lat, lon],
        popup=folium.Popup('Food Forward SA Warehouses Locations: ' + locations
                           , min_width=300, max_width=300, height=300),
        icon=folium.features.CustomIcon(img, icon_size=(50, 50), icon_anchor=(15, 15),
                                        popup_anchor=(-3, -76))
        ).add_to(Food_Forward_sa_fg)
#
### SA Harvest:

    SA_Harvest_sa_fg = folium.FeatureGroup(name='SA Harvest Locations', show=False)

    KZN.add_child(SA_Harvest_sa_fg)

    for lat, lon, locations in zip(sa_harvest.Latitude, sa_harvest.Longitude, sa_harvest.Locations):
        folium.Marker(
        location=[lat, lon],
        popup=folium.Popup('SA Harvest Locations: ' + locations
                           , min_width=300, max_width=300, height=300),
        icon=folium.features.CustomIcon(simg, icon_size=(50, 50), icon_anchor=(15, 15),
                                        popup_anchor=(-3, -76))
        ).add_to(SA_Harvest_sa_fg)

## layer Control:

    folium.LayerControl().add_to(KZN)

## Mini Map:

    minimap = MiniMap()
    minimap.add_to(KZN)


    KZN

    KZN.save(outfile= "HelloChoiceDemonstration.html")
#
# #
    return KZN._repr_html_()
#
#
if __name__ == '__main__':
    app.run()
#
#
#
#
#
#














