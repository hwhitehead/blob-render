import numpy
import shutil
import argparse
from astropy.io import fits
from blobrender.paths import SIM_DAT, RESULTS
import os

def get_image(fitsfile):
        input_hdu = fits.open(fitsfile)[0]
        if len(input_hdu.data.shape) == 2:
                image = numpy.array(input_hdu.data[:,:])
        elif len(input_hdu.data.shape) == 3:
                image = numpy.array(input_hdu.data[0,:,:])
        else:
                image = numpy.array(input_hdu.data[0,0,:,:])
        return image


def flush_fits(newimage,fitsfile):
        f = fits.open(fitsfile,mode='update')
        input_hdu = f[0]
        if len(input_hdu.data.shape) == 2:
                input_hdu.data[:,:] = newimage
        elif len(input_hdu.data.shape) == 3:
                input_hdu.data[0,:,:] = newimage
        else:
                input_hdu.data[0,0,:,:] = newimage
        f.flush()

def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('--model_fits', required=True)
        parser.add_argument('--wsclean_fits', required=True)
        parser.add_argument('--op_fits', required=True)
        args = parser.parse_args()

        model_fits = os.path.join(SIM_DAT, os.path.basename(args.model_fits)) #'ffile_ri0.001_rb0.02_k0.1_lz25_6hhres_newprs2_0_1.7GHz.fits'
        wsclean_fits = args.wsclean_fits #'brender_emerlin_inpmodel_0-image.fits'
        op_fits = args.op_fits #'brender_emerlin_inpmodel_0-model.fits'

        shutil.copyfile(wsclean_fits,op_fits)
        img = get_image(model_fits)
        flush_fits(img,op_fits)
        outhdu = fits.open(op_fits,mode='update')
        outhdr = outhdu[0].header
        outhdr.set('BUNIT','JY/PIXEL')
        hh = outhdr.get('HISTORY')
        for i in range(0,len(hh)):
                outhdr.remove('HISTORY')
                outhdu.flush()

if __name__ == "__main__":
        main()

