import React from 'react';
import Card from 'react-bootstrap/Card';
import './GameCard.css';

class GameCard extends React.Component {
    constructor(props){
        super(props);
    }

    render(){
        return(
            <div>
                <div className="card bg-light mb-3 game-card" style={{ width: '18rem'}}>
                <div className="card-header">{this.props.game.date}</div>
                <div className="card-body">
                    <h5 className="card-title">Light Title</h5>
                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                </div>
                </div>
            </div>
        );
    }
}

export default GameCard;