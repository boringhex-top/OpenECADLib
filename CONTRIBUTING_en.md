# Contribution Guide

This repository uses the GitHub [`fork + pull request`](https://aaronflower.github.io/essays/github-fork-pull-workflow.html) collaboration method. If you want to contribute to the repository, you can follow the steps below.

## Creating a New Component

### Schematic Symbol

Contributors should first check if the schematic symbol they need is already being worked on in the repository's `Issues` and `Pull requests`. If it is, they can collaborate with other contributors to complete it.

If a new schematic symbol is needed, a new `issue` should be submitted, indicating that you are working on it. Then `fork` the repository to your account, `clone` it to your local machine, create a new `new/ad/sym-xxxx` branch, and push it to your remote repository. Create a `pull request` draft so that other contributors can see that this symbol file has been created, to avoid conflicts when merging into the main branch.

Schematic symbol files start with `sym-`, followed by a 4-digit serial number, such as `sym-0001.SchLib`. Each schematic symbol file can only contain one schematic symbol of the same name, for example, the schematic symbol in `sym-0001.SchLib` is `sym-0001`.

After creating the new schematic symbol and checking it for errors, create a schematic symbol thumbnail, push it to the remote repository, and then submit a `pull request` for review.

### Drawing Guides

1. Use imperial units, grid points should preferably be multiples of 100mil.
2. Use the schematic symbol template file `templates/ad/symbol-template.SchLib` to create new schematic symbol files.
3. Preferably use a double-column pin layout.
4. When using a four-sided pin layout, the number of pins should not exceed 48.
5. Consider splitting into multiple parts when the number of pins exceeds 60.
6. Pin length should not be less than 100mil and not more than 400mil, and should be appropriate to the size of the symbol theme.
7. The pin spacing should not be less than 50mil, preferably 100mil, and the pins must align with the grid points.
8. The schematic symbol pin layout does not have to match the device pin layout, but the pin numbers must match the device pin numbers. Consider common circuit schematic drawing habits and prioritize pin function grouping.
9. Low-level effective pins should preferably be represented by `/`, such as `/RESET`; AD's "\" syntax can also be used; however, try to keep it consistent with the device datasheet.
10. The font should be `Consolas`, size `10`.

### Default Font Setting

In `Altium Designer`, you can set the default font through `Preferences`. The setting method is as follows:

![Default font setting](figures/image-1.png)

Set the font of `Comment`, `Designator`, `Pin` in the schematic symbol library file to `Consolas`, and the size to `10`. This can keep the font of all schematic symbols consistent.

`Consolas` is a monospaced font, installed by default on `Win10` and above, suitable for drawing schematic symbols. The display effect of `10` font size on A4 paper is also good.

### Schematic Symbol Thumbnail and Report

After drawing the schematic symbol and checking it for errors, use the `Report` function of `Altium Designer` to generate a schematic symbol thumbnail and report. The report contains information such as the pin definition, pin function, and electrical characteristics of the schematic symbol. Push the thumbnail and report to the remote repository, then submit a `pull request` and wait for review.

The method and settings are as follows:

![Report](figures/image-2.png)

![Settings](figures/image-3.png)

> Note:
> 
> The generated report is saved in the `report` folder. The thumbnail filename is random characters, you need to change the filename to the corresponding symbol number, such as "SYM-0001", and move it to the `preview` folder, then commit and push to the remote repository.
>
> When there is only one schematic symbol in a schematic symbol library file, the 'sym-xxxx_2.html' in the generated report file has no content, you can delete this file.
>
> For schematic symbols split into multiple parts, thumbnails need to be generated for each, all filled into a multi-dimensional table. You can also use the [online stitching tool](https://uutool.cn/photo-collage/) to stitch multiple thumbnails together and upload.

One symbol, one commit, one PR, this can make the main branch history clearer.

### PCB Footprint

Similarly, if you want to create a new footprint library, you should create a new `new/ad/fp-xxxx` branch after `cloning` the repository, and push it to the remote repository, so that other contributors can see that this footprint library file has been created, to avoid conflicts when merging into the main branch.

PCB footprint files start with `fp-`, followed by a 4-digit serial number, such as `fp-0001.PcbLib`. Each PCB footprint file can only contain one PCB footprint of the same name, for example, the PCB footprint in `fp-0001.PcbLib` is `fp-0001`. For footprint variants, suffixes can be added to the filename to indicate, 3d model variants use numeric suffixes, such as `fp-0001-1.PcbLib`; assembly density variants use `L`, `M` to indicate, regular density `N` can be omitted, such as `fp-0001-M.PcbLib`, indicating low density; package direction variants use `Q1`, `Q2`, `Q3`, `Q4` to indicate, such as `fp-0001-Q1.PcbLib`, indicating the package direction is `Q1`, packages that comply with the IPC-7351C standard direction can be omitted.

After creating the new PCB footprint and checking it for errors, create a PCB footprint thumbnail, push it to the remote repository, and then submit a `pull request` for review.

### 3D Model

3D model files start with `3d-`, followed by the same serial number as the corresponding PCB footprint. For example, `3d-0001.step`.

> Note: PCB footprint files and 3D model files are usually larger than 100kB, you need to use `git lfs` to track these files. Click to view the `git lfs` [installation method](https://docs.github.com/zh/repositories/working-with-files/managing-large-files/installing-git-large-file-storage).