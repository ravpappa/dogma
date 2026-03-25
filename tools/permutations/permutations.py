from pyscript import window, document, when

# Find and manipulate DOM elements.

@when("click", "#btn-show")
def print_message(event):
    my_element = document.querySelector("#show-output")
    my_element.innerText = "Hello from Python!