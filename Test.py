import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import os, copy
import time
import OMRobjects as OMR
import imp
imp.reload(OMR)

%matplotlib inline

sheet_path = './data/You_to_me_me_to_you'
sheets = [OMR.Sheet(os.path.join(sheet_path, page_path), order=i) for i, page_path in enumerate(sorted(os.listdir(sheet_path)))]


sample_idx = 0

sheets[sample_idx].preprocess_image(threshold=200)
sys_pos = sheets[sample_idx].create_system(sheets[sample_idx])
