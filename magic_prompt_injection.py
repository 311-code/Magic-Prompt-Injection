# Please support 311_code on https://ko-fi.com/311_code

import comfy.model_patcher
import comfy.samplers
import torch
import torch.nn.functional as F

class CLIPTextEncode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"text": ("STRING", {"multiline": True, "dynamicPrompts": True}), "clip": ("CLIP",)}}
    RETURN_TYPES = ("CONDITIONING",) 
    FUNCTION = "encode"
    CATEGORY = "conditioning"

    def encode(self, clip, text):
        tokens = clip.tokenize(text)
        cond, pooled = clip.encode_from_tokens(tokens, return_pooled=True)
        return ([cond, {"pooled_output": pooled}],)

class MagicInjection:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "clip": ("CLIP",)
            },
            "optional": {
                "prompt_for_conditioning": ("STRING", {"multiline": True, "dynamicPrompts": True}),
                "input_4_text": ("STRING", {"multiline": True, "dynamicPrompts": True}),
                "input_4_weight": ("FLOAT", {"default": 1.0, "min": -2.0, "max": 5.0, "step": 0.05}),
                "input_5_text": ("STRING", {"multiline": True, "dynamicPrompts": True}),
                "input_5_weight": ("FLOAT", {"default": 1.0, "min": -2.0, "max": 5.0, "step": 0.05}),
                "input_7_text": ("STRING", {"multiline": True, "dynamicPrompts": True}),
                "input_7_weight": ("FLOAT", {"default": 1.0, "min": -2.0, "max": 5.0, "step": 0.05}),
                "input_8_text": ("STRING", {"multiline": True, "dynamicPrompts": True}),
                "input_8_weight": ("FLOAT", {"default": 1.0, "min": -2.0, "max": 5.0, "step": 0.05}),
                "middle_0_text": ("STRING", {"multiline": True, "dynamicPrompts": True}),
                "middle_0_weight": ("FLOAT", {"default": 1.0, "min": -2.0, "max": 5.0, "step": 0.05}),
                "output_0_text": ("STRING", {"multiline": True, "dynamicPrompts": True}),
                "output_0_weight": ("FLOAT", {"default": 1.0, "min": -2.0, "max": 5.0, "step": 0.05}),
                "output_1_text": ("STRING", {"multiline": True, "dynamicPrompts": True}),
                "output_1_weight": ("FLOAT", {"default": 1.0, "min": -2.0, "max": 5.0, "step": 0.05}),
                "output_2_text": ("STRING", {"multiline": True, "dynamicPrompts": True}),
                "output_2_weight": ("FLOAT", {"default": 1.0, "min": -2.0, "max": 5.0, "step": 0.05}),
                "output_3_text": ("STRING", {"multiline": True, "dynamicPrompts": True}),
                "output_3_weight": ("FLOAT", {"default": 1.0, "min": -2.0, "max": 5.0, "step": 0.05}),
                "output_4_text": ("STRING", {"multiline": True, "dynamicPrompts": True}),
                "output_4_weight": ("FLOAT", {"default": 1.0, "min": -2.0, "max": 5.0, "step": 0.05}),
                "output_5_text": ("STRING", {"multiline": True, "dynamicPrompts": True}),
                "output_5_weight": ("FLOAT", {"default": 1.0, "min": -2.0, "max": 5.0, "step": 0.05}),
                "start_at": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.001}),
                "end_at": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.001}),
            }
        }

    RETURN_TYPES = ("MODEL", "CONDITIONING")
    RETURN_NAMES = ("MODEL", "NOT_USED_YET")
    FUNCTION = "patch"
    CATEGORY = "advanced/model"

    def patch(self, model: comfy.model_patcher.ModelPatcher, clip, prompt_for_conditioning=None, input_4_text=None, input_4_weight=1.0, input_5_text=None, input_5_weight=1.0, input_7_text=None, input_7_weight=1.0, input_8_text=None, input_8_weight=1.0, middle_0_text=None, middle_0_weight=1.0, output_0_text=None, output_0_weight=1.0, output_1_text=None, output_1_weight=1.0, output_2_text=None, output_2_weight=1.0, output_3_text=None, output_3_weight=1.0, output_4_text=None, output_4_weight=1.0, output_5_text=None, output_5_weight=1.0, weight=1.0, start_at=0.0, end_at=1.0):
        if not any((input_4_text, input_5_text, input_7_text, input_8_text, middle_0_text, output_0_text, output_1_text, output_2_text, output_3_text, output_4_text, output_5_text)):
            return (model,)

        m = model.clone()
        sigma_start = m.get_model_object("model_sampling").percent_to_sigma(start_at)
        sigma_end = m.get_model_object("model_sampling").percent_to_sigma(end_at)

        patchedBlocks = {}

        def add_patch(block, index, text, weight):
            if text is not None:
                conditioning = CLIPTextEncode().encode(clip, text)[0][0]  # Ensure the text is encoded using the external class
                patchedBlocks[f"{block}:{index}"] = (conditioning, weight)

        add_patch('input', 4, input_4_text, input_4_weight)
        add_patch('input', 5, input_5_text, input_5_weight)
        add_patch('input', 7, input_7_text, input_7_weight)
        add_patch('input', 8, input_8_text, input_8_weight)
        add_patch('middle', 0, middle_0_text, middle_0_weight)
        add_patch('output', 0, output_0_text, output_0_weight)
        add_patch('output', 1, output_1_text, output_1_weight)
        add_patch('output', 2, output_2_text, output_2_weight)
        add_patch('output', 3, output_3_text, output_3_weight)
        add_patch('output', 4, output_4_text, output_4_weight)
        add_patch('output', 5, output_5_text, output_5_weight)

        m.set_model_attn2_patch(build_patch(patchedBlocks, sigma_start=sigma_start, sigma_end=sigma_end))

        if prompt_for_conditioning:
            conditioning = CLIPTextEncode().encode(clip, prompt_for_conditioning)[0][0]
        else:
            conditioning = None

        return (m, conditioning)

