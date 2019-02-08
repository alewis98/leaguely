import React from 'react';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import Organization from "./components/Organization";
import Form from "./components/Form";
import Home from "./views/Home";
import HomeNavbar from './components/HomeNavbar';


class App extends React.Component {

  // getSomething = async (e) => {
  //   e.preventDefault();
  //   const call = await fetch(`http://localhost:8000/api/organizations/`);
  //   const data = await call.json();
  //   console.log(data);
  // }

  render() {
    return(
      <Router>
        <div>
          <HomeNavbar />
          <Route exact path="/" component={Home}/>
        </div>
      </Router>
    )
  }
};

export default App;
      