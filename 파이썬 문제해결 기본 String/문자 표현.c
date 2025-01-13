// 문자열로 된 숫자를 정수로 변환
int atoi(const char *string)
{
  int value = 0, digit, c;
  while ((c = *string++) != '\0'){
    if (c >= '0' && c <= '9')
      digit = c - '0';
    else
      break;

    value = (value * 10) + digit;
  }
  return value;
}
