import gradio as gr

from quiz_data import QUIZ_QUESTIONS


def generate_question_texts():
    return [question["question"] for question in QUIZ_QUESTIONS]


def find_question_index(selected_question):
    for index, question in enumerate(QUIZ_QUESTIONS):
        if question["question"] == selected_question:
            return index

    return None


def quiz_interface(selected_question):
    question_index = find_question_index(selected_question)

    if question_index is None:
        return (
            gr.Textbox(value=None),
            gr.Radio(choices=[], value=None),
            gr.Textbox(value=""),
        )

    question = QUIZ_QUESTIONS[question_index]
    return (
        gr.Textbox(value=question["question"]),
        gr.Radio(
            choices=question["options"],
            value=None,
        ),
        gr.Textbox(value=""),
    )


def check_answer(selected_question, selected_option):
    if not selected_question or not selected_option:
        return "Please select a question and an answer first."

    question_index = find_question_index(selected_question)

    if question_index is None:
        return "Please select a question and an answer first."

    question = QUIZ_QUESTIONS[question_index]

    if selected_option == question["answer"]:
        return "Correct! 🎉"
    else:
        return f"Not quite. {question['explanation']}"


def build_quiz_app():
    question_texts = generate_question_texts()

    with gr.Blocks() as demo:
        gr.Markdown("# 🐍 Python Foundations Quiz\nChoose a question and test the basics.")

        question_selector = gr.Dropdown(
            choices=question_texts,
            label="Select a question",
            value=None,
        )
        question_display = gr.Textbox(
            label="Question",
            interactive=False,
        )
        answer_options = gr.Radio(
            choices=[],
            label="Choose an answer",
        )
        check_button = gr.Button("Check Answer")
        feedback_display = gr.Textbox(
            label="Feedback",
            interactive=False,
        )

        question_selector.change(
            fn=quiz_interface,
            inputs=question_selector,
            outputs=[question_display, answer_options, feedback_display],
        )
        check_button.click(
            fn=check_answer,
            inputs=[question_selector, answer_options],
            outputs=feedback_display,
        )

    return demo


if __name__ == "__main__":
    demo = build_quiz_app()
    demo.launch()
