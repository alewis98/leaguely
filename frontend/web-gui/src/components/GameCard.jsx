import React from 'react';
import Card from 'react-bootstrap/Card';
import './GameCard.css';

class GameCard extends React.Component {
    render(){
        return(
            <div>
                {/* <Card bg="light" style={{ width: '18rem' }}>
                    <Card.Header>Header</Card.Header>
                    <Card.Body>
                    <Card.Title>ManChestHair United vs Arsenel</Card.Title>
                    <Card.Text>
                        Some quick example text to build on the card title and make up the bulk
                        of the card's content.
                    </Card.Text>
                    </Card.Body>
                </Card> */}
                <div className="card bg-light mb-3 game-card" style={{ width: '18rem'}}>
                <div className="card-header">Header</div>
                <div className="card-body">
                    <h5 className="card-title">Light card title</h5>
                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                </div>
                </div>
            </div>
        );
    }
}

export default GameCard;