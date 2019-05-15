import React from 'react';
import Card from 'react-bootstrap/Card';
import './GameCard.css';

class GameCard extends React.Component {
    constructor(props){
        super(props);
    }

    render(){
        var date = new Date(this.props.game.date);
        var options = {hour:'numeric', minute:'2-digit'};
        var score = 
        return(
            <div>
                <div className="card bg-light mb-3 game-card" style={{ width: '18rem'}}>
                <div className="card-header">{date.toLocaleDateString("en-US", options)}</div>
                <div className="card-body">
                    <div className="score-row"></div>
                    <h5 className="card-title">Light Title</h5>
                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                </div>
                </div>
            </div>
        );
    }
}

export default GameCard;