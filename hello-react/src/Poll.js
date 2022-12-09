import { useState, useEffect } from "react";
import axios from "axios";
import PollItem from "./PollItem";

const Poll = () => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const fetchData = async () => {
            setLoading(true);
            try {
                const response = await axios.get(
                    'http://localhost:8000/items'
                );
                setData(response.data);
            } catch(e) {
                console.log(e);
            }
            setLoading(false);
        };
        fetchData();
    }, []);

    if(loading) {
        return <div>대기 중...</div>;
    }
    if(!data) {
        return null;
    }
    return (
        <div>
            {data.data.map(item=> (
                <PollItem key={item.id} poll={item.data} showVote={false} />
            ))}
        </div>
    )
}

export default Poll;