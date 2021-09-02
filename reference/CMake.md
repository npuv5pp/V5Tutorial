# CMake

CMake 参考资料下载站：[CMake - 足球机器人基地参考资料下载站 > CMake (npu5v5.cn)](https://files.npu5v5.cn/CMake/)

## CMake 简介

CMake 是一个代码构建系统，可以用来编译大型工程，是目前主流的代码构建系统。需要注意的是，ROS现在使用的构建系统 catkin 也是基于 CMake 的。

> **CMake**是个一个[开源](https://zh.wikipedia.org/wiki/开源)的[跨平台](https://zh.wikipedia.org/wiki/跨平台)[自动化建构](https://zh.wikipedia.org/wiki/Build_automation)系统，用来管理软件建置的程序，并不依赖于某特定编译器，并可支持多层目录、多个应用程序与多个库。 它用配置文件控制建构过程（build process）的方式和[Unix](https://zh.wikipedia.org/wiki/Unix)的[make](https://zh.wikipedia.org/wiki/Make)相似，只是CMake的配置文件取名为CMakeLists.txt。CMake并不直接建构出最终的软件，而是产生标准的建构档（如Unix的Makefile或Windows [Visual C++](https://zh.wikipedia.org/wiki/Visual_C%2B%2B)的projects/workspaces），然后再依一般的建构方式使用。这使得熟悉某个[集成开发环境](https://zh.wikipedia.org/wiki/整合開發環境)（IDE）的开发者可以用标准的方式建构他的软件，这种可以使用各平台的原生建构系统的能力是CMake和[SCons](https://zh.wikipedia.org/wiki/SCons)等其他类似系统的区别之处。 CMake配置文件（CMakeLists.txt）可设置源代码或目标程序库的路径、产生[适配器](https://zh.wikipedia.org/wiki/適配器)（wrapper）、还可以用任意的顺序建构可执行文件。CMake支持in-place建构（二进档和源代码在同一个目录树中）和out-of-place建构（二进档在别的目录里），因此可以很容易从同一个源代码目录树中建构出多个二进档。CMake也支持静态与动态程序库的建构。
>
> “CMake”这个名字是"Cross platform Make"的缩写。虽然名字中含有"make"，但是CMake和Unix上常见的“make”系统是分开的，而且更为高端。 它可与原生建置环境结合使用，例如：make、ninja、[苹果](https://zh.wikipedia.org/wiki/蘋果公司)的Xcode与[微软](https://zh.wikipedia.org/wiki/微软)的Visual Studio。

## CMake 参考资料

### CMake Practice

+ 作者：Cjacker

+ 链接：[CMake Practice.pdf (npu5v5.cn)](https://files.npu5v5.cn/CMake/CMake%20Practice.pdf)
+ 推荐理由：结合一系列实例来讲解 CMake，是入门的好教材

### Modern CMake

+ 作者：Henry Schreiner

+ 链接：[An Introduction to Modern CMake · Modern CMake (cliutils.gitlab.io)](https://cliutils.gitlab.io/modern-cmake/)

+ 推荐理由：讲解了现代 CMake 的一些特性，并给出了很多 Best practice

### Modern CMake 中文版

+ 作者：**[Modern-CMake-CN](https://github.com/Modern-CMake-CN)**

+ 链接：[Introduction · Modern CMake (modern-cmake-cn.github.io)](https://modern-cmake-cn.github.io/Modern-CMake-zh_CN/)
+ 源链接：[Modern-CMake-CN/Modern-CMake-zh_CN](https://github.com/Modern-CMake-CN/Modern-CMake-zh_CN)

+ 推荐理由：上述 《Modern CMake》中文版，由**基地同学创建的组织翻译**，欢迎加入我们！