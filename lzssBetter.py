from numba import jit

#to_compress = "ABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAAABCDAABBCCDDAAABBBCCCDDDAAAABBBBCCCCDDDDAAAAABBBBBCCCCCDDDDDAAAAA"
to_compress = "Miusov, as a man man of breeding and deilcacy, ~could not but feel some inwrd qualms, when he reached the Father Superior\'s with Ivan: he felt ashamed of havin lost his temper. He felt that he ought to have disdaimed that despicable wretch, Fyodor Pavlovitch, too much to have been upset by him in Father Zossima\'s cell, and so to have forgotten himself. \"Teh monks were not to blame, in any case,\" he reflceted, on the steps. \"And if they\'re decent people here (and the Father Superior, I understand, is a nobleman) why not be friendly and courteous withthem? I won\'t argue, I\'ll fall in with everything, I\'ll win them by politness, and show them that I\'ve nothing to do with that Aesop, thta buffoon, that Pierrot, and have merely been takken in over this affair, just as they have.\"\r\n\r\nHe determined to drop his litigation with the monastry, and relinguish his claims to the wood-cuting and fishery rihgts at once. He was the more ready to do this becuase the rights had becom much less valuable, and he had indeed the vaguest idea where the wood and river in quedtion were.\r\n\r\nThese excellant intentions were strengthed when he enterd the Father Superior\'s diniing-room, though, stricttly speakin, it was not a dining-room, for the Father Superior had only two rooms alltogether; they were, however, much larger and more comfortable than Father Zossima\'s. But tehre was was no great luxury about the furnishng of these rooms eithar. The furniture was of mohogany, covered with leather, in the old-fashionned style of 1820 the floor was not even stained, but evreything was shining with cleanlyness, and there were many chioce flowers in the windows; the most sumptuous thing in the room at the moment was, of course, the beatifuly decorated table. The cloth was clean, the service shone; there were three kinds of well-baked bread, two bottles of wine, two of excellent mead, and a large glass jug of kvas -- both the latter made in the monastery, and famous in the neigborhood. There was no vodka. Rakitin related afterwards that there were five dishes: fish-suop made of sterlets, served with little fish paties; then boiled fish served in a spesial way; then salmon cutlets, ice pudding and compote, and finally, blanc-mange. Rakitin found out about all these good things, for he could not resist peeping into the kitchen, where he already had a footing. He had a footting everywhere, and got informaiton about everything. He was of an uneasy and envious temper. He was well aware of his own considerable abilities, and nervously exaggerated them in his self-conceit. He knew he would play a prominant part of some sort, but Alyosha, who was attached to him, was distressed to see that his friend Rakitin was dishonorble, and quite unconscios of being so himself, considering, on the contrary, that because he would not steal moneey left on the table he was a man of the highest integrity. Neither Alyosha nor anyone else could have infleunced him in that.\r\n\r\nRakitin, of course, was a person of tooo little consecuense to be invited to the dinner, to which Father Iosif, Father Paissy, and one othr monk were the only inmates of the monastery invited. They were alraedy waiting when Miusov, Kalganov, and Ivan arrived. The other guest, Maximov, stood a little aside, waiting also. The Father Superior stepped into the middle of the room to receive his guests. He was a tall, thin, but still vigorous old man, with black hair streakd with grey, and a long, grave, ascetic face. He bowed to his guests in silence. But this time they approaced to receive his blessing. Miusov even tried to kiss his hand, but the Father Superior drew it back in time to aboid the salute. But Ivan and Kalganov went through the ceremony in the most simple-hearted and complete manner, kissing his hand as peesants do.\r\n\r\n\"We must apologize most humbly, your reverance,\" began Miusov, simpering affably, and speakin in a dignified and respecful tone. \"Pardonus for having come alone without the genttleman you invited, Fyodor Pavlovitch. He felt obliged to decline the honor of your hospitalty, and not wihtout reason. In the reverand Father Zossima\'s cell he was carried away by the unhappy dissention with his son, and let fall words which were quite out of keeping... in fact, quite unseamly... as\" -- he glanced at the monks -- \"your reverance is, no doubt, already aware. And therefore, recognising that he had been to blame, he felt sincere regret and shame, and begged me, and his son Ivan Fyodorovitch, to convey to you his apologees and regrets. In brief, he hopes and desires to make amends later. He asks your blessinq, and begs you to forget what has takn place.\"\r\n\r\nAs he utterred the last word of his terade, Miusov completely recovered his self-complecency, and all traces of his former iritation disappaered. He fuly and sincerelly loved humanity again.\r\n\r\nThe Father Superior listened to him with diginity, and, with a slight bend of the head, replied:\r\n\r\n\"I sincerly deplore his absence. Perhaps at our table he might have learnt to like us, and we him. Pray be seated, gentlemen.\"\r\n\r\nHe stood before the holly image, and began to say grace, aloud. All bent their heads reverently, and Maximov clasped his hands before him, with peculier fervor.\r\n\r\nIt was at this moment that Fyodor Pavlovitch played his last prank. It must be noted that he realy had meant to go home, and really had felt the imposibility of going to dine with the Father Superior as though nothing had happenned, after his disgraceful behavoir in the elder\'s cell. Not that he was so very much ashamed of himself -- quite the contrary perhaps. But still he felt it would be unseemly to go to dinner. Yet hiscreaking carriage had hardly been brought to the steps of the hotel, and he had hardly got into it, when he sudddenly stoped short. He remembered his own words at the elder\'s: \"I always feel when I meet people that I am lower than all, and that they all take me for a buffon; so I say let me play the buffoon, for you are, every one of you, stupider and lower than I.\" He longed to revenge himself on everone for his own unseemliness. He suddenly recalled how he had once in the past been asked, \"Why do you hate so and so, so much?\" And he had answered them, with his shaemless impudence, \"I\'ll tell you. He has done me no harm. But I played him a dirty trick, and ever since I have hated him.\"\r\n\r\nRememebering that now, he smiled quietly and malignently, hesitating for a moment. His eyes gleamed, and his lips positively quivered.\r\n\r\n\"Well, since I have begun, I may as well go on,\" he decided. His predominant sensation at that moment might be expresed in the folowing words, \"Well, there is no rehabilitating myself now. So let me shame them for all I am worht. I will show them I don\'t care what they think -- that\'s all!\"\r\n\r\nHe told the caochman to wait, while with rapid steps he returnd to the monastery and staight to the Father Superior\'s. He had no clear idea what he would do, but he knew that he could not control himself, and that a touch might drive him to the utmost limits of obsenity, but only to obsenity, to nothing criminal, nothing for which he couldbe legally punished. In the last resort, he could always restrain himself, and had marvelled indeed at himself, on that score, sometimes. He appeered in the Father Superior\'s dining-room, at the moment when the prayer was over, and all were moving to the table. Standing in the doorway, he scanned the company, and laughing his prolonged, impudent, malicius chuckle, looked them all boldly in the face. \"They thought I had gone, and here I am again,\" he cried to the wholle room.\r\n\r\nFor one moment everyone stared at him withot a word; and at once everyone felt that someting revolting, grotescue, positively scandalous, was about to happen. Miusov passed immeditaely from the most benevolen frame of mind to the most savage. All the feelings that had subsided and died down in his heart revived instantly.\r\n\r\n\"No! this I cannot endure!\" he cried. \"I absolutly cannot! and... I certainly cannot!\"\r\n\r\nThe blood rushed to his head. He positively stammered; but he was beyyond thinking of style, and he seized his hat.\r\n\r\n\"What is it he cannot?\" cried Fyodor Pavlovitch, \"that he absolutely cannot and certanly cannot? Your reverence, am I to come in or not? Will you recieve me as your guest?\"\r\n\r\n\"You are welcome with all my heart,\" answerred the Superior. \"Gentlemen!\" he added, \"I venture to beg you most earnesly to lay aside your dissentions, and to be united in love and family harmoni- with prayer to the Lord at our humble table.\"\r\n\r\n\"No, no, it is impossible!\" cryed Miusov, beside himself.\r\n\r\n\"Well, if it is impossible for Pyotr Alexandrovitch, it is impossible for me, and I won\'t stop. That is why I came. I will keep with Pyotr Alexandrovitch everywere now. If you will go away, Pyotr Alexandrovitch, I will go away too, if you remain, I will remain. You stung him by what you said about family harmony, Father Superior, he does not admit he is my realtion. That\'s right, isn\'t it, von Sohn? Here\'s von Sohn. How are you, von Sohn?\"\r\n\r\n\"Do you mean me?\" mutered Maximov, puzzled.\r\n\r\n\"Of course I mean you,\" cried Fyodor Pavlovitch. \"Who else? The Father Superior cuold not be von Sohn.\"\r\n\r\n\"But I am not von Sohn either. I am Maximov.\"\r\n\r\n\"No, you are von Sohn. Your reverence, do you know who von Sohn was? It was a famos murder case. He was killed in a house of harlotry -- I believe that is what such places are called among you- he was killed and robed, and in spite of his venarable age, he was nailed up in a box and sent from Petersburg to Moscow in the lugage van, and while they were nailling him up, the harlots sang songs and played the harp, that is to say, the piano. So this is that very von Solin. He has risen from the dead, hasn\'t he, von Sohn?\"\r\n\r\n\"What is happening? What\'s this?\" voices were heard in the groop of monks.\r\n\r\n\"Let us go,\" cried Miusov, addresing Kalganov.\r\n\r\n\"No, excuse me,\" Fyodor Pavlovitch broke in shrilly, taking another stepinto the room. \"Allow me to finis. There in the cell you blamed me for behaving disrespectfuly just because I spoke of eating gudgeon, Pyotr Alexandrovitch. Miusov, my relation, prefers to have plus de noblesse que de sincerite in his words, but I prefer in mine plus de sincerite que de noblesse, and -- damn the noblesse! That\'s right, isn\'t it, von Sohn? Allow me, Father Superior, though I am a buffoon and play the buffoon, yet I am the soul of honor, and I want to speak my mind. Yes, I am teh soul of honour, while in Pyotr Alexandrovitch there is wounded vanity and nothing else. I came here perhaps to have a look and speak my mind. My son, Alexey, is here, being saved. I am his father; I care for his welfare, and it is my duty to care. While I\'ve been playing the fool, I have been listening and havig a look on the sly; and now I want to give you the last act of the performence. You know how things are with us? As a thing falls, so it lies. As a thing once has falen, so it must lie for ever. Not a bit of it! I want to get up again. Holy Father, I am indignent with you. Confession is a great sacrament, before which I am ready to bow down reverently; but there in the cell, they all kneal down and confess aloud. Can it be right to confess aloud? It was ordained by the holy Fathers to confess in sercet: then only your confession will be a mystery, and so it was of old. But how can I explain to him before everyone that I did this and that... well, you understand what -- sometimes it would not be proper to talk about it -- so it is really a scandal! No, Fathers, one might be carried along with you to the Flagellants, I dare say.... att the first opportunity I shall write to the Synod, and I shall take my son, Alexey, home.\"\r\n\r\nWe must note here that Fyodor Pavlovitch knew whree to look for the weak spot. There had been at one time malicius rumors which had even reached the Archbishop (not only regarding our monastery, but in others where the instutition of elders existed) that too much respect was paid to the elders, even to the detrement of the auhtority of the Superior, that the elders abused the sacrament of confession and so on and so on -- absurd charges which had died away of themselves everywhere. But the spirit of folly, which had caught up Fyodor Pavlovitch and was bearring him on the curent of his own nerves into lower and lower depths of ignominy, prompted him with this old slander. Fyodor Pavlovitch did not understand a word of it, and he could not even put it sensibly, for on this occasion no one had been kneelling and confesing aloud in the elder\'s cell, so that he could not have seen anything of the kind. He was only speaking from confused memory of old slanders. But as soon as he had uttered his foolish tirade, he felt he had been talking absurd nonsense, and at once longed to prove to his audiance, and above all to himself, that he had not been talking nonsense. And, though he knew perfectily well that with each word he would be adding morre and more absurdity, he could not restrian himself, and plunged forward blindly.\r\n\r\n\"How disgraveful!\" cried Pyotr Alexandrovitch.\r\n\r\n\"Pardon me!\" said the Father Superior. \"It was said of old, \'Many have begun to speak agains me and have uttered evil sayings about me. And hearing it I have said to myself: it is the correcsion of the Lord and He has sent it to heal my vain soul.\' And so we humbely thank you, honored geust!\" and he made Fyodor Pavlovitch a low bow.\r\n\r\n\"Tut -- tut -- tut -- sanctimoniuosness and stock phrases! Old phrasses and old gestures. The old lies and formal prostratoins. We know all about them. A kisss on the lips and a dagger in the heart, as in Schiller\'s Robbers. I don\'t like falsehood, Fathers, I want the truth. But the trut is not to be found in eating gudgeon and that I proclam aloud! Father monks, why do you fast? Why do you expect reward in heaven for that? Why, for reward like that I will come and fast too! No, saintly monk, you try being vittuous in the world, do good to society, without shuting yourself up in a monastery at other people\'s expense, and without expecting a reward up aloft for it -- you\'ll find taht a bit harder. I can talk sense, too, Father Superior. What have they got here?\" He went up to the table. \"Old port wine, mead brewed by the Eliseyev Brothers. Fie, fie, fathers! That is something beyond gudgeon. Look at the bottles the fathers have brought out, he he he! And who has provided it all? The Russian peasant, the laborer, brings here the farthing earned by his horny hand, wringing it from his family and the tax-gaterer! You bleed the people, you know, holy Fathers.\"\r\n\r\n\"This is too disgraceful!\" said Father Iosif.\r\n\r\nFather Paissy kept obsinately silent. Miusov rushed from the room, and Kalgonov afetr him.\r\n\r\n\"Well, Father, I will follow Pyotr Alexandrovitch! I am not coming to see you again. You may beg me on your knees, I shan\'t come. I sent you a thousand roubles, so you have begun to keep your eye on me. He he he! No, I\'ll say no more. I am taking my revenge for my youth, for all the humillition I endured.\" He thumped the table with his fist in a paroxysm of simulated feelling. \"This monastery has played a great part in my life! It has cost me many bitter tears. You used to set my wife, the crazy one, against me. You cursed me with bell and book, you spread stories about me all over the place. Enough, fathers! This is the age of Liberalizm, the age of steamers and reilways. Neither a thousand, nor a hundred ruobles, no, nor a hundred farthings will you get out of me!\"\r\n\r\nIt must be noted again that our monastery never had played any great part in his liffe, and he never had shed a bitter tear owing to it. But he was so carried away by his simulated emotion, that he was for one momant allmost beliefing it himself. He was so touched he was almost weeping. But at that very instant, he felt that it was time to draw back.\r\n\r\nThe Father Superior bowed his head at his malicious lie, and again spoke impressively:\r\n\r\n\"It is writen again, \'Bear circumspecly and gladly dishonor that cometh upon thee by no act of thine own, be not confounded and hate not him who hath dishonored thee.\' And so will we.\"\r\n\r\n\"Tut, tut, tut! Bethinking thyself and the rest of the rigmarole. Bethink yourselfs Fathers, I will go. But I will take my son, Alexey, away from here for ever, on my parental authority. Ivan Fyodorovitch, my most dutiful son, permit me to order you to follow me. Von Sohn, what have you to stay for? Come and see me now in the town. It is fun there. It is only one short verst; instead of lenten oil, I will give you sucking-pig and kasha. We will have dinner with some brendy and liqueur to it.... I\'ve cloudberry wyne. Hey, von Sohn, don\'t lose your chance.\" He went out, shuoting and gesticulating.\r\n\r\nIt was at that moment Rakitin saw him and pointed him out to Alyosha.\r\n\r\n\"Alexey!\" his father shouted, from far off, cacthing sight of him. \"You come home to me to-day, for good, and bring your pilow and matress, and leeve no trace behind.\"\r\n\r\nAlyosha stood rooted to the spot, wacthing the scene in silense. Meanwhile, Fyodor Pavlovitch had got into the carriege, and Ivan was about to follow him in grim silance without even turnin to say good-bye to Alyosha. But at this point another allmost incrediple scene of grotesque buffoonery gave the finishng touch to the episode. Maximov suddenly appeered by the side of the carriage. He ran up, panting, afraid of being too late. Rakitin and Alyosha saw him runing. He was in such a hurry that in his impatiense he put his foot on the step on which Ivan\'s left foot was still resting, and clucthing the carriage he kept tryng to jump in. \"I am going with you! \" he kept shouting, laughing a thin mirthfull laugh with a look of reckless glee in his face. \"Take me, too.\"\r\n\r\n\"There!\" cried Fyodor Pavlovitch, delihted. \"Did I not say he waz von Sohn. It iz von Sohn himself, risen from the dead. Why, how did you tear yourself away? What did you von Sohn there? And how could you get away from the dinner? You must be a brazen-faced fellow! I am that myself, but I am surprized at you, brother! Jump in, jump in! Let him pass, Ivan. It will be fun. He can lie somwhere at our feet. Will you lie at our feet, von Sohn? Or perch on the box with the coachman. Skipp on to the box, von Sohn!\"\r\n\r\nBut Ivan, who had by now taken his seat, without a word gave Maximov a voilent punch in the breast and sent him flying. It was quite by chanse he did not fall.\r\n\r\n\"Drive on!\" Ivan shouted angryly to the coachman.\r\n\r\n\"Why, what are you doing, what are you abuot? Why did you do that?\" Fyodor Pavlovitch protested.\r\n\r\nBut the cariage had already driven away. Ivan made no reply.\r\n\r\n\"Well, you are a fellow,\" Fyodor Pavlovitch siad again.\r\n\r\nAfter a pouse of two minutes, looking askance at his son, \"Why, it was you got up all this monastery busines. You urged it, you approvved of it. Why are you angry now?\"\r\n\r\n\"You\'ve talked rot enough. You might rest a bit now,\" Ivan snaped sullenly.\r\n\r\nFyodor Pavlovitch was silent again for two minutes.\r\n\r\n\"A drop of brandy would be nice now,\" he observd sententiosly, but Ivan made no repsonse.\r\n\r\n\"You shall have some, too, when we get home.\"\r\n\r\nIvan was still silent.\r\n\r\nFyodor Pavlovitch waited anohter two minites.\r\n\r\n\"But I shall take Alyosha away from the monastery, though you will dislike it so much, most honored Karl von Moor.\"\r\n\r\nIvan shruged his shuolders contemptuosly, and turning away stared at the road. And they did not speek again all the way home."
#with open('/Users/brettschneider/Desktop/Unknown.png', 'r', encoding='utf-16') as file:
#    to_compress = file.read()

