# administrative-division-code-of-China

本项目提供中华人民共和国行政区划数据（4级：省级、地级、县级、乡级），并提供多种格式的副本。

本项目的Github镜像地址为：[https://github.com/FHZDCJ/administrative-division-code-of-China](https://github.com/FHZDCJ/administrative-division-code-of-China)

本项目的Gitee镜像地址为：[https://gitee.com/FHZDCJ/administrative-division-code-of-china](https://gitee.com/FHZDCJ/administrative-division-code-of-china)

## 数据来源

本项目数据来源于民政部旗下的[中国•国家地名信息库](https://dmfw.mca.gov.cn/XzqhVersionPublish.html)，本项目当前已更新至2025年数据（截止日期为2025年12月31日）。

由于香港特别行政区、澳门特别行政区、台湾省的相关区划代码尚未公布，因此本项目不包含上述三个行政区划的数据。

## 在线查看

本项目现在已经提供在线查看与检索功能，现在可以[在线查看](https://fhzdcj.github.io/administrative-division-code-of-China/WebPages/OnlineQuery/)行政区划数据了。

如果你的网络环境无法打开以上链接，可以通过[镜像站点(阿里云)](https://cn-admin.fhzdcj.cn/WebPages/OnlineQuery/) [镜像站点(腾讯云)](https://cn-admin-tc.fhzdcj.cn/WebPages/OnlineQuery/)来查看。

## 数据下载

### 原始数据

|               文件名称               |         文件说明          |
|:--------------------------------:|:---------------------:|
|  [data.csv](./RawData/data.csv)  |     csv格式的完整原始数据      |
| [data.xlsx](./RawData/data.xlsx) |     xlsx格式的完整原始数据     |
|   [data.db](./RawData/data.db)   |  SQlite3数据库格式的完整原始数据  |
| [data.json](./RawData/data.json) | json格式的完整原始数据（包含层级联动） |

### 联动数据

| 文件                |           不包含行政区划编码           |                包含行政区划编码                 |
|:------------------|:-----------------------------:|:---------------------------------------:|
| 省级、地级（2级联动）       |   [pc.json](./Dist/pc.json)   |   [pc-code.json](./Dist/pc-code.json)   |
| 省级、地级、县级（3级联动）    |  [pca.json](./Dist/pca.json)  |  [pca-code.json](./Dist/pca-code.son)   |
| 省级、地级、县级、乡级（4级联动） | [pcas.json](./Dist/pcas.json) | [pcas-code.json](./Dist/pcas-code.json) |

## 原始数据预览

| id |  name  | code | father_code | level | type |
|:--:|:------:|:----:|:-----------:|:-----:|:----:|
| 1  |  北京市   |  11  |     00      |   1   | 直辖市  |
| 2  |  天津市   |  12  |     00      |   1   | 直辖市  |
| 3  |  河北省   |  13  |     00      |   1   |  省   |
| 4  |  山西省   |  14  |     00      |   1   |  省   |
| 5  | 内蒙古自治区 |  15  |     00      |   1   | 自治区  |

## 脚本

|                 文件                 |                                    用途                                     |
|:----------------------------------:|:-------------------------------------------------------------------------:|
| [convert.py](./Scripts/convert.py) | 通过设置脚本参数，可以根据自己的需要生成json文件，支持自定义最大层级(1-4)，支持自定义启用name/code/level/type等数据。 |

## 镜像资源
本项目除了Github Pages以外，还使用阿里云ESA提供的Pages服务。

由于阿里云和腾讯云的免费Pages服务有限制，因此请注意访问频率以免超限。

| 名称           | 地址                                                                                                                                 |
|--------------|------------------------------------------------------------------------------------------------------------------------------------|
| Github Pages | [https://fhzdcj.github.io/administrative-division-code-of-China/](https://fhzdcj.github.io/administrative-division-code-of-China/) |
| 阿里云 Pages    | [https://cn-admin.fhzdcj.cn/](https://cn-admin.fhzdcj.cn/)                                                                         |
| 腾讯云 Pages    | [https://cn-admin-tc.fhzdcj.cn/](https://cn-admin-tc.fhzdcj.cn/)                                                                   |


## 特别说明

由于数据发布方式的变更，现在部分区划可能没有地级区划（例如北京市的下级区划直接为各市辖区），与过往的《统计用行政区划代码》添加2级区划“市辖区”的做法不太一致，如下所示：

| id  |  name   |  code  | father_code | level | type |
|:---:|:-------:|:------:|:-----------:|:-----:|:----:|
|  1  |   北京市   |   11   |     00      |   1   | 直辖市  |
| 365 |   东城区   | 110101 |     11      |   3   | 市辖区  |
| 366 |   西城区   | 110102 |     11      |   3   | 市辖区  |
| 367 |   朝阳区   | 110105 |     11      |   3   | 市辖区  |
| 368 |   丰台区   | 110106 |     11      |   3   | 市辖区  |
| ... | ....... | ...... |     ...     |  ...  | ...  |


## 开源协议 (License)
本项目采用 [Silent Public License (SPL) v1.0](./LICENSE) 授权，核心原则如下：

- ✅ **集成友好**：允许在商业或非商业项目中集成使用（如：作为地址联动选择器的数据源），**无需署名**，且**不会传染**您的主体项目（无需开源您的业务代码）。
- 🔄 **强传染性**：如果您对本项目的网页 UI 或原始数据集进行修改、换壳并发布**直接衍生作品**，该衍生作品必须强制沿用 SPL 协议。
- ❌ **严禁售卖**：禁止将本项目及其衍生品作为独立商品销售，或基于本项目核心功能进行任何形式的收费。
- ⚖️ **合规要求**：严禁用于任何违反中华人民共和国法律法规的用途。

详细条款请参阅 [LICENSE](./LICENSE) 文件。


## 数据来源及免责声明

本项目的数据来源于民政部的[中国•国家地名信息库](https://dmfw.mca.gov.cn/XzqhVersionPublish.html)，由人工整理形成，除了删除了没有详细数据的台湾省、香港特别行政区、澳门特别行政区的区划信息以外，未作其他修改。若要使用本项目，请自行确保数据准确性，项目作者不对但不对因数据错误或遗漏造成的任何损失负责。

