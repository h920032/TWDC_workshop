import xarray as xr
import pandas as pd
import numpy as np

def cloud_free_landsat8(dataset_in):
    output = xr.Dataset({}, coords = dataset_in.drop_dims('time').coords)
    for band in list(dataset_in.data_vars.keys()):
        if band != 'pixel_qa':
            temp1 = dataset_in.get([band]).where(dataset_in.get([band]) > 0).where(dataset_in.pixel_qa == 322).median(dim='time')
            output = output.merge(temp1)
    return output

def dataset_to_dataframe(dataset_in):
    data = {}
    for band in list(dataset_in.data_vars.keys()):
        data[band] = dataset_in[band].values.reshape((1,dataset_in[band].values.size))[0]
    df = pd.DataFrame(data=data)
    return df
