# 随机视唱音阶生成器

这个项目用于生成随机的视唱音名，以帮助记忆。你可以通过点击项目中的按钮来触发对应的音频文件。

要生成可执行文件（将保存在 `dist` 文件夹中），运行以下 Python 命令：

```bash
pyinstaller --onefile --noconsole --icon="NERV.ico" --add-data "Solfège;Solfège" Random_Solfège_Generator.py
```

如果出现错误，提示 `distutils` 模块未安装，可能是因为 Python 3.12 已弃用并移除了 `distutils`，并将其迁移至 `setuptools`。在 Python 3.12 中，你可能需要手动安装 `setuptools` 或更新相关依赖项。

### 修复 Python SDK 错误

如果你遇到以下错误信息：

>   `无法为 Python 3.12 (Random Solfège Generator) 设置 Python SDK (C:/Users/.../Random Solfège Generator/.venv/Scripts/python.exe)。该 SDK 似乎无效。`

你可以按照以下步骤进行解决：

1. **安装 `setuptools`**

你可以尝试使用 `pip` 安装或更新 `setuptools` 以替代 `distutils` 的功能。

在终端中运行以下命令：

要安装 `setuptools`：

```bash
pip install setuptools
```

或者，升级现有的 `setuptools` 安装：

```bash
pip install --upgrade setuptools
```

2. **使用 `ensurepip` 修复 `pip`**

如果你在安装 `setuptools` 时仍遇到问题，可以尝试使用 Python 内置的 `ensurepip` 工具来修复 `pip`。

在终端中运行以下命令：

```bash
python -m ensurepip --upgrade
```

此命令将安装或升级 `pip` 和 `setuptools`。
