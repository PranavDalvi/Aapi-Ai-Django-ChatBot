"use strict";
const fadeIn_fadeOut_transition_speed = 300;


// Function to prevent refresh
let form = document.querySelector("#myForm");
function handleForm(event) { event.preventDefault(); } 
form.addEventListener('submit', handleForm);

function showBotFun(){
    // Initialize Variables
    const chatBotWindow =  document.getElementById("botWindow");

    //Main Logic to show chatBot
    chatBotWindow.style.opacity=0;
    chatBotWindow.style.transform=`translateY(10%)`;
    document.querySelector(".container").classList.remove("hidden");

    //Pausing the flow of the code for 0.3 secs
    setTimeout(() => {
        chatBotWindow.style.transform=`translateY(0%)`;
        chatBotWindow.style.opacity=1;
    }, fadeIn_fadeOut_transition_speed);

    //Main Logic to hide Chat button
    const showBot = document.getElementById("showBotbtn");
    showBot.style.opacity=0;

    //Pausing the flow of the code for 0.3 secs
    setTimeout(() => {
        document.querySelector(".showBot").classList.add("hidden");
    }, fadeIn_fadeOut_transition_speed);

}

function hideBotFun(){
    // Initialize Variables
    const showBot = document.getElementById("showBotbtn");

    //Main Logic to show Chat button
    showBot.style.opacity=0;

    //Pausing the flow of the code for 0.3 secs
    document.querySelector(".showBot").classList.remove("hidden");
    setTimeout(() => {
            showBot.style.opacity=1;
    }, fadeIn_fadeOut_transition_speed);

    //Main Logic to hide chat bot
    const chatBotWindow =  document.getElementById("botWindow");
    chatBotWindow.style.transform=`translateY(11%)`;
    chatBotWindow.style.opacity=0;
    
    //Pausing the flow of the code for 0.3 secs
    setTimeout(() => {
        document.querySelector(".container").classList.add("hidden");
    }, fadeIn_fadeOut_transition_speed);


}


