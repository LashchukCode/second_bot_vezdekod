from vkwave.bots import SimpleLongPollBot, SimpleBotEvent
import config
import strings
import keyboard


users = {}


class user:
    id = 0
    chatState = 0
    wins = 0

    def __init__(self, id):
        self.id = id


bot = SimpleLongPollBot(tokens=config.TOKEN, group_id=config.PUBLIC_ID)

@bot.message_handler()
async def info(event: SimpleBotEvent) -> str:
    print(event)
    if not event.from_id in users:
        users[event.from_id] = user(event.from_id)
        await event.answer(strings.first_msg, keyboard=keyboard.main_menu.get_keyboard())
    else:
        if event.object.object.message.text in ['Начать', 'Start']:
            await event.answer(strings.first_msg, keyboard=keyboard.main_menu.get_keyboard())
        elif event.object.object.message.text == strings.question_go:
            users[event.from_id].chatstate = 1
            await event.answer(strings.question_go_msg, keyboard=keyboard.question_go_menu.get_keyboard())
        elif event.object.object.message.text == strings.faq:
            users[event.from_id].chatstate = 1
            await event.answer(strings.faq_msg, keyboard=keyboard.faq_menu.get_keyboard())
        elif event.object.object.message.text == strings.lisl_question:
            users[event.from_id].chatstate = 2
            await event.answer(strings.lisl_question_msg, keyboard=keyboard.lisl_question_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_1:
            users[event.from_id].chatstate = 3
            await event.answer(strings.vopros_1_msg, keyboard=keyboard.vopros_1_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_1_1:
            await event.answer(strings.vopros_1_t, keyboard=keyboard.vopros_1_true_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_1_2:
            await event.answer(strings.vopros_1_f, keyboard=keyboard.vopros_1_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_1_3:
            await event.answer(strings.vopros_1_f, keyboard=keyboard.vopros_1_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_1_4:
            await event.answer(strings.vopros_1_f, keyboard=keyboard.vopros_1_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_2:
            users[event.from_id].chatstate = 3
            await event.answer(strings.vopros_2_msg, keyboard=keyboard.vopros_2_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_2_1:
            await event.answer(strings.vopros_2_f, keyboard=keyboard.vopros_2_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_2_2:
            await event.answer(strings.vopros_2_f, keyboard=keyboard.vopros_2_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_2_3:
            await event.answer(strings.vopros_2_f, keyboard=keyboard.vopros_2_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_2_4:
            await event.answer(strings.vopros_2_t, keyboard=keyboard.vopros_2_true_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_3:
            users[event.from_id].chatstate = 3
            await event.answer(strings.vopros_3_msg, keyboard=keyboard.vopros_3_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_3_1:
            await event.answer(strings.vopros_3_f, keyboard=keyboard.vopros_3_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_3_2:
            await event.answer(strings.vopros_3_t, keyboard=keyboard.vopros_3_true_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_3_3:
            await event.answer(strings.vopros_3_f, keyboard=keyboard.vopros_3_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_3_4:
            await event.answer(strings.vopros_3_f, keyboard=keyboard.vopros_3_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_4:
            users[event.from_id].chatstate = 3
            await event.answer(strings.vopros_4_msg, keyboard=keyboard.vopros_4_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_4_1:
            await event.answer(strings.vopros_4_t, keyboard=keyboard.vopros_4_true_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_4_2:
            await event.answer(strings.vopros_4_f, keyboard=keyboard.vopros_4_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_4_3:
            await event.answer(strings.vopros_4_f, keyboard=keyboard.vopros_4_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_4_4:
            await event.answer(strings.vopros_4_f, keyboard=keyboard.vopros_4_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_5:
            users[event.from_id].chatstate = 3
            await event.answer(strings.vopros_5_msg, keyboard=keyboard.vopros_5_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_5_1:
            await event.answer(strings.vopros_5_t, keyboard=keyboard.vopros_5_true_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_5_2:
            await event.answer(strings.vopros_5_f, keyboard=keyboard.vopros_5_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_5_3:
            await event.answer(strings.vopros_5_f, keyboard=keyboard.vopros_5_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_5_4:
            await event.answer(strings.vopros_5_f, keyboard=keyboard.vopros_5_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_6:
            users[event.from_id].chatstate = 3
            await event.answer(strings.vopros_6_msg, keyboard=keyboard.vopros_6_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_6_1:
            await event.answer(strings.vopros_6_f, keyboard=keyboard.vopros_6_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_6_2:
            await event.answer(strings.vopros_6_t, keyboard=keyboard.vopros_6_true_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_6_3:
            await event.answer(strings.vopros_6_f, keyboard=keyboard.vopros_6_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_6_4:
            await event.answer(strings.vopros_6_f, keyboard=keyboard.vopros_6_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_7:
            users[event.from_id].chatstate = 3
            await event.answer(strings.vopros_7_msg, keyboard=keyboard.vopros_7_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_7_1:
            await event.answer(strings.vopros_7_t, keyboard=keyboard.vopros_7_true_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_7_2:
            await event.answer(strings.vopros_7_f, keyboard=keyboard.vopros_7_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_7_3:
            await event.answer(strings.vopros_7_f, keyboard=keyboard.vopros_7_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_7_4:
            await event.answer(strings.vopros_7_f, keyboard=keyboard.vopros_7_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_8:
            users[event.from_id].chatstate = 3
            await event.answer(strings.vopros_8_msg, keyboard=keyboard.vopros_8_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_8_1:
            await event.answer(strings.vopros_8_t, keyboard=keyboard.vopros_8_true_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_8_2:
            await event.answer(strings.vopros_8_f, keyboard=keyboard.vopros_8_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_8_3:
            await event.answer(strings.vopros_8_f, keyboard=keyboard.vopros_8_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_8_4:
            await event.answer(strings.vopros_8_f, keyboard=keyboard.vopros_8_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.go_q:
            users[event.from_id].chatstate = 2
            await event.answer(strings.vopros_1_p_msg, keyboard=keyboard.vopros_1_p_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_1_1_p:
            await event.answer(strings.vopros_1_t_p)
            await event.answer(strings.vopros_2_p_msg, keyboard=keyboard.vopros_2_p_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_1_2_p:
            users[event.from_id].chatstate = 4
            await event.answer(strings.vopros_1_f_p, keyboard=keyboard.vopros_1_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_1_3_p:
            users[event.from_id].chatstate = 4
            await event.answer(strings.vopros_1_f_p, keyboard=keyboard.vopros_1_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_1_4_p:
            users[event.from_id].chatstate = 4
            await event.answer(strings.vopros_1_f_p, keyboard=keyboard.vopros_1_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_2_1_p:
            users[event.from_id].chatstate = 5
            await event.answer(strings.vopros_2_f_p, keyboard=keyboard.vopros_2_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_2_2_p:
            users[event.from_id].chatstate = 5
            await event.answer(strings.vopros_2_f_p, keyboard=keyboard.vopros_2_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_2_3_p:
            users[event.from_id].chatstate = 5
            await event.answer(strings.vopros_2_f_p, keyboard=keyboard.vopros_2_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_2_4_p:
            await event.answer(strings.vopros_2_t_p)
            await event.answer(strings.vopros_3_p_msg, keyboard=keyboard.vopros_3_p_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_3_1_p:
            users[event.from_id].chatstate = 6
            await event.answer(strings.vopros_3_f_p, keyboard=keyboard.vopros_3_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_3_2_p:
            await event.answer(strings.vopros_3_t_p)
            await event.answer(strings.vopros_4_p_msg, keyboard=keyboard.vopros_4_p_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_3_3_p:
            users[event.from_id].chatstate = 6
            await event.answer(strings.vopros_3_f_p, keyboard=keyboard.vopros_3_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_3_4_p:
            users[event.from_id].chatstate = 6
            await event.answer(strings.vopros_3_f_p, keyboard=keyboard.vopros_3_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_4_1_p:
            await event.answer(strings.vopros_4_t_p)
            await event.answer(strings.vopros_5_p_msg, keyboard=keyboard.vopros_5_p_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_4_2_p:
            users[event.from_id].chatstate = 7
            await event.answer(strings.vopros_4_f_p, keyboard=keyboard.vopros_4_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_4_3_p:
            users[event.from_id].chatstate = 7
            await event.answer(strings.vopros_4_f_p, keyboard=keyboard.vopros_4_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_4_4_p:
            users[event.from_id].chatstate = 7
            await event.answer(strings.vopros_4_f_p, keyboard=keyboard.vopros_4_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_5_1_p:
            await event.answer(strings.vopros_5_t_p)
            await event.answer(strings.vopros_6_p_msg, keyboard=keyboard.vopros_6_p_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_5_2_p:
            users[event.from_id].chatstate = 8
            await event.answer(strings.vopros_5_f_p, keyboard=keyboard.vopros_5_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_5_3_p:
            users[event.from_id].chatstate = 8
            await event.answer(strings.vopros_5_f_p, keyboard=keyboard.vopros_5_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_5_4_p:
            users[event.from_id].chatstate = 8
            await event.answer(strings.vopros_5_f_p, keyboard=keyboard.vopros_5_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_6_1_p:
            users[event.from_id].chatstate = 9
            await event.answer(strings.vopros_6_f_p, keyboard=keyboard.vopros_6_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_6_2_p:
            await event.answer(strings.vopros_6_t_p)
            await event.answer(strings.vopros_7_p_msg, keyboard=keyboard.vopros_7_p_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_6_3_p:
            users[event.from_id].chatstate = 9
            await event.answer(strings.vopros_6_f_p, keyboard=keyboard.vopros_6_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_6_4_p:
            users[event.from_id].chatstate = 9
            await event.answer(strings.vopros_6_f_p, keyboard=keyboard.vopros_6_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_7_1_p:
            await event.answer(strings.vopros_7_t_p)
            await event.answer(strings.vopros_8_p_msg, keyboard=keyboard.vopros_8_p_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_7_2_p:
            users[event.from_id].chatstate = 10
            await event.answer(strings.vopros_7_f_p, keyboard=keyboard.vopros_7_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_7_3_p:
            users[event.from_id].chatstate = 10
            await event.answer(strings.vopros_7_f_p, keyboard=keyboard.vopros_7_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_7_4_p:
            users[event.from_id].chatstate = 10
            await event.answer(strings.vopros_7_f_p, keyboard=keyboard.vopros_7_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_8_1_p:
            users[event.from_id].chatstate = 2
            await event.answer(strings.vopros_8_t_p, keyboard=keyboard.vopros_8_p_true_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_8_2_p:
            users[event.from_id].chatstate = 11
            await event.answer(strings.vopros_8_f_p, keyboard=keyboard.vopros_8_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_8_3_p:
            users[event.from_id].chatstate = 11
            await event.answer(strings.vopros_8_f_p, keyboard=keyboard.vopros_8_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.vopros_8_4_p:
            users[event.from_id].chatstate = 11
            await event.answer(strings.vopros_8_f_p, keyboard=keyboard.vopros_8_p_false_menu.get_keyboard())
        elif event.object.object.message.text == strings.back:
            if users[event.from_id].chatstate == 1:
                await event.answer(strings.im_back, keyboard=keyboard.main_menu.get_keyboard())
            if users[event.from_id].chatstate == 2:
                await event.answer(strings.im_back, keyboard=keyboard.question_go_menu.get_keyboard())
            if users[event.from_id].chatstate == 3:
                await event.answer(strings.im_back, keyboard=keyboard.lisl_question_menu.get_keyboard())
            if users[event.from_id].chatstate == 4:
                await event.answer(strings.im_back, keyboard=keyboard.vopros_1_p_menu.get_keyboard())
            if users[event.from_id].chatstate == 5:
                await event.answer(strings.im_back, keyboard=keyboard.vopros_2_p_menu.get_keyboard())
            if users[event.from_id].chatstate == 6:
                await event.answer(strings.im_back, keyboard=keyboard.vopros_3_p_menu.get_keyboard())
            if users[event.from_id].chatstate == 7:
                await event.answer(strings.im_back, keyboard=keyboard.vopros_4_p_menu.get_keyboard())
            if users[event.from_id].chatstate == 8:
                await event.answer(strings.im_back, keyboard=keyboard.vopros_5_p_menu.get_keyboard())
            if users[event.from_id].chatstate == 9:
                await event.answer(strings.im_back, keyboard=keyboard.vopros_6_p_menu.get_keyboard())
            if users[event.from_id].chatstate == 10:
                await event.answer(strings.im_back, keyboard=keyboard.vopros_7_p_menu.get_keyboard())
            if users[event.from_id].chatstate == 11:
                await event.answer(strings.im_back, keyboard=keyboard.vopros_8_p_menu.get_keyboard())
            users[event.from_id].chatstate -= 1





if __name__ == '__main__':
    bot.run_forever()