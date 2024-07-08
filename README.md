# ComfyUI Prompt Injection

![Prompt Injection](https://github.com/DataCTE/prompt_injection/assets/23625562/25d61586-935d-4afa-9709-6874f3e62783)

<p align="center">
  <a href="https://ko-fi.com/311_code"><img src="https://img.shields.io/badge/Support%20Me-Ko--Fi-red?style=for-the-badge&logo=ko-fi&logoColor=white" alt="Support me on Ko-Fi"></a>
  <a href="https://github.com/your-username/ComfyUI-Prompt-Injection/releases"><img src="https://img.shields.io/github/v/release/your-username/ComfyUI-Prompt-Injection?style=for-the-badge&color=blue" alt="GitHub AI Video Injection Releases (Coming Soon)"></a>
  <a href="[https://github.com/your-username/ComfyUI-Prompt-Injection/issues](https://github.com/brentjohnston/prompt_injection_advanced)"><img src="https://img.shields.io/github/issues/your-username/ComfyUI-Prompt-Injection?style=for-the-badge" alt="GitHub Issues"></a>
</p>

## Introduction

Welcome to the **ComfyUI Prompt Injection** repository! This project integrates advanced prompt injection techniques with the ComfyUI framework to enhance your AI image generation capabilities.

![ComfyUI Prompt Injection SVD 1.1 Demo coming soon]([https://github.com/DataCTE/prompt_injection/assets/23625562/25d61586-935d-4afa-9709-6874f3e62783](https://github.com/brentjohnston/prompt_injection_advanced))

## Features

- **Advanced Prompt Injection**: Leverage state-of-the-art techniques for prompt injection of SDXL-based models, ensuring better control and significantly reducing unwanted outputs.
- **SDXL Block Prompting**: Directly prompt SDXL blocks and individual block strengths for more precise control over image content.
- **Enhanced Scheduler Integration**: Use Nvidia Align your steps scheduler with a samplercustomadvanced in ComfyUI for optimal results.
- **Magic Model Injector**: A forthcoming node to inject SD3 weights and bias layers, improvements on common issues like the "woman in grass" problem. A sort of "swiss army knife" node.

## How to Use

1. **Download and Install**:
    - **Option 1**: Download the ZIP file from the repository and extract it:
      ```sh
      Place in /ComfyUI/custom_nodes
      ```
    - **Option 2**: Clone the repository directly into the `ComfyUI\custom_nodes` directory (Windows):
      ```sh
      Install git https://git-scm.com/downloads
      cd to ComfyUI/custom_nodes go to top of explorer and type "cmd"
      git clone https://github.com/brentjohnston/prompt_injection_advanced.git
      Start comfyui and load the example workflow
      Zerooutconditioning to positive and negative prompt to ksampler. Use this node instead to prompt, but you can do it either way.
      ```

## Recommended Configuration

- **Scheduler**: Use Nvidia Align your steps scheduler.
- **Sampler**: Attach to a samplercustomadvanced in ComfyUI.
- **Guider**: Connect the guider and other requirements of samplercustomadvanced.
- **Conditioning**: Use conditioningzeroout on both positive and negative prompts.
- **Connect Node**: Connect the Magic Prompt Injection node and start promping directly to unet blocks in the model.

## Preview of Magic Model Injector

PS. I am working on another more advanced node (that will do all of this and more). It injects SD3 weights and bias layers to fix common issues (like the woman in grass). This upcoming node is called **Magic Model Injector**.

Magic Model Injector Coming Soon.. ![preview_magic_model_injector](https://github.com/DataCTE/prompt_injection/assets/23625562/83d84b79-1372-4891-9c53-238f769e637b)

> *Don't ask me why the woman shows up in a bikini when you corrupt certain SD3 joint block layers! Maybe it breaks some sort of ablation. Quality is bad for now and I will attempt to fix it.*

## Support Me

Creating and maintaining this project takes a lot of effort and dedication. If you find it useful, please consider supporting me:

<p align="center">
  <a href="https://ko-fi.com/311_code" target="_blank"><img src="https://img.shields.io/badge/Support%20Me-Ko--Fi-red?style=for-the-badge&logo=ko-fi&logoColor=white" alt="Support me on Ko-Fi"></a>
</p>

Your support helps me keep these projects alive and continually improve it.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.
