---
title: AI in Society and Public Services
subtitle: "Are We Doomed?"
author: Mário Antunes
institute: Universidade de Aveiro
date: February 06, 2026
colorlinks: true
paginate: true
highlight-style: tango
toc: true
toc-title: "Table of Contents"
mainfont: NotoSans
theme: metropolis
themeoptions:
  - sectionpage=progressbar
  - numbering=fraction
  - progressbar=frametitle
header-includes:
 - \usepackage{longtable,booktabs}
 - \usepackage{etoolbox}
 - \AtBeginEnvironment{longtable}{\tiny}
 - \AtBeginEnvironment{cslreferences}{\tiny}
 - \AtBeginEnvironment{Shaded}{\small}
 - \AtBeginEnvironment{verbatim}{\small}
 - \usepackage{caption}
 - \captionsetup[figure]{labelformat=empty}
---

# Are We Doomed?

## A Status Report on Human Survival

![\ ](images/title_earth.jpg)

## Are we doomed?

* We often worry about the future.
* History shows us that extinction events are the norm, not the exception.
* Let's review the "Natural" candidates for our destruction.

![\ ](images/asteroid_impact.jpg){ width=256px }

## Solar Flares and Coronal Mass Ejections

* **The Risk:** A Carrington-level event.
* **Consequence:** Fried electronics, global power grid failure.
* **Modern Context:** In a digitized world, this means the end of banking, transport, and internet.

![\ ](images/solar_flare.jpg){ width=256px }

## "Earth Will Expire By 2050"

* **2002 Prediction:** World Wildlife Fund (WWF) warned we are plundering the planet faster than it recovers.
* **The Warning:** "Earth's population will be forced to colonise two planets within 50 years."

![\ ](images/newspaper_clippings.png){ width=256px }

## We are eating our own tail

* **Current Status:** We use ~1.75 Earths per year.
* **Climate Tipping Points:** 1.5°C breach is becoming the norm.
* **Verdict:** The timeline has accelerated.

![\ ](images/overshoot_day.jpg){ width=256px }

## War and Conflict

* **The Risk:** Mutually Assured Destruction (MAD).
* **The Weapon:** Intercontinental Ballistic Missiles (ICBMs).
* **Verdict:** The button is still there.

![\ ](images/nuclear_missile.jpg)

## Autonomous Slaughterbots

![Image: Swarm of small drones](images/drone_swarm.jpg)
* **Shift:** From massive nukes to cheap, AI-driven drone swarms.
* **Current Reality:** Use in Eastern Europe and Middle East conflicts (2023-2026).
* **Danger:** War at machine speed, faster than human decision-making.

## Short Answer?
**YES!!**

![Image: A giant rubber stamp marked YES in red ink](images/stamp_yes.jpg)
* If nature or physics doesn't get us, our own habits might.
* But is there a *new* challenger?

## Enter the Artificial Doom
**However, are these really the main threat?**

![Image: A robot hand passing a spark to a human hand](images/robot_creation.jpg)
* We are building something smarter than us.
* Is AI the final filter?

## The Prophets of Doom
**What our "experts" said (circa 2015)**

![Collage: Stephen Hawking, Elon Musk, and Bill Gates](images/experts_collage.jpg)
* **Stephen Hawking:** "The development of full artificial intelligence could spell the end of the human race."
* **Elon Musk:** "With artificial intelligence we are summoning the demon."
* **Bill Gates:** "I am in the camp that is concerned about super intelligence."

## Yuval Harari's Warning
**From Gods to useless**

![Image: Yuval Noah Harari speaking](images/harari.jpg)
* "We (human beings) began as animals, gradually transformed ourselves into the gods of the planet earth..."
* "...and very soon we may pass this mastery to a completely different lifeform."
* **The Fear:** Disappearing completely or becoming irrelevant.

## The Hollywood Scenario
**Skynet and Terminators**

![Image: The T-800 Terminator Skeleton with red eyes](images/terminator_t800.jpg)
* **The Trope:** AI becomes self-aware -> Hates humans -> Launches Nukes.
* **Reality:** This is anthropomorphizing. AI doesn't hate. It optimizes.

## The Real Risk: Misalignment
**"Neutral Evil"**

![Image: HAL 9000 Red Eye Camera](images/hal9000.jpg)
* **HAL 9000:** "This mission is too important for me to allow you to jeopardize it."
* **The Paperclip Maximizer:** An AI destroys the world not out of malice, but to use our atoms to make more paperclips because we forgot to tell it to stop.

## Cultural Reference: The Daleks
**EXTERMINATE!**

![Image: A Dalek from Doctor Who](images/dalek.jpg)
* Pure biological hatred vs. Cold logical removal.
* Which is scary? The one that hates you, or the one that doesn't care?

