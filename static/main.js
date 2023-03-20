$(document).ready(function() {
    const $chatForm = $("#chat-form");
    const $chatMessages = $("#chat-messages");
    const $userInput = $("#user-input");

    $chatForm.submit(function(event) {
      event.preventDefault();
      const user_input = $userInput.val();
      if (!user_input.trim()) return;
      $chatMessages.append(`<li class="user-message"><span class="message-text right">${user_input}</span></li>`);
      $userInput.val("");
      $.post("/ask", {"text": user_input}, function(response) {
        $chatMessages.append(`<li class="bot-message"><span class="message-text left">${response}</span></li>`);
        // Scroll to the last message
        $chatMessages.scrollTop($chatMessages.prop("scrollHeight"));
      });
    });

    // Focus the input field on page load
    $userInput.focus();
  });
    // clear the chat messages
    function reset() {
        document.getElementById("user-input").value = "";
        document.getElementById("chat-messages").innerHTML = "";
    };