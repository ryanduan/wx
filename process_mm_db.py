# -*- coding: utf-8 -*-

"""
Create at 16/10/19

wc/wc***-***.db  朋友圈
fts_message.db  -- fts_username_id
"""

__author__ = 'TT'

import sqlite3
import time

import hashlib
from connect import con_1, con_2, con_3

con_list = []

# for k, v in con_1.iteritems():
#     m = hashlib.md5
#     m.update(k)
#     print m.hexdigest()

name_tb_0 = dict(
    Chat_013de30e1924c23a1f4a3034e30448ac=u'boqi-Wendy',
    Chat_0166b4deea2708d80c9505d933ac1b46=u'boqi-yuwei',
    Chat_01f71164497aa092264a6fc7d8084a88=u'luoha-lanzhengwei',
    Chat_02547b2c09f95ca5ebddc73142eddba1=u'luoha-zhangxiangyu',
    Chat_028927c95a6eac938772caba35639471=None,
    Chat_02a1804c1d2055e8d3ccbc7fbd25fa22=u'common-002',
    Chat_039a16b6cbb7898cc13cd7d46e744e44=u'common-022',
    Chat_04e6e5139902b04d32074a56ec445fc6=u'common-006',
    Chat_05d1c43ce52132b1626e684f1f9bb33f=u'luoha-group-0006',
    Chat_061fc4a03a8948fbd28002971943fd05=None,
    Chat_0771eabf1e9de4bccade62b4b0a9ae5d=u'common-040',
    Chat_0891e765c5635fdcaa0cb2a50ca7a33d=u'boqi-helijia',
    Chat_0970ac03ca61901a064e90149e82025f=u'luoha-duanjingjing',
    Chat_09d618e51d09f084786259b88bf4166c=u'luoha-yangweiqing',
    Chat_0a01d1d095a01acc5822fee03369234a=u'luoha-zhangfeng',
    Chat_0ac7e1d3b35d9d9f139ac3285edd8eff=u'boqi-leige',
    Chat_0c74888f9566036e74ddadeebaf8c2b1=None,
    Chat_0d15bc8aee17a68c8727c4ea45128b23=u'common-shijuezhi',
    Chat_0d7c1f3966aa4158be59429a0e969e49=u'boqi-zhaohongcai',
    Chat_0e39b9bce1077f2ca37486a5392dfb45=u'common-news',
    Chat_0e460e483be648f9e8960e6914bd6287=u'friend-sister-1',
    Chat_0ea36c9eb34ffab7c5900199a3effe64=u'friend-cat-1',
    Chat_0f7cad9d05e0c648191b0cf937c6f983=u'boqi-chunbo',
)
name_tb_1 = dict(
    Chat_100d95607624d12b59d6fdfa8ff97ba5=None,
    Chat_1032d0d950c86087c7d44295f56c80d6=None,
    Chat_108b18334152e7fffbbcd6f45acef08f=None,
    Chat_110a38f6873885f332d71f0a44a5a748=None,
    Chat_1193ce8dd3a46347ea6b23f995df0817=u'xuhui-shiyou-002',
    Chat_1380509146287e15f1af93983b508526=u'old-group-lan',
    Chat_1417edc4bbecff2c112be931b0b3dc78=u'common-044',
    Chat_14dcfd8ea0e542322247504a858bccd4=u'group-xuhui-002',
    Chat_15436577b0c52bcb226ced6dea9b8ecb=None,
    Chat_16058400d6da94fa895678ae1cfa6ecb=None,
    Chat_180b2138d30d42fdeacf2813670cf4b4=u'common-jiaofei',
    Chat_188b4b837334790a2fdf58923caa992b=None,
    Chat_190b46308decb0c0750ee60972b388c9=u'ziru-0002',
    Chat_19164772e7a8b79ce39a42c12d4c1c94=u'boqi-tinging',
    Chat_1933ba2935b3f52f72c38cf194d1e335=u'luoha-who0003',
    Chat_195985474dd5112d6cc7d0724079eece=u'luoha-liyunyan',
    Chat_1a98efb9dcd3d8ed6cc38fe7db1e7312=u'luoha-wuye',
    Chat_1a9b299af8dd1014eed235fb18bd64e8=u'group-daxue',
    Chat_1abb5ed47d308fb7acda8843c05bb9fe=None,
    Chat_1adce527c302cab143dd22474ad32f98=u'group-q1',
    Chat_1c698d25c964234dfe76b09d43e9ca50=u'luoha-iphone-ershou',
    Chat_1ca5272d584a8bb3ca97127ad49fdb39=None,
    Chat_1e667f8fdc376ffcafdb7b371a8aa492=u'boqi-group-p1',
    Chat_1e6fc2e31c2e4fa84e664c36053d6eb6=u'common-new1',
    Chat_1e93e98d37cec90b0ed06c0a470f2357=None,
    Chat_1ed674f342e68508913bd4b5a9549ff6=u'boqi-helijia',
    Chat_1fba1142421cfdcef9b295b6a7b067b3=u'common-001',
)
name_tb_2 = dict(
    Chat_202eb4bc1924556b44865f53bc519602=None,
    Chat_20f4cf492ae53cf33f9edc3cc7abbe46=u'group-luoha-football',
    Chat_2195010994b0bed51ac5c1dcc7e49931=u'luoha-no-00002',
    Chat_2202432c4db9404e4de3c2e6de435f6e=u'm-sister',
    Chat_224e1436fed173397e09871dedae720e=u'group-zhangjiang-me',
    Chat_2409aaf77a93595aa8d71142f193dc68=u'common-move',
    Chat_2555463175904fa01fc7742f01a4a93a=u'm-mom',
    Chat_25dcc5315932e9e9cbd295d38e9a83c6=None,
    Chat_2613feb8e39b2217fec20236962a0980=u'boqi-tongcheng',
    Chat_268955d0b856af08789631bbeea53414=u'luoha-xiaokun',
    Chat_270dcaef46f1ab910b47afa287e4502a=u'common-luohashuo',
    Chat_272d597f7e52379d285290ad2a01758d=None,
    Chat_273235547c86188e899436d89605891d=u'ziru-lihongyan',
    Chat_274439b2f6e852c971c35647cbed2b66=None,
    Chat_286b390075ce87a2c822b73e507d4b1e=u'common-meitesibangwei',
    Chat_29ab36aca5e111a7c37327142d9539ed=u'common-020',
    Chat_29ded44af0edebbd06648171a4074c8b=None,
    Chat_2bc892ff14cc70b2e4acc8eafe729baa=u'common-pizza',
    Chat_2c041b783bca98d2f3df95ee0b080cff=u'luoha-lijie',
    Chat_2c478013d3177ef17ada0284bc50bd1c=None,
    Chat_2c55788a58c0b3a7cbb6765cfde6571b=None,
    Chat_2c561c187e075c3ddfa95edd6b17ee48=u'zhangjiang-zufang',
    Chat_2eca7d12757a69fd784552f3696ac821=u'common-003',
    Chat_2f6ea3a3659f6e900db55e05ac2b5193=u'star-hh-yajie',
    Chat_2f95d2d94200bb7d8e648f958364c79d=None,
    Chat_2facaef21f1ce7a46195416d56efe94a=u'common-004',
)
name_tb_3 = dict(
    Chat_313cfa2599cafa999afe9a988d3c7c5c=None,
    Chat_314086b1be3c2a35061d34386a3279df=u'ziru-machenhui',
    Chat_314a8ea76ba5a252eb23eb325334b9a5=u'tt-group-common-a1',
    Chat_31d0811a6eb73279fc6e74bee49c69df=u'group-xuhui-003',
    Chat_3239492cf14b4efb77717e2b42d3ca52=u'common-061',
    Chat_32883b8dd2d3e79aaa8b717c21fe5a29=u'group-me-10001',
    Chat_32ef8e581353621afac7ce88c716ce81=u'luoha-ershou-jiaju',
    Chat_3324198fa80021dacebcc912b20e89eb=u'old-lan-000',
    Chat_33638ea9b767a71f97a07fa15bd0a800=u'old-youquan',
    Chat_339d8b3f32b002e15ff00d7986913533=None,
    Chat_34ab6d854cc2b9e8f63f2c9d7311f337=u'common-yinhang',
    Chat_352e9793df051073f65c2dee4d147c77=u'zhaojianxi-me',
    Chat_3557ba670de8cdc30d599b9479bd6be1=u'fuck-who-10001',
    Chat_35ab7c4ab321a98fe0ff69422709e711=u'common-021',
    Chat_360fe964e9fe183f666ae52250b22f31=u'common-031',
    Chat_36510792ddf4c525706a0be4973ebfc0=u'true-luoha-yangbiao',
    Chat_36f87294f3f084ec6bf490d82e544eb0=u'luoha-wushuai',
    Chat_3722834700af1eb5c3a751ec7dcc0d36=u'old-no-00001',
    Chat_37af4e94beeff9056dfa4675771a987f=None,
    Chat_382b758d3b02c6b36536784796081ad1=u'zhangjun-me',
    Chat_3958e515d1223eadf4f82a1d1079af36=u'common-050',
    Chat_3a1959c57f1dfd2e728eacac0d8e6a29=u'boqi-wuye',
    Chat_3a548a52652f8129572c1cb218dbe8c4=u'boqi-leader',
    Chat_3bf51f8573564d2d0097d4a3759acf78=u'fuck-0001',
    Chat_3c307b83f4c94ac9f945f105ce9ba53d=u'luoha-guanzheng',
    Chat_3d50e8edeba24b5adcd592378d743221=None,
    Chat_3e17dd90ae7d32b5341cc8ed3384218a=None,
    Chat_3eb77f4aa5c090ee2bdfedadba9b2d49=u'star-550',
    Chat_3f9720c5236dc8557fa5c53ba05b629e=None,
    Chat_3fc4f466b60bb520f70534f0b2bb4602=None,
)
name_tb_4 = dict(
    Chat_40f8876cc1489864b1785c34145c1723=u'boqi-taoshifu',
    Chat_415724d2c57083fbfd452c892ff1b463=u'boqi-longmao',
    Chat_41aae20212a55d674c57fe2cace79921=u'qingke-001',
    Chat_41bcd528295ac4bbfc93a902ebe8f4b8=u'luoha-group-0009',
    Chat_420860a7fa70953346830913f215b967=u'boqi-group-10001',
    Chat_420ae7561db8179b80ebaef70ec23f0d=None,
    Chat_423e82bb36f845840d6baf256a15a336=u'luoha-group-0100',
    Chat_423ffee905bf0879c2a47210074578e8=None,
    Chat_43247b196c0ae61f105d5348cc8fe896=u'no-wuzhong',
    Chat_435dd272eb468855aa2bc6c3107705f6=u'group-me-jj',
    Chat_43b54ad71350226a3d2ad703de9c45ed=u'luoha-shenjie',
    Chat_44fad4a561e4bac05a052044ae465169=u'fuck-xiaoerbi',
    Chat_455fd77b1d2313f4649b853a40f9a908=u'common-jiudian',
    Chat_465e20e544257ef6045c0d7dc6969b29=u'boqi-jingjing',
    Chat_48240460e582edc438b2adbba8dae323=u'luoha-no-00001',
    Chat_489742183834d1c6689366b33911a430=None,
    Chat_48e27ba019ec8003d77c648de2a6e682=u'fuck-group-0001',
    Chat_493d4635c726359638a5d984ede8ea2b=None,
    Chat_493f97e137b2c9f995c7590f2db75d1d=u'luoha-group-0101',
    Chat_49ac69802af1b150f94aeb078cd0eda8=None,
    Chat_4a25854aa5dd7d7030f772cddca7f2c3=u'luoha-group-0001',
    Chat_4a301bc43d6790a6230fa0bda4595bde=u'daoyou-0001',
    Chat_4a48ce15df0924556302b9a292f0db4c=u'daxue-0001',
    Chat_4c4e82555ccb0a7df468e07c51a0e1d5=u'group-cat-001',
    Chat_4c8c44c239fc0518f84ee49b1275b654=u'luoha-daimao',
    Chat_4d02df0fe19c20aa7a1925e47bbe7f7a=None,
    Chat_4d525affd179bf7a000842eaa98578f8=u'luoha-group-0002-me',
    Chat_4de573809f388f3f9f6fddc221b34b2d=u'common-005',
    Chat_4dee0c844b8ad7eb111e24ff0d587826=u'luoha-group-0003-me',
    Chat_4eb7a49733c87034958fa12fc6dd7521=u'common-007',
    Chat_4ef9e79992dc65f57667dd7195c8b01d=u'boqi-Linda',
    Chat_4f198a117a6126d2648e620ad9766147=u'common-008',
    Chat_4f34cca7fe9338bffc72dc6367ed3377=u'fuck-tongxue-0002',
    Chat_4f354b8d1346a2d642862553980d391f=u'xuhui-wuqili-shiyou',
    Chat_4fd91dc24b718024011cb753ae7cc4e9=None,
)
name_tb_5 = dict(
    Chat_51151c772be4cb61466e5e95aada9353=u'group-20001',
    Chat_51a172d34b2501df07211409c80bcc33=u'luoha-group-0010',
    Chat_525849a4abbcc369971b9a01564fc5fb=u'cpu',
    Chat_535b972fa73972ce3a1158d90ee164ab=None,
    Chat_53888dae83f9fdc25f3f59d4e5219cbd=u'luoha-group-20001',
    Chat_553f9122a0a6d59a13b61ae2557bad7f=None,
    Chat_56a9303864703f4bfc0b164ac86dd03a=None,
    Chat_56d399edfcb009337bda02882ee9a534=None,
    Chat_56d3da9ca7873dc4394309f31745cfcf=None,
    Chat_56ff9a36f054e4c5595461e55804de5e=u'tt-common',
    Chat_57ad3ae7ec2bd9f0e083a1a33dd56de8=None,
    Chat_57c1e6a8810cbd93b7b664188b4fd3e5=None,
    Chat_57d20e84b868b68fc0a3619a11bc4da2=u'luoha-zhaoshengling',
    Chat_57dca66fd10f79cb03979423cbbcc3b8=u'group-me-550-00001',
    Chat_5a1e58538bb09c88167964a24077f949=u'xuhui-xiwang-shiyou-fuck',
    Chat_5a8d013a635fbe8ec4d574ef145fcda3=None,
    Chat_5b753b2a51868d330a7f215c092321e7=u'group-0004',
    Chat_5c62d12b457c837593f1cca611ecad3e=None,
    Chat_5c89f8d0bb51ccd47c95947a88174df4=u'common-009',
    Chat_5d9a760c0f30fb1fe2bd941ad5875ecb=u'luoha-who-0001',
    Chat_5ef24646dec0adcd7e102686d542d6bf=u'fuck-wangruoyu',
    Chat_5ef62ce2a073af8b87de04269f45ba7c=u'common-yingfu',
    Chat_5eff973ceee198aac6e91b504782fd30=None,
)
name_tb_6 = dict(
    Chat_6256180c0da4c0403ecd78ecd003c27c=u'luoha-group-no-0001',
    Chat_625bd7a432313cc064bc8500f8d27e72=None,
    Chat_644a0e418078dfda4b0b740245427695=None,
    Chat_6472d367cc029eef5640e6c34579c99e=u'old-datian',
    Chat_659842e0dad02bfac67adc7d83af1588=u'luoha-wangjingli',
    Chat_6628205b415fef7194bd10474f50e23c=u'common-shunfeng',
    Chat_667333c4a9b6660098eb46bddf48a596=u'luoha-who-10001',
    Chat_67d604768d64375b0515b8efd35d7ec6=None,
    Chat_67e638fcd08cf591ea8a7e4552a03769=None,
    Chat_67ec95dce5b8fce8a6e1f52835d0fc0c=None,
    Chat_6890c9c77646a8b76eb755060784ab4c=u'm-m',
    Chat_68e22fe4b793115c3e6f481e59c9bb44=None,
    Chat_68ebb842ea2578f419042da3daa9ec3a=None,
    Chat_69ac324d05bdc330d936997b43aeb2b2=u'boqi-group-0008',
    Chat_69b94d0d37498c46a00d7a7507e95bbe=None,
    Chat_69f40e9d3a3678a961dc6976bf5ef348=u'common-025',
    Chat_6a3f9f2d518c5360f25b308009559807=None,
    Chat_6b2d1a883683933cf103437e58178ddf=None,
    Chat_6b8fac3c8ef279d9ce7b731637b53005=u'star-yajun',
    Chat_6c7cfff1f6a847a2e2c734ec8b0193c3=u'common-010',
    Chat_6c91017eb0be9c84d0f746caa30c50b0=None,
    Chat_6d8266998f238eaf08c31b1fbd9ecad0=u'group-me-jjt-disteny',
    Chat_6d8774a97915ed6f72b2e73fa3f46068=None,
    Chat_6e7a5ec33d2fdba2030cd6e6898310b7=u'luoha-zhangfan',
    Chat_6f0b3a3e0145fe79b74b8016108d1aca=u'luoha-jeff',
)
name_tb_7 = dict(
    Chat_719829a60253f395141098919fd55c0b=None,
    Chat_727d0467d7887dadc36c455911650023=None,
    Chat_7286998705053bd020d942cae1a8a284=u'boqi-siji-miao',
    Chat_735fe1267d128ce8cdff3d69c6b84368=None,
    Chat_738dd77255d93fb2b807a37e7eed2d8f=u'luoha-group-0102',
    Chat_73a95a78434cf17e31fd31798af6368c=u'common-026',
    Chat_73d5627bf49be343de2e5e4c85bef879=u'luoha-baizhen',
    Chat_742ab2ec976d049da7d6fc3208d4452e=u'common-036',
    Chat_742e393075d682ce83fdc77138eada8d=u'common-037',
    Chat_7482f66938926acb8b03914fd0059631=u'fuck-who-10002',
    Chat_74a4cda28977151162b922d11d05630d=None,
    Chat_74ab92dd1899a0da19ae2b2518bf6cce=None,
    Chat_751a2aa7a804844a5896ae873ab5e229=u'fuck-longpeng',
    Chat_752539b17a5127dac94417ce0f612270=None,
    Chat_75bc6c6f4911be987ea349bc5c16d9ea=None,
    Chat_768ba2f49ec2c9062199e97b82c18c12=u'boqi-group-0100',
    Chat_77205773e4cc63b00b7f02159cba9031=u'who-lihanlin',
    Chat_78a2e741df83e9fbcff3b8e091cda9c6=None,
    Chat_792418d24210bf0dd81365b507efbdf3=u'luoha-wangguorong',
    Chat_79dd2e6c705c11a4598d8d2ecf44f039=u'common-027',
    Chat_7a5042bd375bc233be2447a8a73525b8=u'common-012',
    Chat_7a7a37142991ddcd32f05c37d1c41067=u'luoha-group-0008',
    Chat_7bfc29246581a03e1ac508c8ffa71dbf=u'luoha-sunzhenhan',
    Chat_7c3caaa372f60b3d6f485611c9f20644=u'common-013',
    Chat_7c4ecf4e53c510e2d316f588b5bd161f=u'common-014',
    Chat_7f1499934fb7a09282333b318e0df86b=u'luoha-xiaoman',
)
name_tb_8 = dict(
    Chat_80cafabdb3fd4ed04f9b34d4973e226a=u'group-xuhui-0005',
    Chat_80d337378e0feafa7c869743361836be=None,
    Chat_80d5df61072069dcbdfa2251f37219b9=None,
    Chat_822ac39bcbc9aaaa597d1b241ec68824=None,
    Chat_825bde67e9131e9cf8f3c718d00a05cb=None,
    Chat_831b2307aa880a5bc3054eb2e5808603=u'common-041',
    Chat_8439353bf0ae73ba010b94349477187d=u'who-who-0001',
    Chat_843af0e27a3604265c8f922dd7ed70d1=None,
    Chat_84fee023939e8dee7bc8395b97e55b9a=None,
    Chat_8512634dc604dd535ed364b8545e3cc2=u'group-xuhui-10001',
    Chat_854886b83f8f35432ddf62f3a5776801=u'luoha-jiazhongjie',
    Chat_861e3ea881fb34c446cd4dd7ac48716c=u'ziru-sunwangyuan',
    Chat_86240a2bede224d106457e48a45b67bc=u'no-banjia-lizong',
    Chat_8699e3f9fe2208672cf7db15deed248f=u'common-051',
    Chat_870e99d083f23adf14425f5b91e5f35a=u'luoha-xieyuli',
    Chat_8747549d02cb4b131bc0a47dd4f8d1d5=u'true-luoha-hujunjie',
    Chat_89de55fbe3a34b8b6e8586623f994344=None,
    Chat_8a09517292b5df24e6c0e69714b3956b=u'luoha-lijunze',
    Chat_8a57eca2d731f9c2c6e14d8f4bbe61c6=None,
    Chat_8c2a204c99b386e70916ea8e6a317091=u'luoha-lixiangyou',
    Chat_8c80957438be744dfc27333c59c5fadb=u'luoha-who-0003',
    Chat_8cdf2d13b31e2848546ce1216b389afb=u'common-016',
    Chat_8dad499c5d8d0a1cfd9eafa34bf9d42a=u'common-017',
    Chat_8dcd6a56b06ab2494ce95383aa6ce218=u'group-xuhui-001',
    Chat_8dce951de1dfcb8613f1d94acc8f93ca=u'boqi-sohu',
    Chat_8e4d06885d9ffbf789b95c3b00099a3e=u'common-xingbake',
    Chat_8e848970e3b04cf53748b98c0512c577=u'ziru-0001',
    Chat_8eada3fd06335cf7e5152bbe0023806c=u'luoha-shifeng',
    Chat_8f5428a717090703e72887da134857c5=u'common-018',
)
name_tb_9 = dict(
    Chat_900027d0a763791a44da134239fed3c2=u'cat-who0001',
    Chat_903c9f29764a9302d471afb58e5cacf6=u'boqi-it01',
    Chat_923077a18c100de2c657bb2dd83bc470=u'common-060',
    Chat_92b0d38a1459f87591cdf9f90ec99695=None,
    Chat_93ae8df46bc31a93fc889d97d1e44cd4=None,
    Chat_949d268b7cf74fd3fe8b4a4ad4224581=u'common-042',
    Chat_94a8565bbf4d8e678f03578899caa3bb=None,
    Chat_95f9ded82e62491500b7491f5222c180=None,
    Chat_96623c5fbcf1a484f8b5f80d9847ab40=u'group-20002',
    Chat_96ed42d4d14814d91506a17b51f9cec0=u'common-028',
    Chat_9736db565f8895f6cd2e01ab1906e192=u'common-052',
    Chat_985f128356a0d7dd6a35580b7eb3043f=None,
    Chat_987cb2e8d94d26dbe06b1d28b45afcb7=None,
    Chat_99dbe6eeb36db254a2bebd2fe76bb37b=u'common0029',
    Chat_9b925e3a77594baf5d7589cb64b7dd72=None,
    Chat_9be555de56a98e9ca449f8b41e0b9418=u'common-luoha-yiqimei',
    Chat_9c5a3d585486496f9fa5784f71e797bc=u'who-fuyu',
    Chat_9c75efa38e8dbdbd90441c040902930c=u'luoha-xiaoming',
    Chat_9d76e1b26741fbf908f21bf533c7e855=u'common-xinyongka',
)
name_tb_s = dict(
    Chat_a0305d94cfe10ad4b3a8421edda1e70f=u'luoha-no-who-0002',
    Chat_a238e51372fe33c6ba18d9731e7e5652=u'luoha-jiange-no',
    Chat_a25573c276f16cebc3257d15ef58bc61=None,
    Chat_a34221df4b5cd5a231978a36a67c034e=u'me-group-lol',
    Chat_a42051a0c43dcf433e65d8aab361c0e2=None,
    Chat_a4bee47ab03fd8f9e1174b89d998334f=u'no-me-group-0001',
    Chat_a6b269c357321143dd58c0f362f952bc=None,
    Chat_a6fc5978e96c344b1952a6f675947fb8=u'common-064',
    Chat_a787fc9ff8d6d83d570ce35104a1494c=None,
    Chat_a7daae062d9238e33bf19f9de4066b37=u'boqi-dev-0001',
    Chat_a808f6784ca8fa44e7b1f3b1294b3575=None,
    Chat_a8152b63bc1229bad7b06411ed937af6=None,
    Chat_a8f3fbabf6828754884d4ce656ec9cb8=u'luoha-no-who0002',
    Chat_a924dce0c415fb23dffbf6735d73bd26=None,
    Chat_aa53e6396dd09bb653d255441e3daee7=None,
    Chat_aa7ddcedf16caac1377daca3b6a347aa=None,
    Chat_aa96e6fbb9f3bb718522a7b284c8252d=None,
    Chat_ab51a5f7bb72d8295d753c1d6b41d215=u'no-werun',
    Chat_ab86796cc36aadd0cc7b43a5ddecd44c=None,
    Chat_abe1dcf42f6b901162100d806affa27d=None,
    Chat_ac13644f39c0e01fcd0b486b3bb56616=None,
    Chat_ad0d26a0f244b8738242eebc519c00b5=None,
    Chat_aeaebbffd5565dd50a98d587271102b1=None,
    Chat_af4953478f695bd5ffc5fc0986b2b7a6=None,
    Chat_afbe52758106c53f461ee58cb26a3d91=None,
    Chat_b18173f12e1f25ef7d29c697f9731b73=None,
    Chat_b290e93361cd62e0226a0929c0e5c15f=None,
    Chat_b29f6c32320981e0aeaf729091d14e56=None,
    Chat_b32d1bfb327de95f65da073cdf723de2=None,
    Chat_b395836576a08c3c0a54ab9882a02391=None,
    Chat_b3bbb36cc3398c55bb6ace93e1884b6a=None,
    Chat_b3e3d9ecfe904c7476e15f24d01146ee=None,
    Chat_b3f7be992ceeb78f2032714e54af1b1e=None,
    Chat_b93889e167cd3f30b05fd932ec1d6f5c=None,
    Chat_b950d68a6131d5efac2ca78090fd3ff7=None,
    Chat_b96e2f6dac8a8b815ac468c0237ae172=None,
    Chat_bbf43a01a2a6689f8757eb25088ec5ae=None,
    Chat_bc52579d7fa669928221c5c8617ea76e=None,
    Chat_bc939421e7740997340d876daab80cf7=None,
    Chat_bd1d30c863170425286fcaae1858d991=None,
    Chat_bda5bf4e207e1b00ee4b98d6d0ed4af1=None,
    Chat_bea88553b412b88325af3baf73044015=None,
    Chat_beb1c3295fd562214f4d7de0c6c0c43d=None,
    Chat_bf4080580d6cf8bbe4799a021bb88aa1=None,
    Chat_bf4e6456844be06b1652cde4780b91e1=None,
    Chat_bfcffe96d433e33a6959a4a5ff6f7742=None,
    Chat_c156d1a38aa55c427b37494e8f31104c=None,
    Chat_c18d4aae02a71f77daa9f7c940afe3bb=None,
    Chat_c25b4acca6cf0aaf0d714884c8c5c867=None,
    Chat_c2824ac3957408a438cf83a104ed3c26=None,
    Chat_c283926aba65094339ca21c1ef992074=None,
    Chat_c2bebd68fe331a03016fba9aa05044bb=None,
    Chat_c2fe931d3e9ab5ad8473c328e109d47c=None,
    Chat_c3535ddd2bebfab1173e6eb7f790ff02=None,
    Chat_c40c56caa5a0731400b2fba36e624b85=None,
    Chat_c40f038f6127ce3d52387af84162ccf2=None,
    Chat_c4c6928bea207516acf7190c61616fa9=None,
    Chat_c51de89dd9a76eaa5138e0178f7e8cbd=None,
    Chat_c5a8f4bf95e07868da4e01517495ecfa=None,
    Chat_c64bee50d2a90cd754cec1ea752fc3db=None,
    Chat_c65f7c299e87f6fe938063d85058a676=None,
    Chat_c6d5811906140a78daedfe72192f8b41=None,
    Chat_c70618531b79ec18a7173025f07e4df4=None,
    Chat_c72f01f43da0083bdd9714b6279e4229=None,
    Chat_c7715a39580167d92414035478924702=None,
    Chat_c777f2c5c858080357f7573037a36f3a=None,
    Chat_c7d3cd2474c1fc9d6c0080e98ff4de08=None,
    Chat_c8e6160833468d619e5dca0acfd43254=None,
    Chat_c8f988c73683bcd5928f95ccab163964=None,
    Chat_c92c16cf11a6268eadde189bdebc2e05=None,
    Chat_c98b6c1c5eae2418e562397a0351c98f=None,
    Chat_c9c14e1aeab22a8afe2b8c27cedb09e1=None,
    Chat_cad2ef2e43b55a20dbd3dae986ba5d01=None,
    Chat_cbd279f08e4284aecee345efa839bdc3=None,
    Chat_cbd833e72c8455c7e303bb78a85cdee9=None,
    Chat_cc56286a47f5b44ec5c9da322d109510=None,
    Chat_cc6b411054771f83d7832e295959d098=None,
    Chat_cd59f64710aee0dd745be08177323c0e=None,
    Chat_ce6df2927ae515b5a9c1a99d3a00d062=None,
    Chat_cee6ff76f63a7298f4874acb6dce98f6=None,
    Chat_d0000a5e29cd7c1a2a33d4f5df9a8b24=None,
    Chat_d2a0b8e422d743f5231e7165896c82bd=None,
    Chat_d4caf4548f61f8e7eda6f79ad4af057f=None,
    Chat_d4daa14fe8b55795070dbd99e92b628d=None,
    Chat_d6437a73ad99af3a1cb0032eee10756b=None,
    Chat_d668149a504bd6d74e9b7beb841ab703=None,
    Chat_d6950e072bf5ae67a796d1005c380dc4=None,
    Chat_d6f488832c2229ab12d17f5959aa6a29=None,
    Chat_d70413f255c8c40882f15ae1c2dd69ee=None,
    Chat_d723b2539fd4848aabba7749ac6ed4cf=None,
    Chat_d725ef35d2b55d406b65c7478b71eafb=None,
    Chat_d873986aa45826222aa1a4d79c543ea8=None,
    Chat_dc22ff77b38a83664b1580c2f54845d4=None,
    Chat_dc2cda4d20514f9eeec7062685cffb27=None,
    Chat_dc3287bf40b29a9e0aa6fd5553bd613a=None,
    Chat_dd42eece016b8e8596dd7a9ec0932480=None,
    Chat_dd5c6c4b8a122fcc629d103126edced0=None,
    Chat_de1554e48bc44494918b388801c94c49=None,
    Chat_dee67bd47fc19a4633014044b3058d5f=None,
    Chat_dffdff55cbe046d00e62baa47067278f=None,
    Chat_e013171e9458b6196a0e9f9bfb330e30=None,
    Chat_e0734b350cd89882b7bcb25f1ddfcf47=None,
    Chat_e12b52269c8e449a367cf52b38bc8071=None,
    Chat_e4282ee605f98aaa63b1ce190ba5ae8c=None,
    Chat_e43e8434b0e645df406818d4aa9ff3b7=None,
    Chat_e452072eed5b6f64e77b68304c8b6d29=None,
    Chat_e4ff74054179412400976a1c627cebac=None,
    Chat_e6db5306b94e19eb4ecfd70cca511a51=None,
    Chat_e70105b8516705d345fb55ba07f418e8=None,
    Chat_e80c431e385bd14ecb6af4b47dd242be=None,
    Chat_e8bbd8eef5501bde3abc44d1c01d84a8=None,
    Chat_e8c8cd357f62a0d03aed5b846a4fe639=None,
    Chat_e8e849cb7d5a5cb1f321188f2fe2e546=None,
    Chat_eac9f68a2a12cc9af42e027b72bf863d=None,
    Chat_ebf886fa5fe934262cc99ae456f04f07=None,
    Chat_ec47ddd4d1a313e6e0ae30c00636026f=None,
    Chat_ecc8099bd0cd164c5e2d619e38463866=None,
    Chat_ed49f1c503a125690c42a0973a6cc5a0=None,
    Chat_ed799daa23ec2a2ce83ddfca7a04613b=None,
    Chat_ee9603ffd97c03354590bd2849aee463=None,
    Chat_ee9cc5059d8e3572f9db8bf2e9e5f18c=None,
    Chat_eeaca95fb5709876a2bbe709a5270818=None,
    Chat_f0753845718f65de9bb2fd209fb7fde5=None,
    Chat_f09c322bc3c3e146ee8d4fbb4232fdb5=None,
    Chat_f0fb7654768c685f32d360b328591acf=None,
    Chat_f0fdc1a7a3c31712d01c36821decdaec=None,
    Chat_f16b9af2ad470795cf688843d54602cf=None,
    Chat_f1a0a182337bdb3d99d27cd42e3b3628=None,
    Chat_f1acb49ab678b3ddea1c65213f4c24e3=None,
    Chat_f1c413d4d4f13390d02103f57bac1d2c=None,
    Chat_f21777b9bda4cc0a2f2fc9e9d4cc4dbd=None,
    Chat_f237d79ef317f6b2d94709d074d674a3=None,
    Chat_f2696f16c81d5d4410a3de1f8b2f579c=None,
    Chat_f26eefc3bc542f1ccb88ddc67d0b8508=None,
    Chat_f394defd29dd473a9c08c69e59135533=None,
    Chat_f4ca475db8c0e6ec1a776738e7ce006e=None,
    Chat_f54c1e55e8307592160ab995daa5c068=None,
    Chat_f61b37c43fec04c9e1856fa1914fb438=None,
    Chat_f6ce1563d01528c5b948c85f955d3989=None,
    Chat_f71a7c598ce835a86f60c2d05e3cc3f4=None,
    Chat_f9511e0d19c11e6154b12301b52c10cf=None,
    Chat_fa7d4c6aa6596dfa79c2b63e49fdb7f8=None,
    Chat_fa8d8a7ae0e079471e348eee41efb38c=None,
    Chat_fbc4b4fa7368a70dfca29abb2d0799e4=None,
    Chat_fc4bae7bc9ab5f587fa7c2ecf5222045=None,
    Chat_feb732e2b630a88c78bcef255fb7e017=None,
    Chat_ff4e494ac9120743f6cec752a3419466=None,
    Chat_ff838781504c55fbf16b6a3a299fd97b=None,
    Chat_ffa5de00c3b19345e220d32e752458ad=None,
    Chat_ffcc9697ac3309e93d80f7773b133f88=None,
)

