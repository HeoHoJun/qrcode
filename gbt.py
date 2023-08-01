import qrcode

def generate_qrcode(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# 구글 지도를 사용하여 서울특별시의 위치를 표시하는 링크 생성
seoul_location_link = "https://www.google.com/maps/place/Seoul,+South+Korea/"

# QR 코드 생성 및 파일로 저장
filename = "seoul_map_qrcode.png"
generate_qrcode(seoul_location_link, filename)
print(f"서울특별시 지도에 대한 QR 코드가 {filename} 파일로 생성되었습니다.")
