#!/usr/bin/env python3
import json

# New Chris Rock vocabulary entries to add
new_entries = [
    {
      "word": "divisive",
      "definition": "Causing disagreement or hostility between people; tending to divide or create discord; from Latin 'divisus' meaning 'divided'",
      "context": "What's the biggest issue in America right now? The most <b>divisive</b> issue in America is affirmative action. A lot of people think it's to do with the '60s, the back of the bus, separate lunch counters.",
      "comedian": "Chris Rock",
      "special": "Never Scared (2004)",
      "category": "Political/Social",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "perpetuated",
      "definition": "Made to continue indefinitely; kept alive or maintained; from Latin 'perpetuare' meaning 'to make perpetual'",
      "context": "You know the stripper myth. There's a stripper myth that's being <b>perpetuated</b> throughout society. The stripper myth is, 'I'm stripping to pay my tuition.' No, you're not. There's no strippers at college.",
      "comedian": "Chris Rock",
      "special": "Never Scared (2004)",
      "category": "Academic/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "misogynistic",
      "definition": "Showing hatred, dislike, or prejudice against women; from Greek 'misein' (to hate) + 'gyne' (woman)",
      "context": "That's why people always say rap music is <b>misogynistic</b> and it's degrading to women. But what I realise, man, is women that like rap don't give a fuck. Women that like rap don't care what they saying.",
      "comedian": "Chris Rock",
      "special": "Never Scared (2004)",
      "category": "Social/Greek-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "responsibility",
      "definition": "The state or fact of having a duty to deal with something or of having control over someone; from Latin 'respondere' meaning 'to answer'",
      "context": "Somebody has to take on the monumental <b>responsibility</b> that the strippers do. Somebody's gotta do it, somebody has to entertain the married men of America.",
      "comedian": "Chris Rock",
      "special": "Never Scared (2004)",
      "category": "Formal/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "hypocrisy",
      "definition": "The practice of claiming to have moral standards or beliefs that one's own behavior does not conform to; pretense of virtue; from Greek 'hypokrisis' meaning 'acting on a stage'",
      "context": "That's why people hate America... the <b>hypocrisy</b> of our democracy, OK? That's why they hate America. White man makes guns, kids shoot up each other in schools, nobody gives a fuck. Black rapper says 'gun', Congressional hearing.",
      "comedian": "Chris Rock",
      "special": "Never Scared (2004)",
      "category": "Philosophical/Greek-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "schizophrenic",
      "definition": "Characterized by contradictory or fragmented elements; relating to schizophrenia, a mental disorder; from Greek 'schizein' (to split) + 'phren' (mind)",
      "context": "America does good things, America does bad things, America does <b>schizophrenic</b> things. One cool thing America does, that I love, is we feed other countries.",
      "comedian": "Chris Rock",
      "special": "Never Scared (2004)",
      "category": "Medical/Psychological",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "humanitarian",
      "definition": "Concerned with promoting human welfare; a person who seeks to promote human welfare; from Latin 'humanus' (human) + 'tarie' (manner)",
      "context": "Shit, we call ourselves <b>humanitarians</b>, meanwhile we're dropping 50-pound sacks on 40-pound people. Drink up. Have some gravy. People going, 'I love America! It's raining gravy!'",
      "comedian": "Chris Rock",
      "special": "Never Scared (2004)",
      "category": "Ethical/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "descendants",
      "definition": "People who are descended from a particular ancestor; offspring or progeny; from Latin 'descendere' meaning 'to come down'",
      "context": "And some of the richest, most powerful people in the United States are the <b>descendants</b> of drug dealers. Kennedys, Brockmans, it's all drug money. They call it bootlegging but that's just a white word that means drug dealing.",
      "comedian": "Chris Rock",
      "special": "Never Scared (2004)",
      "category": "Genealogical/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "bootlegging",
      "definition": "The illegal production, distribution, or sale of goods, especially alcohol; originally referred to hiding liquor in boot legs during Prohibition",
      "context": "Kennedys, Brockmans, it's all drug money. They call it <b>bootlegging</b> but that's just a white word that means drug dealing. They didn't sell boots, they sold the crack of their day.",
      "comedian": "Chris Rock",
      "special": "Never Scared (2004)",
      "category": "Historical/Criminal",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "empowering",
      "definition": "Giving someone the authority or power to do something; making someone stronger and more confident; from 'em-' (in) + 'power'",
      "context": "Wealth is <b>empowering</b>. Wealth can uplift communities from poverty, OK? A white man gets wealthy, he builds Wal-Marts and makes other white people have some motherfucking money.",
      "comedian": "Chris Rock",
      "special": "Never Scared (2004)",
      "category": "Social/Motivational",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "accustomed",
      "definition": "Familiar with something through repeated experience; used to; from Latin 'accustomare' meaning 'to make customary'",
      "context": "They go to court, start talking some shit: 'Your Honor, I'm used to this, I'm used to that, I'm <b>accustomed</b> to this...' Yo, what the fuck is 'accustomed'? What's that got to do with shit?",
      "comedian": "Chris Rock",
      "special": "Bring the Pain (1996)",
      "category": "Formal/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "acquitted",
      "definition": "Found not guilty of a criminal charge; freed from blame or fault; from Latin 'acquitare' meaning 'to set at rest'",
      "context": "O.J. Simpson was <b>acquitted</b> of murder charges. O.J. was big. That's right. Black people too happy, white people too mad. The white people like: 'That is a bullshit!' I ain't seen white people that nasty since they cancelled M.A.S.H.!",
      "comedian": "Chris Rock",
      "special": "Bring the Pain (1996)",
      "category": "Legal/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "domestic",
      "definition": "Relating to the running of a home or to family relations; within a country; from Latin 'domesticus' meaning 'of the house'",
      "context": "That's the big thing now, <b>domestic</b> abuse! That's the big shit in '96, domestic abuse! Everybody's doing it: OJ, Warren Moon, Billy Dee Williams... Billy Dee Williams beating on women!",
      "comedian": "Chris Rock",
      "special": "Bring the Pain (1996)",
      "category": "Legal/Social",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "ignorant",
      "definition": "Lacking knowledge, education, or awareness; showing a lack of knowledge or awareness; from Latin 'ignorare' meaning 'to not know'",
      "context": "Every time black people want to have a good time, <b>ignorant</b> niggas fuck it up! You can't do shit! You can't do shit without some ignorant niggas fucking it up!",
      "comedian": "Chris Rock",
      "special": "Bring the Pain (1996)",
      "category": "Social/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "conservative",
      "definition": "Averse to change or innovation; holding traditional values; politically right-wing; from Latin 'conservare' meaning 'to preserve'",
      "context": "See, the whole damn country is so damn <b>conservative</b>. Everybody says: 'Jails ain't tough enough. Jails ain't tough enough.' 'We gotta have the death penalty.'",
      "comedian": "Chris Rock",
      "special": "Bring the Pain (1996)",
      "category": "Political/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "patriotism",
      "definition": "Devotion to and vigorous support for one's country; national pride; from Latin 'patriota' meaning 'fellow countryman'",
      "context": "No, when the war started, it was great. Brought out a lot of <b>patriotism</b>. Patriotism's beautiful. But slowly but surely, the patriotism turned into hate-riotism.",
      "comedian": "Chris Rock",
      "special": "Never Scared (2004)",
      "category": "Political/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "surveillance",
      "definition": "Close observation, especially of a suspected person; monitoring of behavior or activities; from French 'surveiller' meaning 'to watch over'",
      "context": "Gunned down in a recording studio in Queens, OK? They had <b>surveillance</b> footage of people coming in and out, they ain't arrested nobody. It's like the guy came in the studio, shot Jay, recorded an album, then left.",
      "comedian": "Chris Rock",
      "special": "Never Scared (2004)",
      "category": "Legal/Security",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "obsolete",
      "definition": "No longer produced or used; out of date; no longer valid or useful; from Latin 'obsoletus' meaning 'grown old'",
      "context": "If I was you, I would diversify my portfolio. You know, ever since the end of the Cold War, I find NATO <b>obsolete</b>.",
      "comedian": "Chris Rock",
      "special": "Never Scared (2004)",
      "category": "Technical/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "portfolio",
      "definition": "A range of investments held by a person or organization; a collection of works or documents; from Italian 'portafoglio' meaning 'to carry leaves'",
      "context": "I never got a smart lap dance. I never got a girl that sat on my lap and said, 'If I was you, I would diversify my <b>portfolio</b>.'",
      "comedian": "Chris Rock",
      "special": "Never Scared (2004)",
      "category": "Financial/Business",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "renegotiate",
      "definition": "To negotiate again or differently; to discuss and attempt to revise the terms of an agreement; from Latin 're-' (again) + 'negotiari' (to do business)",
      "context": "And it's weird we're doing that with our relationships. All of us are doing that with our relationships. But I think we need to <b>renegotiate</b> our relationship to the government you know. It's like — yeah, we need to renegotiate our relationship to the government it doesn't work.",
      "comedian": "Chris Rock",
      "special": "SNL Monologue (2020)",
      "category": "Political/Business",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "predicament",
      "definition": "A difficult, unpleasant, or embarrassing situation; a dilemma; from Latin 'praedicamentum' meaning 'category or predicament'",
      "context": "That's how we got in this <b>predicament</b>. You know what I mean– I mean, it should be some rules to being the president. You realize there's more rules to a game show than running for president?",
      "comedian": "Chris Rock",
      "special": "SNL Monologue (2020)",
      "category": "Formal/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "scrutiny",
      "definition": "Critical observation or examination; close and careful attention; from Latin 'scrutinium' meaning 'search or examination'",
      "context": "It's like real <b>scrutiny</b>, man and do the democrats even want to win do they even want to win it's like trump, he runs against — the democrats just keep putting up 75-year-old people to run against Trump.",
      "comedian": "Chris Rock",
      "special": "SNL Monologue (2020)",
      "category": "Formal/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "indicators",
      "definition": "Things that provide information about the state or level of something; gauges or measures; from Latin 'indicare' meaning 'to point out'",
      "context": "Mr President, when's the economy gonna pick up? Well, we're talking to people, and economic <b>indicators</b> indicate that indications are coming to the indicator.",
      "comedian": "Chris Rock",
      "special": "SNL Monologue (2020)",
      "category": "Economic/Technical",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "marginalized",
      "definition": "Treated as insignificant or peripheral; pushed to the edge of society; excluded from mainstream; from Latin 'margo' meaning 'edge'",
      "context": "I have no problem with it at all. I'm all for social justice. I'm all for, for <b>marginalized</b> people getting their rights. The thing I have a problem with is the selective outrage.",
      "comedian": "Chris Rock",
      "special": "Selective Outrage (2023)",
      "category": "Sociological/Academic",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "discrimination",
      "definition": "The unjust treatment of different categories of people; prejudice; from Latin 'discriminare' meaning 'to distinguish between'",
      "context": "I walk by and in the window of every Lululemon, there's a sign that says, 'We don't support racism, sexism, <b>discrimination</b>, or hate.' And I'm like, 'Who gives a fuck?' You're just selling yoga pants.",
      "comedian": "Chris Rock",
      "special": "Selective Outrage (2023)",
      "category": "Legal/Social",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "opioids",
      "definition": "A class of drugs that include both prescription pain relievers and illegal drugs like heroin; act on opioid receptors in the brain; from Greek 'opion' (poppy juice)",
      "context": "They say we're addicted to <b>opioids</b>. They say we're addicted to opioids and we are. I like a good opioid when I could get my hand on it. There's, like, no pharmacist has ever paid to come to my show.",
      "comedian": "Chris Rock",
      "special": "Selective Outrage (2023)",
      "category": "Medical/Pharmaceutical",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "infamy",
      "definition": "The state of being well known for some bad quality or deed; evil fame or reputation; from Latin 'in-' (not) + 'fama' (fame)",
      "context": "Number two easiest way to get attention is to be <b>infamous</b>. Yeah. Do some fucked up shit. Shoot up a school. Try to stab Dave Chappelle at a show. That's right, infamy. You will get attention.",
      "comedian": "Chris Rock",
      "special": "Selective Outrage (2023)",
      "category": "Literary/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "excellence",
      "definition": "The quality of being outstanding or extremely good; superiority; from Latin 'excellere' meaning 'to surpass'",
      "context": "Number three easiest way to get attention, that's right, to be <b>excellent</b>. That's right. Like Serena Williams, greatest tennis player to ever play the game. Absolutely excellent! Being excellent will get you attention, but it's hard being excellent.",
      "comedian": "Chris Rock",
      "special": "Selective Outrage (2023)",
      "category": "Formal/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "trauma",
      "definition": "A deeply distressing or disturbing experience; emotional shock following a stressful event; from Greek 'trauma' meaning 'wound'",
      "context": "There are real victims in this world. There are people that have gone through unspeakable <b>trauma</b>, and they need your love, your support, and they need your care.",
      "comedian": "Chris Rock",
      "special": "Selective Outrage (2023)",
      "category": "Medical/Psychological",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "colonialism",
      "definition": "The policy or practice of acquiring full or partial political control over another country; occupation and exploitation; from Latin 'colonus' meaning 'settler'",
      "context": "It's the royal family. They're the original racists! They invented <b>colonialism</b>! They're the OGs of racism. They're the Sugarhill Gang of racism.",
      "comedian": "Chris Rock",
      "special": "Selective Outrage (2023)",
      "category": "Historical/Political",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "inclusive",
      "definition": "Including all the services or facilities normally expected; not excluding any particular group; from Latin 'includere' meaning 'to shut in'",
      "context": "The Kardashians are <b>inclusive</b>! And they love Black people more than Black people love Black people. Shit, the father freed O.J.",
      "comedian": "Chris Rock",
      "special": "Selective Outrage (2023)",
      "category": "Social/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "equality",
      "definition": "The state of being equal, especially in status, rights, or opportunities; from Latin 'aequalis' meaning 'uniform or identical'",
      "context": "I mean, honestly, I wanna live in a world with real <b>equality</b>. I wanna live in a world where an equal amount of white kids are shot every month. An equal world.",
      "comedian": "Chris Rock",
      "special": "Tamborine (2018)",
      "category": "Political/Social",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "orientation",
      "definition": "The determination of the relative position of something; introduction or training to a new situation; from Latin 'oriens' meaning 'rising' or 'east'",
      "context": "She just started high school and I had to take her to freshman <b>orientation</b>. You ever go to freshman orientation? It's the most boring thing you will ever do with your kids.",
      "comedian": "Chris Rock",
      "special": "Tamborine (2018)",
      "category": "Educational/Formal",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "endangered",
      "definition": "Seriously at risk of extinction or harm; threatened; from Old French 'en-' (in) + 'danger'",
      "context": "Some people say young black men are an <b>endangered</b> species. But, that's not true. Because endangered species are protected by the government.",
      "comedian": "Chris Rock",
      "special": "Tamborine (2018)",
      "category": "Environmental/Legal",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "custody",
      "definition": "The legal right or duty to care for someone, especially a child; imprisonment or detention; from Latin 'custodia' meaning 'guardianship'",
      "context": "Had to go through a <b>custody</b> fight for my kids. Just to see my kids, man. That shit's fucked up, man. First of all, you don't wanna be a man in family court.",
      "comedian": "Chris Rock",
      "special": "Tamborine (2018)",
      "category": "Legal/Family",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "humiliating",
      "definition": "Making someone feel ashamed or foolish; causing loss of pride or dignity; from Latin 'humiliare' meaning 'to humble'",
      "context": "That shit was, like, <b>humiliating</b>, man. Trying to prove your parenthood, man. So I know I said you're not supposed to compete in a relationship, but after you go through that shit, you're like, 'Am I gonna lose my kids?'",
      "comedian": "Chris Rock",
      "special": "Tamborine (2018)",
      "category": "Emotional/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "parenthood",
      "definition": "The state of being a parent; the responsibilities and experiences of raising children; from 'parent' + '-hood' (state of being)",
      "context": "That shit was, like, humiliating, man. Trying to prove your <b>parenthood</b>, man. So I know I said you're not supposed to compete in a relationship, but after you go through that shit, you're like, 'Am I gonna lose my kids?'",
      "comedian": "Chris Rock",
      "special": "Tamborine (2018)",
      "category": "Family/Social",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "unconditional",
      "definition": "Not subject to any conditions; absolute; without limitations or restrictions; from Latin 'un-' (not) + 'condicio' (agreement)",
      "context": "You get older, the one thing I learned... Only women, children and dogs... are loved <b>unconditionally</b>. Women, children, and dogs are loved unconditionally. A man is only loved under the condition that he provides something.",
      "comedian": "Chris Rock",
      "special": "Tamborine (2018)",
      "category": "Emotional/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "facilitate",
      "definition": "To make an action or process easier; to help bring about; from Latin 'facilis' meaning 'easy'",
      "context": "Ladies, when you meet a new guy, what do your friends ask you? 'What does he do? What the fuck does that nigga do that can help you out? Can this motherfucker <b>facilitate</b> a dream or not?'",
      "comedian": "Chris Rock",
      "special": "Tamborine (2018)",
      "category": "Business/Formal",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "circumstances",
      "definition": "The conditions or facts that affect an event or situation; surrounding conditions; from Latin 'circum' (around) + 'stare' (to stand)",
      "context": "And I realize everybody in the room, born to much better <b>circumstances</b> than me. I'm from Bed-motherfucking-Stuy, baby. And everybody in there is there to take my money.",
      "comedian": "Chris Rock",
      "special": "Tamborine (2018)",
      "category": "Formal/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "desensitized",
      "definition": "Made less sensitive or responsive to something; emotionally dulled through repeated exposure; from Latin 'de-' (down) + 'sensus' (feeling)",
      "context": "And, what happens, too, you watch too much porn, you get <b>desensitized</b>. You know? It's like, when you start watching porn, it's like, any porn will do. It's like, 'Ah, they're naked! Ooh-hoo!' Then later on, now you're all fucked up.",
      "comedian": "Chris Rock",
      "special": "Tamborine (2018)",
      "category": "Psychological/Medical",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "indignity",
      "definition": "Treatment or circumstances that cause one to feel shame or loss of dignity; from Latin 'in-' (not) + 'dignitas' (worthiness)",
      "context": "And my mother told me when she was a little girl, it was against the law for a Black person to go to a white dentist. Against the law for a Black person to go to a white dentist, right? And if you were a little child and you needed your teeth taken out, like all children do, if you're a little Black child and you needed your teeth taken out, and you couldn't find a Black dentist, you had to go to a vet. Yeah, motherfucker. A vet in America. I'm talking about my mother. I'm not talking about Harriet Tubman. I'm talking about my mother. Shit, she's sitting over there, okay? My mother went to a vet, okay? Went to a vet. And think about it. The same woman that had to go through the <b>indignity</b> of getting her teeth taken out by a fucking vet, the same woman now, twice a year, gets on a plane, flies to Paris, and has coffee with her granddaughter, who is going to culinary school.",
      "comedian": "Chris Rock",
      "special": "Selective Outrage (2023)",
      "category": "Formal/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "entanglement",
      "definition": "A complicated or compromising relationship or situation; the state of being twisted together; from Old French 'entangler' meaning 'to tangle'",
      "context": "I didn't. I did not have any <b>entanglement</b>. For people that don't know what everybody knows. Will Smith, his wife was fucking her son's friend, okay? Now, I normally would not talk about this shit. But for some reason, these niggas put that shit on the Internet.",
      "comedian": "Chris Rock",
      "special": "Selective Outrage (2023)",
      "category": "Formal/Relational",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "auditioning",
      "definition": "Trying out for a role or position; demonstrating one's skills for evaluation; from Latin 'audire' meaning 'to hear'",
      "context": "When you're single, you get the best blow jobs in the world, 8, 12, 15 minutes straight like the girl's <b>auditioning</b> on your dick, like she's giving your dick a second opinion, like she's going for her scuba licence.",
      "comedian": "Chris Rock",
      "special": "Never Scared (2004)",
      "category": "Entertainment/Formal",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "telekinetic",
      "definition": "Relating to the supposed movement of objects by mental power alone; from Greek 'tele' (distant) + 'kinesis' (movement)",
      "context": "It's amazing! It's like we're <b>telekinetic</b>, we're telekinetic. It's incredible, my God. Nobody gets a soul mate. It don't happen. Nobody. Not even James Brown, the godfather of soul, he don't even get a soul mate, as we all saw a couple of weeks ago.",
      "comedian": "Chris Rock",
      "special": "Never Scared (2004)",
      "category": "Paranormal/Greek-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "sacrilegious",
      "definition": "Involving or committing the violation or misuse of what is regarded as sacred; from Latin 'sacer' (sacred) + 'legere' (to gather)",
      "context": "I mean, here's the thing. I think the act of helping God is <b>sacrilegious</b>. If you think you can help God out, you don't believe in God. If you really had faith you'd really have faith.",
      "comedian": "Chris Rock",
      "special": "Tamborine (2018)",
      "category": "Religious/Latin-derived",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "extremists",
      "definition": "People who hold extreme political or religious views; those who advocate extreme measures; from Latin 'extremus' meaning 'outermost'",
      "context": "You ever watch the news, they're always talking about religious <b>extremists</b>. We're at war with extremists. Extremists. What is a religious extremist? A religious extremist is a person that extremely believes in God.",
      "comedian": "Chris Rock",
      "special": "Tamborine (2018)",
      "category": "Political/Religious",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    },
    {
      "word": "nuanced",
      "definition": "Characterized by subtle shades of meaning or expression; showing awareness of subtle distinctions; from French 'nuance' meaning 'shade'",
      "context": "Republicans lie. Republicans lie. Biggest liars in the world. Republicans lie, and Democrats leave out key pieces of the truth... that would lead to a more <b>nuanced</b> argument. The whole country is fucked up.",
      "comedian": "Chris Rock",
      "special": "Selective Outrage (2023)",
      "category": "Academic/Formal",
      "difficulty": "high",
      "image": "images/Chris-Rock-Never-Scared-2004-Transcript.jpg"
    }
]

# Read existing vocabulary
with open('/mnt/data/openclaw/workspace/.openclaw/workspace/comedy-vocab-site/vocabulary.json', 'r') as f:
    data = json.load(f)

# Count existing Chris Rock entries
existing_chris_count = sum(1 for entry in data['vocabulary'] if entry['comedian'] == 'Chris Rock')
print(f"Existing Chris Rock entries: {existing_chris_count}")

# Add new entries
data['vocabulary'].extend(new_entries)

# Count new total
new_chris_count = sum(1 for entry in data['vocabulary'] if entry['comedian'] == 'Chris Rock')
print(f"New Chris Rock entries: {new_chris_count}")
print(f"Total vocabulary entries: {len(data['vocabulary'])}")

# Write back
with open('/mnt/data/openclaw/workspace/.openclaw/workspace/comedy-vocab-site/vocabulary.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Successfully appended Chris Rock vocabulary entries!")
