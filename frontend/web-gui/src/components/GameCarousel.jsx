import React from 'react';
import GameCard from './GameCard';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import CardGroup from 'react-bootstrap/CardGroup';
import Collapse from 'react-bootstrap/Collapse';
import './GameCarousel.css';
import axios from 'axios';

class GameCarousel extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            games : []
        };
    }

    componentDidMount(){
        axios.get('http://localhost:8000/api/organizations/1/leagues/1/divisions/1/games/')
        .then(res => {
            const games = res.data;
            this.setState({ games });
          })
    }

    render(){
        var gameCards = [];
        for (var i = 0; i < this.state.games.length; i++) {
            gameCards.push(<GameCard game={this.state.games[i]} />);
        }
        //return <tbody>{rows}</tbody>;
        return(
            <div className="container-outer">
                <div className="container-inner">
                    <div className="card-group game-card-group">
                        {/* <GameCard />
                        <GameCard />
                        <GameCard />
                        <GameCard />
                        <GameCard />
                        <GameCard />
                        <GameCard />
                        <GameCard />
                        <GameCard />
                        <GameCard />
                        <GameCard /> */}
                        {gameCards}
                    </div>
                </div>
            </div>
        );
    }
}

export default GameCarousel;