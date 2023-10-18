"""
    스크립트에는 몇가지 규칙이 있습니다. PEP8
    맨위에는 독스트링으로 본 스크립트를 설명합니다.
"""
    
import datetime as dt 
# 임폴트 문은 모든 파일맨위에, 한 행씩 작성, 표준라이브러리 먼저, 그다음 서드파티, 마지막으로 직접제작한 모듈

TEMPERATURE_SCALES = ("fahrenheit", "kelvin", "celsius")
# 상수는 대문자 언더바만 사용하여 표시

#클라스와 함수는 빈행 두개로 구분
class TemperatureConverter:  #직접만든 클라스는 첫글자 대문자로 표기 
    pass  #인라인 주석은 코드와 최소 공백 두칸이상


def convert_to_celsius(degrees, source="fahrenheit"):  #함수와 함수인자는 소문자로만 표기
    """
    이 함수는 화씨나 칼빈을 섭씨로 바꿉니다.  함수설명 독스트링 넣기
    """
    if source.lower() == "fahrenheit":  #콜론주위에 공백을 넣지 마세요
        return (degrees-32) * (5/9)  #수학연산자 사이에는 좌우에 공백을 넣으세요, 연산자가 여러개일 경우 마지막연산에만 공백넣기
    elif source.lower() == "kelvin":
        return degrees - 273.15
    else:
        return f"Don't know how to convert from {source}"
    
celsius = convert_to_celsius(88, source="kelvin")  #변수이름음 소문자로 변수에 값을 할당할때 = 에는 공백을 넣고 함수호출키워드 인자의 =은 붙여쓴다.
non_celsius_scales = TEMPERATURE_SCALES[:-1]  #인덱스와 스라이스를 쓸 때는 대괄호 주위에 공백을 넣지 않습니다.

print("Current time: " + dt.datetime.now().isoformat())
print(f"The temperature in Celsius is: {celsius}")
print(non_celsius_scales)
