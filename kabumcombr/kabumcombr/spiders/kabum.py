# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from scrapy_splash import SplashRequest


class KabumSpider(Spider):
    name = 'kabum'
    allowed_domains = ['kabum.com.br']
    options = '?pagina=1&ordem=5&limite=100000&prime=false'
    CAT_LIMIT   = 3     # 0 - NO limit
    ITEM_LIMIT  = 10    # Use this variables to control how deep the spider goes
    start_urls = ['https://www.kabum.com.br/hardware/coolers',
    'https://www.kabum.com.br/hardware/disco-rigido-hd',
    'https://www.kabum.com.br/hardware/drives',
    'https://www.kabum.com.br/hardware/fontes',
    'https://www.kabum.com.br/hardware/memoria-ram',
    'https://www.kabum.com.br/hardware/placa-de-video-vga',
    'https://www.kabum.com.br/hardware/placa-usb',
    'https://www.kabum.com.br/hardware/placas-de-som',
    'https://www.kabum.com.br/hardware/placas-mae',
    'https://www.kabum.com.br/hardware/processadores',
    'https://www.kabum.com.br/hardware/rede-wired-com-fio',
    'https://www.kabum.com.br/hardware/rede-wireless-sem-fio',
    'https://www.kabum.com.br/hardware/ssd-2-5',
    'https://www.kabum.com.br/hardware/switch-kvm',
    'https://www.kabum.com.br/perifericos/acessorios',
    'https://www.kabum.com.br/perifericos/adaptadores',
    'https://www.kabum.com.br/perifericos/cabos',
    'https://www.kabum.com.br/perifericos/energia',
    'https://www.kabum.com.br/perifericos/escritorio',
    'https://www.kabum.com.br/perifericos/gabinetes',
    'https://www.kabum.com.br/perifericos/headset-gamer',
    'https://www.kabum.com.br/perifericos/kit-gamer',
    'https://www.kabum.com.br/perifericos/mesa-digitalizadora',
    'https://www.kabum.com.br/perifericos/bolsas',
    'https://www.kabum.com.br/perifericos/-mouse-gamer',
    'https://www.kabum.com.br/perifericos/pen-drive',
    'https://www.kabum.com.br/perifericos/som-acessorios',
    'https://www.kabum.com.br/perifericos/streamer',
    'https://www.kabum.com.br/perifericos/suportes',
    'https://www.kabum.com.br/perifericos/suprimentos',
    'https://www.kabum.com.br/perifericos/teclado-mouse',
    'https://www.kabum.com.br/perifericos/teclado-gamer',
    'https://www.kabum.com.br/perifericos/video-conferencia',
    'https://www.kabum.com.br/perifericos/webcam',
    'https://www.kabum.com.br/gamer/cadeiras-gamer',
    'https://www.kabum.com.br/gamer/e-sports',
    'https://www.kabum.com.br/gamer/mesa-gamer',
    'https://www.kabum.com.br/gamer/nintendo-switch',
    'https://www.kabum.com.br/gamer/pc',
    'https://www.kabum.com.br/gamer/playstation-4',
    'https://www.kabum.com.br/gamer/playstation-5',
    'https://www.kabum.com.br/gamer/tectoy',
    'https://www.kabum.com.br/gamer/xbox-360',
    'https://www.kabum.com.br/gamer/xbox-one',
    'https://www.kabum.com.br/gamer/xbox-series',
    'https://www.kabum.com.br/cadeiras/cadeiras-gamer',
    'https://www.kabum.com.br/cadeiras/cadeiras-office',
    'https://www.kabum.com.br/computadores/computadores',
    'https://www.kabum.com.br/computadores/computador-gamer',
    'https://www.kabum.com.br/computadores/impressoras',
    'https://www.kabum.com.br/computadores/monitores',
    'https://www.kabum.com.br/computadores/notebook-gamer',
    'https://www.kabum.com.br/computadores/notebooks-ultrabooks',
    'https://www.kabum.com.br/computadores/scanners',
    'https://www.kabum.com.br/computadores/servidores',
    'https://www.kabum.com.br/computadores/softwares',
    'https://www.kabum.com.br/computadores/tablets',
    'https://www.kabum.com.br/computadores/tablets-acessorios',
    'https://www.kabum.com.br/celular-telefone/celulares',
    'https://www.kabum.com.br/celular-telefone/smartphones',
    'https://www.kabum.com.br/celular-telefone/smartphones-acessorios',
    'https://www.kabum.com.br/celular-telefone/telefones',
    'https://www.kabum.com.br/tv/acessorios-para-tvs',
    'https://www.kabum.com.br/tv/smart-tv',
    'https://www.kabum.com.br/tv/tv-4k',
    'https://www.kabum.com.br/tv/tv-8k',
    'https://www.kabum.com.br/tv/tv-led',
    'https://www.kabum.com.br/tv/tv-monitor',
    'https://www.kabum.com.br/beneficio/prime',
    'https://www.kabum.com.br/eletroportateis/abridor-de-vinho',
    'https://www.kabum.com.br/eletroportateis/acessorios-e-pecas',
    'https://www.kabum.com.br/eletroportateis/adega',
    'https://www.kabum.com.br/eletroportateis/aquecedor',
    'https://www.kabum.com.br/eletroportateis/ar-portatil',
    'https://www.kabum.com.br/eletroportateis/armadilha-para-mosquito',
    'https://www.kabum.com.br/eletroportateis/aspirador-de-po',
    'https://www.kabum.com.br/eletroportateis/aspirador-de-po-portatil',
    'https://www.kabum.com.br/eletroportateis/balanca',
    'https://www.kabum.com.br/eletroportateis/batedeira',
    'https://www.kabum.com.br/eletroportateis/bebedouro',
    'https://www.kabum.com.br/eletroportateis/beleza-e-saude',
    'https://www.kabum.com.br/eletroportateis/blender-shake',
    'https://www.kabum.com.br/eletroportateis/cafeteira',
    'https://www.kabum.com.br/eletroportateis/centrifuga',
    'https://www.kabum.com.br/eletroportateis/cervejeira',
    'https://www.kabum.com.br/eletroportateis/chaleira',
    'https://www.kabum.com.br/eletroportateis/churrasqueira',
    'https://www.kabum.com.br/eletroportateis/churrasqueira-eletrica',
    'https://www.kabum.com.br/eletroportateis/circulador-de-ar',
    'https://www.kabum.com.br/eletroportateis/climatizador',
    'https://www.kabum.com.br/eletroportateis/cooktop',
    'https://www.kabum.com.br/eletroportateis/desumidificador',
    'https://www.kabum.com.br/eletroportateis/espremedor',
    'https://www.kabum.com.br/eletroportateis/ferro-a-seco',
    'https://www.kabum.com.br/eletroportateis/ferro-a-vapor',
    'https://www.kabum.com.br/eletroportateis/ferro-eletrico',
    'https://www.kabum.com.br/eletroportateis/forno-eletrico',
    'https://www.kabum.com.br/eletroportateis/frigobar-',
    'https://www.kabum.com.br/eletroportateis/fritadeira',
    'https://www.kabum.com.br/eletroportateis/fritadeira-sem-oleo',
    'https://www.kabum.com.br/eletroportateis/garrafa-termica',
    'https://www.kabum.com.br/eletroportateis/grill',
    'https://www.kabum.com.br/eletroportateis/kit-cozinha',
    'https://www.kabum.com.br/eletroportateis/limpadora-de-pisos',
    'https://www.kabum.com.br/eletroportateis/liquidificador',
    'https://www.kabum.com.br/eletroportateis/maquina-de-costura',
    'https://www.kabum.com.br/eletroportateis/maquina-de-cupcake',
    'https://www.kabum.com.br/eletroportateis/microondas',
    'https://www.kabum.com.br/eletroportateis/mini-geladeira',
    'https://www.kabum.com.br/eletroportateis/mixer',
    'https://www.kabum.com.br/eletroportateis/moedor-de-cafe',
    'https://www.kabum.com.br/eletroportateis/moedor-de-temperos',
    'https://www.kabum.com.br/eletroportateis/multiprocessador',
    'https://www.kabum.com.br/eletroportateis/omeleteira',
    'https://www.kabum.com.br/eletroportateis/panela-de-arroz',
    'https://www.kabum.com.br/eletroportateis/panela-de-pressao',
    'https://www.kabum.com.br/eletroportateis/panela-eletrica',
    'https://www.kabum.com.br/eletroportateis/panela-fondue-eletrica',
    'https://www.kabum.com.br/eletroportateis/panquequeira',
    'https://www.kabum.com.br/eletroportateis/passadeira-a-vapor',
    'https://www.kabum.com.br/eletroportateis/pipoqueira',
    'https://www.kabum.com.br/eletroportateis/processadores',
    'https://www.kabum.com.br/eletroportateis/purificador-de-agua',
    'https://www.kabum.com.br/eletroportateis/purificador-de-ar',
    'https://www.kabum.com.br/eletroportateis/sanduicheira-e-grill',
    'https://www.kabum.com.br/eletroportateis/seladora-a-vacuo',
    'https://www.kabum.com.br/eletroportateis/torradeira',
    'https://www.kabum.com.br/eletroportateis/tostador',
    'https://www.kabum.com.br/eletroportateis/umidificador',
    'https://www.kabum.com.br/eletroportateis/vaporizador',
    'https://www.kabum.com.br/eletroportateis/ventilador',
    'https://www.kabum.com.br/audio/caixa-de-som',
    'https://www.kabum.com.br/audio/dj',
    'https://www.kabum.com.br/audio/dvd-e-blue-ray',
    'https://www.kabum.com.br/audio/fone-de-ouvido',
    'https://www.kabum.com.br/audio/home-theater',
    'https://www.kabum.com.br/audio/mini-e-micro-system',
    'https://www.kabum.com.br/audio/radio-portatil',
    'https://www.kabum.com.br/audio/soundbar',
    'https://www.kabum.com.br/audio/toca-discos-e-vitrolas',
    'https://www.kabum.com.br/conectividade/access-point',
    'https://www.kabum.com.br/conectividade/adaptador-usb',
    'https://www.kabum.com.br/conectividade/antena',
    'https://www.kabum.com.br/conectividade/cabos',
    'https://www.kabum.com.br/conectividade/conversor-de-midia',
    'https://www.kabum.com.br/conectividade/mini-servidor',
    'https://www.kabum.com.br/conectividade/modem',
    'https://www.kabum.com.br/conectividade/patch-panel',
    'https://www.kabum.com.br/conectividade/placas-de-rede',
    'https://www.kabum.com.br/conectividade/protetor-de-surto',
    'https://www.kabum.com.br/conectividade/radio',
    'https://www.kabum.com.br/conectividade/repetidor',
    'https://www.kabum.com.br/conectividade/roteadores',
    'https://www.kabum.com.br/conectividade/roteadores-wired',
    'https://www.kabum.com.br/conectividade/switches',
    'https://www.kabum.com.br/conectividade/terminal-',
    'https://www.kabum.com.br/conectividade/transceiver',
    'https://www.kabum.com.br/beleza-saude/aparador-de-pelos',
    'https://www.kabum.com.br/beleza-saude/aspirador-nasal-',
    'https://www.kabum.com.br/beleza-saude/assento-ortopedico',
    'https://www.kabum.com.br/beleza-saude/balanca-eletronica',
    'https://www.kabum.com.br/beleza-saude/barbeador',
    'https://www.kabum.com.br/beleza-saude/cortador-de-cabelos',
    'https://www.kabum.com.br/beleza-saude/depilador',
    'https://www.kabum.com.br/beleza-saude/escova-dental',
    'https://www.kabum.com.br/beleza-saude/escova-modeladora',
    'https://www.kabum.com.br/beleza-saude/escova-secadora',
    'https://www.kabum.com.br/beleza-saude/escova-sonica',
    'https://www.kabum.com.br/beleza-saude/fita-kinesio',
    'https://www.kabum.com.br/beleza-saude/inalador',
    'https://www.kabum.com.br/beleza-saude/kit-cuidados-pessoais',
    'https://www.kabum.com.br/beleza-saude/maquina-de-cortar-cabelo',
    'https://www.kabum.com.br/beleza-saude/massageador',
    'https://www.kabum.com.br/beleza-saude/modelador-de-cabelo',
    'https://www.kabum.com.br/beleza-saude/prancha',
    'https://www.kabum.com.br/beleza-saude/relogio',
    'https://www.kabum.com.br/beleza-saude/saude',
    'https://www.kabum.com.br/beleza-saude/secador',
    'https://www.kabum.com.br/beleza-saude/termometro',
    'https://www.kabum.com.br/beleza-saude/umidificadores',
    'https://www.kabum.com.br/eletrodomesticos/adega-de-vinho',
    'https://www.kabum.com.br/eletrodomesticos/bebedouros',
    'https://www.kabum.com.br/eletrodomesticos/chopeira',
    'https://www.kabum.com.br/eletrodomesticos/coifas-e-depuradores',
    'https://www.kabum.com.br/eletrodomesticos/cooktop',
    'https://www.kabum.com.br/eletrodomesticos/fornos-e-fogoes',
    'https://www.kabum.com.br/eletrodomesticos/lava-e-seca-maquina-de-lavar-e-tanquinho']

    def start_requests(self):
        count = 1
        for url in self.start_urls:
            #Just limiting scraped itens during dev times
            if  count > self.CAT_LIMIT > 0:
                break

            count +=1
            yield SplashRequest(url+self.options, self.parse, 
                endpoint='render.html',
                args={'wait': 0.5},
                meta={'category': url.split(sep='/')[-1]}
            )

    def parse(self, response):
        #PRODUCT LINES BLOCK
        #//div[@id="listagem-produtos"]/div/div/div
        products = response.xpath('//div[@id="listagem-produtos"]/div/div')
        count = 1
        for product in products:
            #TODO: The first 2 divs and the last one should be discarted, the following if do that in an ugly way.
            #if you are code reviewing you could try to use [2:] instead
            if count <= 2:
                count +=1
                continue

            #Just limiting scrapped itens during dev time
            if count > self.ITEM_LIMIT > 0:
                break
            # ./div/a/img           - image
            # ./div/div[1]/a        - name
            # ./div/div[1]/a        - link
            img = product.xpath('./div/a/img/@src').extract_first()

            name = product.xpath('./div/div[1]/a/text()').extract_first()
            link = response.urljoin( product.xpath('./div/div[1]/a/@href').extract_first() )

            #PRICING BLOCK
            #./div/div[2]/div[1]
            pblock = './div/div[2]/div[1]'
            #                   ./div[1] Old Price (Occurs 0-1)   ->  If is not present, the other divs should be re-indexed
            #                   ./div[2] Price (Occurs aways)
            #                   ./div[3] Installment (Occurs aways)
            #                   ./div[4] Cash Price (Occurs aways)
            #                   ./div[5] Cash Payment Type (Occurs aways)

            old_price =         product.xpath(pblock+'/div[1]/text()').extract_first()
            if old_price is not None and old_price != '' and old_price.find('De') and old_price.find('por'):
                #that means the div[1] is really an old price
                #there is an old price and thus 5 div are shown
                price =         product.xpath(pblock+'/div[2]/text()').extract_first()
                installment =   product.xpath(pblock+'/div[3]/text()').extract_first()
                cash =          product.xpath(pblock+'/div[4]/text()').extract_first()
                cash_tpay =     product.xpath(pblock+'/div[5]/text()').extract_first()
            else:
                #there is no old price and thus 4 div are shown
                old_price = ''
                price =         product.xpath(pblock+'/div[1]/text()').extract_first()
                installment =   product.xpath(pblock+'/div[2]/text()').extract_first()
                cash =          product.xpath(pblock+'/div[3]/text()').extract_first()
                cash_tpay =     product.xpath(pblock+'/div[4]/text()').extract_first()

            count += 1
            yield {
                'category': response.meta['category'],
                'name': name, 
                'link': link, 
                'img': img, 
                'old_price': old_price, 
                'price': price, 
                'installment': installment, 
                'cash': cash,
                'cash_tpay': cash_tpay
            }

        #TODO: When a product page is loaded, I'm passing 'opstions' variable to include 100.000 products in one page
        #that should be enough, but if there are more that that, we should consider inplement this next page code
        # more_pages = response.xpath('//div[contains(text(),"Próxima")]/@disabled=""').extract_first()
        # # 0 means there is still pages to be parsed
        # # 1 means there is no page
        # if more_pages == 0:
        #     page_count += 1
        #     next_page_url = response.urljoin("?pagina=" + str(page_count))
        #     yield SplashRequest(next_page_url, meta={'category': response.meta['category']}, callback=self.parse_category)
    
    


