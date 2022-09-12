public class add01 {
   public static void main (String args[]) {
      int a, b, c;		// 숫자형 변수 a, b, c 선언.
      a=50;			// 변수 a에 50 저장
      b=20;			// 변수 b에 20 저장
      c=a+b;			// 변수 c에 a+b의 값 저장
      System.out.print(c);	// 변수 c에 저장된 값(70)을 화면에 출력
      a=10.5;			// 정수형 변수에 실수형 자료를 저장 (오류)
      b="abc";			// 정수형 변수에 문자형 자료를 저장 (오류)
   }
}
