folderPath = '/Users/jingtan/Dropbox (Tripledot)/My Mac (Jings-MacBook-Pro.local)/Documents/GitHub/Maya-Rigs/scripts'
sys.path.append(folderPath)

import importlib
import quadrupedAutorigger
# importlib.reload(quadrupedAutorigger)
quadrupedAutorigger.showWindow()

# TODO: Expose neck joints, spinen joints, tail joints, name convention prefix to UI

''' script folders
/Applications/Autodesk/maya2022/plug-ins/MASH/scripts
/Applications/Rokoko Motion Library/maya/2022/scripts
/Applications/Autodesk/maya2022/plug-ins/fbx/scripts
/Applications/Autodesk/maya2022/plug-ins/camd/scripts
/Applications/Autodesk/Arnold/mtoa/2022/scripts
/Applications/Substance in Maya/2022/scripts
/Applications/Autodesk/maya2022/plug-ins/sweep/scripts
/Applications/Autodesk/maya2022/plug-ins/xgen/scripts
/Applications/Autodesk/maya2022/Maya.app/Contents/Frameworks/Python.framework/Versions/Current/lib/python37.zip
/Applications/Autodesk/maya2022/Maya.app/Contents/Frameworks/Python.framework/Versions/Current/lib/python3.7
/Applications/Autodesk/maya2022/Maya.app/Contents/Frameworks/Python.framework/Versions/Current/lib/python3.7/lib-dynload
/Applications/Autodesk/maya2022/Maya.app/Contents/Frameworks/Python.framework/Versions/Current/lib/python3.7/site-packages
/Applications/Autodesk/maya2022/Maya.app/Contents/Frameworks/Python.framework/Versions/Current/lib/python37.zip/lib-tk
/Users/jingtan/Library/Preferences/Autodesk/maya/2022/prefs/scripts
/Users/jingtan/Library/Preferences/Autodesk/maya/2022/scripts
/Users/jingtan/Library/Preferences/Autodesk/maya/scripts
/Applications/Autodesk/Arnold/mtoa/2022/scripts/mtoa/ui
/Applications/Autodesk/Arnold/mtoa/2022/scripts/mtoa/ui
/Applications/Autodesk/Arnold/mtoa/2022/scripts/mtoa/ui
/Applications/Autodesk/Arnold/mtoa/2022/scripts/mtoa/ui
/Applications/Autodesk/Arnold/mtoa/2022/extensions

add your own path:
    sys.path.append('drive:/path/to/my/scripts/folder')
    
check maya script path:
import sys
for path in sys.path:
    print(path)

'''