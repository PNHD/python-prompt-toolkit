from prompt_toolkit.clipboard import InMemoryClipboard
from prompt_toolkit.enums import EditingMode
from prompt_toolkit.input.defaults import create_pipe_input
from prompt_toolkit.output import DummyOutput
from prompt_toolkit.shortcuts import PromptSession


def test_ctrl_y_yanks_text_killed_by_ctrl_u_in_vi_insert_mode():
    with create_pipe_input() as inp:
        inp.send_text("hello\x15\x19\r")
        session = PromptSession(
            input=inp,
            output=DummyOutput(),
            editing_mode=EditingMode.VI,
            clipboard=InMemoryClipboard(),
        )
        result = session.prompt()

    assert result == "hello"
