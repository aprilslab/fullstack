import './App.css';
import { Component } from 'react';
import { Route, Routes, Link } from 'react-router-dom';
import Home from './Home';
import Vote from './Vote';
import Like from './Like';
class App extends Component {
  render() {
    return (
      <div>
        <ul>
          <li><Link to='/'>홈</Link></li>
          <li><Link to='/vote'>투표</Link></li>
        </ul>
        <hr/>
        <Routes>
          <Route path='/' element={<Home/>} />
          <Route path='/vote' element={<Vote/>} />
          <Route path='/tour' element={<Vote/>} />
          <Route path='/like/:item_id' element={<Like/>} />
          <Route path='*' element={<div>페이지가 없습니다.</div>} />
        </Routes>
      </div>
    )
  }
}

export default App;
