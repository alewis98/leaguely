import React from 'react';
import Titles from "./components/Titles"
import Form from "./components/Form"

class App extends React.Component {

  getSomething = async (e) => {
    e.preventDefault();
    const call = await fetch(`http://localhost:8000/api/users/`);
    const data = await call.json();
    console.log(data);
  }

  render() {
    return(
      <div>
        <Titles></Titles>
        <Form getSomething={this.getSomething}/>
      </div>
    )
  }
};

export default App;
      