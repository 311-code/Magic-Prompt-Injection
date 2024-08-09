# ✨🔮 ComfyUI Magic Prompt Injection 🔮✨

![Prompt Injection](https://github.com/DataCTE/prompt_injection/assets/23625562/25d61586-935d-4afa-9709-6874f3e62783)

<p align="center">
  <a href="https://ko-fi.com/311_code"><img src="https://img.shields.io/badge/Support%20Me-Ko--Fi-red?style=for-the-badge&logo=ko-fi&logoColor=white" alt="Support me on Ko-Fi"></a>

## ✨ Introduction

This project integrates advanced prompt injection techniques with the ComfyUI framework to enhance your SDXL and SD 1.5 based AI image generation capabilities. 

The image above has a blurry background because layer that has background was disabled and not prompted! Another example coming soon with a more detailed prompt.

## 🔮 Features

- 🪄 **Advanced Prompt Injection**: Leverage state-of-the-art techniques for prompt injection of SDXL-based/SD1.5 models, ensuring better control and significantly reducing unwanted outputs.
- 🪄 **SDXL/SD1.5 Block Prompting**: Directly prompt an SDXL model's unet blocks and set individual block strengths for precise control over image content. Use two conditioning zero out nodes for full utilization (workflow coming soon)
- 🪄 **Enhanced Scheduler Integration**: Recommended to use Nvidia Align your steps scheduler with a samplercustomadvanced in ComfyUI for optimal results.
- 🪄 **Magic Model Injector**: A forthcoming node to inject SD3 weights and bias layers, improving common issues like the "woman in grass" problem. this is sort of "swiss army knife" nodes and does many other things, such as batch images latent injection at one time to a tensor or latent and squeezing it all in.

## 🛠️ How to Use

1. **Download and Install**:
    - **Option 1**: Download the ZIP file from the repository and extract it:
      ```sh
      Place in /ComfyUI/custom_nodes
      ```
    - **or Option 2**: Clone the repository directly into the `ComfyUI\custom_nodes` directory (Windows):
      ```sh
      Install git https://git-scm.com/downloads
      cd to ComfyUI/custom_nodes go to top of explorer and type "cmd"
      git clone https://github.com/brentjohnston/prompt_injection_advanced.git
      Start comfyui and load the example workflow
      Zerooutconditioning to positive and negative prompt to ksampler. Use this node instead to prompt, but you can do it either way.
      ```
    - **or option 3 Linux users**: You know what to do!

## ⚙️ Recommended Configuration

- **Scheduler**: Use Nvidia Align your steps scheduler.
- **Sampler**: Attach to a samplercustomadvanced in ComfyUI.
- **Guider**: Connect the guider and other requirements of samplercustomadvanced.
- **Conditioning**: Use conditioningzeroout on both positive and negative prompts.
- **Connect Node**: Connect the Magic Prompt Injection node and start prompting directly to unet blocks in the model. decrease and increase weights per layer.

## 🔮 Preview of Magic Model Injector SD3, SDXL, and soon Flux

PS. I am working on another more advanced node (that will do all of this and lot more). It injects SD3 weights and bias layers to help mitigate common issues like the woman in grass nightmare limbs SD3 or model ablation. This upcoming project is called **Magic Model Injector**.

Disclaimer: This came out a bit lewd somehow, apologies ahead of time. SD3 example:

Magic Model Injector Coming Soon with SD3 support.. ![preview_magic_model_injector](https://github.com/DataCTE/prompt_injection/assets/23625562/83d84b79-1372-4891-9c53-238f769e637b)

> *Don't ask me why the woman shows up in a bikini.. it happened when I inject certain SD3 joint block layers with real women in grass! Maybe it breaks some sort of ablation here, I dunno. Quality is bad for now and I will attempt to fix it before release.*

## 💖 Support Me

Creating and maintaining this project takes a lot of effort and dedication. If you find it useful, please consider supporting me:

<p align="center">
  <a href="https://ko-fi.com/311_code" target="_blank"><img src="https://img.shields.io/badge/Support%20Me-Ko--Fi-red?style=for-the-badge&logo=ko-fi&logoColor=white" alt="Support me on Ko-Fi"></a>
</p>

Your support helps me keep these projects alive and continually improve it.

## 🤝 Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## 📜 License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.
