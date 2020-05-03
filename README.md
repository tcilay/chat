#### 套接字常用方法
    s.bind()            # 绑定地址
    s.listen()          # 启动TCP监听器
    s.accept()          # 等待客户端连接
    s.connect()         # 主动发起服务器连接
    s.connect_ex()      # connect 的扩展,此时会以错误码的形式返回问题，而不是抛出异常
    s.recv()            # 接收消息
    s.recv_into()       # 接收消息到指定缓冲区
    s.send()            # 发送TCP消息
    s.sendall()         # 完整地发送TCP消息
    s.recvfrom()        # 接收UDP消息
    s.recvfrom_into()   # 接收UDP消息到指定的缓冲区
    s.sendto()          # 发送UDP消息
    s.getpeername()     # 连接到套接字（TCP）的远程地址
    s.getsockname()     # 当前套接字的地址
    s.getsockopt()      # 返回给定套接字选项的值
    s.setsockopt()      # 设置给定套接字选项的值
    s.shutdown()        # 关闭连接
    s.close()           # 关闭套接字
    s.detach()          # 在未关闭文件描述符的情况下关闭套接字，返回文件描述符
    s.ioctl()           # 控制套接字的模式（仅支持window）
    s.setblocking()     # 设置套接字的阻塞或非阻塞模式
    s.settimeout()      # 设置阻塞套接字操作的超时时间
    s.gettimeout()      # 获取阻塞套接字操作的超时时间
    s.fileno()          # 套接字的文件描述符
    s.makefile()        # 创建与套接字关联的文件对象
    s.family            # 套接字家族（属性）
    s.type              # 套接字类型（属性）
    s.proto             # 套接字协议（属性）
    
    
#### TCP 
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    

#### TCP 服务器伪代码
>"""  
>>ss = socket()                   # 创建伪代码  
>>ss.bind()                       # 套接字与地址绑定  
>>ss.listen()                     # 监听连接  
>>inf_loop:                       # 服务器无线循环  
>>>cs = ss.accept()            #接受客户端连接  
>>>comm_loop:                  #通信循环  
>>>> cs.recv()/cs.send()      # 对话（接受/发送） 

>>>cs.close()                  # 关闭客户都套接字  

>>ss.close()                      # 关闭服务器套接字 #（可选）  
>>  
>"""

#### TCP 客户端伪代码
>"""  
>>cs = socket()               # 创建客户端套接字  
>>cs.connect()                # 尝试连接服务器  
>>comm_loop:                  # 通信循环  
>>>cs.send()/cs.recv()     # 对话（发送/接收）
  
>>cs.close()                  # 关闭客户端套接字  
>>    
>"""


#### UDP
    udp_socket = socket.socket(AF_INET, SOCK_DGRAM)
    
####UDP 服务器伪代码

>"""
>>ss = socket()                           # 创建服务器套接字  
>>ss.bind()                               # 绑定服务器套接字  
>>inf_loop:                               # 服务器无限循环  
>>>cs = ss.recvfrom()/ss.sendto()      # 关闭（接收/发送）  
>>
>>ss.close()                              # 关闭服务器套接字
>>  
>"""

####UDP 客户端伪代码

>"""    
>>cs = socket()                       # 创建客户端套接字  
>>comm_loop:                          # 通信循环  
>>>cs.sendto()/cs.recvfrom()       # 对话（发送/接收） 
>> 
>>cs.close()                          # 关闭客户端  
>>  
>"""