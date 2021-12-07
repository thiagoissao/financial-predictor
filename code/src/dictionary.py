negate = ["não é", "não pode", "não posso", "não poderia", "não posso",
          "não podia", "não me atrevia", "não tinha", "não era", "não podia", "não devia",
          "nem", "não tenho", "não posso", "não devo", "não preciso",
          "nunca", "nenhum", "nem", "nada", "lugar nenhum", "não deveria", "não era",
          "deveria", "sem", "não", "não faria", "não ",
          "não faria", "raramente", "raramente", "apesar de", "ninguém"]


# Loughran and McDonald Sentiment Word Lists (https://sraf.nd.edu/textual-analysis/resources/)
lmdict = {
    'Negative': [
        'mínima',
        'queda',
        'pessimista',
        'cai',
        'caírem',
        'dólar subiu',
        'dólar subir',
        'afundou',
        'caem',
        'desvalorizou',
        'desvalorização',
        'volatilidade',
        'abandonar',
        'abandono',
        'abdicado',
        'abdica',
        'aberrante',
        'aberração',
        'aberracional',
        'aberrações',
        'cumplicidade',
        'anormal',
        'anormalidades',
        'anormalidade',
        'anormalmente',
        'abolir',
        'abolido',
        'abolindo',
        'revogar',
        'revogação',
        'abrupta',
        'abruptamente',
        'abrupção',
        'ausência',
        'ausências',
        'absenteísmo',
        'abuso',
        'abusado',
        'abusos',
        'abusar',
        'abusivo',
        'abusivamente',
        'abusividade',
        'acidente',
        'acidental',
        'acidentalmente',
        'acidentes',
        'acusação',
        'acusações',
        'acusar',
        'acusado',
        'acusa',
        'aquiesce',
        'absolver',
        'absolvição',
        'absolvições',
        'absolvido',
        'adulterado',
        'adulteração',
        'adversário',
        'adverso',
        'adversamente',
        'adversidades',
        'adversidade',
        'consequências',
        'contra',
        'agravar',
        'alertado',
        'alienado',
        'alienação',
        'alienações',
        'alegação',
        'alegações',
        'alegada',
        'alegadamente',
        'alegando',
        'irritar',
        'aborrecimento',
        'aborrecimentos',
        'aborrecido',
        'irritante',
        'anular',
        'anulado',
        'anulação',
        'anomalias',
        'anômalo',
        'anomalamente',
        'anomalia',
        'anticompetitivo',
        'antitruste',
        'argumentar',
        'argumentado',
        'argumento',
        'argumentativo',
        'argumentos',
        'atraso',
        'atrasos',
        'prisão',
        'preso',
        'prisões',
        'artificialmente',
        'agressão',
        'agredido',
        'agressões',
        'afirmações',
        'atrito',
        'aversamente',
        'retroativo',
        'ruim',
        'fiança',
        'resgate',
        'recusar',
        'falido',
        'falências',
        'falência',
        'proibições',
        'barrado',
        'barreira',
        'barreiras',
        'gargalo',
        'gargalos',
        'boicote',
        'violação',
        'quebra',
        'suborno',
        'ponte',
        'quebrado',
        'fardo',
        'onerado',
        'encargos',
        'pesado',
        'queimado',
        'calamidades',
        'calamitoso',
        'calamidade',
        'cancelar',
        'cancelado',
        'cancelando',
        'descuidado',
        'descuido',
        'catástrofe',
        'catástrofes',
        'catastrófico',
        'catastroficamente',
        'cautela',
        'advertência',
        'cessar',
        'censurar',
        'censurado',
        'censura',
        'desafio',
        'desafiado',
        'desafios',
        'desafiadores',
        'contornar',
        'evasão',
        'evasões',
        'reivindicação',
        'reivindicações',
        'recuperação',
        'fechado',
        'caos',
        'cairem',
        'coagir',
        'coagido',
        'coage',
        'coerção',
        'incerteza',
        'incertezas',
        'coercivo',
        'colapso',
        'colisão',
        'colisões',
        'conivência',
        'conluio',
        'reclamar',
        'reclamação',
        'reclamações',
        'complicar',
        'complicação',
        'complicações',
        'compulsão',
        'ocultado',
        'conceder',
        'concedido',
        'concede',
        'preocupação',
        'interessado',
        'preocupações',
        'conciliação',
        'conciliações',
        'condenar',
        'condena',
        'tolera',
        'confessa',
        'confissão',
        'confinar',
        'confinado',
        'confinamento',
        'confiscar',
        'conflito',
        'conflitos',
        'confronto',
        'confrontos',
        'confrontado',
        'confrontando',
        'confronta',
        'confunde',
        'confuso',
        'confusão',
        'conspirações',
        'conspiração',
        'conspirador',
        'conspiratório',
        'conspiradores',
        'conspirar',
        'desacato',
        'contenda',
        'contendas',
        'contencioso',
        'contestado',
        'contração',
        'contrações',
        'contradizem',
        'contradições',
        'contraditório',
        'contradiz',
        'contrário',
        'controverso',
        'controvérsia',
        'condenado',
        'condenando',
        'convicção',
        'convicções',
        'corrigido',
        'corrigindo',
        'correção',
        'correções',
        'corrige',
        'corrompido',
        'corrupção',
        'corrupções',
        'caro',
        'reconvenção',
        'contrafação',
        'falsificador',
        'contrafactores',
        'contrafacção',
        'contrafacções',
        'contra-medidas',
        'crime',
        'crimes',
        'criminosos',
        'crises',
        'críticas',
        'critica',
        'criticou',
        'crucial',
        'crucialmente',
        'culpabilidade',
        'culpável',
        'restringir',
        'reduzido',
        'redução',
        'corte',
        'ciberataque',
        'ciberataques',
        'cyberbullying',
        'cibercrime',
        'cibercrimes',
        'cibercriminoso',
        'cibercriminosos',
        'danificar',
        'danificado',
        'danos',
        'amortecer',
        'perigo',
        'perigoso',
        'perigosamente',
        'perigos',
        'impasse',
        'peso morto',
        'exclusão',
        'excluído',
        'falecido',
        'fraude',
        'enganoso',
        'engano',
        'enganar',
        'decepções',
        'enganosamente',
        'declínio',
        'desfigurar',
        'difamação',
        'difamatório',
        'difamado',
        'padrão',
        'inadimplente',
        'padrões',
        'derrota',
        'derrotado',
        'defeito',
        'defeituoso',
        'defeitos',
        'defender',
        'réu',
        'réus',
        'defendido',
        'defesa',
        'defensiva',
        'adiar',
        'deficiências',
        'deficiência',
        'deficiente',
        'déficit',
        'déficits',
        'defraudar',
        'defraude',
        'extinto',
        'degradação',
        'degradar',
        'degradado',
        'degrada',
        'degradante',
        'atrasado',
        'deletério',
        'deliberado',
        'deliberadamente',
        'delinquências',
        'delinquência',
        'delinquente',
        'delinquentemente',
        'delinquentes',
        'falecimento',
        'demolir',
        'rebaixar',
        'negar',
        'negado',
        'nega',
        'denegrir',
        'esgotar',
        'depreciação',
        'deprimir',
        'privação',
        'privar',
        'privado',
        'priva',
        'privando',
        'abandonado',
        'depreciativo',
        'desestabilização',
        'desestabilizar',
        'destruir',
        'destruição',
        'destrutivo',
        'deter',
        'detido',
        'detenção',
        'detenções',
        'dissuadir',
        'deteriorar',
        'deterioração',
        'dissuadido',
        'dissuasão',
        'dissuasores',
        'prejudicar',
        'prejudicial',
        'detrimentos',
        'desvalorizar',
        'desvalorizado',
        'devastar',
        'devastado',
        'devastador',
        'devastação',
        'desviar',
        'desvio',
        'desvios',
        'devolver',
        'devolvido',
        'involuir',
        'difícil',
        'dificuldades',
        'dificilmente',
        'dificuldade',
        'diminuir',
        'diminuição',
        'desvantagem',
        'desfavorecido',
        'desvantajoso',
        'desvantagens',
        'desacordo',
        'discordo',
        'desagradável',
        'discorda',
        'discordâncias',
        'disallow',
        'disallowance',
        'disallowances',
        'desautorizar',
        'desaparecer',
        'desaparecimento',
        'desaparecimentos',
        'desapareceu',
        'desaparecendo',
        'desaparece',
        'decepciona',
        'desapontado',
        'decepcionante',
        'desapontador',
        'decepção',
        'desaprovação',
        'desaprova',
        'desaprovado',
        'desassocia',
        'dissociação',
        'desastre',
        'desastres',
        'desastroso',
        'desastrosamente',
        'disciplinar',
        'renunciado',
        'isenção de responsabilidade',
        'renúncia',
        'divulgar',
        'divulgado',
        'divulga',
        'revelando',
        'descontinuidade',
        'descontinuações',
        'descontinuação',
        'descontinuar',
        'descontinuado',
        'desencorajar',
        'desencorajado',
        'desencoraja',
        'desacredita',
        'descrédito',
        'discrepâncias',
        'discrepância',
        'desfavorecer',
        'desfavorece',
        'despeja',
        'vergonha',
        'vergonhoso',
        'vergonhosamente',
        'desonesto',
        'desonestamente',
        'desonestidade',
        'desonra',
        'desonroso',
        'desonrosamente',
        'desonrado',
        'desincentivos',
        'desinteressado',
        'desinteresse',
        'desleal',
        'deslealdade',
        'desanimador',
        'desalentador',
        'despedir',
        'demitindo',
        'desordenada',
        'desacreditar',
        'desacreditado',
        'depreciativa',
        'disparidades',
        'disparidade',
        'desloca',
        'deslocado',
        'deslocamento',
        'deslocamentos',
        'deslocando',
        'dispor',
        'despojar',
        'despossuídos',
        'desapropriados',
        'desproporção',
        'desproporcional',
        'desproporcionalmente',
        'disputa',
        'disputada',
        'desqualificação',
        'desqualificado',
        'desqualifica',
        'desqualificante',
        'desconsiderado',
        'interromper',
        'interrompido',
        'perturbador',
        'perturbação',
        'perturbações',
        'perturba',
        'insatisfação',
        'insatisfeito',
        'dissidentes',
        'dissolução',
        'dissoluções',
        'distorcer',
        'distorcida',
        'distorcendo',
        'distorção',
        'distorções',
        'distorce',
        'distrai',
        'distração',
        'distrações',
        'angústia',
        'angustiado',
        'perturbar',
        'perturbado',
        'desviado',
        'desvia',
        'desinvestimento',
        'desinvestimentos',
        'divórcio',
        'divorciado',
        'dúvida',
        'duvidado',
        'duvidoso',
        'dúvidas',
        'rebaixamento',
        'downgrade',
        'downgrades',
        'downsize',
        'downsized',
        'downsizes',
        'downsizing',
        'downsizings',
        'downtimes',
        'downtsizings',
        'downs',
        'downwards',
        'drag',
        'drástico',
        'drasticamente',
        'caiu',
        'seca',
        'secas',
        'coação',
        'disfunção',
        'disfuncional',
        'disfunções',
        'atenuação',
        'flagrante',
        'flagrantemente',
        'embargo',
        'embargado',
        'embaraço',
        'embaraçado',
        'embaraça',
        'embaraçoso',
        'embaraços',
        'desfalque',
        'usurpe',
        'invada',
        'usurpação',
        'onerar',
        'estorvos',
        'em perigo',
        'ameaça',
        'ordenar',
        'erodir',
        'corroer',
        'erode',
        'erodindo',
        'erosão',
        'errático',
        'erraticamente',
        'errou',
        'errôneo',
        'erroneamente',
        'erro',
        'erros',
        'errar',
        'escalar',
        'evadir',
        'evasivo',
        'despejar',
        'despejado',
        'despejo',
        'despejos',
        'exacerbar',
        'exacerbando',
        'exacerbação',
        'exacerbações',
        'exagerar',
        'excessivo',
        'excessivamente',
        'desculpar',
        'desculpam',
        'exoneram',
        'exonera',
        'explora',
        'exploração',
        'explorações',
        'explorador',
        'explorado',
        'explorando',
        'expor',
        'exposta',
        'expõe',
        'expondo',
        'expropria',
        'expropriação',
        'expropriações',
        'expulsão',
        'expulsões',
        'reprovação',
        'falha',
        'falhas',
        'precipitação',
        'falso',
        'falsamente',
        'falsificação',
        'falsificações',
        'falsificado',
        'falsifica',
        'falsidade',
        'fatalidades',
        'fatalidade',
        'fatalmente',
        'medo',
        'medos',
        'criminoso',
        'fictício',
        'multado',
        'multas',
        'demitido',
        'demissão',
        'imperfeito',
        'proibir',
        'proibido',
        'forçar',
        'forçado',
        'foreclosed',
        'forecloses',
        'foreclosure',
        'forego',
        'foregoes',
        'foregone',
        'antecipar',
        'desistir',
        'perdidos',
        'falsificadores',
        'fraudes',
        'fraudulento',
        'frívolo',
        'levianamente',
        'frustrar',
        'frustração',
        'frustrações',
        'fugitivos',
        'gratuitos',
        'gratuitamente',
        'queixas',
        'grosseiramente',
        'sem fundamento',
        'culpado',
        'parar',
        'dificultar',
        'dificulta',
        'assedia',
        'assediado',
        'assédio',
        'sofrimento',
        'dano',
        'prejudicado',
        'severo',
        'mais severo',
        'severamente',
        'aspereza',
        'atrapalhar',
        'obstáculo',
        'obstáculos',
        'hostil',
        'hostilidade',
        'ferir',
        'ocioso',
        'ignorar',
        'ignorado',
        'ignora',
        'ignorando',
        'mal',
        'ilegal',
        'ilegalidades',
        'ilegalidade',
        'ilegalmente',
        'ilegível',
        'ilícito',
        'ilicitamente',
        'ilíquido',
        'iliquidez',
        'desequilíbrio',
        'desequilíbrios',
        'imaturo',
        'imoral',
        'impedimentos',
        'prejudicam',
        'impasses',
        'impedem',
        'impedimento',
        'impedindo',
        'iminente',
        'imperativo',
        'imperfeição',
        'imperfeições',
        'inadmissível',
        'implicar',
        'implicado',
        'impossibilidade',
        'impossível',
        'apreendido',
        'impraticável',
        'impraticabilidade',
        'impróprio',
        'indevidamente',
        'impropriedades',
        'impropriedade',
        'imprudente',
        'imprudentemente',
        'incapacidade',
        'inacessível',
        'imprecisões',
        'imprecisão',
        'impreciso',
        'inação',
        'inativar',
        'inativado',
        'inativa',
        'inativação',
        'inativações',
        'inatividade',
        'inadequações',
        'inadequação',
        'inadequada',
        'inadvertida',
        'inadvertidamente',
        'inadvisibilidade',
        'desaconselhável',
        'inapropriado',
        'inadequadamente',
        'desatenção',
        'incapaz',
        'incapacitado',
        'encarcerado',
        'encarceramentos',
        'incidência',
        'incidentes',
        'incompatibilidades',
        'incompatibilidade',
        'incompatível',
        'incompetência',
        'incompetente',
        'incompetentemente',
        'incompetentes',
        'incompletos',
        'inconclusivos',
        'inconsistências',
        'inconsistência',
        'inconsistente',
        'inconveniência',
        'inconveniências',
        'inconveniente',
        'incorreto',
        'incorretamente',
        'indecência',
        'indecente',
        'irrevogável',
        'indefensável',
        'indiciar',
        'acusável',
        'indiciado',
        'ineficaz',
        'inefetividade',
        'ineficiências',
        'ineficiência',
        'ineficiente',
        'inelegibilidade',
        'inelegível',
        'desigual',
        'injustificadamente',
        'iniquidades',
        'iniquidade',
        'inevitável',
        'inexperiência',
        'inexperiente',
        'inferior',
        'infligido',
        'infração',
        'infrações',
        'infringir',
        'infringido',
        'infracções',
        'infringe',
        'inibido',
        'injunção',
        'injunções',
        'ferido',
        'desordenado',
        'inquérito',
        'inseguro',
        'insensível',
        'insolvências',
        'insolvência',
        'insolvente',
        'instabilidade',
        'insubordinação',
        'insuficiência',
        'insuficiente',
        'insurreição',
        'insurreições',
        'intencional',
        'interferir',
        'interferência',
        'interferências',
        'interfere',
        'intermitente',
        'intermitentemente',
        'interrompendo',
        'interrupção',
        'interrupções',
        'intimidação',
        'intrusão',
        'inválido',
        'invalidar',
        'invalidado',
        'invalida',
        'invalidando',
        'invalidação',
        'invalidez',
        'investigar',
        'investigado',
        'investiga',
        'investigando',
        'investigação',
        'investigações',
        'involuntariamente',
        'involuntário',
        'irreconciliável',
        'irrecuperável',
        'irregular',
        'irregularidades',
        'irregularidade',
        'irregularmente',
        'irreparável',
        'irreparavelmente',
        'irreversível',
        'comprometido',
        'justificável',
        'propina',
        'propinas',
        'conscientemente',
        'falta',
        'sem brilho',
        'lapso',
        'caducado',
        'lapsos',
        'lavagem',
        'dispensa',
        'mentira',
        'limitação',
        'limitações',
        'remanescente',
        'liquidar',
        'liquidações',
        'liquidatário',
        'liquidatários',
        'litigante',
        'litigantes',
        'litigam',
        'litigaram',
        'litígios',
        'bloqueio',
        'bloqueios',
        'perder',
        'perdendo',
        'perda',
        'perdas',
        'perdido',
        'mentindo',
        'mau funcionamento',
        'malícia',
        'malicioso',
        'maliciosamente',
        'negligência',
        'manipular',
        'manipulação',
        'manipulações',
        'manipulativo',
        'remarcação',
        'aplicação incorreta',
        'aplicação indevida',
        'apropriação indevida',
        'apropriação indébita',
        'marca incorreta',
        'cálculo incorreto',
        'descaracterização',
        'classificação incorreta',
        'comunicação incorreta',
        'conduta imprópria',
        'data incorreta',
        'contravenção',
        'contravenções',
        'mal direcionado',
        'maltratado',
        'mal informado',
        'desinformação',
        'interpretação incorreta',
        'misinterpretation',
        'misinterpretations',
        'misinterpreted',
        'erro de julgamento',
        'rótulo incorreto',
        'rotulado incorretamente',
        'induzir em erro',
        'enganadoramente',
        'engana',
        'má gestão',
        'mismatch',
        'mismatched',
        'mismatches',
        'misplaced',
        'misprice',
        'mispricing',
        'deturpação',
        'perdida',
        'passo errado',
        'passos errados',
        'por engano',
        'anulação do julgamento',
        'mal-entendido',
        'mal compreendido',
        'mau uso',
        'mal usado',
        'monopolista',
        'monopolistas',
        'monopolização',
        'monopolizar',
        'monopoliza',
        'monopólio',
        'moratória',
        'moratórias',
        'mothballed',
        'mothballing',
        'negativado',
        'negativamente',
        'negativo',
        'negligenciado',
        'negligente',
        'negligencia',
        'não realização',
        'não competitivo',
        'não conformidade',
        'não conforme',
        'não-conformidades',
        'não-conformidade',
        'não divulgação',
        'não funcional',
        'não pagamento',
        'não desempenho',
        'sem desempenho',
        'não produtivo',
        'não recuperável',
        'não renovável',
        'incômodo',
        'incômodos',
        'anula',
        'anulando',
        'objetou',
        'objeção',
        'questionável',
        'objeções',
        'obsceno',
        'obscenidade',
        'obsolescência',
        'obsoleto',
        'obstruir',
        'obstrução',
        'obstruções',
        'ofensa',
        'ofensas',
        'ofender',
        'ofendido',
        'ofensor',
        'infratores',
        'omissão',
        'omissões',
        'omitir',
        'omitido',
        'oneroso',
        'oportunista',
        'opor-se',
        'oposição',
        'oposições',
        'desatualizado',
        'antiquado',
        'overage',
        'overages',
        'overbuild',
        'overbuilding',
        'overbuilds',
        'sobrecarregado',
        'excesso de capacidade',
        'sobrecarregar',
        'superar',
        'superação',
        'superestimar',
        'superestimação',
        'superestimações',
        'sobrecarga',
        'sobrecarregando',
        'sobrecargas',
        'negligenciar',
        'pago em excesso',
        'pagamento em excesso',
        'pagamentos em excesso',
        'superproduzida',
        'superproduz',
        'superprodução',
        'supera',
        'ofusca',
        'superestima',
        'exagerado',
        'exagero',
        'excesso de oferta',
        'abertamente',
        'derrubada',
        'revertido',
        'reviravolta',
        'reviravoltas',
        'sobrevalorizar',
        'pânico',
        'penalizar',
        'penalidades',
        'penalidade',
        'perjúrio',
        'perpetrar',
        'persistir',
        'persistente',
        'persistência',
        'persistentemente',
        'persiste',
        'penetrante',
        'generalizado',
        'penetração',
        'mesquinho',
        'piquete',
        'reclamante',
        'demandantes',
        'apelo',
        'contestação',
        'pobre',
        'posar',
        'adia',
        'precipitado',
        'precipitadamente',
        'impede',
        'impedido',
        'predatório',
        'preconceito',
        'preconceituoso',
        'prematuro',
        'prematuramente',
        'pressionando',
        'pré-julgamento',
        'prevenção',
        'previne',
        'problema',
        'problemático',
        'problemas',
        'prolongar',
        'prolongamento',
        'prolongamentos',
        'prolongado',
        'prolongando',
        'prolonga',
        'propenso',
        'processar',
        'processado',
        'protestado',
        'manifestante',
        'manifestantes',
        'protestando',
        'protestador',
        'protestos',
        'provocar',
        'provocou',
        'provoca',
        'provocando',
        'punido',
        'pune',
        'punição',
        'punições',
        'punitiva',
        'suposto',
        'supostamente',
        'questionado',
        'questionamento',
        'perguntas',
        'extorsão',
        'racionalização',
        'racionaliza',
        'reavaliação',
        'reavaliações',
        'reatribuir',
        'reassignments',
        'reassigns',
        'recall',
        'recalls',
        'recessão',
        'recessivo',
        'recessões',
        'imprudência',
        'redigir',
        'redigido',
        'redigindo',
        'redação',
        'redações',
        'redefinir',
        'corrigir',
        'reparado',
        'recusado',
        'rejeitar',
        'rejeitado',
        'rejeição',
        'rejeições',
        'renunciar',
        'renúncias',
        'relutância',
        'relutante',
        'renegociar',
        'renegociação',
        'renegociações',
        'reparação',
        'reparações',
        'reintegração de posse',
        'repudiar',
        'repudia',
        'renuncia',
        'renunciou',
        'reafirmou',
        'reafirmação',
        'reafirmações',
        'reafirma',
        'reestruturar',
        'reestruturação',
        'reestruturações',
        'retaliação',
        'retaliações',
        'retribuição',
        'retribuições',
        'revogações',
        'ridicularizar',
        'mais arriscado',
        'arriscado',
        'sabotagem',
        'sacrifício',
        'sacrificado',
        'sacrifícios',
        'escandaloso',
        'escândalos',
        'escrutinar',
        'escrutinado',
        'examinado',
        'sigilo',
        'apreender',
        'apreensão',
        'sentença',
        'sério',
        'seriedade',
        'revés',
        'contratempos',
        'severa',
        'cortada',
        'severidades',
        'severidade',
        'acentuada',
        'chocado',
        'escassez',
        'encolhimento',
        'desligar',
        'fechar',
        'caluniar',
        'calunioso',
        'caluniador',
        'deslizamento',
        'deslizamentos',
        'lento',
        'desaceleração',
        'desacelerações',
        'desacelerado',
        'mais lento',
        'lentidão',
        'solvências',
        'solvência',
        'spam',
        'spammers',
        'spamming',
        'escalonamento',
        'estagnado',
        'estagnação',
        'paralisação',
        'paralisações',
        'roubado',
        'paradas',
        'parado',
        'parando',
        'tensão',
        'tenso',
        'tensões',
        'estresse',
        'estressado',
        'estressante',
        'rigoroso',
        'submetido',
        'sujeitar',
        'sujeição',
        'intimação',
        'intimado',
        'intimações',
        'abaixo do padrão',
        'processa',
        'sofre',
        'sofreu',
        'convoca',
        'convocação',
        'suscetibilidade',
        'suscetível',
        'suspeito',
        'suspeitos',
        'suspender',
        'suspensão',
        'suspensões',
        'suspeita',
        'suspeitas',
        'contaminado',
        'encerrar',
        'encerrado',
        'testemunhar',
        'ameaçar',
        'ameaças',
        'endurecimento',
        'tolerar',
        'tolerância',
        'tortuoso',
        'tortuosamente',
        'tragédias',
        'tragédia',
        'trágico',
        'tragicamente',
        'traumático',
        'turbulência',
        'inaceitável',
        'inaceitavelmente',
        'não contabilizado',
        'não anunciado',
        'não antecipado',
        'não aprovado',
        'não atraente',
        'não autorizado',
        'indisponibilidade',
        'indisponível',
        'inevitavelmente',
        'desconhecido',
        'incobrável',
        'incompleto',
        'inescrupuloso',
        'inescrupulosamente',
        'incontrolável',
        'incontrolavelmente',
        'não controlado',
        'não corrigido',
        'descobrir',
        'impossibilidade de entrega',
        'undelivered',
        'undercapitalized',
        'undercut',
        'undercuts',
        'undercutting',
        'subestimar',
        'subestimado',
        'subfinanciado',
        'mal pago',
        'underpayment',
        'underpayments',
        'underpays',
        'underperform',
        'underperformance',
        'underperforming',
        'underperforms',
        'underproduced',
        'underproduction',
        'subavaliação',
        'subestimação',
        'subestima',
        'subutilização',
        'subutilizado',
        'indesejável',
        'indetectado',
        'indeterminado',
        'não divulgado',
        'indocumentado',
        'indevido',
        'não econômico',
        'antieconômico',
        'antiético',
        'desempregado',
        'desemprego',
        'não justificado',
        'inesperado',
        'inesperadamente',
        'injusto',
        'injustamente',
        'desfavorável',
        'inviável',
        'inaptidão',
        'imprevisível',
        'imprevisto',
        'infeliz',
        'infelizmente',
        'infundado',
        'não realizado',
        'não financiado',
        'não segurado',
        'não intencional',
        'não intencionalmente',
        'injustificável',
        'injustificado',
        'não saber',
        'sem saber',
        'não licenciado',
        'não liquidado',
        'não comercializável',
        'não meritório',
        'desnecessariamente',
        'desnecessário',
        'inalcançável',
        'desocupado',
        'não pago',
        'não executado',
        'não planejado',
        'impopular',
        'imprevisibilidade',
        'imprevisivelmente',
        'improdutivo',
        'não lucrativo',
        'não qualificado',
        'irrealista',
        'irracional',
        'não recuperado',
        'não reembolsado',
        'não confiável',
        'não remediada',
        'não relatado',
        'não resolvido',
        'inquietação',
        'invendável',
        'insatisfatório',
        'não programado',
        'não vendível',
        'não vendido',
        'não sólido',
        'não estabilizado',
        'instável',
        'sem sucesso',
        'não adequado',
        'insuspeito',
        'desavisado',
        'insustentável',
        'inoportuno',
        'inverdade',
        'mentiroso',
        'inverdades',
        'inutilizável',
        'indesejado',
        'indisposto',
        'indisposição',
        'chateado',
        'urgência',
        'urgente',
        'usurário',
        'usurpar',
        'usura',
        'vandalismo',
        'veredicto',
        'veredictos',
        'vetados',
        'vítimas',
        'violar',
        'violado',
        'violações',
        'violativo',
        'violador',
        'violadores',
        'violência',
        'violento',
        'violentamente',
        'viciado',
        'agravamento',
        'esvaziado',
        'volátil',
        'volatilidade',
        'vulnerabilidades',
        'vulnerabilidade',
        'vulnerável',
        'vulneravelmente',
        'avisar',
        'avisado',
        'aviso',
        'avisos',
        'desperdiçado',
        'desperdício',
        'fraco',
        'enfraquecido',
        'enfraquecimento',
        'enfraquece',
        'mais fraco',
        'fraqueza',
        'se preocupa',
        'pior',
        'piora',
        'inútil',
        'baixa',
        'errado',
        'coronavírus'
    ],
    'Positive': [
        'otimismo',
        'máxima',
        'capaz',
        'alta',
        'abundância',
        'abundante',
        'aclamado',
        'realizado',
        'realizando',
        'realização',
        'realizações',
        'alcançar',
        'alcançado',
        'adequadamente',
        'avanço',
        'avanços',
        'avançando',
        'vantagem',
        'vantajoso',
        'vantajosamente',
        'vantagens',
        'aliança',
        'alianças',
        'assegurar',
        'assegurado',
        'assegura',
        'assegurando',
        'atingir',
        'atingindo',
        'atinge',
        'atraente',
        'manter',
        'atratividade',
        'belo',
        'lindamente',
        'benéfico',
        'benefício',
        'beneficiado',
        'beneficiando',
        'melhor',
        'reforçado',
        'boom',
        'crescendo',
        'boost',
        'boosted',
        'breakthrough',
        'breakthroughs',
        'brilhante',
        'caridoso',
        'colaborar',
        'estável',
        'colaborou',
        'colabora',
        'colaborando',
        'colaboração',
        'colaborações',
        'colaborativo',
        'colaborador',
        'colaboradores',
        'elogio',
        'complementar',
        'elogiado',
        'elogios',
        'conclusivo',
        'conducente',
        'confiante',
        'construtivo',
        'construtivamente',
        'cortês',
        'criativo',
        'criativamente',
        'criatividade',
        'deleite',
        'encantado',
        'delicioso',
        'deliciosamente',
        'encantando',
        'delícias',
        'confiabilidade',
        'confiável',
        'desejável',
        'desejado',
        'apesar de',
        'destinado',
        'diligente',
        'diligentemente',
        'distinção',
        'azul',
        'distinções',
        'distinto',
        'distintamente',
        'sonho',
        'mais fácil',
        'facilmente',
        'fácil',
        'eficaz',
        'eficiências',
        'eficiência',
        'eficiente',
        'eficientemente',
        'capacitar',
        'habilitar',
        'habilitando',
        'encorajado',
        'encorajamento',
        'incentiva',
        'encorajando',
        'melhorar',
        'aprimorado',
        'aprimoramento',
        'aprimoramentos',
        'desfrutar',
        'agradável',
        'curtiu',
        'curtindo',
        'gozo',
        'goza',
        'entusiasmo',
        'entusiasmado',
        'entusiasticamente',
        'excelência',
        'excelente',
        'excepcional',
        'excepcionalmente',
        'emoção',
        'emocionante',
        'exclusivo',
        'exclusivamente',
        'exclusividade',
        'exclusividades',
        'exemplar',
        'fantástico',
        'favorável',
        'favorecido',
        'favorito',
        'favoritos',
        'amigável',
        'ganho',
        'ganhos',
        'bom',
        'ótimo',
        'maior',
        'grandemente',
        'grandeza',
        'mais feliz',
        'feliz',
        'felicidade',
        'mais elevado',
        'honra',
        'honrado',
        'honras',
        'ideal',
        'impressionar',
        'impressionado',
        'impressiona',
        'impressionando',
        'impressionante',
        'impressionantemente',
        'melhora',
        'melhorou',
        'melhoria',
        'melhorias',
        'incrível',
        'incrivelmente',
        'influente',
        'informativo',
        'engenhosidade',
        'inovar',
        'inovação',
        'inovações',
        'inovador',
        'capacidade de inovação',
        'inovadores',
        'perspicaz',
        'inspiração',
        'inspirador',
        'integridade',
        'inventar',
        'inventado',
        'inventando',
        'invenção',
        'invenções',
        'inventivo',
        'inventividade',
        'inventor',
        'inventores',
        'liderança',
        'líder',
        'leal',
        'lucrativo',
        'meritório',
        'oportunidades',
        'oportunidade',
        'otimista',
        'outperform',
        'outperformed',
        'outperforming',
        'outperforms',
        'perfect',
        'aperfeiçoado',
        'perfeitamente',
        'aperfeiçoa',
        'agradavelmente',
        'satisfeito',
        'prazer',
        'popular',
        'popularidade',
        'positiva',
        'positivamente',
        'preeminência',
        'preeminente',
        'premier',
        'estreia',
        'prestígio',
        'prestigioso',
        'proativo',
        'proficiência',
        'proficiente',
        'proficientemente',
        'lucratividade',
        'lucrativamente',
        'progresso',
        'progrediu',
        'progride',
        'prosperou',
        'prosperidade',
        'próspero',
        'prospera',
        'rebote',
        'receptivo',
        'recupera',
        'resolve',
        'revolucionar',
        'recompensar',
        'recompensador',
        'recompensa',
        'satisfação',
        'satisfatoriamente',
        'satisfatório',
        'satisfaz',
        'suaviza',
        'suavemente',
        'resolvendo',
        'espetacular',
        'espetacularmente',
        'estabilidade',
        'estabilização',
        'estabilizações',
        'estabilizar',
        'estável',
        'força',
        'fortalecer',
        'fortalecido',
        'fortalecendo',
        'fortalece',
        'forte',
        'mais forte',
        'sucesso',
        'superior',
        'ultrapassar',
        'transparência',
        'tremendo',
        'tremendamente',
        'incomparável',
        'insuperável',
        'subida',
        'subidas',
        'valioso',
        'versátil',
        'versatilidade',
        'vibração',
        'vibrante',
        'ganhar',
        'vencedor',
        'vencedores',
        'digno',
    ],
}