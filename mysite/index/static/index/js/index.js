const swiper = new Swiper('.swiper', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
    autoplay: {
        delay: 3000,
    },
    speed: 1000,
    disableOnInteraction: false,
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });


  $(".django__acc").accordion({
    heightStyle: "content",
    collapsible: true,
  });

    // window.addEventListener('DOMContentLoaded', function() {
    //     document.querySelector('.fulls').addEventListener('click', function() {
    //         document.querySelector('.full').classList.toggle('is-open')
    //     })

    //     document.querySelector('.reversed').addEventListener('click', function() {
    //         document.querySelector('.reverse').classList.toggle('is-open')
    //     })

    //     document.querySelector('.securited').addEventListener('click', function() {
    //         document.querySelector('.security').classList.toggle('is-open')
    //     })

    //     document.querySelector('.scaled').addEventListener('click', function() {
    //         document.querySelector('.scale').classList.toggle('is-open')
    //     })

    //     document.querySelector('.comforted').addEventListener('click', function() {
    //         document.querySelector('.comfort').classList.toggle('is-open')
    //     })

    //     document.querySelector('.portabled').addEventListener('click', function() {
    //         document.querySelector('.portable').classList.toggle('is-open')
    //     })
    // })


    $('.header__menu-btn').on('click', function(e){
        e.preventDefault;
        $(this).toggleClass('menu-active');
    });

    window.addEventListener('DOMContentLoaded', function(){
        this.document.querySelector('#burger').addEventListener('click', function(){
            document.querySelector('#menu').classList.toggle('is-active')
        })
    })