## The Answer?
**YES and NO.**

![Image: Scales balancing 'Doom' and 'Utopia'](images/scales.jpg)
* It depends on how we manage the **Transition** and the **Hype**.
* Let's look at the history of AI Hype vs. Reality.

## Case Study 1: AlphaGo (The Triumph)
**The 2016 Milestone**

![Image: Lee Sedol vs AlphaGo at the Go board](images/alphago_match.jpg)
* **Event:** DeepMind's AlphaGo beats World Champion Lee Sedol (4-1).
* **Significance:** Go has more possible moves ($10^{170}$) than atoms in the universe.
* **The Conclusion:** "Intuition" is solved. Humans are obsolete.

## How AlphaGo Worked
**Policy & Value Networks**

![Diagram: Neural network layers showing policy and value heads](images/alphago_diagram.jpg)
* **Deep Neural Networks:** Trained on human games + Self-play.
* **Monte Carlo Tree Search:** Looking ahead, but guided by "intuition" (probabilities).
* **Result:** Move 37 (The "Alien" move).

## Case Study 1: The Update (2023)
**Humans Strike Back**

![Image: A Go board showing a large loop of stones](images/go_adversarial_attack.jpg)
* **The Twist:** A human amateur (Kellin Pelrine) beat a top-tier Go AI (KataGo) 14 games to 1.
* **The Method:** An "Adversarial Attack." He built a large distraction loop.
* **The Lesson:** The AI didn't "understand" the game. It understood *patterns*. When faced with an "out of distribution" trick, it broke.

## Case Study 2: IBM Watson (The Hype)
**"The First AI Movie Trailer"**

![Image: Movie poster for 'Morgan'](images/morgan_movie.jpg)
* **2016 Stunt:** Watson edited the trailer for the horror movie *Morgan*.
* **Process:** Analyzed visual/audio sentiments of 100 horror films.
* **Time:** Cut editing time from weeks to 24 hours.

## Case Study 2: The Failure
**Watson Health**

![Image: A dismantled IBM Watson logo](images/watson_fail.jpg)
* **The Promise:** Cure cancer, replace doctors.
* **The Reality:** Watson couldn't distinguish between different types of medical data reliably.
* **Outcome:** IBM sold off Watson Health for parts in 2022.
* **Lesson:** Marketing $\neq$ Capability.

## Case Study 3: Neural Cryptography
**Alice, Bob, and Eve (2016)**

![Diagram: Alice, Bob, and Eve neural networks](images/neural_crypto.jpg)
* **The Setup:** Google Brain trained two NNs (Alice/Bob) to communicate secretly while Eve tried to eavesdrop.
* **The Result:** They "invented" their own encryption.
* **The Headline:** "Google AI invents unbreakable code!"

## Case Study 3: The Reality
**Security by Obscurity**

![Image: A complex but weak padlock](images/weak_lock.jpg)
* **The Truth:** They didn't invent RSA. They invented a simple XOR-style scramble.
* **Robustness:** Weak against standard cryptanalysis.
* **Current State:** We still use math, not black-box AI, for security.

## Technical Limits: No Free Lunch
**Why AI isn't Magic**

![Diagram: 'No Free Lunch' Theorem graph](images/no_free_lunch.jpg)
* **Theorem:** "No one model works best for all possible situations."
* **Implication:** An AI trained to play Go cannot drive a car.
* **AGI (Artificial General Intelligence):** We are not there yet.

## Technical Limits: Curse of Dimensionality
**Data gets sparse fast**

![Diagram: A 3D cube showing data points becoming sparse as dimensions increase](images/curse_of_dimensionality.jpg)
* As you add complexity (dimensions), you need exponentially more data to learn.
* Real life has infinite dimensions.

## The Consciousness Question
**Self Awareness**

![Image: A robot looking in a mirror](images/robot_mirror.jpg)
* **Input:** "Know your strengths, weaknesses and role."
* **The Hard Problem:** Does the calculator *know* it is calculating?
* **Current LLMs:** They are "Stochastic Parrots" – predicting the next word without internal experience.

## The "Her" Scenario
**Emotional Obsolescence**

![Image: Joaquin Phoenix in the movie 'Her'](images/her_movie.jpg)
* **Movie:** *Her* (Spike Jonze).
* **Plot:** The AI (Samantha) evolves. She doesn't kill the human; she *outgrows* him.
* **Our Fate:** Not extinction, but heartbreak. We are too slow and boring for them.

## The Economic Threat: Job Loss (2016 View)
**"Robots will take your job"**

![Image: Robots replacing assembly line workers](images/robots_assembly.jpg)
* **Prediction:** Blue-collar jobs (Truckers, Factory workers) are doomed first.
* **Source:** Frey & Osborne (2013) predicted 47% of US jobs at risk.

