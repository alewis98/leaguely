import React from "react";

class Form extends React.Component {
    render() {
        return(
            <form onSubmit={this.props.getSomething}>
                <button>Get Weather</button>
            </form>
        )
    }
}

export default Form;