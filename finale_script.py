import pandas as pd
import numpy as np
import cPickle
import statistics
from sklearn.preprocessing import Imputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor

data = pd.read_json('dataset.json')

data['DAMAGE_ESTIMATE'] = data['DAMAGE_ESTIMATE_x']
data['DAMAGE_ESTIMATE'].fillna(data['DAMAGE_ESTIMATE_y'], inplace=True)
data = data.drop('DAMAGE_ESTIMATE_x',1)
data = data.drop('DAMAGE_ESTIMATE_y',1)

data['COUNTRY'] = data['COUNTRY_x']
data['COUNTRY'].fillna(data['COUNTRY_y'], inplace=True)
data = data.drop('COUNTRY_x',1)
data = data.drop('COUNTRY_y',1)

data['DAMAGE_MILLIONS_DOLLARS'] = data['DAMAGE_MILLIONS_DOLLARS_x']
data['DAMAGE_MILLIONS_DOLLARS'].fillna(data['DAMAGE_MILLIONS_DOLLARS_y'], inplace=True)
data = data.drop('DAMAGE_MILLIONS_DOLLARS_x',1)
data = data.drop('DAMAGE_MILLIONS_DOLLARS_y',1)

# asdsadaadsad
data['DAY'] = data['DAY_x']
data['DAY'].fillna(data['DAY_y'], inplace=True)
data = data.drop('DAY_x',1)
data = data.drop('DAY_y',1)

data['FATALITIES'] = data['FATALITIES_x']
data['FATALITIES'].fillna(data['FATALITIES_y'], inplace=True)
data = data.drop('FATALITIES_x',1)
data = data.drop('FATALITIES_y',1)

data['FATALITY_ESTIMATE'] = data['FATALITY_ESTIMATE_x']
data['FATALITY_ESTIMATE'].fillna(data['FATALITY_ESTIMATE_y'], inplace=True)
data = data.drop('FATALITY_ESTIMATE_x',1)
data = data.drop('FATALITY_ESTIMATE_y',1)

data['HOUSES_DAMAGED'] = data['HOUSES_DAMAGED_x']
data['HOUSES_DAMAGED'].fillna(data['HOUSES_DAMAGED_y'], inplace=True)
data = data.drop('HOUSES_DAMAGED_x',1)
data = data.drop('HOUSES_DAMAGED_y',1)

data['HOUSES_DESTROYED'] = data['HOUSES_DESTROYED_x']
data['HOUSES_DESTROYED'].fillna(data['HOUSES_DESTROYED_y'], inplace=True)
data = data.drop('HOUSES_DESTROYED_x',1)
data = data.drop('HOUSES_DESTROYED_y',1)

data['HOUSE_DAMAGE_ESTIMATE'] = data['HOUSE_DAMAGE_ESTIMATE_x']
data['HOUSE_DAMAGE_ESTIMATE'].fillna(data['HOUSE_DAMAGE_ESTIMATE_y'], inplace=True)
data = data.drop('HOUSE_DAMAGE_ESTIMATE_x',1)
data = data.drop('HOUSE_DAMAGE_ESTIMATE_y',1)

data['HOUSE_DESTRUCTION_ESTIMATE'] = data['HOUSE_DESTRUCTION_ESTIMATE_x']
data['HOUSE_DESTRUCTION_ESTIMATE'].fillna(data['HOUSE_DESTRUCTION_ESTIMATE_y'], inplace=True)
data = data.drop('HOUSE_DESTRUCTION_ESTIMATE_x',1)
data = data.drop('HOUSE_DESTRUCTION_ESTIMATE_y',1)

#injury
data['INJURIES'] = data['INJURIES_x']
data['INJURIES'].fillna(data['INJURIES_y'], inplace=True)
data = data.drop('INJURIES_x',1)
data = data.drop('INJURIES_y',1)

data['INJURY_ESTIMATE'] = data['INJURY_ESTIMATE_x']
data['INJURY_ESTIMATE'].fillna(data['INJURY_ESTIMATE_y'], inplace=True)
data = data.drop('INJURY_ESTIMATE_x',1)
data = data.drop('INJURY_ESTIMATE_y',1)

data['LATITUDE'] = data['LATITUDE_x']
data['LATITUDE'].fillna(data['LATITUDE_y'], inplace=True)
data = data.drop('LATITUDE_x',1)
data = data.drop('LATITUDE_y',1)


data['LOCATION'] = data['LOCATION_x']
data['LOCATION'].fillna(data['LOCATION_y'], inplace=True)
data = data.drop('LOCATION_x',1)
data = data.drop('LOCATION_y',1)


data['LONGITUDE'] = data['LONGITUDE_x']
data['LONGITUDE'].fillna(data['LONGITUDE_y'], inplace=True)
data = data.drop('LONGITUDE_x',1)
data = data.drop('LONGITUDE_y',1)

