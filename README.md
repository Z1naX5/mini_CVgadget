# README

写了一些自用脚本，基本都是图像处理相关。  
但他们都不是特别灵活。

他们大多起源于[这](https://zenaxu.cn/2024/08/20/Plaidctf2024-%E5%A4%8D%E7%8E%B0/)

### bmp2ipg

```angular2html
把目标文件夹中所有的.bmp变换为.jpg
之后会升级成各种格式互转
```

### click_me

```angular2html
导入一张图片，鼠标点击后显示点击的坐标，按esc键退出
默认以yaml格式的键值对保存在 output.yaml 中，key是从“A”开始的ascii码，也可以自定key_list,list不足的长度从“A”开始补全。value的值为(x,y)
```

### split_video

```angular2html
支持两个功能
一个是裁切视频 split_ROI
还有一个是视频切片 split_video
裁切视频的一些参数需要修改函数内部
```

### trace

```angular2html
可以跟踪一个目标
默认实现方法是open-cv库的CSRT
然后带了一个预处理函数，可以根据实际情况写点东西微调图像
trace()会返回中心点坐标
```

### search_output

```angular2html
select()筛选静止帧
search()寻找坐标表下对应的内容并输出
寻找静止的帧，并且输出这个坐标（value）对应的key
如果判断为静止帧但是找不到符合范围的key，则输出“Sorry,QAQ”
# 本身这个文件就是为了配合 click_me 和 trace 而写的，所以功能也是和他们非常的配合（
```