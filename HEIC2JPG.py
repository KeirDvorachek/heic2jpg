import os, sys
from PIL import Image, ExifTags
from pillow_heif import register_heif_opener
from datetime import datetime
import glob
import piexif
import shutil

register_heif_opener()

#Grabs the dropped folder from the .bat file.
path = sys.argv[1]
#path = f"insert heic folder path here between the double qoutes if desired"
#Creating new folders to drop processed and unprocessed files in their perspective bin.
jpgDir = path + "/ProcessedImages"
heicDir = path + "/HEICImages"
if not os.path.exists(jpgDir):
    os.mkdir(jpgDir)
if not os.path.exists(heicDir):
    os.mkdir(heicDir)
#Setting variable for completion status.
filesToProcess = glob.glob(os.path.join(path, "*.HEIC"), recursive = False)
totalFiles = len(filesToProcess)
processedFiles = 1

#Loops through the dropped folder and grabs each HEIC file.
for file in filesToProcess:
    #Progress Status
    print(processedFiles, "/", totalFiles, "files processed -- ", int(processedFiles/totalFiles*100), "% Complete", end="\r", flush=True)
    try:
        #Save string variable of filename without ".HEIC"
        fileNameExt = os.path.basename(file)
        fileName = fileNameExt.removesuffix(".HEIC")
        with Image.open(path + "/" + fileNameExt) as image: #Opening .HEIC image file.
            imageExif = image.getexif()
            #Next block parses through the EXIF data and gets it ready for .jpg format, DateTime, and Orientation.
            if imageExif:
                exif = { ExifTags.TAGS[k]: v for k, v in imageExif.items() if k in ExifTags.TAGS and type(v) is not bytes }
                exifDict = piexif.load(image.info["exif"])
                exifDict["0th"][piexif.ImageIFD.Orientation] = 1
                exifBytes = piexif.dump(exifDict)
                 #Save's individual image to newly created folder.
                image.save(jpgDir + "/" + fileName + ".jpg", "jpeg", exif = exifBytes)
                #Move old file to new HEIC folder
                shutil.move(path + '/' + fileNameExt, heicDir + "/" + fileNameExt)
                processedFiles += 1
            else:
                print("Unable to get exif data for", file)
    except OSError as ose:
        print("cannot convert", file)
        print(ose)