data['MAXIMUM_HEIGHT'] = data['MAXIMUM_HEIGHT_x']
data['MAXIMUM_HEIGHT'].fillna(data['MAXIMUM_HEIGHT_y'], inplace=True)
data = data.drop('MAXIMUM_HEIGHT_x',1)
data = data.drop('MAXIMUM_HEIGHT_y',1)

data['MONTH'] = data['MONTH_x']
data['MONTH'].fillna(data['MONTH_y'], inplace=True)
data = data.drop('MONTH_x',1)
data = data.drop('MONTH_y',1)

data['REGION_CODE'] = data['REGION_CODE_x']
data['REGION_CODE'].fillna(data['REGION_CODE_y'], inplace=True)
data = data.drop('REGION_CODE_x',1)
data = data.drop('REGION_CODE_y',1)

data['STATE/PROVINCE'] = data['STATE/PROVINCE_x']
data['STATE/PROVINCE'].fillna(data['STATE/PROVINCE_y'], inplace=True)
data = data.drop('STATE/PROVINCE_x',1)
data = data.drop('STATE/PROVINCE_y',1)

data['VALIDITY'] = data['VALIDITY_x']
data['VALIDITY'].fillna(data['VALIDITY_y'], inplace=True)
data = data.drop('VALIDITY_x',1)
data = data.drop('VALIDITY_y',1)

data['YEAR'] = data['YEAR_x']
data['YEAR'].fillna(data['YEAR_y'], inplace=True)
data = data.drop('YEAR_x',1)
data = data.drop('YEAR_y',1)

data[['ALL_DAMAGE_MILLIONS']] = data[['ALL_DAMAGE_MILLIONS']].replace(['nan',''], [0,0])
data['ALL_DAMAGE_MILLIONS'] = data['ALL_DAMAGE_MILLIONS'].astype(float)

data[['ALL_HOUSES_DAMAGED']] = data[['ALL_HOUSES_DAMAGED']].replace(['nan',''], [0,0])
data['ALL_HOUSES_DAMAGED'] = data['ALL_HOUSES_DAMAGED'].astype(float)

data[['INTENSITY_SOLOVIEV']] = data[['INTENSITY_SOLOVIEV']].replace(['nan',''], [0,0])
data['INTENSITY_SOLOVIEV'] = data['INTENSITY_SOLOVIEV'].astype(float)

data[['ALL_HOUSES_DESTROYED']] = data[['ALL_HOUSES_DESTROYED']].replace(['nan',''], [0,0])
data['ALL_HOUSES_DESTROYED'] = data['ALL_HOUSES_DESTROYED'].astype(float)

data[['ALL_INJURIES']] = data[['ALL_INJURIES']].replace(['nan',''], [0,0])
data['ALL_INJURIES'] = data['ALL_INJURIES'].astype(float)


data[['ALL_MISSING']] = data[['ALL_MISSING']].replace(['nan',''], [0,0])
data['ALL_MISSING'] = data['ALL_MISSING'].astype(float)

data[['DAMAGE_TOTAL']] = data[['DAMAGE_TOTAL']].replace(['nan',''], [0,0])
data['DAMAGE_TOTAL'] = data['DAMAGE_TOTAL'].astype(float)

data[['DISTANCE_FROM_SOURCE']] = data[['DISTANCE_FROM_SOURCE']].replace(['nan',''], [0,0])
data['DISTANCE_FROM_SOURCE'] = data['DISTANCE_FROM_SOURCE'].astype(float)

data[['LATITUDE']] = data[['LATITUDE']].replace(['nan',''], [0,0])
data['LATITUDE'] = data['LATITUDE'].astype(float)

data[['LONGITUDE']] = data[['LONGITUDE']].replace(['nan',''], [0,0])
data['LONGITUDE'] = data['LONGITUDE'].astype(float)


x = data[['ALL_DAMAGE_MILLIONS','ALL_FATALITIES','ALL_HOUSES_DAMAGED','ALL_HOUSES_DESTROYED','ALL_INJURIES','ALL_MISSING','DAMAGE_TOTAL','DISTANCE_FROM_SOURCE','LATITUDE','LONGITUDE']]
y = data['INTENSITY_SOLOVIEV']

temp_data = pd.concat([x,y],1)
imr = Imputer(missing_values = 'NaN',strategy = 'median')

imputed_data = pd.DataFrame(imr.fit_transform(temp_data))
imputed_data.columns = temp_data.columns
imputed_data.index = temp_data.index

x = imputed_data.drop('INTENSITY_SOLOVIEV',1)
y = imputed_data['INTENSITY_SOLOVIEV']
regr_rf = RandomForestRegressor(max_depth=30, random_state=2)
regr_rf.fit(x,y)


with open('../model', 'wb') as f:
    cPickle.dump(rf, f)