import React from "react";
import Container from 'react-bootstrap/Container';
import GameCarousel from '../components/GameCarousel';

class Home extends React.Component{
    render(){
        return(
            <div>
                <GameCarousel />
                <Container>
                    <h2>Welcome</h2>
                </Container>
            </div>
        );
    }
}

export default Home;