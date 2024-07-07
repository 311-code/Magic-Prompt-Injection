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
- **SDXL Block Prompting**: Directly prompt SDXL blocks and indivual block stengths for more precise control over video content.
- **Enhanced Scheduler Integration**: Use Nvidia Align your steps scheduler with a samplercustomadvanced in ComfyUI for optimal results.
- **Magic Model Injector**: A forthcoming feature to inject SD3 weights and bias layers, improvements for common issues like the "woman in grass" problem.

## How to Use

1. **Download and Install**:
    - **Option 1**: Download the ZIP file from the repository and extract it:
      ```sh
      Place in /ComfyUI/custom_nodes
      ```
    - **Option 2**: Clone the repository directly into the `ComfyUI\custom_nodes` directory:
      ```sh
      Install git https://git-scm.com/downloads
      cd to ComfyUI/custom_nodes
      git clone https://github.com/brentjohnston/prompt_injection_advanced.git
      Search for attn2 prompt injection node, search for zerooutconditioning node and add it.
      Zero out conditioning to positive and negative prompt to ksampler. Use this node instead to prompt.
      ```

2. **Setup**: Ensure you have ComfyUI installed and properly configured.

3. **Integrate**: Connect the `samplercustomadvanced` and `conditioningzeroout` nodes for both positive and negative conditioning.

4. **Run**: Execute your ComfyUI workflow with the integrated prompt injection nodes for enhanced video generation.

## Recommended Configuration

- **Scheduler**: Use Nvidia Align your steps scheduler.
- **Sampler**: Attach to a samplercustomadvanced in ComfyUI.
- **Guider**: Connect the guider for optimal performance.
- **Conditioning**: Use conditioningzeroout on both positive and negative prompts.

## Preview of Magic Model Injector

PS. I am working on a node that will do all of this and more, injecting SD3 weights and bias layers to fix common issues (like the woman in grass). This upcoming feature is called **Magic Model Injector**.

![Magic Model Injector](https://github.com/DataCTE/prompt_injection/assets/23625562/8cb1cc9b-5271-477d-9a3d-64a35c16d231)

> *Don't ask me why the woman shows up in a bikini when you corrupt certain SD3 joint block layers!*

## Support Me

Creating and maintaining this project takes a lot of effort and dedication. If you find it useful, please consider supporting me:

<p align="center">
  <a href="https://ko-fi.com/311_code" target="_blank"><img src="https://img.shields.io/badge/Support%20Me-Ko--Fi-red?style=for-the-badge&logo=ko-fi&logoColor=white" alt="Support me on Ko-Fi"></a>
</p>

Your support helps me keep this project alive and continually improve it.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
