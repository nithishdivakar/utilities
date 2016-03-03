from keras.callbacks import Callback
import os

class ModelSnapshotRBM(Callback):
    def __init__(self, log_folder="LOG", epoch_interval=1, model_name="bla",verbose=True):
        self.log_folder = log_folder
        self.model_name = model_name
        self.epoch_interval = epoch_interval
        self.verbose = verbose
        if not os.path.exists(self.log_folder):
            os.makedirs(log_folder)
            if self.verbose:
                print "Creating log folder"

    def on_epoch_begin(self,epoch, logs={}):
        if epoch % self.epoch_interval == 0:
            f_name='{}_snapshot_at_{}_epoch.hdf5'.format(self.model_name,epoch)
            if self.verbose:
                print "Saving model snapshot to {}".format(f_name)
            self.model.layers[0].save_weights(os.path.join(self.log_folder,f_name),overwrite=True)

