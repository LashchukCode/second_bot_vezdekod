# Импорты для раздела Клавиатуры
from vkwave.bots.utils.keyboards.keyboard import Keyboard
from vkwave.bots.utils.keyboards.keyboard import ButtonColor
import strings

# Главное меню
main_menu = Keyboard()
main_menu.add_text_button(strings.question_go, color=ButtonColor.POSITIVE)
main_menu.add_row()
main_menu.add_text_button(strings.faq, color=ButtonColor.NEGATIVE)

# Меню "Перейти к вопросам"
question_go_menu = Keyboard(one_time=True)
question_go_menu.add_text_button(strings.lisl_question, color=ButtonColor.POSITIVE)
question_go_menu.add_text_button(strings.go_q, color=ButtonColor.PRIMARY)
question_go_menu.add_row()
question_go_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню "FAQ"
faq_menu = Keyboard()
faq_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню списком
lisl_question_menu = Keyboard(one_time=True)
lisl_question_menu.add_text_button(strings.vopros_1, color=ButtonColor.POSITIVE)
lisl_question_menu.add_text_button(strings.vopros_2, color=ButtonColor.PRIMARY)
lisl_question_menu.add_row()
lisl_question_menu.add_text_button(strings.vopros_3, color=ButtonColor.SECONDARY)
lisl_question_menu.add_text_button(strings.vopros_4, color=ButtonColor.POSITIVE)
lisl_question_menu.add_row()
lisl_question_menu.add_text_button(strings.vopros_5, color=ButtonColor.PRIMARY)
lisl_question_menu.add_text_button(strings.vopros_6, color=ButtonColor.SECONDARY)
lisl_question_menu.add_row()
lisl_question_menu.add_text_button(strings.vopros_7, color=ButtonColor.POSITIVE)
lisl_question_menu.add_text_button(strings.vopros_8, color=ButtonColor.PRIMARY)
lisl_question_menu.add_row()
lisl_question_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 1
vopros_1_menu = Keyboard(inline=True)
vopros_1_menu.add_text_button(strings.vopros_1_1, color=ButtonColor.POSITIVE)
vopros_1_menu.add_row()
vopros_1_menu.add_text_button(strings.vopros_1_2, color=ButtonColor.POSITIVE)
vopros_1_menu.add_row()
vopros_1_menu.add_text_button(strings.vopros_1_3, color=ButtonColor.POSITIVE)
vopros_1_menu.add_row()
vopros_1_menu.add_text_button(strings.vopros_1_4, color=ButtonColor.POSITIVE)
vopros_1_menu.add_row()
vopros_1_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 1 (для правильного ответа)
vopros_1_true_menu = Keyboard(inline=True)
vopros_1_true_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 1 (для неправильного ответа)
vopros_1_false_menu = Keyboard(inline=True)
vopros_1_false_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 2
vopros_2_menu = Keyboard(inline=True)
vopros_2_menu.add_text_button(strings.vopros_2_1, color=ButtonColor.POSITIVE)
vopros_2_menu.add_text_button(strings.vopros_2_2, color=ButtonColor.POSITIVE)
vopros_2_menu.add_row()
vopros_2_menu.add_text_button(strings.vopros_2_3, color=ButtonColor.POSITIVE)
vopros_2_menu.add_text_button(strings.vopros_2_4, color=ButtonColor.POSITIVE)

# Меню вопрос 2 (для правильного ответа)
vopros_2_true_menu = Keyboard(inline=True)
vopros_2_true_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 2 (для неправильного ответа)
vopros_2_false_menu = Keyboard(inline=True)
vopros_2_false_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 3
vopros_3_menu = Keyboard(inline=True)
vopros_3_menu.add_text_button(strings.vopros_3_1, color=ButtonColor.POSITIVE)
vopros_3_menu.add_row()
vopros_3_menu.add_text_button(strings.vopros_3_2, color=ButtonColor.POSITIVE)
vopros_3_menu.add_row()
vopros_3_menu.add_text_button(strings.vopros_3_3, color=ButtonColor.POSITIVE)
vopros_3_menu.add_row()
vopros_3_menu.add_text_button(strings.vopros_3_4, color=ButtonColor.POSITIVE)

# Меню вопрос 3 (для правильного ответа)
vopros_3_true_menu = Keyboard(inline=True)
vopros_3_true_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 3 (для неправильного ответа)
vopros_3_false_menu = Keyboard(inline=True)
vopros_3_false_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 4
vopros_4_menu = Keyboard(inline=True)
vopros_4_menu.add_text_button(strings.vopros_4_1, color=ButtonColor.POSITIVE)
vopros_4_menu.add_text_button(strings.vopros_4_2, color=ButtonColor.POSITIVE)
vopros_4_menu.add_row()
vopros_4_menu.add_text_button(strings.vopros_4_3, color=ButtonColor.POSITIVE)
vopros_4_menu.add_text_button(strings.vopros_4_4, color=ButtonColor.POSITIVE)

