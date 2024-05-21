# ECAD软件元器件库

[English](README_en.md)

For Altium Designer, KiCad...

## 简介

该仓库旨在为ECAD（电子计算机辅助设计）软件提供全面的电子元器件库，涵盖流行的平台，包括Altium Designer、KiCad等。

## 特性

- **广泛的元器件覆盖：** 我们的库包含各种电子元器件，从电阻和电容到集成电路和连接器，确保您在PCB（印刷电路板）设计中有多样化的选择。

- **与供应商无关：** 元器件以与供应商无关的方式组织，可根据项目需求从各种制造商中选择元器件。

- **封装兼容性：** 每个元件都附有封装信息，确保能够无缝集成到您的PCB布局中。封装设计与主流ECAD软件平台兼容。

- **定期更新：** 库会定期更新，以包括最新的元器件和改进。我们欢迎社区的贡献和反馈，以提升整体质量和覆盖范围。

## 入门指南

### Altium Designer

安装前可以先阅读 [这篇文章](https://mp.weixin.qq.com/s?__biz=MzA3NzMyNTIyOA==&mid=2651482479&idx=1&sn=d79a11fe80da1f39fe1e46ea2c6870a0&chksm=84ad7facb3daf6ba008c8f7219550a07e711cfb7742180b865ad2c836176ce6982926200e28f#rd) 了解一些背景知识。

#### 1. 安装PostgreSQL数据库驱动

ADLib元器件库使用PostgreSQL数据库存储元器件信息，所以需要安装PostgreSQL数据库驱动，可以到 [PostgreSQL官网](https://odbc.postgresql.org/) 下载对应的驱动，建议安装64位版。访问官网有困难的同学可以到百度网盘下载：

链接: https://pan.baidu.com/s/1DnWgRIRjggwleEUL5EnFAw?pwd=ty4h 提取码: ty4h

安装13.2版本就可以。

安装好ODBC驱动后，到Windows的数据源管理器中添加ODBC数据源：

![ODBC数据源](https://imgs.boringhex.top/blog/20240327173633.png)

我安装的是64位驱动，所以这里打开的是64位的ODBC管理器：

![添加数据源](https://imgs.boringhex.top/blog/20240327173849.png)

打开后选择添加，然后选择刚才安装的数据库对应的驱动：

![选择数据库驱动](https://imgs.boringhex.top/blog/20240327174100.png)

填写数据源名称和描述（可以不修改，保持默认），配置连接参数，然后点击测试连接，如果连接成功，点击确定完成添加。

![配置数据源名称和连接参数](https://imgs.boringhex.top/blog/20240327174552.png)

至此，数据源就添加好了。

#### 2. 下载元器件库

AD数据库类型的元器件库，元器件信息存储在数据库中，元器件符号和封装依然使用对应库文件。

到[GitHub](https://github.com/boringhex-top/OpenECADLib)下载元器件库文件：

![下载元器件库](https://imgs.boringhex.top/blog/20240521113407.png)

这里下载zip压缩包或使用git clone都可以，建议使用git clone，这样可以方便后续更新。

对git不熟悉的可以参考 [Pro Git](https://git-scm.com/book/zh/v2)。

不方便访问GitHub的小伙伴可以`clone`以下地址：

```powershell
git clone https://github.boringhex.top/github.com/boringhex-top/OpenECADLib.git
```

当然也可以用上面截图中的加速器。

#### 3. 配置ADLib元器件库

下载好元器件库后，建议将元器件库存放在一个固定的位置，方便后续更新。

将元器件库中的`example.std-lib.DbLib`修改文件名为`std-lib.DbLib`，然后用Altium Designer打开：

![构建数据库连接](https://imgs.boringhex.top/blog/20240521120755.png)

如果前面的ODBC数据源名称跟我前面的示例一致，这里只修改`User ID`和`Password`即可。

如果ODBC数据源名称不一致，可以点击`Build`修改数据源配置，根据向导选择对应的ODBC数据源。

然后点击`Connect`测试连接，连接成功后点击`Ctrl + S`保存DbLib文件。

#### 4. 使用ADLib元器件库

新建工程，然后安装基于文件的库：

![安装库](https://imgs.boringhex.top/blog/20240521121821.png)

![安装ADLib](https://imgs.boringhex.top/blog/20240521122003.png)

可以全局安装这个库，这样在所有工程中都可以使用。

![元器件面板](https://imgs.boringhex.top/blog/20240521132018.png)

#### 5. 更新元器件库

在元器件库目录下，使用`git pull`命令更新库文件：

```powershell
git pull
```

可以参考 [这篇文章](https://mp.weixin.qq.com/s?__biz=MzA3NzMyNTIyOA==&mid=2651482574&idx=1&sn=c10e90584e712b18b73796287c3f7dd2&chksm=84ad7f0db3daf61b284c754657658cc72e5c4beb3d66265b91f7e756938e2b4d4812bd040d38#rd)。

### KiCad

1. 克隆仓库到本地机器。
2. 在KiCad中，转到“Preferences”并选择“Manage Symbol Libraries”。
3. 将克隆仓库的路径添加为符号库。
4. 现在库中的元件可以在KiCad项目中使用。

## 贡献指南

我们欢迎对库的覆盖范围和质量进行贡献。如果您有新的元器件、封装或对现有条目的改进，请随时提交拉取请求。请遵循我们的[贡献指南](CONTRIBUTING.md)以便进行顺畅的协作。

## 许可证

该库采用[MIT许可证](LICENSE)发布，确保保持对社区的开放和可访问性。

## 致谢

我们要感谢那些为使这个库成为ECAD社区宝贵资源的贡献者们。

---

**注意：** 如果您遇到任何问题或有建议，请在[问题页面](https://github.com/boringhex-top/OpenECADLib/issues)上提出，或加入我们的[社区论坛讨论](https://github.com/boringhex-top/OpenECADLib/discussions)。

## 支持我们

我们非常感谢你考虑支持我们的项目！你的支持将帮助我们继续改进和扩展这个项目。

### 如何捐助

如果你想要捐款支持我们的项目，你可以点击下面的捐助按钮：

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/T6T5X0A38)

这将会带你到我们的Ko-fi页面，你可以在那里进行捐款。

或者直接使用支付宝/微信进行捐助：

[<img src="https://imgs.boringhex.top/blog/圆角-alipay.webp" alt="Alipay" width="200"/>](https://imgs.boringhex.top/blog/alipay.webp)

[<img src="https://imgs.boringhex.top/blog/圆角-wechatpay.webp" alt="Wechatpay" width="200"/>](https://imgs.boringhex.top/blog/wechatpay.webp)


### 其他支持方式

除了捐款，还有许多其他方式可以支持我们的项目：

- 贡献代码： 我们欢迎所有的代码贡献，无论是新功能，bug修复，还是文档改进。
- 宣传项目： 你可以通过在社交媒体上分享我们的项目，或者向你的朋友和同事推荐我们的项目来帮助我们。

再次感谢你的支持！