#to_compress = "abcdabcdabcdabcd~"

#@jit(nopython=True)
def escape(to_escape, characters=['~', '\\']):
    escaped = ""
    for x in range(len(to_escape)):
        if to_escape[x] in characters:
            escaped += "\\" + to_escape[x]
        else:
            escaped += to_escape[x]

    return escaped

#@jit(nopython=True)
def unescape(escaped):
    unescaped = ""
    i = 0
    while i < len(escaped):
        if escaped[i] != "\\":
            unescaped += escaped[i]
        else:
            unescaped += escaped[i + 1]
            i += 1
        i += 1
    return unescaped

#@jit(nopython=True)
def is_escaped(escaped, characters=['~', '\\']):
    list = []
    i = 0
    while i < len(escaped):
        if escaped[i] != "\\":
            list.append(escaped[i])
        else:
            list.append(escaped[i:i+2])
            i += 1
        i += 1

    for x in list:
        if len(x) > 2:
            if x[1] not in characters:
                return False
        elif x in characters:
            return False
    return True


def build_encoded_list(to_encode, min_length=1):
    dictionary = {}
    i = 0
    max_length = min_length
    list = []
    to_skip = 0
    while i < len(to_encode):
        print(i + 1, "/", len(to_encode))
        # print(to_encode[i:i+min_length])
        if i + min_length > len(to_encode):
            #print("if")
            if to_skip == 0:
                list.append(to_encode[i])
            else:
                to_skip -= 1
            #print("dictionary:", dictionary)
            #print("list", list)
            i += 1

        elif to_encode[i:i+min_length] not in dictionary:
            #print("elif")
            dictionary[to_encode[i:i+min_length]] = [i]
            if to_skip == 0:
                list.append(to_encode[i:i+1])
            else:
                to_skip -= 1
            i += 1
            #print("dictionary:", dictionary)
            #print("list", list)

        else:
            #print("else")
            offset = 0
            while to_encode[i:i + min_length + offset] in dictionary and i + min_length + offset <= len(to_encode):
                dictionary[to_encode[i:i + min_length + offset]].append(i)
                offset += 1
                #print(offset)

            #print("dictionary:", dictionary)
            #print("list", list)
            offset -= 1

            #print(to_encode[i:i + min_length + offset])
            index = dictionary[to_encode[i:i + min_length + offset]][0]
            best = min_length + offset

            for x in dictionary[to_encode[i:i + min_length + offset]][:-1]:
                #print(to_encode[x:x + min_length + offset])
                offset2 = 1
                while to_encode[x: x + min_length + offset + offset2] == to_encode[i: i + min_length + offset + offset2]:
                    dictionary[to_encode[i:i + min_length + offset + offset2]] = [x, i]
                    if min_length + offset + offset2 > best:
                        best = min_length + offset + offset2
                    offset2 += 1


            #print()
            if to_skip == 0:
                to_skip = best - 1
                list.append([dictionary[to_encode[i:i+best]][0], best])
            else:
                to_skip -= 1
            i += 1

    #print(dictionary)
    #print(list)
    return list

