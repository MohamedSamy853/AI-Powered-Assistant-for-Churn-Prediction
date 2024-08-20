from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from langchain_core.language_models.llms import LLM
from langchain.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain.llms.ollama import Ollama
from typing import Literal 
import os

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

model_checkpoint = 'meta-llama/Meta-Llama-3-8B-Instruct'
llm = HuggingFaceEndpoint(endpoint_url=model_checkpoint, add_to_git_credential=True , 
                          repetition_penalty=1.09 , temperature=0.1 ,stop_sequences=['[INST]' , '[\INST]'] )



def add_tags(text):
   return "[INST] "+text+'[\INST]'+"\nAnswer:\n"


class LLama3LLM(LLM):
    def _call(
        self,
        prompt: str,
        stop =  None,
        run_manager= None,
        **kwargs,
    ) -> str:
        
        full_prompt = add_tags(prompt)
        response = llm(full_prompt)
        return response
    
    @property
    def _llm_type(self) -> str:
        """Get the type of language model used by this chat model. Used for logging purposes only."""
        return "custom"
def get_model(type:Literal['online',  'ollama', 'offline']='online'):
    '''get model according to type 
    online : acceess model through API 
    ollama : access model locally using ollama '''
    
    if type == 'online':
       
        return LLama3LLM(name='llama3-8b-instruct')
    elif type == 'ollama':
        
        return Ollama(name='llama3:latest')
    else :
       
        raise ValueError("Expected online or ollama but got {}".format(type))
    
    
    
