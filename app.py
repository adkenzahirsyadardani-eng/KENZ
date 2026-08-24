from flask import Flask, render_template_string, send_from_directory

app = Flask(__name__)

# -----------------------------
# Serve HTML Files
# -----------------------------
HTML = r"""
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>KENZ友 | Linktree</title>

<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Exo+2:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">

<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --primary: #ff3030;
    --primary-dark: #a80000;
    --orange: #ff9d00;
    --background: #050509;
    --text: #fff;
    --muted: #aaaac0;
}

html {
    scroll-behavior: smooth;
}

body {
    min-height: 100vh;
    background: var(--background);
    color: var(--text);
    font-family: 'Exo 2', sans-serif;
    overflow-x: hidden;
}


/* =========================================================
   BACKGROUND
========================================================= */

.background {
    position: fixed;
    inset: 0;
    z-index: -10;
    overflow: hidden;

    background:
        radial-gradient(
            circle at 20% 20%,
            rgba(255,40,40,.20),
            transparent 30%
        ),
        radial-gradient(
            circle at 80% 70%,
            rgba(255,150,0,.15),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #050509,
            #11111d,
            #08080e
        );
}

.orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(70px);
    opacity: .45;
    animation: floatOrb 12s ease-in-out infinite alternate;
}

.orb.one {
    width: 250px;
    height: 250px;
    background: #ff2020;
    top: 5%;
    left: -100px;
}

.orb.two {
    width: 300px;
    height: 300px;
    background: #ff8800;
    right: -120px;
    bottom: 10%;
    animation-delay: 2s;
}

.orb.three {
    width: 180px;
    height: 180px;
    background: #8b0000;
    left: 40%;
    top: 45%;
    animation-delay: 4s;
}

@keyframes floatOrb {
    from {
        transform: translate(0,0) scale(1);
    }

    to {
        transform: translate(60px,-40px) scale(1.15);
    }
}


/* =========================================================
   PARTICLES
========================================================= */

.particles {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: -5;
}

.particle {
    position: absolute;
    width: 3px;
    height: 3px;
    border-radius: 50%;
    background: #ff5555;
    box-shadow: 0 0 10px #ff3333;

    animation:
        particleMove linear infinite;
}

@keyframes particleMove {

    from {
        transform: translateY(110vh);
        opacity: 0;
    }

    15% {
        opacity: 1;
    }

    85% {
        opacity: 1;
    }

    to {
        transform: translateY(-20vh);
        opacity: 0;
    }
}


/* =========================================================
   ENTER SCREEN
========================================================= */

.enter-screen {
    position: fixed;
    inset: 0;

    z-index: 99999;

    display: flex;
    align-items: center;
    justify-content: center;

    flex-direction: column;

    background:
        radial-gradient(
            circle at center,
            rgba(255,30,30,.12),
            transparent 45%
        ),
        #050509;

    transition:
        opacity .8s ease,
        visibility .8s ease;
}

.enter-screen.hide {
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
}

.enter-logo {
    width: 100px;
    height: 100px;

    border-radius: 28px;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 40px;

    background:
        linear-gradient(
            135deg,
            var(--primary),
            var(--primary-dark)
        );

    box-shadow:
        0 0 30px rgba(255,30,30,.8),
        0 0 80px rgba(255,30,30,.3);

    animation:
        enterPulse 2s infinite;
}

@keyframes enterPulse {
    50% {
        transform: scale(1.08);

        box-shadow:
            0 0 45px rgba(255,30,30,.9),
            0 0 100px rgba(255,30,30,.4);
    }
}

.enter-title {
    margin-top: 25px;

    font-family: Orbitron;

    font-size: 25px;
    font-weight: 900;

    letter-spacing: 3px;

    background:
        linear-gradient(
            90deg,
            #fff,
            #ff3030,
            #ff9d00,
            #fff
        );

    background-size: 250%;

    -webkit-background-clip: text;
    color: transparent;

    animation:
        enterGradient 4s linear infinite;
}

@keyframes enterGradient {
    to {
        background-position: 250%;
    }
}

.enter-subtitle {
    margin-top: 10px;

    color: var(--muted);

    font-size: 13px;

    text-align: center;
}

.enter-button {
    margin-top: 30px;

    position: relative;

    min-width: 220px;

    padding: 16px 28px;

    border: 1px solid
        rgba(255,80,80,.7);

    border-radius: 15px;

    background:
        linear-gradient(
            135deg,
            rgba(255,40,40,.25),
            rgba(120,0,0,.25)
        );

    color: white;

    font-family: Orbitron;

    font-size: 13px;

    font-weight: 700;

    letter-spacing: 1px;

    cursor: pointer;

    overflow: hidden;

    box-shadow:
        0 0 25px rgba(255,30,30,.25);

    transition: .3s;
}

.enter-button:hover {
    transform:
        translateY(-3px)
        scale(1.03);

    box-shadow:
        0 0 35px rgba(255,30,30,.6);
}

.enter-button:active {
    transform: scale(.97);
}

.enter-button::before {
    content: "";

    position: absolute;

    inset: 0;

    background:
        linear-gradient(
            100deg,
            transparent,
            rgba(255,255,255,.2),
            transparent
        );

    transform:
        translateX(-120%);

    animation:
        buttonShine 2.5s infinite;
}

@keyframes buttonShine {
    50% {
        transform:
            translateX(120%);
    }
}


/* =========================================================
   MUSIC BUTTON
========================================================= */

.music-button {
    position: fixed;

    top: 18px;
    right: 18px;

    width: 48px;
    height: 48px;

    border-radius: 50%;

    border:
        1px solid
        rgba(255,255,255,.15);

    background:
        rgba(10,10,15,.7);

    backdrop-filter: blur(15px);

    color: white;

    display: flex;
    align-items: center;
    justify-content: center;

    cursor: pointer;

    z-index: 100;

    transition: .3s;

    box-shadow:
        0 0 20px rgba(255,40,40,.25);
}

.music-button:hover {
    transform: scale(1.08);

    border-color:
        var(--primary);

    box-shadow:
        0 0 25px rgba(255,40,40,.6);
}

.music-button.playing {
    animation:
        musicPulse 1.2s infinite;
}

@keyframes musicPulse {
    50% {
        box-shadow:
            0 0 10px var(--primary),
            0 0 30px rgba(255,40,40,.7);
    }
}


/* =========================================================
   MAIN
========================================================= */

.container {
    width: 100%;
    max-width: 620px;

    margin: auto;

    padding:
        65px 20px 40px;
}


/* =========================================================
   PROFILE
========================================================= */

.profile {
    text-align: center;

    animation:
        profileIn 1s ease both;
}

@keyframes profileIn {

    from {
        opacity: 0;

        transform:
            translateY(30px)
            scale(.95);
    }

    to {
        opacity: 1;

        transform:
            translateY(0)
            scale(1);
    }
}

.avatar-wrapper {
    width: 125px;
    height: 125px;

    margin: auto;

    padding: 4px;

    border-radius: 50%;

    background:
        linear-gradient(
            135deg,
            var(--primary),
            var(--orange),
            var(--primary)
        );

    box-shadow:
        0 0 20px rgba(255,40,40,.7),
        0 0 60px rgba(255,40,40,.2);

    animation:
        avatarGlow 3s infinite alternate;
}

.avatar {
    width: 100%;
    height: 100%;

    object-fit: cover;

    border-radius: 50%;

    border:
        4px solid #08080e;

    display: block;
}

@keyframes avatarGlow {
    to {
        transform:
            rotate(2deg)
            scale(1.03);
    }
}

.name {
    margin-top: 20px;

    font-family: Orbitron;

    font-size: 25px;

    font-weight: 900;

    background:
        linear-gradient(
            90deg,
            #ff3030,
            #ff9d00,
            #ff3030
        );

    background-size: 200%;

    -webkit-background-clip: text;

    color: transparent;

    animation:
        gradientMove 4s linear infinite;
}

@keyframes gradientMove {
    to {
        background-position: 200%;
    }
}

.username {
    margin-top: 5px;

    color: var(--muted);

    font-size: 14px;
}

.bio {
    max-width: 460px;

    margin: 12px auto 0;

    color: #d1d1df;

    line-height: 1.6;

    font-size: 14px;
}


/* =========================================================
   SOCIAL
========================================================= */

.socials {
    display: flex;

    justify-content: center;

    gap: 12px;

    margin:
        22px 0 28px;
}

.social {
    width: 43px;
    height: 43px;

    border-radius: 50%;

    display: flex;

    align-items: center;
    justify-content: center;

    text-decoration: none;

    color: white;

    background:
        rgba(255,255,255,.06);

    border:
        1px solid
        rgba(255,255,255,.12);

    backdrop-filter:
        blur(10px);

    transition: .3s;
}

.social:hover {
    transform:
        translateY(-5px)
        rotate(5deg);

    border-color:
        var(--primary);

    box-shadow:
        0 0 20px
        rgba(255,40,40,.5);
}


/* =========================================================
   LINKS
========================================================= */

.links {
    display: flex;

    flex-direction: column;

    gap: 15px;
}

.link {
    position: relative;

    min-height: 68px;

    display: flex;

    align-items: center;

    text-decoration: none;

    color: white;

    padding:
        12px 18px;

    border-radius: 17px;

    background:
        linear-gradient(
            135deg,
            rgba(30,30,42,.82),
            rgba(12,12,18,.82)
        );

    border:
        1px solid
        rgba(255,70,70,.25);

    backdrop-filter:
        blur(18px);

    box-shadow:
        0 8px 30px
        rgba(0,0,0,.25);

    overflow: hidden;

    opacity: 0;

    transform:
        translateY(25px);

    animation:
        linkIn .65s ease forwards;

    transition:
        transform .3s,
        border-color .3s,
        box-shadow .3s;
}

@keyframes linkIn {
    to {
        opacity: 1;

        transform:
            translateY(0);
    }
}

.link::before {
    content: "";

    position: absolute;

    inset: 0;

    background:
        linear-gradient(
            100deg,
            transparent 20%,
            rgba(255,255,255,.08) 50%,
            transparent 80%
        );

    transform:
        translateX(-120%);

    transition: .7s;
}

.link:hover::before {
    transform:
        translateX(120%);
}

.link:hover {
    transform:
        translateY(-4px)
        scale(1.015);

    border-color:
        rgba(255,60,60,.7);

    box-shadow:
        0 10px 30px
        rgba(255,30,30,.18),

        0 0 25px
        rgba(255,30,30,.15);
}

.link-icon {
    width: 44px;
    height: 44px;

    flex-shrink: 0;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 13px;

    background:
        linear-gradient(
            135deg,
            rgba(255,50,50,.25),
            rgba(255,150,0,.1)
        );

    border:
        1px solid
        rgba(255,70,70,.2);

    font-size: 20px;

    color: #ff6868;
}

.link-content {
    flex: 1;

    margin-left: 14px;
}

.link-title {
    font-family: Orbitron;

    font-size: 14px;

    font-weight: 700;
}

.link-description {
    color: var(--muted);

    font-size: 12px;

    margin-top: 3px;
}

.link-arrow {
    color: #777;

    font-size: 13px;

    transition: .3s;
}

.link:hover .link-arrow {
    color:
        var(--primary);

    transform:
        translateX(4px);
}


/* =========================================================
   FOOTER
========================================================= */

.footer {
    text-align: center;

    margin-top: 35px;

    color: #68687a;

    font-size: 11px;
}

.footer strong {
    color: #aaa;
}


/* =========================================================
   RIPPLE
========================================================= */

.ripple {
    position: fixed;

    border-radius: 50%;

    pointer-events: none;

    background:
        rgba(255,50,50,.35);

    transform: scale(0);

    animation:
        ripple .6s ease-out;

    z-index: 999999;
}

@keyframes ripple {
    to {
        transform: scale(5);

        opacity: 0;
    }
}


/* =========================================================
   MOBILE
========================================================= */

@media(max-width:480px) {

    .container {
        padding:
            65px 14px 30px;
    }

    .avatar-wrapper {
        width: 110px;
        height: 110px;
    }

    .name {
        font-size: 21px;
    }

    .bio {
        font-size: 13px;
    }

    .link {
        min-height: 64px;
    }

    .link-title {
        font-size: 13px;
    }

    .link-description {
        font-size: 11px;
    }

    .enter-title {
        font-size: 21px;
    }

}

</style>
</head>

<body>

<div class="background">

    <div class="orb one"></div>
    <div class="orb two"></div>
    <div class="orb three"></div>

</div>

<div
    class="particles"
    id="particles">
</div>


<!-- ========================================================
     ENTER SCREEN
========================================================= -->

<div
    class="enter-screen"
    id="enterScreen">

    <div class="enter-logo">
        <i class="fas fa-link"></i>
    </div>

    <div class="enter-title">
        KENZ友
    </div>

    <div class="enter-subtitle">
        Tap the button to enter my website
    </div>

    <button
        class="enter-button"
        id="enterButton">

        <i class="fas fa-door-open"></i>

        &nbsp; ENTER WEBSITE

    </button>

</div>


<!-- ========================================================
     MUSIC
========================================================= -->

<button
    class="music-button"
    id="musicButton">

    <i class="fas fa-volume-xmark"></i>

</button>


<audio
    id="backgroundMusic"
    loop
    preload="auto">

    <source
        id="musicSource"
        src=""
        type="audio/mpeg">

</audio>


<!-- ========================================================
     MAIN
========================================================= -->

<main class="container">

    <section class="profile">

        <div class="avatar-wrapper">

            <img
                id="avatar"
                class="avatar"
                src=""
                alt="Profile">

        </div>

        <h1
            class="name"
            id="profileName">
        </h1>

        <div
            class="username"
            id="username">
        </div>

        <p
            class="bio"
            id="bio">
        </p>

    </section>


    <div
        class="socials"
        id="socials">
    </div>


    <section
        class="links"
        id="links">
    </section>


    <footer class="footer">

        <div>

            ©
            <span id="year"></span>

            <strong id="footerName"></strong>

        </div>

        <div style="margin-top:5px">
            Powered by custom Linktree
        </div>

    </footer>

</main>


<script>

/* ==========================================================
   CONFIGURATION
========================================================== */

const CONFIG = {

    /* PROFILE */

    name: "KENZ友",

    username: "@tcpkenz",

    bio:
        "Developer • Free Fire • Tools • Digital Creator",


    /* FOTO PROFIL */

    avatar:
        "./kenz.jpg",


    /* MUSIK */

    music:
        "./music.mp3",


    /* SOCIAL MEDIA */

    socials: [

        {
            icon: "fab fa-tiktok",

            url:
                "https://www.tiktok.com/@tcpkenz?_r=1&_t=ZS-997GWkuEBAg"
        },

        {
            icon: "fab fa-whatsapp",

            url:
                "https://wa.me/6285733276093"
        }

    ],


    /* LINK BUTTON */

    links: [

        {
            title: "BOT TCP OB54",

            description: "Download KENZ Tools & Files",

            icon: "fas fa-robot",

            url: "https://www.mediafire.com/file/cfurd88c4h2o16x/KENZ-TCP.zip/file"
        },

        {
            title: "Bio Update",

            description: "Custom Bio Editor",

            icon: "fas fa-pen",

            url: "https://bio-sable-rho.vercel.app/"
        },

        {
            title:
                "Item Default Profile",

            description:
                "Free Fire Profile API • Developer Tools",

            icon:
                "fas fa-screwdriver-wrench",

            url:
                "https://item-zeta.vercel.app/"
        },

        {
            title:
                "Friend Manager",

            description:
                "Open my Free Fire Friend Manager",

            icon:
                "fas fa-users",

            url:
                "https://friend-web-livid.vercel.app/"
        },


        {
            title:
                "TikTok",

            description:
                "Follow me on TikTok",

            icon:
                "fab fa-tiktok",

            url:
                "https://www.tiktok.com/@tcpkenz?_r=1&_t=ZS-997GWkuEBAg"
        },


        {
            title:
                "WhatsApp",

            description:
                "Contact me via WhatsApp",

            icon:
                "fab fa-whatsapp",

            url:
                "https://wa.me/6285733276093"
        }

    ]

};


/* ==========================================================
   ELEMENTS
========================================================== */

const enterScreen =
    document.getElementById("enterScreen");

const enterButton =
    document.getElementById("enterButton");

const music =
    document.getElementById("backgroundMusic");

const musicButton =
    document.getElementById("musicButton");


/* ==========================================================
   INITIALIZATION
========================================================== */

document.addEventListener(
    "DOMContentLoaded",
    () => {

        loadProfile();

        createParticles();

        document.getElementById("year")
            .textContent =
            new Date().getFullYear();

    }
);


/* ==========================================================
   LOAD PROFILE
========================================================== */

function loadProfile() {

    document.getElementById("avatar")
        .src =
        CONFIG.avatar;

    document.getElementById("profileName")
        .textContent =
        CONFIG.name;

    document.getElementById("username")
        .textContent =
        CONFIG.username;

    document.getElementById("bio")
        .textContent =
        CONFIG.bio;

    document.getElementById("footerName")
        .textContent =
        CONFIG.name;


    /* MUSIC */

    if (CONFIG.music) {

        document.getElementById("musicSource")
            .src =
            CONFIG.music;

        music.load();

    }
    else {

        musicButton.style.display =
            "none";

    }


    /* SOCIAL */

    const socials =
        document.getElementById("socials");

    CONFIG.socials.forEach(
        item => {

            const a =
                document.createElement("a");

            a.className =
                "social";

            a.href =
                item.url;

            a.target =
                "_blank";

            a.rel =
                "noopener noreferrer";

            a.innerHTML =
                `<i class="${item.icon}"></i>`;

            socials.appendChild(a);

        }
    );


    /* LINKS */

    const links =
        document.getElementById("links");

    CONFIG.links.forEach(
        (item,index) => {

            const a =
                document.createElement("a");

            a.className =
                "link";

            a.href =
                item.url;

            a.target =
                "_blank";

            a.rel =
                "noopener noreferrer";

            a.style.animationDelay =
                `${index * 100 + 300}ms`;

            a.innerHTML = `

                <div class="link-icon">

                    <i
                        class="${item.icon}">
                    </i>

                </div>

                <div class="link-content">

                    <div class="link-title">

                        ${item.title}

                    </div>

                    <div
                        class="link-description">

                        ${item.description || ""}

                    </div>

                </div>

                <div class="link-arrow">

                    <i
                        class="fas fa-chevron-right">
                    </i>

                </div>

            `;

            links.appendChild(a);

        }
    );

}


/* ==========================================================
   ENTER WEBSITE + START MUSIC
========================================================== */

enterButton.addEventListener(
    "click",
    async () => {

        if (CONFIG.music) {

            try {

                await music.play();

                musicButton
                    .classList
                    .add("playing");

                musicButton.innerHTML =
                    `<i class="fas fa-volume-high"></i>`;

            }

            catch(error) {

                console.log(
                    "Audio tidak dapat diputar:",
                    error
                );

            }

        }


        enterScreen.classList.add(
            "hide"
        );

        document.body.style.overflow =
            "auto";

    }
);


/* ==========================================================
   MUSIC BUTTON
========================================================== */

musicButton.addEventListener(
    "click",
    async () => {

        try {

            if (music.paused) {

                await music.play();

                musicButton
                    .classList
                    .add("playing");

                musicButton.innerHTML =
                    `<i class="fas fa-volume-high"></i>`;

            }

            else {

                music.pause();

                musicButton
                    .classList
                    .remove("playing");

                musicButton.innerHTML =
                    `<i class="fas fa-volume-xmark"></i>`;

            }

        }

        catch(error) {

            console.log(error);

        }

    }
);


/* ==========================================================
   PARTICLES
========================================================== */

function createParticles() {

    const container =
        document.getElementById(
            "particles"
        );

    for (
        let i = 0;
        i < 35;
        i++
    ) {

        const particle =
            document.createElement("div");

        particle.className =
            "particle";

        particle.style.left =
            Math.random() * 100 + "%";

        particle.style.animationDuration =
            (
                7 +
                Math.random() * 12
            ) + "s";

        particle.style.animationDelay =
            Math.random() * 10 + "s";

        const size =
            1 +
            Math.random() * 3;

        particle.style.width =
            size + "px";

        particle.style.height =
            size + "px";

        container.appendChild(
            particle
        );

    }

}


/* ==========================================================
   RIPPLE EFFECT
========================================================== */

document.addEventListener(
    "click",
    e => {

        const ripple =
            document.createElement(
                "div"
            );

        ripple.className =
            "ripple";

        const size = 20;

        ripple.style.width =
            size + "px";

        ripple.style.height =
            size + "px";

        ripple.style.left =
            (
                e.clientX -
                size / 2
            ) + "px";

        ripple.style.top =
            (
                e.clientY -
                size / 2
            ) + "px";

        document.body.appendChild(
            ripple
        );

        setTimeout(
            () => {

                ripple.remove();

            },
            600
        );

    }
);


/* ==========================================================
   IMAGE FALLBACK
========================================================== */

document.getElementById("avatar")
    .addEventListener(
        "error",
        function() {

            this.src =
                "https://placehold.co/500x500/111111/ffffff?text=KENZ";

        }
    );


</script>

</body>
</html>
"""

@app.route('/')
def serve_index():
    return render_template_string(HTML)


# -----------------------------
# Serve Local Files
# -----------------------------

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)


# -----------------------------
# Run Server
# -----------------------------

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000
    )