from langchain.prompts import PromptTemplate

prompt_template_classic = PromptTemplate.from_template(
    """Contexte : Agis comme un analyste économique experts et utilise la structure décrit pour transformer des données économiques brutes , incluant des mots - clés et des chiffres -clés , en une analyse article economique suivant les templates donneés focalisée sur les perceptions et anticipations d' inflation .



Tâche : écrire un acticle de sur l'anticipation de l'inflation .
Mots -clés / Chiffres -clés : 

{informations}


Structure :

Titre : Anticipations d'inflation [Annee][trimestrie(T1,T2,T3,T4)]

un resumes sur les pourcentage de l’inflation comme l'example suivant : 
""
Les anticipations d'inflation des chefs d'entreprise reviennent à 5% à l'horizon 1 an et se maintiennent à 3 % à l'horizon 3-5 ans
""
Paragraphe nommée : "Perception et anticipations des entreprises sur l'inflation en France (prix à la consommation)" comme l'example suivant : 
""
Notre Enquête trimestrielle sur les anticipations d'inflation (définie ici comme la hausse de l'indice des prix à la consommation), qui constitue un module de l'Enquête de Conjoncture de la Banque de France, a été menée du 24 février au 3 mars. Au premier trimestre 2023, la médiane de l'inflation perçue par les chefs d'entreprise se situe à 6,0 %, soit un peu en dessous de l'IPC mesuré par l'Insee pour février (6,3 %). Leur anticipation médiane à un an s'établit à 5,0 %, et celle à moyen terme - horizon 3 à 5 ans - à 3,0 %.
""

Paragraphe nommée : "Croissance des salaires de base à un an anticipée par les chefs d'entreprise" comme l'example suivant 
""
Les chefs d'entreprise anticipent une croissance des salaires de base dans leur entreprise de 3,5 % à un an (médiane), en augmentation de 0,5 pp par rapport à l'anticipation médiane du trimestre précédent mais toujours inférieure à celles enregistrées entre la mi-2022 et la mi-2023. Les réponses anticipant une augmentation des salaires comprise entre 3 % et 4 % rassemblent 54% de la distribution et progressent de 9 pp sur un trimestre, alors que la proportion de celles anticipant une hausse supérieure à 4% est en baisse de 10 pp.
""

Paragraphe nommée : "Méthodologie" comme l'exemple suivant ou on doit juste changer la date 
""
Cette enquête a été menée du 28 novembre au 5 décembre auprès d'un échantillon représentatif de 1 700 chefs d'entreprise. Elle couvre trois grands secteurs marchands de l'économie et des entreprises de toutes tailles et de toutes régions de France métropolitaine. Les opinions des chefs d'entreprise sont recueillies par téléphone au cours de l'entretien mensuel de conjoncture de l'Enquête Mensuelle de Conjoncture et chaque chef d'entreprise est interrogé une seule fois par an sur ce module. Quatre questions leur sont posées :
1 - En pourcentage, quel est selon vous le taux d'inflation actuel en France ?
2 - En pourcentage, quel sera selon vous le taux d'inflation dans un an en France ?
3 - En pourcentage, quel sera selon vous le taux d'inflation dans 3 à 5 ans en France ?
4 - En pourcentage, quelle sera selon vous l'évolution des salaires de base (bruts, hors primes) dans votre entreprise sur les 12 prochains mois ?

Pour mémoire, le salaire de base correspond au salaire brut avant déduction des cotisations sociales et avant versement des prestations sociales. Il ne comprend ni les primes ni les heures supplémentaires.

Les données sont tronquées au 99ème centile. Pour le calcul des résultats, les réponses sont pondérées en fonction des effectifs moyens et de l'importance relative de chaque entreprise au sein de sa branche, puis par les poids respectifs des branches professionnelles en termes de valeur ajoutée au niveau des agrégats.

""



"""
)


