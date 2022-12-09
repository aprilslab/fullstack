import { useEffect, useState } from "react";
import { useLocation, useParams } from "react-router-dom";
import axios from "axios";
import qs from "qs";

const Like = () => {
    const location = useLocation();
    const query = qs.parse(location.search, {ignoreQueryPrefix: true});
    const {item_id} = useParams();
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState('I Like');
    const fetchData = async () => {
        setLoading(true);
        try {
            const response = await axios.get('http://localhost:8000/item/'+item_id);
            setData(response.data);
        } catch(e) {
            console.log(e);
        }
        setLoading(false);
    }
    const onClick = async () => {
        setLoading(true);
        try {
            const response = await axios.post('http://localhost:8000/item/'+item_id, {message});
            setData(response.data);
        } catch(e) {
            console.log(e);
        }
        setLoading(false);
    }
    const onChange = (e) => {
        setMessage(e.target.value);
    }
    useEffect(()=>{ fetchData(); }, []);
    if(loading) {
        return <p>좋아요...</p>
    }
    if(!data) { return null; }
    return (
        <div> 
            <p>여행지: {data.data.name}</p>
            {query.o=='1'&&<p>{data.data.vote}명이 좋아합니다.</p>}
            <input onChange={onChange} value={message} placeholder="좋아요 메시지를 남겨주세요!" />
            <button onClick={onClick}>좋아요!</button>
            {query.o=='1'&&<ul>
                {data.data.messages.map(
                    msg=><li key={msg.id}>{msg.message}</li>
                )}
            </ul>}
        </div>
    )
}

export default Like;