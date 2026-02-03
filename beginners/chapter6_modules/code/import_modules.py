def list_llms() -> None:
    """
        This method returns list of llms
        :params :- None
        :return :- None
    """
    llms = ["chatgpt", "claude", "gemini", "llama"]

    for llm in llms:
        print(f"Model Name : {llm}")


if __name__ == "__main__":
    list_llms()