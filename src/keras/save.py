import json
import time


CONFIG ={
"keras_weights_extension":"hdf5",
"comment_file_extansion":"txt",
"keras_arch_extension":"json",
"hyper_parameter_extension":"txt",
}


def getuuid(project_name):
    return (project_name,time.strftime("__%Y_%b_%d_%H_%M_%S__"))


def saveEE(project_name, keras_model):
    '''
        project_name  NAme of your projects
        keras_model   Keras model object
        hyper_paramaters Python dictionary containing all hyper parameters
        comments      A list of string putting all comments about the current model
    '''
    temp = getuuid(project_name)
    uuid = temp[0]+temp[1]
    saveArch           (uuid, keras_model)
    saveWeights        (uuid, keras_model)
    return temp[1]

def saveArch (uuid, keras_model):
    json_object = json.loads(keras_model.to_json())
    json_string = json.dumps(json_object,indent = 2, sort_keys=True)
    #print json_string
    open(uuid+"_arch."+CONFIG["keras_arch_extension"],"w").write(json_string)

def saveWeights (uuid, keras_model):
    keras_model.save_weights(uuid+"_weight."+CONFIG["keras_weights_extension"])

def saveHyperParameter (uuid, hyperparameters):
    dict_string = json.dumps(hyperparameters, indent=2, sort_keys=True)
    open(uuid+"_hypar."+CONFIG["hyper_parameter_extension"],"w").write(dict_string)

def saveComments (uuid, comments):
    open(uuid+"_comments."+CONFIG["comment_file_extansion"],"w").write("\n\t".join(comments))

