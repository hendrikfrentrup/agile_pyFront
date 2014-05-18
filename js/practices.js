$(function() {
    var getListUrl = window.qcumber.apiBaseUrl + window.qcumber.apiUrls.getPractices;
    var practiceList = [];
    var hbPracticeTemplate = Handlebars.compile($('#hb-practice-list').html());
    var practiceListContainer = $('.js-practice-list-container');

    $.get(getListUrl).done(function(data) {
        practiceList = data;
        console.log(data);
        addPracticeList(practiceList);
    });

    function addPracticeList(practiceList) {
        var content = hbPracticeTemplate({practices: practiceList});
        practiceListContainer.append(content);
    }

    function addPracticeToQueue(practiceName) {
        
    };
});