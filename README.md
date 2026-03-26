# administrative-division-code-of-China

本项目提供中华人民共和国行政区划数据（4级：省级、地级、县级、乡级），并提供多种格式的副本。

## 数据来源

本项目数据来源于民政部旗下的[中国•国家地名信息库](https://dmfw.mca.gov.cn/XzqhVersionPublish.html)，本项目当前已更新至当2025数据（截止日期为2025年12月31日）。

## 数据下载

### 原始数据

|                           文件名称                           |                文件说明                |
| :----------------------------------------------------------: | :------------------------------------: |
| [data.csv](https://github.com/FHZDCJ/administrative-division-code-of-China/blob/main/RawData/data.csv) |         csv格式的完整原始数据          |
| [data.xlsx](https://github.com/FHZDCJ/administrative-division-code-of-China/blob/main/RawData/data.xlsx) |         xlsx格式的完整原始数据         |
| [data.db](https://github.com/FHZDCJ/administrative-division-code-of-China/blob/main/RawData/data.db) |    SQlite3数据库格式的完整原始数据     |
| [data.json](https://github.com/FHZDCJ/administrative-division-code-of-China/blob/main/RawData/data.json) | json格式的完整原始数据（包含层级联动） |

### 联动数据

| 文件                              |                                               不包含行政区划编码                                               |                                                    包含行政区划编码                                                     |
| :-------------------------------- |:-----------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:|
| 省级、地级（2级联动）             |   [pc.json](https://github.com/FHZDCJ/administrative-division-code-of-China/blob/main/Dist/pc.json)   |   [pc-code.json](https://github.com/FHZDCJ/administrative-division-code-of-China/blob/main/Dist/pc-code.json)   |
| 省级、地级、县级（3级联动）       |  [pca.json](https://github.com/FHZDCJ/administrative-division-code-of-China/blob/main/Dist/pca.json)  |  [pca-code.json](https://github.com/FHZDCJ/administrative-division-code-of-China/blob/main/Dist/pca-code.son)   |
| 省级、地级、县级、乡级（4级联动） | [pcas.json](https://github.com/FHZDCJ/administrative-division-code-of-China/blob/main/Dist/pcas.json) | [pcas-code.json](https://github.com/FHZDCJ/administrative-division-code-of-China/blob/main/Dist/pcas-code.json) |

## 原始数据预览

|  id  |     name     | code | father_code | level |  type  |
| :--: | :----------: | :--: | :---------: | :---: | :----: |
|  1   |    北京市    |  11  |     00      |   1   | 直辖市 |
|  2   |    天津市    |  12  |     00      |   1   | 直辖市 |
|  3   |    河北省    |  13  |     00      |   1   |   省   |
|  4   |    山西省    |  14  |     00      |   1   |   省   |
|  5   | 内蒙古自治区 |  15  |     00      |   1   | 自治区 |

## 脚本

|                             文件                             |                             用途                             |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| [convert.py](https://github.com/FHZDCJ/administrative-division-code-of-China/blob/main/Scripts/convert.py) | 通过设置脚本参数，可以根据自己的需要生成json文件，支持自定义最大层级(1-4)，支持自定义启用name/code/level/type等数据。 |



## 特别说明

由于数据发布方式的变更，现在部分区划可能没有地级区划（例如北京市的下级区划直接为各市辖区），与过往的《统计用行政区划代码》添加2级区划“市辖区”的做法不太一致，如下所示：

|  id  |  name   |  code  | father_code | level |  type  |
| :--: | :-----: | :----: | :---------: | :---: | :----: |
|  1   | 北京市  |   11   |     00      |   1   | 直辖市 |
| 365  | 东城区  | 110101 |     11      |   3   | 市辖区 |
| 366  | 西城区  | 110102 |     11      |   3   | 市辖区 |
| 367  | 朝阳区  | 110105 |     11      |   3   | 市辖区 |
| 368  | 丰台区  | 110106 |     11      |   3   | 市辖区 |
| ...  | ....... | ...... |     ...     |  ...  |  ...   |

## 免责声明

本项目的数据完全来源于民政部旗下的[中国•国家地名信息库](https://dmfw.mca.gov.cn/XzqhVersionPublish.html)，人工整理形成，除了删除了没有详细数据的台湾省、香港特别行政区、澳门特别行政区的区划信息以外，未作其他修改。若要使用本项目，请自行确保数据准确性。
