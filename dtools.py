import base64, codecs
magic = 'aW1wb3J0IG9zLCBzeXMsIHRpbWUsIHJlcXVlc3RzLCBkYXRldGltZSwgcGhvbmVudW1iZXJzDQpmcm9tIHBob25lbnVtYmVycyBpbXBvcnQgZ2VvY29kZXIsIGNhcnJpZXIsIHRpbWV6b25lDQpmcm9tIHN5cyBpbXBvcnQgcGxhdGZvcm0NCmV4Y2VwdCBJbXBvcnRFcnJvcjoNCiAgICB0cnk6DQogICAgICAgIG9zLnN5c3RlbSgncGlwMyBpbnN0YWxsIHJlcXVlc3RzJykNCiAgICAgICAgb3Muc3lzdGVtKCdwaXAzIGluc3RhbGwgcGhvbmVudW1iZXJzJykNCiAgICAgICAgb3Muc3lzdGVtKCdwaXAzIGluc3RhbGwgZGF0ZXRpbWUnKQ0KICAgICAgICBvcy5zeXN0ZW0oJ3BpcDMgaW5zdGFsbCB0aW1lJykNCiAgICBleGNlcHQ6DQogICAgICAgIGlmIHN5cy5wbGF0Zm9ybSA9PSAnd2luMzInOg0KICAgICAgICAgICAgb3Muc3lzdGVtKCdweXRob24gLW0gcGlwIGluc3RhbGwgcmVxdWVzdHMnKQ0KICAgICAgICAgICAgb3Muc3lzdGVtKCdweXRob24gLW0gcGlwIHBob25lbnVtYmVycycpDQogICAgICAgICAgICBvcy5zeXN0ZW0oJ3B5dGhvbiAtbSBwaXAgaW5zdGFsbCBkY'
love = 'KEyqTygMFpcQDbtVPNtVPNtVPNtVPOipl5mrKA0MJ0bW3O5qTuiovNgoFOjnKNtqTygMFpcQDbtVPNtVPNtVTyzVUA5pl5joTS0Mz9loFN9CFNaoTyhqKtaBt0XVPNtVPNtVPNtVPNto3Zhp3ymqTIgXPqmqJEiVUOcpQZtnJ5mqTSfoPOlMKS1MKA0plpcQDbtVPNtVPNtVPNtVPOipl5mrKA0MJ0bW3A1MT8tpTyjZlOcoaA0LJkfVUObo25yoaIgLzIlplpcQDbtVPNtVPNtVPNtVPOipl5mrKA0MJ0bW3A1MT8tpTyjZlOcoaA0LJkfVTEuqTI0nJ1yWlxAPvNtVPNtVPNtVPNtVT9mYaA5p3EyoFtap3IxolOjnKNmVTyhp3EuoTjtqTygMFpcQDbAPt0XMTIzVTWypaAcnPtcBt0XVPNtVTyzVUOfLKEzo3WgVQ09VPWfnJ51rPVto3VtpTkuqTMipz0tCG0tVzkcoaI4ZvV6QDbtVPNtVPNtVT9mYaA5p3EyoFtvL2kyLKVvXD0XVPNtVTIfnJLtpTkuqTMipz0tCG0tVzEupaqcovV6QDbtVPNtVPNtVT9mYaA5p3EyoFtvL2kyLKVvXD0XVPNtVTIfnJLtpTkuqTMipz0tCG0tVaqcowZlVvOipvOjoTS0Mz9loFN9CFNvq2yhAwDvBt0XVPNtVPNtVPOipl5mrKA0MJ0bVzAfplVcQDbtVPNtMJ'
god = 'xzZToNCiAgICAgICAgb3Muc3lzdGVtKCJjbGVhciIpDQoNCg0KZGVmIGNla3VwZGF0ZSgpOg0KICAgIHIgPSByZXF1ZXN0cy5nZXQoImh0dHBzOi8vcGFzdGViaW4uY29tL3Jhdy9xeWVEMFpFeiIpDQogICAgayA9IHIudGV4dA0KICAgIGlmIGsgPT0gIjEuMSI6DQogICAgICAgIHByaW50KGYiLX49PlZlcnNpIHtyLnRleHR9IikNCiAgICBlbHNlOg0KICAgICAgICBwcmludCgiVG9sb25nIFVwZGF0ZSBrZSB2ZXJzaSBzZWxhbmp1dG55YSEiKQ0KDQpkZWYgdG9vbHMxKCk6DQogICAgcHJpbnQoIk1hc3VrYW4gTm9tb3IhIFxuY29udG9oICs2MjEyMzQ1Njc4OSIpDQogICAgbm9tb3IgPSBpbnB1dCgiLX49PiIpDQogICAgcGhvbmUgPSBwaG9uZW51bWJlcnMucGFyc2Uobm9tb3IpDQogICAgYSA9IGdlb2NvZGVyLmRlc2NyaXB0aW9uX2Zvcl9udW1iZXIocGhvbmUsICJlbiIpDQogICAgYiA9IGNhcnJpZXIubmFtZV9mb3JfbnVtYmVyKHBob25lLCAiZW4iKQ0KICAgIGMgPSB0aW1lem9uZS50aW1lX3pvbmVzX2Zvcl9udW1iZXIocGhvbmUpDQogICAgcHJpbnQoIiIpDQo'
destiny = 'tVPNtpUWcoaDbMvVgsw0+GzIaLKWuY0AiqJ50paxtCvO7LK0vXD0XVPNtVUOlnJ50XTLvYK49CyOlo3McMTIlVQ4tr2W9VvxAPvNtVPOjpzyhqPuzVv1+CG5HnJ1yVSciozHtCvO7L30vXD0XQDcxMJLtoJIhqFtcBt0XVPNtVTWypaAcnPtcQDbtVPNtL2IeqKOxLKEyXPxAPvNtVPOxLKEyVQ0tMTS0MKEcoJHhMTS0MKEcoJHhoz93XPxAPvNtVPOjpzyhqPtvYK49CyEio2kmVRW5VREioJyholVcQDbtVPNtpUWcoaDbVv1+CG5GMJA0o3VtITImqTIlVvxAPvNtVPOjpzyhqPuzVv1+CG5GrKEyoFN6VUgjoTS0Mz9loK0vXD0XVPNtVUOlnJ50XTLaYK49CagxLKEyYaA0pzM0nJ1yXPVyDFNyMPNyoFNyJFVcsFpcQDbtVPNtpUWcoaDbVak8sUk8sUk8sUk8sUk8sUk8sUk8sUk8sUk8sUk8sUk8sUk8VvxAPvNtVPOjpzyhqPtvYK49CyfkKFOQMJftnJ5zo3WgLKAcVT5ioJ9lVUEyoTMiovVcQDbtVPNtpTyfnJttCFOcoaO1qPtvYK49CvVcQDbtVPNtnJLtpTyfnJttCG0tVwRvBt0XVPNtVPNtVPO0o29fpmRbXD0XVPNtVTIfp2H6QDbtVPNtVPNtVT1yoaHbXD0XQDbAPz1yoaHbXD=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
