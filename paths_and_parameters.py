#path_shared = '/home/shared/'
path_shared = '../../shared/'

### Input ###
path_scan = path_shared + 'dataXRDXRF/Perugia/PieroDellaFrancesca/Cimasa/'

path_xrd = path_scan + 'AngeloXRD/'          # XRD scan
path_zmap = path_shared + '-'

path_xrf_elements = path_scan + 'AngeloXRF/'       # XRF elements
path_xrf_spectra = None #path_scan + 'AngeloXRF_DAT/'   # XRF scan (put None if there isn't any XRF scan to be read)

path_photo = path_scan + 'AngeloFoto/'       # photo of the scanned section

list_path_database = [path_shared + 'Database/']   # tabulated phases

### Output ###
subfolder_output = 'output/Angelo/'
path_figures = subfolder_output + 'figures/'            # figures generated by the script
path_results = subfolder_output + 'results/'            # results generated by the script: raw data, tif maps
path_database_exp = subfolder_output + 'databaseEXP/'   # experimental phases
path_calibrations = subfolder_output + 'calibrations/'  # calibrated XRD spectra

### Parameters of synthetic phases ###
min_theta = 20
max_theta = 53
min_intensity = 0.1    # among the tabulated peaks, selects only the ones above this threshold of intensity (scale between 0 and 1)
first_n_peaks = None   # selects the first n most intense peaks (if None, leaves all the peaks)
sigma = 0.2            # sigma used in the peaks of synthetic diffraction patterns

### Experimental setting ###
angle_incidence = 10.5 # angle between the incident beam and the plane of the painting
channel_distance = 50 # distance in microns between two adjacent channels of the detector

### Data processing at reading time ###
xrf_axes_flip = [0] # which axes to flip when reading XRF data (0: vertical, 1: horizontal)

# Rotating data clockwise: number of steps of 90 degrees
steps_rotation_photo = 0
steps_rotation_xrf_elements = 0
steps_rotation_xrf_spectra = 0
steps_rotation_xrd = 0