# Меню вопрос 4 (для правильного ответа)
vopros_4_true_menu = Keyboard(inline=True)
vopros_4_true_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 4 (для неправильного ответа)
vopros_4_false_menu = Keyboard(inline=True)
vopros_4_false_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 5
vopros_5_menu = Keyboard(inline=True)
vopros_5_menu.add_text_button(strings.vopros_5_1, color=ButtonColor.POSITIVE)
vopros_5_menu.add_row()
vopros_5_menu.add_text_button(strings.vopros_5_2, color=ButtonColor.POSITIVE)
vopros_5_menu.add_row()
vopros_5_menu.add_text_button(strings.vopros_5_3, color=ButtonColor.POSITIVE)
vopros_5_menu.add_row()
vopros_5_menu.add_text_button(strings.vopros_5_4, color=ButtonColor.POSITIVE)

# Меню вопрос 5 (для правильного ответа)
vopros_5_true_menu = Keyboard(inline=True)
vopros_5_true_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 5 (для неправильного ответа)
vopros_5_false_menu = Keyboard(inline=True)
vopros_5_false_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 6
vopros_6_menu = Keyboard(inline=True)
vopros_6_menu.add_text_button(strings.vopros_6_1, color=ButtonColor.POSITIVE)
vopros_6_menu.add_text_button(strings.vopros_6_2, color=ButtonColor.POSITIVE)
vopros_6_menu.add_row()
vopros_6_menu.add_text_button(strings.vopros_6_3, color=ButtonColor.POSITIVE)
vopros_6_menu.add_text_button(strings.vopros_6_4, color=ButtonColor.POSITIVE)

# Меню вопрос 6 (для правильного ответа)
vopros_6_true_menu = Keyboard(inline=True)
vopros_6_true_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 6 (для неправильного ответа)
vopros_6_false_menu = Keyboard(inline=True)
vopros_6_false_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 7
vopros_7_menu = Keyboard(inline=True)
vopros_7_menu.add_text_button(strings.vopros_7_1, color=ButtonColor.POSITIVE)
vopros_7_menu.add_row()
vopros_7_menu.add_text_button(strings.vopros_7_2, color=ButtonColor.POSITIVE)
vopros_7_menu.add_row()
vopros_7_menu.add_text_button(strings.vopros_7_3, color=ButtonColor.POSITIVE)
vopros_7_menu.add_row()
vopros_7_menu.add_text_button(strings.vopros_7_4, color=ButtonColor.POSITIVE)

# Меню вопрос 7 (для правильного ответа)
vopros_7_true_menu = Keyboard(inline=True)
vopros_7_true_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 7 (для неправильного ответа)
vopros_7_false_menu = Keyboard(inline=True)
vopros_7_false_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 8
vopros_8_menu = Keyboard(inline=True)
vopros_8_menu.add_text_button(strings.vopros_8_1, color=ButtonColor.POSITIVE)
vopros_8_menu.add_text_button(strings.vopros_8_2, color=ButtonColor.POSITIVE)
vopros_8_menu.add_row()
vopros_8_menu.add_text_button(strings.vopros_8_3, color=ButtonColor.POSITIVE)
vopros_8_menu.add_text_button(strings.vopros_8_4, color=ButtonColor.POSITIVE)

# Меню вопрос 8 (для правильного ответа)
vopros_8_true_menu = Keyboard(inline=True)
vopros_8_true_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 8 (для неправильного ответа)
vopros_8_false_menu = Keyboard(inline=True)
vopros_8_false_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Для пошаговых
# Меню вопрос 1
vopros_1_p_menu = Keyboard(inline=True)
vopros_1_p_menu.add_text_button(strings.vopros_1_1_p, color=ButtonColor.POSITIVE)
vopros_1_p_menu.add_row()
vopros_1_p_menu.add_text_button(strings.vopros_1_2_p, color=ButtonColor.POSITIVE)
vopros_1_p_menu.add_row()
vopros_1_p_menu.add_text_button(strings.vopros_1_3_p, color=ButtonColor.POSITIVE)
vopros_1_p_menu.add_row()
vopros_1_p_menu.add_text_button(strings.vopros_1_4_p, color=ButtonColor.POSITIVE)

# Меню вопрос 1 (для неправильного ответа)
vopros_1_p_false_menu = Keyboard(inline=True)
vopros_1_p_false_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 2
vopros_2_p_menu = Keyboard(inline=True)
vopros_2_p_menu.add_text_button(strings.vopros_2_1_p, color=ButtonColor.POSITIVE)
vopros_2_p_menu.add_text_button(strings.vopros_2_2_p, color=ButtonColor.POSITIVE)
vopros_2_p_menu.add_row()
vopros_2_p_menu.add_text_button(strings.vopros_2_3_p, color=ButtonColor.POSITIVE)
vopros_2_p_menu.add_text_button(strings.vopros_2_4_p, color=ButtonColor.POSITIVE)

