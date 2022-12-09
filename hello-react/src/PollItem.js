import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const PollItem = ({poll, showVote}) => {
    const {id, name, vote, messages} = poll;
    const navigate = useNavigate();
    const onClick = async () => {
        navigate("/like/" + id + (showVote?"?o=1":""));
    }
    return (
        <p>
            <button onClick={onClick}>+1</button>
            &nbsp;&nbsp;
            {name}
            {showVote&&<>&nbsp;&nbsp;;-&nbsp;&nbsp;
            <span>{vote} 좋아욤</span></>}
        </p>
    )
}

export default PollItem;