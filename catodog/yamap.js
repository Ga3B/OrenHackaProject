        // Инициализация карты
        ymaps.ready(init);
 
        function init () {
            
            //Центрирование и выбор масштаба карты
            var myMap = new ymaps.Map('map', {
                    center: [51.786542, 55.123780],  
                    zoom: 12
                });
 

 
                // Добавление метки на карту
                myMap.geoObjects
        .add(new ymaps.Placemark([51.786694, 55.135012], {
            balloonContent: 'bluecolor',
            iconCaption: ''
        }, {
            preset: 'islands#circleIcon',
            iconColor: '#3caa3c',
        }))
        .add(new ymaps.Placemark([51.797658, 55.114241], {
            balloonContent: 'bluecolor',
            iconCaption: ''
        }, {
            preset: 'islands#circleIcon',
            iconColor: '#3caa3c',
        }))        
        .add(new ymaps.Placemark([51.773757, 55.113211], {
            balloonContent: 'bluecolor',
            iconCaption: ''
        }, {
            preset: 'islands#circleIcon',
            iconColor: '#ff9900',
        }));

                //Элементы управления   
                myMap.controls
                // Кнопка изменения масштаба
                    .add('zoomControl')
                    // Список типов карты
                    .add('typeSelector')
                    // Кнопка изменения масштаба - справа
                    .add('smallZoomControl', { right: 5, top: 75 })
                    // Стандартный набор кнопок
                    .add('mapTools')    
                    //Линейка масштаба
                   .add(new ymaps.control.ScaleLine());
        }
    