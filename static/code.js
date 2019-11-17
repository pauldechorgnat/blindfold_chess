var socket = io();

check_color = function(color, square){
    var square = document.getElementById('square').innerHTML;
    socket.emit('check_color', {
        'color': color,
        'square': square
    });
}

update_score_box = function(score, square, id){
    var score_box = document.getElementById(id);
    if (score == 1) {
        score_box.style['background-color'] = '#28a745';
    }
    if (score == -1) {
        score_box.style['background-color'] = '#dc3545';
    }
    score_box.innerHTML = square;
}

update_score_bar = function(scores, squares){
    for (var i=0; i<12; i++) {
        update_score_box(scores[i], squares[i], 'score' + i);
    }
}

socket.on('color_checked',
    function(data){
        document.getElementById('square').innerHTML = data['new_square'];
        scores = scores.concat(data['score']);
        scores = scores.slice(1, 13);
        squares_score = squares_score.concat(data['old_square']);
        squares_score = squares_score.slice(1, 13);
        update_score_bar(scores, squares_score);
        }

)