#path_shared = '/home/shared/'
path_shared = '../../shared/'

### Input ###
path_scan = path_shared + 'dataXRDXRF/MunchMuseum/M491/'

path_xrd = path_scan + 'ProfiloXRD/'          # XRD
path_zmap = path_shared + 'VenereBZPosition/'

path_xrf_images = path_scan + 'ProfiloXRF/labels/'   # XRF
path_xrf_spectra = path_scan + 'ProfiloXRF/'

path_photo = path_scan + 'ProfiloFoto/'       # photo of the scanned section

path_database = path_shared + 'Database/'     # tabulated phases

### Output ###
subfolder_output = 'output/MunchMuseum/M491/Profilo/'
path_figures = subfolder_output + 'figures/'          # figures generated by the script
path_results = subfolder_output + 'results/'          # results generated by the script: raw data, tif maps
path_database_exp = subfolder_output + 'databaseEXP/' # experimental phases

### Parameters ###
min_theta = 20
max_theta = 53
min_intensity = 0.1  # among the tabulated peaks, selects only the ones above this threshold of intensity (scale between 0 and 1)
first_n_peaks = 5    # selects the first n most intense peaks (if None, leaves all the peaks)
sigma = 0.2          # sigma used in the peaks of synthetic diffraction patterns

### Experimental setting ###
angle_incidence = 10.5 # angle between the incident beam and the plane of the painting
channel_distance = 50 # distance in microns between two adjacent channels of the detector

### Reading XRF ###
xrf_axes_flip = [1] # which axes to flip when reading XRF data (0: vertical, 1: horizontal)
