model_name = "deepseek-r1:1.5b "
custom_model_name = "crewai_gemma"


# Git the base model 
ollama pull $model_name

# create the model file 
ollama create $custom _model_name -f ./gemmaModelfile