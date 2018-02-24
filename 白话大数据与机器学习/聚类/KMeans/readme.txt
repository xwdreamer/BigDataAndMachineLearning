中国几大区域
#1、华东地区（包括山东、江苏、安徽、浙江、福建、上海）；
#2、华南地区（包括广东、广西壮族自治区、海南）；
#3、华中地区（包括湖北、湖南、河南、江西）；
#4、华北地区（包括北京直辖市、天津直辖市、河北、山西、内蒙古自治区）； 5、西北地区（包括宁夏回族自治区、新疆维吾尔族自治区、青海、陕西、甘肃）；
#6、西南地区（包括四川、云南、贵州、西藏自治区、重庆直辖市）；
#7、东北地区（包括辽宁、吉林、黑龙江）；
#8、台港澳地区（包括台湾、香港、澳门）。

案例根据聚类来划分终于几大区域。

数据集字段介绍

  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `pid` int(11) DEFAULT NULL COMMENT '父id',
  `shortname` varchar(100) DEFAULT NULL COMMENT '简称',
  `name` varchar(100) DEFAULT NULL COMMENT '名称',
  
  `level` tinyint(4) DEFAULT NULL COMMENT '层级 0 1 2 省市区县',
  `pinyin` varchar(100) DEFAULT NULL COMMENT '拼音',
  `code` varchar(100) DEFAULT NULL COMMENT '长途区号',
  `zip_code` varchar(100) DEFAULT NULL COMMENT '邮编',
  `first` varchar(50) DEFAULT NULL COMMENT '首字母',
  `lng` varchar(100) DEFAULT NULL COMMENT '经度',
  `lat` varchar(100) DEFAULT NULL COMMENT '纬度',