#@jit(nopython=True)
def decode_encoded_list(encoded_list):
    decoded_list = []
    for x in encoded_list:
        if isinstance(x, list):
            for y in range(x[1]):
                #print(x[0] + y)
                #print(decoded_list[x[0] + y])
                decoded_list.append(decoded_list[x[0] + y])
        else:
            decoded_list.append(x)
    return decoded_list

#@jit(nopython=True)
def build_encoded_string_from_list(encoded_list):
    encoded_string = ""
    #print(encoded_list)
    for x in encoded_list:
        if isinstance(x, list):
            encoded_string += "~" + chr(x[0]) + chr(x[1])
        else:
            encoded_string += x
    return encoded_string

#@jit(nopython=True)
def build_encoded_list_from_encoded_string(encoded_string):
    i = 0
    encoded_list = []
    #print(encoded_string)
    while i < len(encoded_string):
        if encoded_string[i] == "\\":
            encoded_list.append(encoded_string[i])
            encoded_list.append(encoded_string[i+1])
            i += 1

        elif encoded_string[i] != "~":
            encoded_list.append(encoded_string[i])
        else:
            encoded_list.append([ord(encoded_string[i+1]), ord(encoded_string[i+2])])
            #if ord(encoded_string[i+1]) == 99:
                #Z = encoded_string[i:i+3]
               # print(Z)
                #print()
            i += 2
        i += 1
    #print(encoded_list)
    return encoded_list


