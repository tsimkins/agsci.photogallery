jq(document).ready(function() {
    jq(".contentLeadImageContainer a#parent-fieldname-leadImage, .contentLeadImageContainerLeft a#parent-fieldname-leadImage, .contentLeadImageContainerFullWidth a#parent-fieldname-leadImage").each(
        function () {
            var href = jq(this).attr('href');

            if (href.indexOf('_galleryzoom') >= 0)
            {
                jq(this).addClass('fancybox');
            }
        }
    );

    jq("body.template-atct_album_view #content .photoAlbumImage a").each(
        function () {
            var href = jq(this).attr('href');
            if (href.indexOf('/view') >= 0)
            {
                href = href.replace('/view', '/image_galleryzoom');
                jq(this).attr('href', href);
                jq(this).addClass('fancybox');
            }
        }
    );


    if (window.innerWidth > 520)
    {
        jq(".fancybox").fancybox({'type' : 'image', 'hideOnContentClick' : true , 'closeClick' : true});
    }
    else
    {
        jq(".fancybox").fancybox({'type' : 'image', 'hideOnContentClick' : true , 'closeClick' : true, 'padding' : 0, 'margin' : 2, 'titlePosition' : 'inside'});
    }

});


    