# Меню вопрос 2 (для неправильного ответа)
vopros_2_p_false_menu = Keyboard(inline=True)
vopros_2_p_false_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 3
vopros_3_p_menu = Keyboard(inline=True)
vopros_3_p_menu.add_text_button(strings.vopros_3_1_p, color=ButtonColor.POSITIVE)
vopros_3_p_menu.add_row()
vopros_3_p_menu.add_text_button(strings.vopros_3_2_p, color=ButtonColor.POSITIVE)
vopros_3_p_menu.add_row()
vopros_3_p_menu.add_text_button(strings.vopros_3_3_p, color=ButtonColor.POSITIVE)
vopros_3_p_menu.add_row()
vopros_3_p_menu.add_text_button(strings.vopros_3_4_p, color=ButtonColor.POSITIVE)

# Меню вопрос 3 (для неправильного ответа)
vopros_3_p_false_menu = Keyboard(inline=True)
vopros_3_p_false_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 4
vopros_4_p_menu = Keyboard(inline=True)
vopros_4_p_menu.add_text_button(strings.vopros_4_1_p, color=ButtonColor.POSITIVE)
vopros_4_p_menu.add_text_button(strings.vopros_4_2_p, color=ButtonColor.POSITIVE)
vopros_4_p_menu.add_row()
vopros_4_p_menu.add_text_button(strings.vopros_4_3_p, color=ButtonColor.POSITIVE)
vopros_4_p_menu.add_text_button(strings.vopros_4_4_p, color=ButtonColor.POSITIVE)

# Меню вопрос 4 (для неправильного ответа)
vopros_4_p_false_menu = Keyboard(inline=True)
vopros_4_p_false_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 5
vopros_5_p_menu = Keyboard(inline=True)
vopros_5_p_menu.add_text_button(strings.vopros_5_1_p, color=ButtonColor.POSITIVE)
vopros_5_p_menu.add_row()
vopros_5_p_menu.add_text_button(strings.vopros_5_2_p, color=ButtonColor.POSITIVE)
vopros_5_p_menu.add_row()
vopros_5_p_menu.add_text_button(strings.vopros_5_3_p, color=ButtonColor.POSITIVE)
vopros_5_p_menu.add_row()
vopros_5_p_menu.add_text_button(strings.vopros_5_4_p, color=ButtonColor.POSITIVE)

# Меню вопрос 5 (для неправильного ответа)
vopros_5_p_false_menu = Keyboard(inline=True)
vopros_5_p_false_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 6
vopros_6_p_menu = Keyboard(inline=True)
vopros_6_p_menu.add_text_button(strings.vopros_6_1_p, color=ButtonColor.POSITIVE)
vopros_6_p_menu.add_text_button(strings.vopros_6_2_p, color=ButtonColor.POSITIVE)
vopros_6_p_menu.add_row()
vopros_6_p_menu.add_text_button(strings.vopros_6_3_p, color=ButtonColor.POSITIVE)
vopros_6_p_menu.add_text_button(strings.vopros_6_4_p, color=ButtonColor.POSITIVE)

# Меню вопрос 6 (для неправильного ответа)
vopros_6_p_false_menu = Keyboard(inline=True)
vopros_6_p_false_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 7
vopros_7_p_menu = Keyboard(inline=True)
vopros_7_p_menu.add_text_button(strings.vopros_7_1_p, color=ButtonColor.POSITIVE)
vopros_7_p_menu.add_row()
vopros_7_p_menu.add_text_button(strings.vopros_7_2_p, color=ButtonColor.POSITIVE)
vopros_7_p_menu.add_row()
vopros_7_p_menu.add_text_button(strings.vopros_7_3_p, color=ButtonColor.POSITIVE)
vopros_7_p_menu.add_row()
vopros_7_p_menu.add_text_button(strings.vopros_7_4_p, color=ButtonColor.POSITIVE)

# Меню вопрос 7 (для неправильного ответа)
vopros_7_p_false_menu = Keyboard(inline=True)
vopros_7_p_false_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 8
vopros_8_p_menu = Keyboard(inline=True)
vopros_8_p_menu.add_text_button(strings.vopros_8_1_p, color=ButtonColor.POSITIVE)
vopros_8_p_menu.add_text_button(strings.vopros_8_2_p, color=ButtonColor.POSITIVE)
vopros_8_p_menu.add_row()
vopros_8_p_menu.add_text_button(strings.vopros_8_3_p, color=ButtonColor.POSITIVE)
vopros_8_p_menu.add_text_button(strings.vopros_8_4_p, color=ButtonColor.POSITIVE)

# Меню вопрос 8 (для правильного ответа)
vopros_8_p_true_menu = Keyboard(inline=True)
vopros_8_p_true_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)

# Меню вопрос 8 (для неправильного ответа)
vopros_8_p_false_menu = Keyboard(inline=True)
vopros_8_p_false_menu.add_text_button(strings.back, color=ButtonColor.NEGATIVE)


