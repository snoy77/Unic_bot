import serv.MathModule as MM
import QueryAndAnsver as QA

print("\n------------ mathModule ------------")
print(">> Включение модуля на сообщения:")
def MM_is_test(mes, need = True):

    str_res = ''
    res_itsMe = MM.isItToMe(mes)

    if res_itsMe == need:
        str_res = "  \"" + mes + "\": " + str(res_itsMe)

        res_answer = MM.setAnswerObject(mes, QA.AnswerClass())
        str_res += " >> \"" + res_answer.text + "\""
    else:
        str_res = "! \"" + mes + "\": " + str(res_itsMe)

    print(str_res)


MM_is_test('88+99')
MM_is_test('88+ 99')
MM_is_test('88 +99')
MM_is_test('88 + 99')
MM_is_test('88 * 99')
MM_is_test('88 - 99')
MM_is_test('88 / 99')

MM_is_test('8.8+9.9')
MM_is_test('8.8*9.9')
MM_is_test('8.8/9.9')
MM_is_test('8.8-9.9')
MM_is_test('88+9.9')
MM_is_test('88*9.9')
MM_is_test('88-9.9')
MM_is_test('88/9.9')
MM_is_test('8.8+99')
MM_is_test('8.8/99')
MM_is_test('8.8-99')
MM_is_test('8.8*99')

MM_is_test('8,8+9,9')
MM_is_test('8,8+99')
MM_is_test('88+9,9')

MM_is_test('1 000+99')
MM_is_test('+99')
MM_is_test('+9.9')


input("\n\n\npipa")
