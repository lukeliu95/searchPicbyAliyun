import io
import configparser

from alibabacloud_imagesearch20201214.client import Client
from alibabacloud_imagesearch20201214.models import SearchImageByPicAdvanceRequest
from alibabacloud_tea_openapi.models import Config
from alibabacloud_tea_util.models import RuntimeOptions


def searchImageByPic(image_bytes):
    # 读取key.gitignore文件中的access_key_id和access_key_secret
    config_parser = configparser.ConfigParser()
    config_parser.read('key.gitignore')
    access_key_id = config_parser.get('DEFAULT', 'access_key_id')
    access_key_secret = config_parser.get('DEFAULT', 'access_key_secret')

    request = SearchImageByPicAdvanceRequest()
    # 必填，图像搜索实例名称。注意是实例名称不是实例ID。购买后通过上云层管控台实例信息一栏查看：https://imagesearch.console.aliyun.com/overview
    request.instance_name = 'img001'
    # 图片内容，最多支持 4MB大小图片以及5s的传输等待时间。当前仅支持PNG、JPG、JPEG、BMP、GIF、WEBP、TIFF、PPM格式图片；
    # 对于商品、商标、通用图片搜索，图片长和宽的像素必须都大于等于100且小于等于4096；
    # 对于布料搜索，图片长和宽的像素必须都大于等于448且小于等于4096；
    # 图像中不能带有旋转信息

    # 使用URL方式释放下方注释即可。   
    # url = '<fileUrl>'    
    # f = BytesIO(requests.get(url).content)  

    # 使用传入的图片字节流
    request.pic_content_object = image_bytes
    # 选填，商品类目。
    # 1. 对于商品搜索：若设置类目，则以设置的为准；若不设置类目，将由系统进行类目预测，预测的类目结果可在Response中获取 。
    # 2. 对于布料、商标、通用搜索：不论是否设置类目，系统会将类目设置为88888888。
    request.category_id = 3
    # 选填，返回结果的数目。取值范围：1-100。默认值：10。
    request.num = 12
    # 选填，返回结果的起始位置。取值范围：0-499。默认值：0。
    request.start = 0
    # 选填，是否需要进行主体识别，默认为true。
    # 1.为true时，由系统进行主体识别，以识别的主体进行搜索，主体识别结果可在Response中获取。
    # 2.为false时，则不进行主体识别，以整张图进行搜索。
    # 3.对于布料图片搜索，此参数会被忽略，系统会以整张图进行搜索。
    request.crop = False
    # 选填，图片的主体区域，格式为 x1,x2,y1,y2, 其中 x1,y1 是左上角的点，x2，y2是右下角的点。设置的region 区域不要超过图片的边界。
    # 若用户设置了Region，则不论Crop参数为何值，都将以用户输入Region进行搜索。
    # 3.对于布料图片搜索，此参数会被忽略，系统会以整张图进行搜索。
    request.region="167,467,221,407"
    # 选填，过滤条件
    # int_attr支持的操作符有>、>=、<、<=、=，str_attr支持的操作符有=和!=，多个条件之支持AND和OR进行连接。
    # 示例：
    #  1. 根据IntAttr过滤结果，int_attr>=100
    #  2. 根据StrAttr过滤结果，str_attr!="value1"
    #  3. 根据IntAttr和StrAttr联合过滤结果，int_attr=1000 AND str_attr="value1"
    request.filter = ""

    config = Config()
    # 创建AK/SK参考：https://help.aliyun.com/document_detail/116401.htm
    # 阿里云账号AccessKey拥有所有API的访问权限，建议您使用RAM用户进行API访问或日常运维。
    # 强烈建议不要把AccessKey ID和AccessKey Secret保存到工程代码里，否则可能导致AccessKey泄露，威胁您账号下所有资源的安全。
    # 本示例以将AccessKey ID和AccessKey Secret保存在环境变量为例说明。您也可以根据业务需要，保存到配置文件里。
    config.access_key_id = access_key_id
    config.access_key_secret = access_key_secret
    # 请更换成您购买实例的区域，例如购买的是杭州区域，则endpoint='imagesearch.cn-hangzhou.aliyuncs.com'
    config.endpoint = 'imagesearch.cn-hangzhou.aliyuncs.com'

    # 以下为内网（VPC）访问方式
    # 说明：内网（VPC）访问：仅限同区域ECS或资源的访问，例如您购买的图像搜索实例是华东2（上海），那么您的ECS或资源也必须在华东2（上海）才能通过内网VPC地址访问图搜服务，否则会调用不通，如果遇到调用不通，请先检查您的ECS或资源与图像搜索是否在同一个区域。
    # config.endpointType = 'internal'  // 如果是内网访问图像搜索服务，则endpointType为必填项，值统一为'internal'
    # config.endpoint = 'imagesearch-vpc.<regionId>.aliyuncs.com' // 为内网访问（VPC）地址，请您更换为您购买实例的区域，例如您购买实例的区域为杭州，则endpoint='imagesearch-vpc.cn-hangzhou.aliyuncs.com'

    # 请您更换成您购买实例的区域，例如您购买的实例区域为杭州，则更换为regionId='cn-hangzhou'
    config.region_id = 'cn-hangzhou'
    config.type = 'access_key'
    client = Client(config)
    runtime_option = RuntimeOptions()
    response = client.search_image_by_pic_advance(request, runtime_option)
    print(response.to_map())
    return response.to_map()
    #return response.body.auctions

#if __name__ == '__main__':
    # 这里可以保留用于测试，但实际使用时会从 app.py 调用
#    with open('images/img00001.jpg', 'rb') as f:
#        test_image_bytes = io.BytesIO(f.read())
#    searchImageByPic(test_image_bytes)