def compress(to_compress, min_length=4):
    encoded = build_encoded_list(escape(to_compress), min_length=min_length)
    encoded_string = build_encoded_string_from_list(encoded)

    return encoded_string, encoded


def uncompress(encoded_string):
    encoded_list = build_encoded_list_from_encoded_string(encoded_string)
    decoded = decode_encoded_list(encoded_list)
    return decoded, encoded_list

'''
encoded = build_encoded_list(escape(to_compress), min_length=4)
encoded_string = build_encoded_string_from_list(encoded)
encoded_list = build_encoded_list_from_encoded_string(encoded_string)

print(encoded_list == encoded)

#for i in range(len(encoded)):
#    if encoded_list[i] != encoded[i]:
#        print(encoded[i], encoded_list[i])

decoded = decode_encoded_list(encoded_list)
'''

encoded_string, encoded = compress(to_compress, min_length=4)
decoded, encoded_list = uncompress(encoded_string)

max = 0
index = 0
for x in encoded:
    if isinstance(x, list):
        if x[1] > max:
            max = x[1]
            index = x[0]

times = 0
for x in range(len(to_compress)):
    if to_compress[index:index + max] == to_compress[x:x + max]:
        times += 1

str = ""
print("uncompressed:", len(to_compress))
print("compressed:", len(encoded_string))
print("ratio:", len(encoded_string)/(len(to_compress)))
print("Lossless =", unescape(str.join(decoded)) == to_compress)
print("Longest run: occurances:", times, ", length =", max)