def build_patch(patchedBlocks, sigma_start=0.0, sigma_end=1.0):
    def prompt_injection_patch(n, context_attn1: torch.Tensor, value_attn1, extra_options):
        (block, block_index) = extra_options.get('block', (None, None))
        sigma = extra_options["sigmas"].detach().cpu()[0].item() if 'sigmas' in extra_options else 999999999.9

        batch_prompt = n.shape[0] // len(extra_options["cond_or_uncond"])

        if sigma <= sigma_start and sigma >= sigma_end:
            if (block and f'{block}:{block_index}' in patchedBlocks and patchedBlocks[f'{block}:{block_index}']):
                if context_attn1.dim() == 3:
                    c = context_attn1[0].unsqueeze(0)
                else:
                    c = context_attn1[0][0].unsqueeze(0)
                b = patchedBlocks[f'{block}:{block_index}'][0].repeat(c.shape[0], 1, 1).to(context_attn1.device)
                out = torch.stack((c, b)).to(dtype=context_attn1.dtype) * patchedBlocks[f'{block}:{block_index}'][1]
                out = out.repeat(1, batch_prompt, 1, 1)

                return n, out, out 

        return n, context_attn1, value_attn1
    return prompt_injection_patch

class ConditioningOnlyNode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"prompt_for_conditioning": ("STRING", {"multiline": True, "dynamicPrompts": True}), "clip": ("CLIP",)}}
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "generate_conditioning"
    CATEGORY = "conditioning"

    def generate_conditioning(self, clip, prompt_for_conditioning):
        encoder = CLIPTextEncode()
        conditioning = encoder.encode(clip, prompt_for_conditioning)[0][0]
        return (conditioning,)

NODE_CLASS_MAPPINGS = {
    "MagicInjection": MagicInjection,
    "ConditioningOnlyNode": ConditioningOnlyNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MagicInjection": "Magic Prompt Injection 311_code",
    "ConditioningOnlyNode": "Conditioning Only"
}
           
