//修改请求头信息  设置cookie
function Change_Request()
{
    var RequestHeaders = $request.headers;
    RequestHeaders["Cookie"] ="xxx_api_auth=3034343431356433393365326166303038373736356633313830373264653765";
    console.log(RequestHeaders);
    $done({RequestHeaders});//修改完成之后需要调用$done
}
Change_Request();