tar_dir = '161208'


def format_timestamp(ts):
    """"""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))


class WX(object):
    conn = sqlite3.connect('{}/2725175731508b12f76188d3c617c78432a9dfcb'.format(tar_dir))

    def __init__(self):
        pass

    def list_tb(self):
        res = self.conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
        ret = res.fetchall()
        return [i[0] for i in ret if i[0].startswith('Chat_')]

    def get_msg(self, tb):
        res = self.conn.execute("select CreateTime, Message, Status FROM {} WHERE type!=49 and CreateTime>1480521600".format(tb))
        ret = res.fetchall()
        s_set = set([i[-1] for i in ret])
        if len(s_set) == 1:
            return []
        return ret


def get_name(tb):
    if True:
        return tb
    name_tb = dict(
        Chat_0=name_tb_0, Chat_1=name_tb_1,
        Chat_2=name_tb_2, Chat_3=name_tb_3,
        Chat_4=name_tb_4, Chat_5=name_tb_5,
        Chat_6=name_tb_6, Chat_7=name_tb_7,
        Chat_8=name_tb_8, Chat_9=name_tb_9,
    )
    for k, v in name_tb.iteritems():
        if tb.startswith(k):
            # if tb not in v.keys():
            #     print tb
            return v.get(tb, '') or ''
    # if tb not in name_tb_s.keys():
    #     print tb
    return name_tb_s.get(tb, '') or ''

wx = WX()
tbs = wx.list_tb()
for tb in tbs:
    tbn = get_name(tb)
    msg = wx.get_msg(tb)
    c = ''
    if not msg:
        continue
    for t, m, s in msg:
        d = format_timestamp(t)
        act = '\t--OUT--'
        if s in [4, '4', u'4']:
            act = '--IN--'
        n = '{}:{}:{}:{}\n'.format(act, s, d, m.encode('utf-8'))
        c += n
    target = '{}/msg/{}-{}.txt'.format(tar_dir, tb, tbn.encode('utf-8'))
    writer = open(target, 'w')

    writer.write(c)
    writer.close()
