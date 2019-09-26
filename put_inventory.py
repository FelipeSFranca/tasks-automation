import os


def make_put(inv):
    return f"""curl -X PUT -u transporte@email.com:huru1234 -d "status=SENT&latitude=32.4941937&longitude=-116.9094078" -H "X-NIC-DEVICE: 61656433-3464-6136-0500-040409000705" https://nic.api.hurusystems.com/box/{inv}""".format(inv=inv)


if __name__ == '__main__':
    inventories = [
        "904812b2-f201-431e-a40b-a995b63b378b",
        "2b51c96b-9165-4d68-90c6-2599c8ef43ad",
        "c1bd1b59-2c33-4350-bb2d-9a88874ed184",
        "04873eaf-8d32-4d17-b77a-237c00b49b1a",
        "deda1248-f278-4d50-b79d-1227c1055003",
        "1a580cfb-17b7-4c05-8012-b7f95cbe79b9",
        "44f5236d-8dc0-4d87-9990-937286239276",
        "6ab1692d-8b57-49d3-ad6e-10b260773a06",
        "976bc5c0-b024-4768-b8c1-18cb04b948dd",
        "f7143fc5-0d56-418e-b30d-9da1a5bb90f3",
        "fa650d66-1c62-48a1-b4f6-6a26e8246ec7",
        "6920c79f-7bae-41eb-8428-1651ca2514e3",
        "6f75cb84-fd36-45f4-8792-593cf6c6cbfe",
        "9c485582-8448-47d1-ad9f-3fb6c6971491",
        "d4c8db64-ff9b-4caa-89a6-79294f0c10ea",
        "56dd4bc9-d9ac-4c4f-80ef-eb99cc29ddf8",
        "a87eb489-7571-4e10-aa8f-c80aab2c7215",
        "eed4f059-35df-4cad-9a82-4c76bada4c64",
        "2801bc1c-6eff-4ef9-88de-398faa61c0e8",
        "66bbe81e-77d3-426d-8649-327be54c927c",
        "d0acbfb5-bc18-45e4-b3e3-191fc7aa5a0c",
        "09de9068-d19b-4ddc-b55d-8b6cadccac19",
        "324851f9-eaff-4709-b007-a2d52d36233b",
        "5d31c405-dcd9-432b-a632-2a2f1bf3dc0f",
        "367765f9-841c-415c-8ad2-b983883ed493",
        "8d2bc17b-fb19-43c2-8e2b-053ea2f46fcd",
        "aa0ff5c4-c38c-44ef-8a4c-2c0ab9b8e485",
        "25431baf-a789-4c43-ab07-3764368e2045",
        "936dc35b-6845-477c-9984-67801445724f",
        "90de180d-2c18-403e-9e46-56613ec100b3",
        "8655125b-12f7-4b00-9742-8ff6d30434b8",
        "91c553b5-d307-4d58-8522-6b74afe3102c",
        "0506b821-6713-47e6-860b-b187a0f63688",
        "849a0219-3e85-4774-acb3-5a182af94c62",
        "13eb6c35-5857-41ed-b0ae-a60e80d961d2",
        "7745da66-d922-498d-a429-63680e53868b",
        "c826d93d-d856-47c2-acce-8222ffb47363",
        "fec1ea28-f7f8-451f-b290-5fb5c681013b",
        "c5b28b91-54ed-421e-9761-e8ae91c413f3",
        "45159f99-7671-43f6-a377-686d71a00b1a",
        "a16e5d61-86f8-4416-9c48-690a16e6e903",
        "e0a25fc1-1450-4946-a34c-2ae3c9c0ebd3",
        "0199dffa-056e-4ea7-9d3b-db62ce25e380",
        "acade672-5de0-4a58-95a0-d7454a8ab97f",
        "728005a3-a92f-4824-881f-92c6f3cda693",
        "f81ee0bd-bc7a-4383-aa54-4c43edbd9820",
        "98b4c790-c0a6-48fc-8bc7-b10dd9682349",
        "e2068418-4638-4fce-9ffc-a3cd58affbfe",
        "45c1398f-bda3-495c-aae5-d2cf6b7b524d",
        "9f559330-2646-4893-af31-0bea8a33da40",
        "2793d37b-db68-40f2-87ad-baa54d4a7ab5",
        "13f5f429-3383-46aa-9c49-68645ad92e93",
        "db99303d-8e51-43f5-92ab-19f7d1baf626",
        "28aeb248-8fe6-4d63-a347-516d576adc23",
        "490667ed-cbc3-4822-b5a6-ce524f5b03c3",
        "bbceab20-8538-4033-9f50-59da6560ac16",
        "a91f7488-4810-4504-a635-d4fcbf1e8c10",
        "828ba6a1-d022-4f0d-99bc-dea2b604ac15",
        "8b95e612-bac5-4b0d-9dde-6ffcd6bf1fe0",
        "c9ba17be-992a-4059-a1e4-72d1d74f84f7",
        "8f20a6e3-ca6e-4a25-bb59-eec33d944f71",
        "8395b16e-e096-4d06-9efd-14295e872690",
        "5027abe1-22c6-48f9-99c6-c18fff60b94e",
        "80febc0d-1af2-4bf0-8249-6622e3091213",
        "1241addf-d23b-4c63-9b3b-5ba72d1533fd",
        "e48e2c28-4933-4aa8-be29-9cf34aa63b2c",
        "69e73e8c-b195-42bf-a064-9a8f747e7e81",
        "1a5713f8-635f-4141-8121-72118acd5274",
        "6bc71460-d903-4ebf-b715-f8a241f7b377",
        "fb0e451d-085d-42df-b392-a637c06533dd",
        "5470dfdc-0dcc-425d-8512-0a806c2c9d47",
        "048c6f96-debc-4af9-9769-61585bcc087d",
        "cd9c6e3d-bf5e-4dfd-986d-521db2981e45",
        "4d06bceb-df5c-4a62-bc09-9cbce76ea8b7",
        "a18ecc16-54d1-4095-8271-520c05932c50",
        "20c3c0cd-2f27-4fd3-b119-e6e11596f5c4",
        "cbb6cd9f-2076-4258-9282-d4bccbaf0b85",
        "62866cca-7b07-4e1b-b6fd-e0c3dfbf5523",
        "7207301f-57d0-40c0-b880-30b71174cf74",
        "8f9b7c04-8d3e-497c-9213-c9d142eb6074",
        "e7293100-e96e-4f10-ad8f-d6633d828325",
        "6d59bda2-994b-43e2-98c2-f81eaad12f41",
        "782a6e10-034a-4d72-9cbb-fde3ea9a1c67",
        "fbd96cc5-bb31-4d3d-8f94-e4daea675867",
        "d14b2840-fc82-40b7-bde4-d50f06522b15",
        "355c9b02-d2ab-4b8b-9c96-e60c2f3f00fc",
        "b087026d-4d14-45a4-be47-5a12d46bac5c",
        "f93e86d6-a991-49b2-af0e-878629e72b43",
        "25ffce27-03df-43ec-8aa3-ae1c25cd07a1",
        "61a51d6b-6ad1-448c-8b0b-041b7b5e56bc",
        "9d985a03-d1e9-41e0-9250-df4e1a4d11f7",
        "66ebedf3-b088-4454-bc20-38a99543664c",
        "045062c1-a4b4-40b0-9e16-3f0ac611ea6a",
        "c8bf3a7f-9da0-4fd1-8e30-76eb01eed76e",
        "5b44421e-c8c8-41ee-bb27-c1f179f49048",
        "ba4c3c58-75c5-47df-8804-250fe88b5477",
        "e60e45de-fde1-4104-b23d-e6fdf50ebe44",
        "2642b356-492d-4b48-8eb2-abcfd175106d",
        "343fcec7-b01b-4553-9014-1107dbe7977e",
        "5baf5e39-efb3-4702-bc35-3a53c2b31f70",
        "d7f8ed7e-b73d-4443-9280-134535e230eb",
        "91c3c3b4-724d-4d45-a13b-251b0c084435",
        "362238eb-d463-4139-8040-99fe053e7250",
        "79c75989-189f-4401-9f6a-5d27d1b7b0b2",
        "488ad92c-f5d0-4ae0-a575-658e2cadd723",
        "bf52ea2f-71dd-49aa-8d9c-ce6393ee5485",
        "14539196-43a5-4c1f-8eb5-9ace3fad5e56",
        "ca62aec4-41a5-48fb-b94c-99b67c12f904",
        "6df43166-8cab-44dd-92e3-bcf4e53ae932"
    ]
    for inv in inventories:
        put = make_put(inv)
        os.system(put)