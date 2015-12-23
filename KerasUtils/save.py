import json
import time


CONFIG ={
"keras_weights_extension":"hdf5",
"comment_file_extansion":"txt",
"keras_arch_extension":"json",
"hyper_parameter_extension":"txt",
}


def getuuid(project_name):
    return project_name+time.strftime("_%Y%m%d%H%M%S")

def saveEE(project_name, keras_model, hyper_paramaters, comments):
    '''
        project_name  NAme of your projects
        keras_model   Keras model object
        hyper_paramaters Python dictionary containing all hyper parameters
        comments      A list of string putting all comments about the current model
    '''
    uuid = getuuid(project_name)
    saveArch           (uuid, keras_model)
    saveWeights        (uuid, keras_model)
    saveHyperParameter (uuid, hyper_paramaters)
    saveComments       (uuid, comments)

def saveArch (uuid, keras_model):
    json_string = keras_model.to_json()
    open(uuid+"_arch."+CONFIG["keras_arch_extension"],"w").write(json_string)

def saveWeights (uuid, keras_model):
    keras_model.save_weights(uuid+"_weight."+CONFIG["keras_weights_extension"])

def saveHyperParameter (uuid, hyperparameters):
    dict_string = json.dumps(hyperparameters, indent=2, sort_keys=True)
    open(uuid+"_hypar."+CONFIG["hyper_parameter_extension"],"w").write(dict_string)

def saveComments (uuid, comments):
    open(uuid+"_comments."+CONFIG["comment_file_extansion"],"w").write("\n\t".join(comments))

