import logo from './logo.svg';
import './App.css';
import { Fragment } from 'react';
import { Component } from 'react';
import MyComponent from './MyComponent';
import Counter from './Counter';
import Say from './Say';
import Loader from './Loader';

class App extends Component {
  render() {
    const name = "react";
    return (
      <>
        <div className='react'> {name} </div>
        <MyComponent name='첫번째' favoriteNumber={3}>리액트</MyComponent>
        <Counter />
        <Say />
        <Loader />
      </>
    )
  }
}

export default App;
