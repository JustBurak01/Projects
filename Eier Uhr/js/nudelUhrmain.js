let alarm = new Audio("alarm.wav");
            let timerStarted = false;


            function startTimer() {
                if (!timerStarted) {
                let startTime = new Date().getTime();
                let fiveMinutes = 1000 * 60 * 10;
                let endTime = startTime + fiveMinutes;


                setInterval(function() {
                     let timeLeft = endTime - new Date().getTime();

                     if(timeLeft> 0) {

                     let minutes = timeLeft / (1000 * 60);
                     minutes = Math.floor(minutes);
                     let seconds = (timeLeft / 1000) % 60;
                     seconds = Math.round(seconds);
                     seconds = ("0" + seconds).slice(-2); 
                     let text = "0" + minutes + " : " + seconds;
                     timer.innerHTML = text;
                     } else {
                         alarm.play();
                        timer.innerHTML = "00 : 00";
                     }
                }, 1000);
                timerStarted = true;
            }
            }


let toggleNavStatus = false;

let toggleNav = function() {
    let getSidebar = document.querySelector(".nav-sidebar");
    let getSidebarUl = document.querySelector(".nav-sidebar ul");
    let getSidebarTitle = document.querySelector(".nav-sidebar span");
    let getSidebarLinks = document.querySelectorAll(".nav-sidebar a");

    if(toggleNavStatus === false) {
        getSidebarUl.style.visibility = "visible";
        getSidebar.style.width = "272px";
        getSidebarTitle.style.opacity = "0.5";

        let arrayLength  =getSidebarLinks.length;
        for (let i = 0; i < arrayLength; i++) {
         getSidebarLinks[i].style.opacity = "1";
        }
    
        toggleNavStatus = true;
    }

    
    else if(toggleNavStatus === true) {
        getSidebar.style.width = "50px";
        getSidebarTitle.style.opacity = "0";

        let arrayLength  =getSidebarLinks.length;
        for (let i = 0; i < arrayLength; i++) {
            getSidebarLinks[i].style.opacity = "0";
        }

        getSidebarUl.style.visibility = "hidden";
    
        toggleNavStatus = false;
    }
}