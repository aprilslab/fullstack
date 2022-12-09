import { Component } from "react";

class Counter extends Component {
    constructor(props) {
        super(props)
        this.state = {
            number: 0,
            fixedNumber: 0
        }
    }

    render() {
        const { number, fixedNumber } = this.state;
        return (
            <div>
                <h1>{number}</h1>
                <h2>불변의 숫자: {fixedNumber}</h2>
                <button onClick={ () => {
                    this.setState(prevState => {
                        return {number: prevState.number+1}
                    }, () => {
                        console.log('setState 호출')
                        console.log(this.state)
                    })
                }}> +1 </button> 
            </div>
        )
    }
}

export default Counter;