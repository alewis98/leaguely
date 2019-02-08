import React from 'react';
import GameCard from './GameCard';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import CardGroup from 'react-bootstrap/CardGroup';
import Collapse from 'react-bootstrap/Collapse';
import './GameCarousel.css';

class GameCarousel extends React.Component{
    constructor(props, context){
        super(props, context);

        this.state = {
            appear: true,
        };
    }

    render(){
        const { appear } = this.state;

        return(
            <div className="container-outer">
                <div className="container-inner">
                    <div className="card-group game-card-group">
                        <GameCard />
                        <GameCard />
                        <GameCard />
                        <GameCard />
                        <GameCard />
                        <GameCard />
                        <GameCard />
                        <GameCard />
                        <GameCard />
                        <GameCard />
                        <GameCard />
                    </div>
                </div>
            </div>
        );
    }
}

export default GameCarousel;