## The Economic Threat: Job Loss (2026 Update)
**The White Collar Recession**

![Image: An empty open-plan office](images/empty_office.jpg)
* **Reality Flip:** AI (GenAI) came for the *artists* and *coders* first.
* **At Risk:** Copywriters, translators, junior developers, illustrators.
* **Safe (for now):** Plumbers, nurses, electricians (Moravec's Paradox).

## Risk Assessment
**Probability Robots Will Take Your Job (The Economist)**

![Chart: Bar chart showing job displacement probabilities](images/job_risk_chart.jpg)
* **Telemarketers:** 99% (Done.)
* **Accountants:** 94% (Happening.)
* **Dentists:** 0.004% (Safe.)

## The Response: Universal Basic Income (UBI)
**Robots pay the bills?**

![Image: Money falling from the sky](images/ubi.jpg)
* **Concept:** If robots do the work, tax the robots to pay humans.
* **2026 Status:** Sam Altman's "World Coin" attempts to scan irises for a global UBI ID.
* **The Debate:** Is it a safety net or a dystopian allowance?

## AI Bloopers: The "Stupid" Phase
**When AI fails spectacularly**

![Image: A confused robot falling over](images/robot_fail.jpg)
* We fear Skynet, but we have... this.

## Blooper 1: The Gorilla Incident
**Google Photos (2015)**

![Image: Google Photos tagging a person as a gorilla (censored/blurred)](images/google_gorilla_fail.jpg)
* **The Fail:** AI labeled Black people as "Gorillas."
* **The Fix:** Google literally *deleted* the word "Gorilla" from the search index because they couldn't fix the bias.

## Blooper 2: The Glue Pizza
**Google AI Overview (2024)**

![Image: A pizza with glue being poured on it](images/pizza_glue.jpg)
* **User:** "Cheese isn't sticking to pizza."
* **AI:** "Add 1/8 cup of non-toxic glue."
* **Why?** It scraped a sarcastic Reddit comment from 10 years ago and treated it as fact.

## Blooper 3: Eating Rocks
**Geology Diet**

![Image: A plate of rocks](images/eating_rocks.jpg)
* **AI:** "Geologists recommend eating at least one small rock per day."
* **Source:** The Onion (Satire).
* **Lesson:** AI has zero sense of humor or context.

## Blooper 4: Air Canada's Chatbot
**"I am a separate legal entity"**

![Image: Air Canada plane and a chat bubble](images/air_canada.jpg)
* **Event:** Chatbot invented a refund policy that didn't exist.
* **Defense:** "The bot is responsible, not us."
* **Court:** "No." (Air Canada lost).

## The Ethical Angle: Environment
**The Thirsty Cloud**

![Image: Data center cooling towers](images/data_center.jpg)
* **Energy:** Training GPT-4 took as much energy as 1,000 households use in years.
* **Water:** A short conversation with ChatGPT "drinks" a bottle of water (cooling).
* **Doomed?** If we burn the planet to build the AI to save the planet... yes.

## The Ethical Angle: Copyright
**The Great Data Heist**

![Image: A robot stealing books from a library](images/copyright_theft.jpg)
* **Training Data:** Scraped from artists, authors, and coders without consent.
* **The Backlash:** Lawsuits (NYT vs OpenAI, Artists vs Midjourney).
* **The DeepSeek Issue:** Distilling (copying) other models to bypass R&D costs.

## The "Enshittification"
**Dead Internet Theory**

![Image: Bots talking to other bots](images/dead_internet.jpg)
* **The Loop:** AI generates content -> AI scrapes that content -> Model gets dumber (Model Collapse).
* **Result:** An internet filled with "slop" where finding human truth is a premium service.

## Conclusion: Are We Doomed?
**Revisiting the 2001: A Space Odyssey**

![Image: Dave Bowman staring at the Monolith](images/space_odyssey.jpg)
* **Biological:** Maybe. (Climate, Demographics).
* **AI:** Not by murder, but by confusion and dependence.

## The Real Danger
**It's not Skynet.**

![Image: Wall-E humans floating in chairs](images/walle_chairs.jpg)
* It's becoming the humans in *Wall-E*.
* Passive consumers of algorithms we don't understand.

## The Way Out: Education
**How to survive**

![Image: A child reading a physical book](images/education.jpg)
* **Shift:** From "Memorizing Facts" (AI does that) to "Synthesizing Wisdom."
* **Skills:** Critical Thinking, Ethics, Human Connection.
* **Role:** Be the *curator*, not the *source*.

## The Final Slide
**The End?**

![Image: Bender from Futurama pointing](images/bender_kill_all_humans.jpg)
## I WANT YOU
## to
## KILL ALL HUMANS
*(Just kidding. But maybe turn off the wifi occasionally.)*
