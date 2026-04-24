<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>John Mziray | AI & ML Developer</title>
    
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
    
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.15.1/devicon.min.css">
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        :root {
            --bg-color: #0d1117;
            --surface-color: rgba(22, 27, 34, 0.8);
            --accent-color: #58a6ff;
            --python-color: #3572A5;
            --jupyter-color: #DA5B0B;
            --text-main: #c9d1d9;
            --text-muted: #8b949e;
        }

        body {
            margin: 0;
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            line-height: 1.6;
            scroll-behavior: smooth;
            overflow-x: hidden;
        }

        /* Particle Background Container */
        #particles-js {
            position: fixed;
            width: 100vw;
            height: 100vh;
            top: 0;
            left: 0;
            z-index: -1;
        }

        /* Navigation */
        header {
            position: sticky;
            top: 0;
            background-color: rgba(13, 17, 23, 0.85);
            backdrop-filter: blur(10px);
            padding: 20px 10%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #30363d;
            z-index: 100;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--accent-color);
        }

        nav a {
            color: var(--text-main);
            text-decoration: none;
            margin-left: 30px;
            font-weight: 600;
            transition: color 0.3s;
        }

        nav a:hover {
            color: var(--accent-color);
        }

        /* Hero Section */
        .hero {
            padding: 120px 10% 80px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 50px;
            max-width: 1200px;
            margin: 0 auto;
        }

        .hero-content {
            flex: 1.2;
        }

        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 15px;
            line-height: 1.2;
            color: #ffffff;
        }

        .hero span {
            color: var(--accent-color);
        }

        /* Typing Effect Styles */
        .typing-container {
            font-size: 1.4rem;
            color: var(--accent-color);
            font-weight: 600;
            margin-bottom: 20px;
            height: 30px;
        }

        .cursor {
            display: inline-block;
            width: 3px;
            height: 1.2em;
            background-color: var(--accent-color);
            vertical-align: middle;
            animation: blink 0.8s infinite;
        }

        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0; }
        }

        .hero p {
            font-size: 1.15rem;
            color: var(--text-muted);
            margin-bottom: 40px;
            max-width: 650px;
        }

        /* Avatar Image */
        .hero-image {
            flex: 0.8;
            display: flex;
            justify-content: center;
        }

        .hero-image img {
            width: 100%;
            max-width: 350px;
            border-radius: 50%;
            border: 4px solid #30363d;
            box-shadow: 0 0 30px rgba(88, 166, 255, 0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .hero-image img:hover {
            transform: scale(1.05);
            box-shadow: 0 0 50px rgba(88, 166, 255, 0.4);
        }

        /* Buttons */
        .btn-group {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }

        .btn {
            background-color: #238636;
            color: #ffffff;
            padding: 15px 30px;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 800;
            transition: all 0.3s ease;
            display: inline-block;
            border: none;
            cursor: pointer;
            font-family: inherit;
            font-size: 1rem;
        }

        .btn:hover {
            background-color: #2ea043;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(35, 134, 54, 0.4);
        }

        .btn-outline {
            background-color: transparent;
            border: 2px solid var(--accent-color);
            color: var(--accent-color);
        }

        .btn-outline:hover {
            background-color: rgba(88, 166, 255, 0.1);
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(88, 166, 255, 0.2);
        }

        /* Sections General */
        section {
            padding: 80px 10%;
            max-width: 1200px;
            margin: 0 auto;
        }

        h2.section-title {
            font-size: 2.2rem;
            margin-bottom: 40px;
            border-bottom: 1px solid #30363d;
            padding-bottom: 15px;
            color: #ffffff;
        }

        /* Skills Layout */
        .skills-container {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }

        .skill-tag {
            background-color: var(--surface-color);
            padding: 12px 24px;
            border-radius: 30px;
            font-weight: 600;
            color: var(--text-main);
            border: 1px solid #30363d;
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 1rem;
            backdrop-filter: blur(5px);
            transition: border-color 0.3s, transform 0.3s;
        }
        
        .skill-tag:hover {
            border-color: var(--accent-color);
            transform: translateY(-3px);
        }

        .skill-tag i {
            font-size: 1.2rem;
            color: var(--accent-color); /* Makes FontAwesome icons pop */
        }
        
        .skill-tag i.colored {
            color: inherit; /* Keeps Devicon original colors */
        }

        /* Project Grid */
        .project-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 30px;
        }

        .project-card {
            background-color: var(--surface-color);
            border: 1px solid #30363d;
            border-radius: 12px;
            padding: 30px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            backdrop-filter: blur(5px);
            transform-style: preserve-3d;
        }

        .project-card h3 {
            margin-top: 0;
            font-size: 1.4rem;
            color: var(--accent-color);
            transform: translateZ(30px);
        }

        .project-card p {
            color: var(--text-muted);
            font-size: 0.95rem;
            transform: translateZ(20px);
        }

        .tech-label {
            display: inline-block;
            margin-top: 15px;
            font-size: 0.85rem;
            font-weight: 600;
            transform: translateZ(20px);
        }

        .tech-label::before {
            content: "●";
            margin-right: 5px;
        }

        .python-tag { color: var(--python-color); }
        .jupyter-tag { color: var(--jupyter-color); }

        .project-links {
            margin-top: 25px;
            transform: translateZ(30px);
        }

        .project-links a {
            color: #ffffff;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
        }

        .project-links a:hover {
            color: var(--accent-color);
        }

        /* Contact Form Styles */
        .contact-form {
            max-width: 600px;
            margin: 0 auto;
            background-color: var(--surface-color);
            padding: 40px;
            border-radius: 12px;
            border: 1px solid #30363d;
            backdrop-filter: blur(5px);
        }

        .form-group {
            margin-bottom: 20px;
            text-align: left;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #ffffff;
        }

        .form-group input, .form-group textarea {
            width: 100%;
            padding: 12px;
            border-radius: 6px;
            border: 1px solid #30363d;
            background-color: var(--bg-color);
            color: #ffffff;
            font-family: inherit;
            font-size: 1rem;
            box-sizing: border-box;
        }

        .form-group input:focus, .form-group textarea:focus {
            outline: none;
            border-color: var(--accent-color);
            box-shadow: 0 0 0 2px rgba(88, 166, 255, 0.2);
        }

        .form-group textarea {
            resize: vertical;
            min-height: 120px;
        }

        /* Social Links in Footer */
        .social-links {
            display: flex;
            justify-content: center;
            gap: 25px;
            margin-top: 40px;
            flex-wrap: wrap;
        }

        .social-links a {
            color: var(--text-main);
            text-decoration: none;
            font-size: 1.1rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: color 0.3s, transform 0.3s;
        }

        .social-links a:hover {
            color: var(--accent-color);
            transform: translateY(-2px);
        }

        .social-links i {
            font-size: 1.4rem;
        }

        /* Footer */
        footer {
            text-align: center;
            padding: 80px 10% 40px;
            color: var(--text-muted);
        }

        /* Scroll Reveal Animations */
        .hidden {
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.8s ease-out;
        }
        .show {
            opacity: 1;
            transform: translateY(0);
        }

        /* Mobile Responsiveness */
        @media (max-width: 850px) {
            .hero {
                flex-direction: column-reverse;
                text-align: center;
                padding-top: 80px;
            }
            .hero-image img {
                max-width: 250px;
                margin-bottom: 20px;
            }
            .btn-group {
                justify-content: center;
            }
            .typing-container {
                font-size: 1.1rem;
            }
            .social-links {
                gap: 15px;
            }
        }
    </style>
</head>
<body>

    <div id="particles-js"></div>

    <header>
        <div class="logo">John Mziray</div>
        <nav>
            <a href="#about">About</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </nav>
    </header>

    <section class="hero" id="about">
        <div class="hero-content hidden">
            <h1>Hi there, I'm <span>John Mziray</span></h1>
            
            <div class="typing-container">
                I specialize in <span id="typed-text"></span><span class="cursor"></span>
            </div>

            <p>I am a Software Developer based in Tanzania, currently pursuing a BSc in Artificial Intelligence & Machine Learning at the University of Limerick. I am passionate about building real-world software, with a strong technical focus on Data Analysis and intelligent systems.</p>
            
            <div class="btn-group">
                <a href="https://github.com/jemmziray-tech" target="_blank" class="btn"><i class="fa-brands fa-github"></i> Visit My GitHub</a>
                <a href="resume.pdf" target="_blank" class="btn btn-outline"><i class="fa-solid fa-file-pdf"></i> Download Resume</a>
            </div>
        </div>

        <div class="hero-image hidden">
            <img src="https://github.com/jemmziray-tech.png" alt="John Mziray">
        </div>
    </section>

    <section id="skills">
        <h2 class="section-title hidden">My Tech Stack</h2>
        <div class="skills-container hidden">
            <div class="skill-tag"><i class="devicon-python-plain colored"></i> Python</div>
            <div class="skill-tag"><i class="devicon-opencv-plain colored"></i> OpenCV</div>
            <div class="skill-tag"><i class="devicon-jupyter-plain colored"></i> Jupyter Notebooks</div>
            <div class="skill-tag"><i class="fa-solid fa-network-wired"></i> Machine Learning</div>
            <div class="skill-tag"><i class="fa-solid fa-brain"></i> Generative AI & NLP</div>
            <div class="skill-tag"><i class="fa-solid fa-chart-column"></i> Data Analysis</div>
        </div>
    </section>

    <section id="projects">
        <h2 class="section-title hidden">Featured Projects</h2>
        <div class="project-grid">
            
            <div class="project-card hidden" data-tilt data-tilt-max="10" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.2">
                <div>
                    <h3>FaceLogTZ</h3>
                    <p>An offline-first, locally hosted Smart Attendance System optimized for local African environments. It utilizes deep learning facial encodings to dynamically identify individuals under changing lighting conditions.</p>
                    <span class="tech-label python-tag">Python</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/jemmziray-tech/FaceLogTZ" target="_blank">View Repository &rarr;</a>
                </div>
            </div>

            <div class="project-card hidden" data-tilt data-tilt-max="10" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.2">
                <div>
                    <h3>Atmos-Live-API</h3>
                    <p>A dynamic real-time weather tracking application that integrates live external APIs to process meteorological data and deliver accurate, location-based information.</p>
                    <span class="tech-label python-tag">Python</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/jemmziray-tech/Atmos-Live-API" target="_blank">View Repository &rarr;</a>
                </div>
            </div>

            <div class="project-card hidden" data-tilt data-tilt-max="10" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.2">
                <div>
                    <h3>Netflix Movies Analysis</h3>
                    <p>A deep dive into Netflix's movie catalog using data analysis techniques to uncover trends, patterns, and insights through structured data manipulation.</p>
                    <span class="tech-label jupyter-tag">Jupyter Notebook</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/jemmziray-tech/netflix_movies_analysis" target="_blank">View Repository &rarr;</a>
                </div>
            </div>

            <div class="project-card hidden" data-tilt data-tilt-max="10" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.2">
                <div>
                    <h3>Dar Traffic Project</h3>
                    <p>A data-centric project focused on analyzing and understanding traffic patterns, building towards smarter local infrastructure solutions.</p>
                    <span class="tech-label python-tag">Python</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/jemmziray-tech/Dar_Traffic_Project" target="_blank">View Repository &rarr;</a>
                </div>
            </div>

        </div>
    </section>

    <footer id="contact">
        <h2 class="section-title hidden" style="border:none; text-align:center;">Let's Connect</h2>
        
        <div class="contact-form hidden">
            <form action="https://formsubmit.co/jem.mziray@gmail.com" method="POST">
                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="text" id="name" name="name" required placeholder="John Doe">
                </div>
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" required placeholder="john@example.com">
                </div>
                <div class="form-group">
                    <label for="message">Message</label>
                    <textarea id="message" name="message" required placeholder="Let's talk about AI..."></textarea>
                </div>
                <input type="hidden" name="_captcha" value="false">
                <button type="submit" class="btn" style="width: 100%;"><i class="fa-solid fa-paper-plane"></i> Send Message</button>
            </form>
        </div>

        <div class="social-links hidden">
            <a href="https://github.com/jemmziray-tech" target="_blank" title="GitHub">
                <i class="fa-brands fa-github"></i> GitHub
            </a>
            <a href="https://www.linkedin.com/in/john-mziray-4a0b88392" target="_blank" title="LinkedIn">
                <i class="fa-brands fa-linkedin"></i> LinkedIn
            </a>
            <a href="https://wa.me/255743924467" target="_blank" title="WhatsApp">
                <i class="fa-brands fa-whatsapp"></i> WhatsApp
            </a>
            <a href="mailto:jem.mziray@gmail.com" title="Email">
                <i class="fa-solid fa-envelope"></i> Email
            </a>
        </div>

        <br><br>
        <p>&copy; 2026 John Mziray. Engineered with Precision.</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vanilla-tilt/1.8.1/vanilla-tilt.min.js"></script>

    <script>
        // --- Particle Background Configuration ---
        particlesJS("particles-js", {
            "particles": {
                "number": { "value": 60, "density": { "enable": true, "value_area": 800 } },
                "color": { "value": "#58a6ff" },
                "shape": { "type": "circle" },
                "opacity": { "value": 0.3, "random": false },
                "size": { "value": 3, "random": true },
                "line_linked": {
                    "enable": true,
                    "distance": 150,
                    "color": "#58a6ff",
                    "opacity": 0.2,
                    "width": 1
                },
                "move": { "enable": true, "speed": 1.5, "direction": "none", "out_mode": "out" }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": {
                    "onhover": { "enable": true, "mode": "grab" },
                    "onclick": { "enable": true, "mode": "push" },
                    "resize": true
                },
                "modes": {
                    "grab": { "distance": 140, "line_linked": { "opacity": 0.8 } },
                    "push": { "particles_nb": 4 }
                }
            },
            "retina_detect": true
        });

        // --- Typing Effect Logic ---
        const phrases = ["Computer Vision.", "Natural Language Processing.", "Generative AI.", "Machine Learning."];
        let currentPhraseIndex = 0;
        let isDeleting = false;
        let text = '';
        let typingSpeed = 100;

        function type() {
            const currentPhrase = phrases[currentPhraseIndex];
            
            if (isDeleting) {
                text = currentPhrase.substring(0, text.length - 1);
                typingSpeed = 50; 
            } else {
                text = currentPhrase.substring(0, text.length + 1);
                typingSpeed = 100; 
            }

            document.getElementById('typed-text').innerHTML = text;

            if (!isDeleting && text === currentPhrase) {
                typingSpeed = 2000; 
                isDeleting = true;
            } else if (isDeleting && text === '') {
                isDeleting = false;
                currentPhraseIndex = (currentPhraseIndex + 1) % phrases.length;
                typingSpeed = 500; 
            }

            setTimeout(type, typingSpeed);
        }
        
        document.addEventListener("DOMContentLoaded", type);

        // --- Scroll Reveal Animations ---
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('show');
                }
            });
        }, { threshold: 0.1 });

        const hiddenElements = document.querySelectorAll('.hidden');
        hiddenElements.forEach((el) => observer.observe(el));
    </script>

</body>
</html>
