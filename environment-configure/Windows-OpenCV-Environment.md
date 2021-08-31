## Visual Studio 2019 中 OpenCV 配置教程

### 前言

我这里配置用的是4.5.0版本，但实际配置过程中需要的大部分时间只是路径，因此和版本基本无关。
	
**只有一个地方是和版本有关系的，在配置链接器的 `opencv_wordxyzd.lib` 时，大家一定要注意！！**

<!--more-->


### 1.下载OpenCV

首先我们进入 https://opencv.org/releases/ 在这其中下载OpenCV ，我这里下载的4.5.0 ，选择Windows下载即可。
	
下载结束后我们双击安装包，指定解压目录，我这里解压在了我的G盘，具体路径为 `G:\Opencv450` 

### 2.设置OpenCV的环境变量

我们在 此电脑右键 -> 属性 -> 高级系统设置 -> 环境变量 -> 系统变量 -> 双击Path ->添加如下的环境 
	
`G:\Opencv450\build\x64\vc15\bin` ，这里的路径是根据上面那个路径来看的，如果你上面那个跟我不同，也请看请自己的路径。

![此电脑属性中的高级系统设置][1]

![高级系统设置中的环境变量][2]

![双击系统环境变量中的Path][3]

![新建并加入我们的bin路径][4]

### 3.配置Visual Studio

1. 新建一个C++类型的空项目，随便你如何命名，将模式调节为 **Debug x64**

   ![新建空项目并将模式调节为Debug x64][5]

2. 依次点击 **视图** -> **其他窗口** -> **属性管理器** 

   在打开的 **属性管理器** 中添加新项目属性表，我是4.5.0的版本，为了好记，新建属性表命名为**OpenCV450Debug**

   ![新建一个属性表][6] 

3. 建好以后在其上右键，选择**属性** ，然后依次选择 **VC++ 目录** -> **包含目录** -> **编辑** 

   添加下面两个路径，当然，这两个路径也是取决于你安装OpenCV的路径的。

   `G:\Opencv450\build\include`

   `G:\Opencv450\build\include\opencv2`

   ![更改VC++中的包含目录][7]

   ![更改包含目录中的内容][8]

4. 接下来选择 **VC++ 目录** 中的 **库目录** -> **编辑** ，然后添加（与你OpenCV路径对应）

   `G:\Opencv450\build\x64\vc15\lib`

   ![编辑VC++目录中库目录][9]

5. 接下来选择 **链接器** -> **输入** -> **附加依赖项** -> **编辑**

   在其中加入 `opencv_world450d.lib` ！ 大家这里请注意，不同的版本这里的添加名称不同，通常来说如果你的版本是 `x.y.z`  那么就是 `opencv_worldxyzd.lib`

   ![附加依赖项][10]

6. 最后我们点击确定，然后退出**属性编辑器**。

### 4.测试OpenCV的配置

+ 在源文件中添加一个 **C++** 源程序，我添加的为 `main.cpp`  

  在其中输入如下测试代码

  ```cpp
  #include <iostream>
  #include <opencv2/core.hpp>
  #include <opencv2/imgcodecs.hpp>
  #include <opencv2/highgui.hpp>
  
  using namespace std;
  using namespace cv;
  
  int main(int argc, char** argv)
  {
      String imageName("HappyFish.jpg"); // by default
      if (argc > 1)
          imageName = argv[1];
  
      Mat image = imread(samples::findFile(imageName), IMREAD_COLOR); // Read the file
      if (image.empty()) {  // Check for invalid input
          cout << "Could not open or find the image" << endl;
          return -1;
      }
      namedWindow("Display window", WINDOW_AUTOSIZE); // Create a window for display.
      imshow("Display window", image);                // Show our image inside it.
      waitKey(0);   // Wait for a keystroke in the window
  
      return 0;
  }
  ```

  ![添加代码源文件][11]

+ 接下来我们随便找一张 **jpg** 图片文件，命名为 `HappyFish.jpg` ，保存在你的工程的根目录下/和 **cpp** 文件一个路径。这里我放一张 **jpg** 图片供大家使用~

  

  ![将图片放在项目目录下/和cpp一个路径][12]

  ![HappyFish.jpg][13]

+ 然后在我们的 **Visual Studio 2019** 中按下快捷键 **Ctrl + F5** 编译运行程序，会发现我们成功打开了这张图片，配置就成功了~

  ![配置成功标志][14]

### 5.参考链接

+ [VS2019 上配置 OpenCV4.2.0](https://www.jianshu.com/p/908551afa8fd)


[1]: https://www.zzsqwq.cn/usr/uploads/2020/10/1401048133.png
[2]: https://www.zzsqwq.cn/usr/uploads/2020/10/705625531.png
[3]: https://www.zzsqwq.cn/usr/uploads/2020/10/3556583146.png
[4]: https://www.zzsqwq.cn/usr/uploads/2020/10/3685752206.png
[5]: https://www.zzsqwq.cn/usr/uploads/2020/10/3001499231.png
[6]: https://www.zzsqwq.cn/usr/uploads/2020/10/1199777575.png
[7]: https://www.zzsqwq.cn/usr/uploads/2020/10/2408130113.png
[8]: https://www.zzsqwq.cn/usr/uploads/2020/10/958765988.png
[9]: https://www.zzsqwq.cn/usr/uploads/2020/10/2096976051.png
[10]: https://www.zzsqwq.cn/usr/uploads/2020/10/1791849957.png
[11]: https://www.zzsqwq.cn/usr/uploads/2020/10/1422866535.png
[12]: https://www.zzsqwq.cn/usr/uploads/2020/10/1938099554.png
[13]: https://www.zzsqwq.cn/usr/uploads/2020/10/1150699358.jpg
[14]: https://www.zzsqwq.cn/usr/uploads/2020/10/2092454279.png

